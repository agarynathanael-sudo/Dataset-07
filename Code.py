import pandas as pd

df = pd.read_csv("data.csv")

print("DataFrame:")
print(df)

avg_score = df["Score"].mean()
print("\nAverage Score:", avg_score)

top_student = df.loc[df["Score"].idxmax()]
print("\nTop Student:")
print(top_student)
