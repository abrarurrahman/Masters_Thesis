# 🧬 Predictive Modeling of MSA Posterior Probabilities Using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![BaliBase](https://img.shields.io/badge/Dataset-BaliBase-orange.svg)](https://www.lbgi.fr/balibase/)

A deep learning approach to predict posterior probabilities in Multiple Sequence Alignment (MSA) using the BaliBase benchmark dataset.

## 📚 Table of Contents

- [Overview](#-overview)
- [Directory Structure](#-directory-structure)
- [Environment Setup](#-environment-setup)
- [Data Preparation](#-data-preparation)
- [Model Training](#-model-training)
- [Results](#-results)
- [Contributing](#-contributing)

## 🔍 Overview

### BaliBase Dataset
BaliBase is a comprehensive benchmark dataset used for evaluating Multiple Sequence Alignment (MSA) methods in bioinformatics. The dataset is organized into various reference sets (RV11, RV12, RV20, RV30, RV40, RV50), each containing aligned and unaligned sequence files.

🔗 **Resources**:
- [BaliBase Official Website](https://www.lbgi.fr/balibase/)
- [Dataset Documentation](https://www.lbgi.fr/balibase/documentation/)

## 📂 Directory Structure

```
DataSet/bb3_release/
├── RV11/
│   ├── BB11001/
│   │   ├── aligned_sequences/
│   │   └── unaligned_sequences/
│   ├── BB11002/
│   └── BB11003/
├── RV12/
├── RV20/
├── RV30/
├── RV40/
└── RV50/
```

## 🛠️ Environment Setup

### Installing Zorro on Windows To Prepare Data Set for Model Training (WSL)

#### Prerequisites
- Windows 10/11 with WSL 2
- Ubuntu on WSL
- Active internet connection

#### Installation Steps

1. **Install WSL & Ubuntu**
```powershell
wsl --install -d Ubuntu
```

2. **Verify WSL Version**
```powershell
wsl -l -v
```

3. **Configure Zorro**
```bash
# Move Zorro binary
mv /mnt/c/Users/YOUR_USERNAME/Downloads/zorro_linux_x86_64 ~/

# Set permissions
chmod +x ~/zorro_linux_x86_64

# Move to system bin
sudo mv ~/zorro_linux_x86_64 /usr/local/bin/zorro

# Update PATH
export PATH=$PATH:/usr/local/bin
```

4. **Verify Installation**
```bash
zorro -h
```

## 📊 Data Preparation

### FASTA Format Files
Each sequence folder from balibase data set contains aligned sequences. Since zorro accepts fasta format only, we need to generate fasta version of each file. Attached below sample of what a fasta file looks like. We are using to_fasta_format.py to convert all the aligned sequences we have to fasta format and store the files in a folder named as fasta_format in each subdirectory.

```fasta
>1aab_
---GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTYIPPKGE
>1j46_A
------MQDRVKRPMNAFIVWSRDQRRKMALENP--RMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP
```

### Zorro Score Generation

Once fasta fomat files are ready, we need to preidct zorro score against each aligned column and then store the data in appropriate format to use for model training later on. IT is done by calc_zorro_scores.sh and files are stored in csv format like the sample attached below.

| column_index | alignment_column | zorro_score |
|--------------|-----------------|-------------|
| 1            | ----M--         | 0.000000    |
| 2            | ----K--         | 0.000000    |
| 3            | G---L--         | 1.099790    |
| 4            | K---K--         | 1.162091    |

### Data Validation

Our validation process ensures:
- ✅ Character count matches sequence count
- ✅ CSV rows match sequence length
- ✅ Data integrity across files
validation report checks the csv (zorro score against each aligned column against there corresponding fasta format file to make sure that we haven't missed any data). validate_csv.sh is used to generate csv report of each folder in the following format.
**Validation Report Format:**

| File Name | Sequences | Sequence Length | CSV Rows | Column Length | Status |
|-----------|-----------|-----------------|----------|---------------|--------|
| BB11001   | 4         | 97             | 97       | 4             | ✅     |
| BB11002   | 8         | 235            | 235      | 8             | ✅     |

## 🤖 Model Training and Dat Pre-Processing for Training


### Model Architecture

We employ both **LSTM** and **Bidirectional LSTM (BiLSTM)** models to predict the posterior probabilities of each aligned column in the MSA. The models are designed to capture the sequential dependencies in the alignment columns, leveraging both past and future context.

#### Key Features:
- **Input Layer**: Encodes the alignment columns using an embedding layer.
- **LSTM/BiLSTM Layer**: Captures sequential dependencies in both forward and backward directions.
- **Fully Connected Layer**: Maps the LSTM outputs to the posterior probabilities.
- **Output Layer**: Produces the predicted zorro scores.

### Training Process

1. **Data Splitting**:
   - **Training Set**: 70% of the data
   - **Validation Set**: 20% of the data
   - **Test Set**: 10% of the data

2. **Hyperparameters**:
   - **Learning Rate**: 0.001
   - **Batch Size**: 32
   - **Epochs**: 300
   - **Early Stopping**: Patience of 5 epochs

3. **Loss Function**:
   - **Mean Squared Error (MSE)**: Used to measure the difference between predicted and actual zorro scores.

4. **Optimizer**:
   - **Adam Optimizer**: Efficient and adaptive learning rate optimization.

### Training Code

```python
# Define the LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size=21, hidden_size=64, num_layers=1, window_size=2, max_seq_length=100):
        super(LSTMModel, self).__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.lstm = nn.LSTM(input_size=hidden_size * max_seq_length, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        x = self.embedding(x)
        batch_size = x.size(0)
        x = x.view(batch_size, x.size(1), -1)
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out.squeeze()

# Define the BiLSTM model
class BiLSTMModel(nn.Module):
    def __init__(self, input_size=21, hidden_size=64, num_layers=1, window_size=2, max_seq_length=100):
        super(BiLSTMModel, self).__init__()
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.lstm = nn.LSTM(input_size=hidden_size * max_seq_length, hidden_size=hidden_size, num_layers=num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, 1)

    def forward(self, x):
        x = self.embedding(x)
        batch_size = x.size(0)
        x = x.view(batch_size, x.size(1), -1)
        out, _ = self.lstm(x)
        out = self.fc(out[:, -1, :])
        return out.squeeze()

# Training the model
def train_model(model, X_train, y_train, X_val, y_val, epochs=10, lr=0.001, patience=5):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    train_dataset = torch.utils.data.TensorDataset(X_train, y_train)
    train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    
    val_dataset = torch.utils.data.TensorDataset(X_val, y_val)
    val_dataloader = DataLoader(val_dataset, batch_size=32, shuffle=False)
    
    best_val_loss = float('inf')
    patience_counter = 0
    train_losses = []
    val_losses = []
    
    model.train()
    for epoch in range(epochs):
        model.train()
        total_train_loss = 0
        for inputs, labels in train_dataloader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_train_loss += loss.item()
        
        avg_train_loss = total_train_loss / len(train_dataloader)
        train_losses.append(avg_train_loss)
        
        model.eval()
        total_val_loss = 0
        with torch.no_grad():
            for inputs, labels in val_dataloader:
                outputs = model(inputs)
                loss = criterion(outputs, labels)
                total_val_loss += loss.item()
        
        avg_val_loss = total_val_loss / len(val_dataloader)
        val_losses.append(avg_val_loss)
        
        print(f"Epoch {epoch+1}/{epochs}, Train Loss: {avg_train_loss:.4f}, Val Loss: {avg_val_loss:.4f}")
        
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            patience_counter = 0
            torch.save(model.state_dict(), "best_model.pth")
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(f"Early stopping triggered after epoch {epoch+1}")
                model.load_state_dict(torch.load("best_model.pth"))
                break
    
    plt.figure(figsize=(10, 6))
    plt.plot(train_losses, label='Training Loss')
    plt.plot(val_losses, label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return train_losses, val_losses
```

## 📈 Results and Analysis

### Model Performance



### Evaluation Metrics

The models' performance was evaluated using the following metrics on the test set:

| Metric           | LSTM Value   | BiLSTM Value |
|------------------|--------------|--------------|
| Mean Squared Error (MSE) | 0.0910       | 0.0850       |
| Root Mean Squared Error (RMSE) | 0.3017       | 0.2915       |
| Mean Absolute Error (MAE) | 0.2117       | 0.2050       |
| R² Score         | 0.2135       | 0.2250       |
| Mean Absolute Percentage Error (MAPE) | 21.17%      | 20.50%       |
| Explained Variance Ratio | 0.2117       | 0.2200       |

### Comparison and Analysis

The BiLSTM model outperformed the LSTM model across all metrics, indicating that capturing both past and future context in the sequence data provides a more accurate prediction of posterior probabilities. The BiLSTM model achieved a lower MSE, RMSE, and MAE, and a higher R² score, suggesting better overall performance. The explained variance ratio also improved, indicating that the BiLSTM model captures more variance in the data.

### Residual Analysis

The residuals (difference between predicted and actual values) were analyzed to ensure the models' predictions are unbiased:

**Residual Plot**:
![image](https://github.com/user-attachments/assets/01d4ac31-cbf2-49e0-8029-a3cc7306bc05)



### Q-Q Plot

The Q-Q plot was used to check the normality of the residuals:

**Q-Q Plot**:
![image](https://github.com/user-attachments/assets/9d4f49eb-0f4c-4db2-a2b2-a7ddc8549470)


### Distribution of Residuals

The distribution of residuals was plotted to ensure they are normally distributed around zero:

**Residual Distribution**:
![image](https://github.com/user-attachments/assets/a1211339-b0d5-485f-a624-5aafd4318586)
![image](https://github.com/user-attachments/assets/f104d9f7-db6f-4bc2-9608-215dc74f0e4d)


## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
Made with ❤️ for the bioinformatics community
</p>
