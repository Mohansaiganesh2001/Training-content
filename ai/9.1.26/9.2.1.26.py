# Pandas - pip install pandas

import pandas as pd
from bs4 import BeautifulSoup
import re

df = pd.read_csv('IMDB Dataset.csv')

print(df.head(4))


def clean_str(str):
    str = BeautifulSoup(str, 'html.parser').get_text()
    str = re.sub(r'http\S+|www\S+', '', str)
    str = re.sub(r'[^\x00-\x7f]+', '', str)
    str = re.sub(r'[^A-Za-z0-9\s]', '', str)
    str = re.sub(r'\s+', ' ', str)
    return str

df['cleaned_review'] = df['review'].apply(clean_str)

for i in range(5):
    print(f'Review: {i + 1}')
    print(df.loc[i, 'review'])
    print(df.loc[i, 'cleaned_review'])
    print('-' * 450)

output_file = 'IMDB Dataset Cleaned Reviews.csv'

df[['cleaned_review', 'sentiment']].to_csv(output_file, index=False)

