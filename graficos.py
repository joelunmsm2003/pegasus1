import pandas as pd
reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)

reviews['province'].value_counts().head(10).plot.bar()

import seaborn as sns


tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips);

