import accuasset
import pandas as pd
import seaborn as sns

df = pd.read_csv('../test_data/dir_list.csv')

# print(df.columns)
# print(df.shape)
# print(df.head(3))

# accuasset.domain.eda.visualize.get_cloud(df,target_column='type')
accuasset.domain.eda.visualize.test()

# accuasset.domain.eda.visualize.get_missing_matrix(df)
# accuasset.domain.eda.visualize.get_missing_bar(df)

#accuasset.domain.eda.visualize.get_top_counts(df, 'type', 15)
#accuasset.domain.eda.visualize.SentanceInspect(df['type'])