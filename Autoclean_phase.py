from AutoClean import AutoClean
import pandas as pd

resultant = pd.read_csv("sales.csv")
pipeline = AutoClean(resultant)
x=pipeline.output
print(x)