# Predictive Modeling of Multiple Sequence Alignment Posterior Probabilities Using Deep Learning Methods

## Table of Contents
1. Introduction
   - Overview of Balibase Data Sets
   - Directory Structure
2. Data Preparation
   - Creating FASTA Format Files
   - Generating Zorro Score CSVs
   - Validating Data Integrity
3. Environment Setup
   - Installing Zorro on Windows Using WSL
   - Configuring Dependencies
4. Data Pre-Processing
5. Model Training
6. Results and Analysis

## 1. Introduction

### 1.1 Overview of Balibase (MSA Bioinformatics)
Balibase is a benchmark dataset used for evaluating multiple sequence alignment (MSA) methods in bioinformatics. It consists of various subfolders containing aligned sequence files. Below is an illustration of the directory structure:
```
DataSet\bb3_release\RV11
│── BB11001
│   ├── aligned_sequences and unaligned sequences in different formats
│── BB11002
│   ├── aligned_sequences and unaligned sequences in different formats
│── BB11003
│   ├── aligned_sequences and unaligned sequences in different formats
```
Similiar structure in other folders (RV12,RV20,RV30,RV40,RV50)
You can find more information about the [Balibase Dataset](https://www.lbgi.fr/balibase/) here.

### 1.2 Directory Structure
Each subfolder contains sequence files, which need to be converted into FASTA format and processed further.

## 2. Environment Setup for Data Preparation (Installing Zorro in Windows)

### 2.1 Installing Zorro on Windows Using WSL
#### 📌 Prerequisites
- Windows 10/11 with **WSL 2** installed
- Ubuntu installed via WSL
- Internet connection

#### 🚀 Installation Steps
1️⃣ Install WSL & Ubuntu:
```powershell
wsl --install -d Ubuntu
```

2️⃣ Verify WSL Version:
```powershell
wsl -l -v
```
Ensure Ubuntu is running **WSL version 2**.

3️⃣ Move Zorro to WSL:
```bash
mv /mnt/c/Users/YOUR_WINDOWS_USERNAME/Downloads/zorro_linux_x86_64 ~/
```

4️⃣ Grant Execute Permission:
```bash
chmod +x ~/zorro_linux_x86_64
```

5️⃣ Move to `/usr/local/bin`:
```bash
sudo mv ~/zorro_linux_x86_64 /usr/local/bin/zorro
```

6️⃣ Add Zorro to PATH:
```bash
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc && source ~/.bashrc
```

7️⃣ Verify Installation:
```bash
zorro -h
```
If ZORRO options appear, installation is successful! ✅


## 3. Data Preparation

### 3.1 Creating FASTA Format Files
Each subfolder will contain a `fasta_format` folder with FASTA files for aligned sequences. The `to_fasta.py` script is used to generate these files.

**Example FASTA Format:**
```
>1aab_
---GKGDPKKPRGKMSSYAFFVQTSREEHKKKHPDASVNFSEFSKKCSERWKTMSAKEKGKFEDMAKADKARYEREMKTYIPPKGE----------
>1j46_A
------MQDRVKRPMNAFIVWSRDQRRKMALENP--RMRNSEISKQLGYQWKMLTEAEKWPFFQEAQKLQAMHREKYPNYKYRPRRKAKMLPK---
```

### 3.2 Generating Zorro Score CSVs
Each aligned sequence file is processed using the `calc_zorro_score.sh` script to generate Zorro score CSVs against each aligned column in the fasta format aligned sequence files, which are stored in a `zorro_scores` folder inside the `fasta_format` folder.

**Example Zorro Score Data Format:**
```
#### **Sample Zorro Score CSV Output**
| column_index | alignment_column | zorro_score |
|--------------|-----------------|-------------|
| 1            | ----M--         | 0.000000    |
| 2            | ----K--         | 0.000000    |
| 3            | ----K--         | 0.000000    |
| 4            | G---L--         | 1.099790    |
| 5            | K---K--         | 1.162091    |
| 6            | G---K--         | 1.211217    |
| 7            | D-M-H--         | 2.183136    |
| 8            | P-Q-P--         | 2.334078    |
| 9            | K-D-D-M         | 4.083154    |

```

### 3.3 Validating Data Integrity
Data integrity is validated by checking:
- The number of characters in the `alignment_column` matches the number of sequences in the file.
- The number of rows in the CSV equals the sequence length in the corresponding file.
- validate_data.sh script is used to perform validation and genrate csv reports in the following format

**Validation Example:**
| File Name | Num of Sequences | Length of Sequences | Num of Rows in CSV | Alignment Column Length | Validation |
|-----------|-----------------|----------------------|--------------------|------------------------|------------|
| BB11001   | 4               | 97                   | 97                 | 4                      | ✅          |
| BB11002   | 8               | 235                  | 235                | 8                      | ✅          |


## 4. Data Pre-Processing
*(Details to be added)*

## 5. Model Training
*(Details to be added)*

## 6. Results and Analysis
*(Details to be added)*

