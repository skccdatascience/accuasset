import re
import numpy as np
import pandas

def test():
    print('\n', )
    print('domain > nlp 에 preprocessing 입니다.')

def preprocess_txt(df, DATA_COLUMN):
    df[DATA_COLUMN] = df[DATA_COLUMN].str.replace(r'\${img=[a-zA-Z0-9_.]+}', '')  # 이미지 태그 제거
    df[DATA_COLUMN] = df[DATA_COLUMN].str.replace(r'[a-zA-Z0-9_-]+@[a-z]+.[a-z]+', '')  # 메일 제거
    df[DATA_COLUMN] = df[DATA_COLUMN].str.replace(r'http[a-zA-Z0-9.:/?=_-]+', '')  # url 제거
    df[DATA_COLUMN] = df[DATA_COLUMN].str.replace(r'\\u\d+', '')  # 유니코드 문자열 제거
    df[DATA_COLUMN] = df[DATA_COLUMN].str.replace(r'010-\d{4}-\d{4}', '')  # 핸드폰 번호 제거
    df[DATA_COLUMN] = df[DATA_COLUMN].str.replace(r'[^a-zA-Z가-힣0-9\s]+', "", regex=True)
    df[DATA_COLUMN] = df[DATA_COLUMN].str.split().str.join(' ') # 다중 공백 제거
    print(df.head())
    print("데이터 전처리 완료")
    return df