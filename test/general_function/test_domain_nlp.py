import accuasset
import pandas as pd

df = pd.read_csv('../test_data/dir_list.csv')

# print(df.columns)
# print(df.shape)
# print(df.head(3))

accuasset.domain.nlp.preprocessing.test()
#accuasset.domain.nlp.preprocessing.preprocess_txt(df, 'type')