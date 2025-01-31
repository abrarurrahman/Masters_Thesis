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

### Installing Zorro on Windows (WSL)

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
Each sequence folder contains aligned sequences in FASTA format. Example:

```fasta
>1aab_
---GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTYIPPKGE
>1j46_A
------MQDRVKRPMNAFIVWSRDQRRKMALENP--RMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRP
```

### Zorro Score Generation

The system generates Zorro scores for each aligned column in the sequence files. Scores are stored in CSV format:

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
