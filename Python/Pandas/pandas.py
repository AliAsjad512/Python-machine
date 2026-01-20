import pandas as pd

df = pd.DataFrame({
    "age": [25, 30, 22],
    "score": [80, 85, 90],
    "passed": [True, True, True]
})

# Feature selection using label
X = df.loc[:, ["age", "score"]]   # Select age and score columns
print(X)

# Feature selection using position
X = df.iloc[:, 0:2]      
print(X)