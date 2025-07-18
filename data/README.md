# Data Directory

This directory contains the data files for the TDSP (Team Data Science Process) project.

## Directory Structure

- `raw/`: Contains the original, unprocessed data files
- `processed/`: Contains preprocessed and transformed data files
- `results/`: Contains model results, visualizations, and reports

## Large Files

Due to GitHub's file size limitations (100MB per file), the following large files are excluded from version control:

### Raw Data
- `creditcard.csv` (144MB) - Original credit card fraud dataset

### Processed Data
- `X_train_balanced.csv` (256MB) - Balanced training features
- `X_test_scaled.csv` (32MB) - Scaled test features
- `y_train_balanced.csv` (1.3MB) - Balanced training labels
- `y_test.csv` (167KB) - Test labels
- `scaler.pkl` (1.4KB) - Scaler object

### Results
- Various PNG files for visualizations (132KB - 355KB each) - **INCLUDED in repository**

## How to Get the Data

1. **Download the original dataset**: The `creditcard.csv` file can be downloaded from Kaggle or other sources
2. **Run preprocessing scripts**: Use the scripts in `scripts/preprocessing/` to generate the processed files
3. **Run training scripts**: Use the scripts in `scripts/training/` to generate the results

## Data Sources

- **Credit Card Fraud Dataset**: Available on Kaggle at [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

## Notes

- Small configuration files and `.gitkeep` files are included to maintain directory structure
- **Images, HTML reports, and small data files ARE included** in the repository for analysis
- Only large CSV files (>100MB) and model files are excluded
- The preprocessing and training scripts will regenerate all necessary files
- Consider using Git LFS (Large File Storage) if you need to version control large files 