# %%
# Importing libraries and dependencies
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
from sdv.metadata import SingleTableMetadata
from sdv.single_table import GaussianCopulaSynthesizer

# %%
# Load csv dataset into SQLite3
df = pd.read_csv("healthcare-dataset-stroke-data.csv")
connection = sqlite3.connect("demo.db")
df.to_sql("stroke_data", connection, if_exists="replace")

# %%
# Show a sample of the dataset after loading in SQLite
query = "SELECT * FROM stroke_data LIMIT 5"
df_sample = pd.read_sql(query, connection)
print(df_sample)

# %%
# Show the number of records and columns of the dataset before synthesizing
df.shape

# %% [markdown]
# **Data Synthesizing**
# 

# %%
# Detect metadata from the original dataset
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(df)

# Initialize the SDV synthesizer
synthesizer = GaussianCopulaSynthesizer(metadata)

# Fit the synthesizer to the original data
synthesizer.fit(df)

# %%
# Generate synthetic data (same number of rows as original data)
synthetic_data = synthesizer.sample(num_rows=len(df))

print("\nSynthetic Data:")
print(synthetic_data.head())

# %%
# Concatenate original and synthetic data
total_data = pd.concat([df, synthetic_data], ignore_index=True)

print("\ntotal Data:")
print(total_data.head())

# %%
# Save combined data to a new table
total_data.to_sql("total_table", connection, if_exists="replace", index=False)

# Close connection
connection.close()

print("Combined data saved to SQLite database successfully.")

# %%
total_data.describe()

# %%
print(total_data.tail())

# %%
# To ensure the synthetic data is add to the original data
total_data.shape

# %%
total_data.dtypes

# %% [markdown]
# **📌Key Measures of Tendencies:**
# 

# %%
# Calculating the mean of each numerical column
print("Mean ID:", total_data["id"].mean())
print("Mean Age:", total_data["age"].mean())
print("Mean Hypertension:", total_data["hypertension"].mean())
print("Mean Heart Disease:", total_data["heart_disease"].mean())
print("Mean Avg Glucose Level:", total_data["avg_glucose_level"].mean())
print("Mean BMI:", total_data["bmi"].mean())
print("Mean Stroke:", total_data["stroke"].mean())

# %%
# Calcuating the median of each numerical column
print("median ID:", total_data["id"].median())
print("median Age:", total_data["age"].median())
print("median Hypertension:", total_data["hypertension"].median())
print("median Heart Disease:", total_data["heart_disease"].median())
print("median Avg Glucose Level:", total_data["avg_glucose_level"].median())
print("median BMI:", total_data["bmi"].median())
print("median Stroke:", total_data["stroke"].median())

# %%
# Calcuating the mode of each column
print("mode ID:", df["id"].mode())
print("mode Age:", df["age"].mode())
print("mode Hypertension:", df["hypertension"].mode())
print("mode Heart Disease:", df["heart_disease"].mode())
print("mode Avg Glucose Level:", df["avg_glucose_level"].mode())
print("mode BMI:", df["bmi"].mode())
print("mode Stroke:", df["stroke"].mode())
print("mode gender:", df["gender"].mode())
print("mode ever_married:", df["ever_married"].mode())
print("mode work_type:", df["work_type"].mode())
print("mode Residence_type:", df["Residence_type"].mode())
print("mode smoking_status:", df["smoking_status"].mode())

# %% [markdown]
# **Dispersion (Spread of Data):**
# 

# %%
# Calcuating the variance of each numerical column
print("var ID:", total_data["id"].var())
print("var Age:", total_data["age"].var())
print("var Hypertension:", total_data["hypertension"].var())
print("var Heart Disease:", total_data["heart_disease"].var())
print("var Avg Glucose Level:", total_data["avg_glucose_level"].var())
print("var BMI:", total_data["bmi"].var())
print("var Stroke:", total_data["stroke"].var())

# %%
# Calcuating the standard deviation of each numerical column
print("std ID:", df["id"].std())
print("std Age:", df["age"].std())
print("std Hypertension:", df["hypertension"].std())
print("std Heart Disease:", df["heart_disease"].std())
print("std Avg Glucose Level:", df["avg_glucose_level"].std())
print("std BMI:", df["bmi"].std())
print("std Stroke:", df["stroke"].std())

# %%
# Show the maximum and minimum number of each numerical column
print("max ID:", total_data["id"].max(), "~ min ID:", total_data["id"].min())
print("max Age:", total_data["age"].max(), "~ min Age:", total_data["age"].min())
print(
    "max Hypertension:",
    total_data["hypertension"].max(),
    "~ min Hypertension:",
    total_data["hypertension"].min(),
)
print(
    "max Heart Disease:",
    total_data["heart_disease"].max(),
    "~ min Heart Disease:",
    total_data["heart_disease"].min(),
)
print(
    "max Avg Glucose Level:",
    total_data["avg_glucose_level"].max(),
    "~ min Avg Glucose Level:",
    total_data["avg_glucose_level"].min(),
)
print("max BMI:", total_data["bmi"].max(), "~ min BMI:", total_data["bmi"].min())
print(
    "max Stroke:",
    total_data["stroke"].max(),
    "~ max Stroke:",
    total_data["stroke"].min(),
)

# %% [markdown]
# **Distribution Shape:**
# 

# %%
# Calcuating the skew of each numerical column
print("skew ID:", total_data["id"].skew())
print("skew Age:", total_data["age"].skew())
print("skew Hypertension:", total_data["hypertension"].skew())
print("skew Heart Disease:", total_data["heart_disease"].skew())
print("skew Avg Glucose Level:", total_data["avg_glucose_level"].skew())
print("skew BMI:", total_data["bmi"].skew())
print("skew Stroke:", total_data["stroke"].skew())

# %%
# Calcuating the kurtosis of each numerical column
print("kurt ID:", total_data["id"].kurt())
print("kurt Age:", total_data["age"].kurt())
print("kurt Hypertension:", total_data["hypertension"].kurt())
print("kurt Heart Disease:", total_data["heart_disease"].kurt())
print("kurt Avg Glucose Level:", total_data["avg_glucose_level"].kurt())
print("kurt BMI:", total_data["bmi"].kurt())
print("kurt Stroke:", total_data["stroke"].kurt())

# %% [markdown]
# **📌 Key Measures of Qualities:**
# 

# %%
total_data.info()

# %%
# Show unique values for each column
print("unique ID:", total_data["id"].unique().sum())
print("unique Age:", total_data["age"].unique().sum())
print("unique Hypertension:", total_data["hypertension"].unique().sum())
print("unique Heart Disease:", total_data["heart_disease"].unique().sum())
print("unique Avg Glucose Level:", total_data["avg_glucose_level"].unique().sum())
print("unique BMI:", total_data["bmi"].unique().sum())
print("unique Stroke:", total_data["stroke"].unique().sum())
print("unique gender:", total_data["gender"].unique().sum())
print("unique ever_married:", total_data["ever_married"].unique().sum())
print("unique work_type:", total_data["work_type"].unique().sum())
print("unique Residence_type:", total_data["Residence_type"].unique().sum())
print("unique smoking_status:", total_data["smoking_status"].unique().sum())

# %%
# Show the number of null values ​​in each column
total_data.isnull().sum()

# %%
total_data.duplicated().sum()

# %%
Q1 = total_data["age"].quantile(0.25)
Q3 = total_data["age"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = (total_data["age"] < lower_bound) | (total_data["age"] > upper_bound)

print("Outliers using IQR method:")
print(outliers.sum())

# Create a boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=total_data["age"])

plt.title("Boxplot for Outlier Detection")
plt.show()

# %%
Q1 = total_data["hypertension"].quantile(0.25)
Q3 = total_data["hypertension"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = (total_data["hypertension"] < lower_bound) | (
    total_data["hypertension"] > upper_bound
)

print("Outliers using IQR method:")
print(outliers.sum())

# Create a boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=total_data["age"])

plt.title("Boxplot for Outlier Detection")
plt.show()

# %%
Q1 = total_data["heart_disease"].quantile(0.25)
Q3 = total_data["heart_disease"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = (total_data["heart_disease"] < lower_bound) | (
    total_data["heart_disease"] > upper_bound
)

print("Outliers using IQR method:")
print(outliers.sum())

# Create a boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=total_data["heart_disease"])

plt.title("Boxplot for Outlier Detection")
plt.show()

# %%
Q1 = total_data["avg_glucose_level"].quantile(0.25)
Q3 = total_data["avg_glucose_level"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = (total_data["avg_glucose_level"] < lower_bound) | (
    total_data["avg_glucose_level"] > upper_bound
)

print("Outliers using IQR method:")
print(outliers.sum())

# Create a boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=total_data["avg_glucose_level"])

plt.title("Boxplot for Outlier Detection")
plt.show()

# %%
Q1 = total_data["bmi"].quantile(0.25)
Q3 = total_data["bmi"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = (total_data["bmi"] < lower_bound) | (total_data["bmi"] > upper_bound)

print("Outliers using IQR method:")
print(outliers.sum())

# Create a boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=total_data["bmi"])

plt.title("Boxplot for Outlier Detection")
plt.show()

# %%
Q1 = total_data["stroke"].quantile(0.25)
Q3 = total_data["stroke"].quantile(0.75)
IQR = Q3 - Q1

# Define outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = (total_data["stroke"] < lower_bound) | (total_data["stroke"] > upper_bound)

print("Outliers using IQR method:")
print(outliers.sum())

# Create a boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=total_data["stroke"])

plt.title("Boxplot for Outlier Detection")
plt.show()


