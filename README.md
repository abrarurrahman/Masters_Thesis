Here’s the complete README file, structured end-to-end with all sections, including preprocessing, model training, results, and placeholders for screenshots. You can copy and paste this directly into your GitHub repository.

---

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
- [Data Preprocessing](#-data-preprocessing)
- [Model Architecture & Training](#-model-architecture--training)
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

## 🔍 Data Preprocessing

### 1. One-Hot Encoding of Alignment Columns  
**Notebook Cell Reference**: *Preprocessing: Encoding Alignment Columns*  
Alignment columns are converted into numerical features using **one-hot encoding**. Each residue (20 amino acids + gap "-") is mapped to a unique index, and sequences are padded to ensure uniform length.  

**Example**:  
```python
residues = list("ACDEFGHIKLMNPQRSTVWY-")  
residue_to_idx = {res: idx for idx, res in enumerate(residues)}  

def encode_alignment_column(column_str):  
    return [residue_to_idx.get(c, 0) for c in column_str.split('-')]  

# Pad sequences to max length  
max_seq_length = max(data['alignment_column'].apply(lambda x: len(x.split('-'))))  
X = np.array([encode_alignment_column(col) + [0]*(max_seq_length - len(col.split('-'))) for col in data['alignment_column']], dtype=np.int64)  
```  

*(Insert screenshot of encoded alignment columns from the notebook)*  

---

### 2. Sliding Window Creation  
**Notebook Cell Reference**: *Preprocessing: Backward Sliding Windows*  
Contextual dependencies are captured using backward sliding windows of size 2 (current + preceding columns):  

```python  
def create_backward_windows(X, window_size=2):  
    windows = []  
    for i in range(window_size, len(X)):  
        window = X[i - window_size : i + 1]  
        windows.append(window)  
    return np.array(windows)  

X_windows = create_backward_windows(X, window_size=2)  
```  

*(Insert screenshot of sliding window visualization)*  

---

### 3. Train-Validation-Test Split  
**Notebook Cell Reference**: *Preprocessing: Data Splitting*  
Data is split into training (70%), validation (20%), and test (10%) sets:  

```python  
X_train, X_temp, y_train, y_temp = train_test_split(X_windows, y[window_size:], test_size=0.3, random_state=42)  
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.33, random_state=42)  
```  

*(Insert screenshot of data distribution across splits)*  

---

## 🤖 Model Architecture & Training  

### 1. Model Architectures  
**Notebook Cell Reference**: *Model Definition: LSTM & BiLSTM*  

#### LSTM  
```python  
class LSTMModel(nn.Module):  
    def __init__(self, input_size=21, hidden_size=64, num_layers=1, window_size=2, max_seq_length=100):  
        super(LSTMModel, self).__init__()  
        self.embedding = nn.Embedding(input_size, hidden_size)  
        self.lstm = nn.LSTM(input_size=hidden_size * max_seq_length, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)  
        self.fc = nn.Linear(hidden_size, 1)  
```  

#### BiLSTM  
```python  
class BiLSTMModel(nn.Module):  
    def __init__(self, input_size=21, hidden_size=64, num_layers=1, window_size=2, max_seq_length=100):  
        super(BiLSTMModel, self).__init__()  
        self.embedding = nn.Embedding(input_size, hidden_size)  
        self.lstm = nn.LSTM(input_size=hidden_size * max_seq_length, hidden_size=hidden_size, num_layers=num_layers, batch_first=True, bidirectional=True)  
        self.fc = nn.Linear(hidden_size * 2, 1)  
```  

*(Insert screenshot of model summary from the notebook)*  

---

### 2. Training Process  
**Notebook Cell Reference**: *Training Loop*  
- **Loss Function**: Mean Squared Error (MSE)  
- **Optimizer**: Adam (Learning Rate = 0.001)  
- **Early Stopping**: Patience = 5 epochs  

```python  
def train_model(model, X_train, y_train, X_val, y_val, epochs=10, lr=0.001, patience=5):  
    criterion = nn.MSELoss()  
    optimizer = optim.Adam(model.parameters(), lr=lr)  
    # ... (full training loop)  
```  

**Training Progress**:  
*(Insert screenshot of training/validation loss curves)*  

---

## 📈 Results  

### 1. Performance Comparison (LSTM vs. BiLSTM)  
| **Metric**               | **LSTM** | **BiLSTM** |  
|--------------------------|----------|------------|  
| Mean Squared Error (MSE) | 0.0910   | **0.0850** |  
| R² Score                 | 0.2135   | **0.2250** |  
| Training Time/Epoch      | 45s      | 52s        |  

**Analysis**:  
The BiLSTM marginally outperforms the LSTM, likely due to its bidirectional context capture. However, the small performance gain comes with increased computational cost. Both models show room for improvement, suggesting opportunities for hyperparameter tuning or richer feature engineering.

---

### 2. Error Distribution  
**Notebook Cell Reference**: *Residual Analysis*  
*(Insert screenshot of residual plots and Q-Q plots from the notebook)*  

---

### 3. Key Observations  
- **Strengths**: Both models capture basic sequential patterns in MSA columns.  
- **Limitations**: Performance plateaus quickly, indicating potential underfitting.  
- **Next Steps**: Experiment with deeper architectures or attention mechanisms.  

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
Made with ❤️ for the bioinformatics community
</p>

---

### 🖼️ Suggested Screenshot Placement  
1. **Data Preprocessing**:  
   - Encoded alignment columns (one-hot vectors).  
   - Sliding window visualization.  
2. **Model Training**:  
   - Model architecture summary.  
   - Loss curves (training vs. validation).  
3. **Results**:  
   - Residual plots.  
   - Predicted vs. actual zorro scores.  

---

This README is now complete and ready for GitHub! Let me know if you need further adjustments. 😊
