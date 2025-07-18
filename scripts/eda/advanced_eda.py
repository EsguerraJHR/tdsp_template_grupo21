"""
Advanced Exploratory Data Analysis for Credit Card Fraud Detection
Generates comprehensive visualizations to inform preprocessing decisions.
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm, mannwhitneyu
import warnings
warnings.filterwarnings('ignore')

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

PROCESSED_DIR = 'data/processed'
os.makedirs(PROCESSED_DIR, exist_ok=True)

def load_data():
    try:
        df = pd.read_csv('data/raw/creditcard.csv')
        print(f"Dataset loaded successfully: {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: creditcard.csv not found in data/raw/")
        return None

def plot_class_distribution(df):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    sns.countplot(data=df, x='Class', palette=['lightblue', 'red'])
    plt.title('Class Distribution')
    plt.xlabel('Class (0: Normal, 1: Fraud)')
    plt.ylabel('Count')
    total = len(df)
    for i, v in enumerate(df['Class'].value_counts().sort_index()):
        plt.text(i, v + 100, f"{v:,}\n({v/total*100:.2f}%)", ha='center', va='bottom', fontweight='bold')
    plt.subplot(1, 2, 2)
    class_counts = df['Class'].value_counts()
    plt.pie(class_counts.values, labels=['Normal', 'Fraud'], autopct='%1.2f%%', colors=['lightblue', 'red'])
    plt.title('Class Distribution (Pie Chart)')
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/class_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_amount_distribution(df):
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 3, 1)
    plt.hist(df['Amount'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Overall Amount Distribution')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.yscale('log')
    plt.subplot(2, 3, 2)
    normal_amounts = df[df['Class'] == 0]['Amount']
    fraud_amounts = df[df['Class'] == 1]['Amount']
    plt.hist(normal_amounts, bins=30, alpha=0.7, label='Normal', color='lightblue')
    plt.hist(fraud_amounts, bins=30, alpha=0.7, label='Fraud', color='red')
    plt.title('Amount Distribution by Class')
    plt.xlabel('Amount')
    plt.ylabel('Frequency')
    plt.legend()
    plt.yscale('log')
    plt.subplot(2, 3, 3)
    sns.boxplot(data=df, x='Class', y='Amount')
    plt.title('Amount by Class (Box Plot)')
    plt.subplot(2, 3, 4)
    sns.violinplot(data=df, x='Class', y='Amount')
    plt.title('Amount by Class (Violin Plot)')
    plt.subplot(2, 3, 5)
    amount_stats = df.groupby('Class')['Amount'].agg(['mean', 'median', 'std', 'min', 'max'])
    amount_stats.plot(kind='bar', ax=plt.gca())
    plt.title('Amount Statistics by Class')
    plt.xlabel('Class')
    plt.ylabel('Amount')
    plt.xticks(rotation=0)
    plt.subplot(2, 3, 6)
    stats.probplot(df['Amount'], dist=norm, plot=plt)
    plt.title('Q-Q Plot for Amount')
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/amount_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_time_analysis(df):
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 3, 1)
    plt.hist(df['Time'], bins=50, alpha=0.7, color='green', edgecolor='black')
    plt.title('Time Distribution')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.subplot(2, 3, 2)
    normal_time = df[df['Class'] == 0]['Time']
    fraud_time = df[df['Class'] == 1]['Time']
    plt.hist(normal_time, bins=30, alpha=0.7, label='Normal', color='lightgreen')
    plt.hist(fraud_time, bins=30, alpha=0.7, label='Fraud', color='red')
    plt.title('Time by Class')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.subplot(2, 3, 3)
    plt.scatter(df[df['Class'] == 0]['Time'], df[df['Class'] == 0]['Amount'], alpha=0.5, s=1, color='lightblue', label='Normal')
    plt.scatter(df[df['Class'] == 1]['Time'], df[df['Class'] == 1]['Amount'], alpha=0.7, s=10, color='red', label='Fraud')
    plt.title('Time vs Amount by Class')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amount')
    plt.legend()
    plt.subplot(2, 3, 4)
    df['Hour'] = (df['Time'] // 3600) % 24
    hourly_fraud = df[df['Class'] == 1]['Hour'].value_counts().sort_index()
    hourly_normal = df[df['Class'] == 0]['Hour'].value_counts().sort_index()
    plt.plot(hourly_normal.index, hourly_normal.values, label='Normal', color='lightblue')
    plt.plot(hourly_fraud.index, hourly_fraud.values, label='Fraud', color='red')
    plt.title('Hourly Distribution by Class')
    plt.xlabel('Hour of Day')
    plt.ylabel('Transaction Count')
    plt.legend()
    plt.subplot(2, 3, 5)
    sns.boxplot(data=df, x='Class', y='Time')
    plt.title('Time by Class (Box Plot)')
    plt.subplot(2, 3, 6)
    time_stats = df.groupby('Class')['Time'].agg(['mean', 'median', 'std'])
    time_stats.plot(kind='bar', ax=plt.gca())
    plt.title('Time Statistics by Class')
    plt.xlabel('Class')
    plt.ylabel('Time (seconds)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/time_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_feature_distributions(df):
    v_features = [col for col in df.columns if col.startswith('V')]
    # First 12 features
    fig, axes = plt.subplots(3, 4, figsize=(20, 12))
    axes = axes.ravel()
    for i, feature in enumerate(v_features[:12]):
        axes[i].hist(df[df['Class'] == 0][feature], bins=30, alpha=0.7, label='Normal', color='lightblue', density=True)
        axes[i].hist(df[df['Class'] == 1][feature], bins=30, alpha=0.7, label='Fraud', color='red', density=True)
        axes[i].set_title(f'{feature} Distribution')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Density')
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/feature_distributions_1.png', dpi=300, bbox_inches='tight')
    plt.close()
    # Next 16 features
    fig, axes = plt.subplots(4, 4, figsize=(20, 16))
    axes = axes.ravel()
    for i, feature in enumerate(v_features[12:28]):
        axes[i].hist(df[df['Class'] == 0][feature], bins=30, alpha=0.7, label='Normal', color='lightblue', density=True)
        axes[i].hist(df[df['Class'] == 1][feature], bins=30, alpha=0.7, label='Fraud', color='red', density=True)
        axes[i].set_title(f'{feature} Distribution')
        axes[i].set_xlabel(feature)
        axes[i].set_ylabel('Density')
        axes[i].legend()
        axes[i].grid(True, alpha=0.3)
    for i in range(len(v_features[12:]), 16):
        axes[i].set_visible(False)
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/feature_distributions_2.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_correlation_analysis(df):
    v_features = [col for col in df.columns if col.startswith('V')]
    correlation_matrix = df[v_features + ['Amount', 'Class']].corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    plt.figure(figsize=(18, 14))
    sns.heatmap(correlation_matrix, mask=mask, annot=False, cmap='coolwarm', center=0, square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Matrix (V Features + Amount + Class)')
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/correlation_matrix.png', dpi=300, bbox_inches='tight')
    plt.close()
    plt.figure(figsize=(10, 8))
    target_corr = correlation_matrix['Class'].sort_values(ascending=False)
    target_corr = target_corr[target_corr.index != 'Class']
    plt.barh(target_corr.index, target_corr.values)
    plt.xlabel('Correlation with Class')
    plt.title('Feature Correlation with Target Variable')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/target_correlation.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_outlier_analysis(df):
    v_features = [col for col in df.columns if col.startswith('V')]
    fig, axes = plt.subplots(4, 7, figsize=(28, 16))
    axes = axes.ravel()
    for i, feature in enumerate(v_features):
        axes[i].boxplot([df[df['Class'] == 0][feature], df[df['Class'] == 1][feature]], labels=['Normal', 'Fraud'])
        axes[i].set_title(f'{feature} Outliers')
        axes[i].set_ylabel(feature)
        axes[i].grid(True, alpha=0.3)
    for i in range(len(v_features), 28):
        axes[i].set_visible(False)
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/outlier_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def plot_feature_importance_analysis(df):
    v_features = [col for col in df.columns if col.startswith('V')]
    feature_importance = {}
    for feature in v_features:
        normal_data = df[df['Class'] == 0][feature]
        fraud_data = df[df['Class'] == 1][feature]
        statistic, p_value = mannwhitneyu(normal_data, fraud_data, alternative='two-sided')
        feature_importance[feature] = -np.log10(p_value) if p_value > 0 else 0
    sorted_features = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
    features, importance = zip(*sorted_features)
    plt.figure(figsize=(12, 8))
    plt.barh(features, importance)
    plt.xlabel('-log10(p-value) (Higher = More Important)')
    plt.title('Feature Importance Based on Mann-Whitney U Test')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{PROCESSED_DIR}/feature_importance.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    print("Loading data...")
    df = load_data()
    if df is None:
        return
    print("\nGenerating comprehensive EDA visualizations...")
    plot_class_distribution(df)
    plot_amount_distribution(df)
    plot_time_analysis(df)
    plot_feature_distributions(df)
    plot_correlation_analysis(df)
    plot_outlier_analysis(df)
    plot_feature_importance_analysis(df)
    print("\nAll visualizations saved to data/processed/")
    print("Review the plots to decide on preprocessing techniques!")

if __name__ == "__main__":
    main() 