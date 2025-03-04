# %% [markdown]
# **Import the required Python libraries**
# 

# %%
# ignore the warnings

import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st
import sqlite3
from tabulate import tabulate

# %% [markdown]
# **Dataset attributes**
# 
# 1. id: unique identifier
# 2. gender: "Male", "Female" or "Other"
# 3. age: age of the patient
# 4. hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
# 5. heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
# 6. ever_married: "No" or "Yes"
# 7. work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
# 8. Residence_type: "Rural" or "Urban"
# 9. avg_glucose_level: average glucose level in blood
# 10. bmi: body mass index
# 11. smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"\*
# 12. stroke: 1 if the patient had a stroke or 0 if not
#     \*Note: "Unknown" in smoking_status means that the information is unavailable for this patient
# 

# %% [markdown]
# **Import the dataset**
# 

# %%
connection= sqlite3.connect("data_source.db")
query = "SELECT * FROM raw_data"
data = pd.read_sql(query, connection)

# %% [markdown]
# # Overview of the dataset
# 

# %% [markdown]
# **data.shape attribute**
# 

# %%
print(data.shape)

# %% [markdown]
# Interpretation
# 
# We can see that our dataset has 10230 rows and 13 columns.
# 

# %% [markdown]
# **data.columns attribute**
# 

# %%
print(data.columns)

# %% [markdown]
# **data.head() and data.tail() methods**
# 

# %% [markdown]
# An overview of the dataset. We can view the top five and bottom five rows of the dataset with data.head() and data.tail() methods respectively.
# 

# %%
data.head

# %%
data.tail

# %% [markdown]
# **data.info() method**
# 
# We can get a concise summary of the dataset with data.info() method. This method prints information about a data including the index, column names and data types, non-null values and memory usage.
# 

# %%
data.info()

# %% [markdown]
# **Interpretation**
# 
# We can see that this method provides information about all columns in the dataset. The dataset contains 10,230 entries (rows) and 13 columns. Most columns have no missing values, except for the bmi column, which has 418 missing values (approximately 4.1% of the data). This indicates that the bmi column requires further attention, such as imputation or analysis to handle the missing data.
# 

# %% [markdown]
# we should check the distribution of bmi to use the appropriate method to fill the missing values
# 
# as follow:
# 

# %%
sns.histplot(data['bmi'], kde=True, bins=30)
plt.title("Histogram of BMI")
plt.show()

# %% [markdown]
# **Interpretation**
# 
# The above plot confirms that the target variable bmi is highly positively skewed, so the appropriate method to handle the missing values is the median()
# 
# as follow:
# 

# %% [markdown]
# Check the bmi after filling the missing values
# 

# %%
# Fill missing values with median
data['bmi'].fillna(data['bmi'].median(), inplace=True)

# %% [markdown]
# Checking the missing values after filling the missing values in bmi
# 

# %%
data.info()

# %% [markdown]
# **tabulate the data**
# 

# %%
# Convert DataFrame to a table
table = tabulate(data, headers='keys', tablefmt='pretty', showindex=False)

# Print the table
print(table)

# %% [markdown]
# **data.describe() method**
# 
# We can view the summary statistics of numerical columns with data.describe() method. It enable us to detect outliers in the data which require further investigation.
# 

# %%
print(data.describe())

# %% [markdown]
# Constructing new attribute 'age_category' based on age to categorize people
# 
# as follow
# 

# %%
data['age_category'] = np.where(data['age'] < 16, 'Pediatric', 'Adult')

# %% [markdown]
# Checking the new attribute in the dataset
# 

# %%
print(data.info())

# %% [markdown]
# Constructing new attribute 'avg_glucose_level' based on age to categorize people
# 
# as follow:
# 

# %%
conditions = [
    data['avg_glucose_level'] < 100,
    (data['avg_glucose_level'] >= 100) & (data['avg_glucose_level'] < 126),
    data['avg_glucose_level'] >= 126
]

categories = ['Normal', 'Prediabetic', 'Diabetic']

data['glucose_category'] = np.select(conditions, categories)

print(data.info())


# %% [markdown]
# **Check for anomalies in the dataset**
# 
# Check with ASSERT statement
# We should confirm that our dataset has no missing values. We can write an assert statement to verify this. We can use an assert statement to programmatically check that no missing, unexpected 0 or negative values are present. This gives us confidence that our code is running properly.
# 
# Assert statement will return nothing if the value being tested is true and will throw an AssertionError if the value is false.
# 
# Asserts
# 
# • assert 1 == 1 (return Nothing if the value is True)
# 
# • assert 1 == 2 (return AssertionError if the value is False)
# 

# %%
#assert that there are no missing values in the dataframe

assert pd.notnull(data).all().all()

# %% [markdown]
# Interpretation
# 
# The above command does not throw any error. Hence, it is confirmed that there are no missing or negative values in the dataset. All the values are greater than or equal to zero.
# 

# %% [markdown]
# # Univariate analysis
# 
# **Measures of central tendency and dispersion**
# Central tendency means a central value which describe a probability distribution. It may also be called a center or location of the distribution. The most common measures of central tendency are the arithmetic mean, the median and the mode. The most common measure of central tendency is the mean. For skewed distribution or when there is concern about outliers, the median may be preferred. So, median is more robust measure than the mean.
# 
# Dispersion is an indicator of how far away from the center, we can find the data values. The most common measures of dispersion are variance, standard deviation and interquartile range(IQR). Variance is the standard measure of spread. The standard deviation is the square root of the variance. The variance and standard deviation are two useful measures of spread.
# 
# A third measure of spread is the interquartile range (IQR). The IQR is calculated using the boundaries of data situated between the 1st and the 3rd quartiles. So, IQR can be calculated as IQR = Q3 - Q1. It is a robust measure of spread.
# 
# The above measures can be calculated by df.describe() method as follows:-
# 

# %%
print(data['stroke'].describe())

# %% [markdown]
# **Interpretation**
# 
# The count, min and max values represent the number of counts, minimum and maximum values of the target variable Absenteeism time in hours.
# 
# The measures of central tendency are given by the mean(0.049560) and median(50% value 0.000000).
# 
# The measure of dispersion is given by the standard deviation given by std(0.217045).
# 
# The 25%, 50% and 75% values show the corresponding percentiles. 50th percentile denote the median of the distribution.
# 
# The IQR is the difference between 75th and 25th percentiles. Hence, IQR = 0.00 - 0.00 = 0.00
# 

# %% [markdown]
# **Skewness**
# 
# Reference range on skewness values
# The rule of thumb for skewness values are:
# 
# If the skewness is between -0.5 and 0.5, the data are fairly symmetrical.
# 
# If the skewness is between -1 and – 0.5 or between 0.5 and 1, the data are moderately skewed.
# 
# If the skewness is less than -1 or greater than 1, the data are highly skewed.
# 
# We can proceed as follows:-
# 

# %%
data['stroke'].skew()

# %% [markdown]
# **Interpretation of skewness**
# 
# The skewness of our target variable storke comes out to be greater than +1. So, we can conclude that the target variable is highly positively skewed.
# 
# We can confirm this by plotting a Seaborn distplot diagram as follows:-
# 

# %%
plt.figure(figsize= (6,4))
sns.distplot(data["stroke"])
plt.title("Distribution of stroke")
plt.show()

# %% [markdown]
# **Conclusion**
# 
# The above plot confirms that the target variable stroke is highly positively skewed.
# 

# %% [markdown]
# # Multivariate analysis
# 
# Examine relationship between target variable and categorical attributes
# In the dataset, we have several categorical attributes like ever_married, work_type, Residence_type and smoking_status. In this section, I will explore the relationship between these categorical attributes and target variable.
# 
# Frequency distribution and visualization of categorical attributes
# Seasons is a categorical attribute. We can find out what categories exist and how many values belong to each category using the value_counts() method as follows:-
# 

# %%
data['ever_married'].value_counts()


# %%
# Plot
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="ever_married", hue="stroke", palette="coolwarm")

# Labels
plt.xlabel("Ever Married")
plt.ylabel("Count")
plt.title("Stroke Count Based on Marriage Status")
plt.legend(title="Stroke", labels=["No Stroke (0)", "Stroke (1)"])

# Show plot
plt.show()

# %%
# Plot
plt.figure(figsize=(8, 5))
sns.countplot(data=data, x="smoking_status", hue="stroke", palette="coolwarm")

# Labels
plt.xlabel("Smoking Status")
plt.ylabel("Count")
plt.title("Stroke Count Based on Smoking Status")
plt.legend(title="Stroke", labels=["No Stroke (0)", "Stroke (1)"])

# Show plot
plt.show()


