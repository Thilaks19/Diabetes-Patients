import numpy as np # for linear algebra
import pandas as pd # data processing, CSV file I/O, etc
import seaborn as sns # for plots
import plotly.graph_objects as go # for plots
import plotly.express as px #for plots
import matplotlib.pyplot as plt # for visualizations and plots
import missingno as msno # for plotting missing data


df = pd.read_csv("C:/Users/THILAK.S/Downloads/Project 2 MeriSKILL/diabetes.csv")
df.head() # displays the top 5 values in the dataset


df.info()


df.describe()


df.isnull().sum()


df["Glucose"] = df["Glucose"].apply(lambda x: np.nan if x == 0 else x)
df["BloodPressure"] = df["BloodPressure"].apply(lambda x: np.nan if x == 0 else x)
df["SkinThickness"] = df["SkinThickness"].apply(lambda x: np.nan if x == 0 else x)
df["Insulin"] = df["Insulin"].apply(lambda x: np.nan if x == 0 else x)
df["BMI"] = df["BMI"].apply(lambda x: np.nan if x == 0 else x)



df.isnull().sum()



px.pie(df, names="Outcome")



sns.countplot(x="Outcome", data=df, palette=random.choice(pallete))


sns.countplot(x="Pregnancies", hue = "Outcome", data=df, palette=random.choice(pallete))



sns.histplot(x="Pregnancies", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))


sns.histplot(x="BloodPressure", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))



sns.histplot(x="Glucose", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))


sns.histplot(x="SkinThickness", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))


sns.histplot(x="Insulin", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))



sns.histplot(x="Age", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))



sns.histplot(x="BMI", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))



sns.histplot(x="DiabetesPedigreeFunction", hue="Outcome", data=df, kde=True, palette=random.choice(pallete))


sns.pairplot(df, hue='Outcome',palette=random.choice(pallete))


fig, axs = plt.subplots(4, 2, figsize=(20,20))
axs = axs.flatten()
for i in range(len(df.columns)-1):
    sns.boxplot(data=df, x=df.columns[i], ax=axs[i], palette=random.choice(pallete))


sns.heatmap(df.corr(), linewidths=0.1, vmax=1.0, square=True, cmap='coolwarm', linecolor='white', annot=True).set_title("Correlation Map")



df.isnull().sum()


msno.bar(df)


msno.matrix(df, figsize=(20,35))


msno.heatmap(df, cmap=random.choice(pallete))


msno.dendrogram(df)


df.isnull().sum()/len(df)*100


df.drop(columns=["Insulin"], inplace=True)


df.describe()



df.skew()



# Highly skewed
df["BMI"].replace(to_replace=np.nan,value=df["BMI"].median(), inplace=True)
df["Pregnancies"].replace(to_replace=np.nan,value=df["Pregnancies"].median(), inplace=True)

# Normal
df["Glucose"].replace(to_replace=np.nan,value=df["Glucose"].mean(), inplace=True)
df["BloodPressure"].replace(to_replace=np.nan,value=df["BloodPressure"].mean(), inplace=True)
df["SkinThickness"].replace(to_replace=np.nan,value=df["SkinThickness"].mean(), inplace=True)



Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)




df_out = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(f'Before: {df.shape}, After: {df_out.shape}')


for col in df.columns[:-1]:
    up_out = df[col].quantile(0.90)
    low_out = df[col].quantile(0.10)
    med = df[col].median()
#     print(col, up_out, low_out, med)
    df[col] = np.where(df[col] > up_out, med, df[col])
    df[col] = np.where(df[col] < low_out, med, df[col])


df.describe()

