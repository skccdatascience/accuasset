import accuasset
import pandas as pd

df = pd.read_csv('../test_data/dir_list.csv')

accuasset.domain.nlp.preprocessing.test()
#accuasset.domain.nlp.preprocessing.preprocess_txt(df, 'type')