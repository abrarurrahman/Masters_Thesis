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

## 🤖 Model Training
*Coming soon*

## 📈 Results and Analysis
*Coming soon*

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
Made with ❤️ for the bioinformatics community
</p>
