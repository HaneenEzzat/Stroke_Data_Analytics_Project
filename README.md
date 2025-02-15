# Stroke Data Analytics Project

## 📌 Overview
This project focuses on performing **Extract, Transform, Load (ETL)** and **Exploratory Data Analysis (EDA)** on the **Stroke Prediction Dataset** from Kaggle. The dataset contains various health parameters used to predict the likelihood of stroke occurrence. The analysis includes **outlier detection, data visualization, and synthetic data generation**.

## 📂 Dataset
The dataset used in this project is the **Stroke Prediction Dataset** from Kaggle, which consists of features such as:
- **id**: Unique identifier for each patient
- **gender**: Male, Female, or Other
- **age**: Age of the patient
- **hypertension**: 0 (No), 1 (Yes)
- **heart_disease**: 0 (No), 1 (Yes)
- **ever_married**: "Yes" or "No"
- **work_type**: Type of occupation
- **Residence_type**: Urban or Rural
- **avg_glucose_level**: Average glucose level in blood
- **bmi**: Body Mass Index
- **smoking_status**: Smoking history
- **stroke**: 0 (No stroke), 1 (Stroke)

## 🛠️ Libraries & Dependencies
The following Python libraries are used:
```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer
```

## 🧪 ETL & Exploratory Data Analysis (EDA)

### 1️⃣ **Loading & Inspecting Data**
- Load the dataset into a Pandas DataFrame
- Check for missing values
- Display summary statistics

### 2️⃣ **Visualizing Outliers Using Boxplots**
- Boxplots are used to **detect and visualize outliers** in numerical features such as:
  - Age
  - Average Glucose Level
  - BMI
- Example visualization:
```python
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['bmi'])
plt.title("Boxplot of BMI")
plt.show()
```

### 3️⃣ **Applying ETL Principles**
- **Extract**: Load data from Kaggle dataset
- **Transform**:
  - Handle missing values
  - Detect and remove outliers
  - Normalize numerical features
- **Load**: Store transformed data in an SQLite database

### 4️⃣ **Data Synthesis Using Gaussian Copula**
- The `GaussianCopulaSynthesizer` is used to generate synthetic data similar to the original dataset.
- Example usage:
```python
# Detect metadata from the original dataset
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(df)

# Initialize the SDV synthesizer
synthesizer = GaussianCopulaSynthesizer(metadata)

# Fit the synthesizer to the original data
synthesizer.fit(df)
```

## 🚀 Next Steps
- Implement **incremental loading** to update data efficiently.
- Restructure **EDA** to follow a more appropriate structure.
- **No machine learning techniques** will be implemented at this stage.
- Continue refining data preprocessing and visualization techniques.

## 📌 Future Work
- Optimize the ETL pipeline for better performance.
- Explore feature engineering techniques for better data insights.
- Consider extending the dataset with additional health parameters.

