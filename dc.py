import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("marketing_campaign.csv", sep="\t")

missing_before = df.isnull().sum()

df["Income"] = df["Income"].fillna(df["Income"].median())

duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

df.columns = df.columns.str.strip().str.lower()

missing_after = df.isnull().sum()

cleaning_report = pd.DataFrame({
    "Missing Before": missing_before,
    "Missing After": missing_after
})

cleaning_report.to_excel("cleaning_report.xlsx")

summary_report = df.describe(include="all")
summary_report.to_excel("summary_report.xlsx")

plt.figure(figsize=(8, 5))
df["income"].hist(bins=20)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Count")
plt.savefig("income_distribution.png")
plt.close()

city_sales = df.groupby("country")["mntwines"].sum() if "country" in df.columns else df["mntwines"]

plt.figure(figsize=(8, 5))
if "country" in df.columns:
    city_sales.plot(kind="bar")
else:
    df["mntwines"].head(20).plot(kind="bar")
plt.title("Wine Spending Analysis")
plt.savefig("wine_spending.png")
plt.close()

print("Data Cleaning Completed")
print("Duplicates Removed:", duplicates_removed)
print("Reports Generated:")
print("- cleaning_report.xlsx")
print("- summary_report.xlsx")
print("- income_distribution.png")
print("- wine_spending.png")