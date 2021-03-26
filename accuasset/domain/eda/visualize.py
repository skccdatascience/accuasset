from wordcloud import WordCloud
from collections import Counter
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import seaborn as sns
import missingno as msno
import os

# To Do: 1) 시각화 default setting 설정

def test():
    print('\n', )
    print('domain > eda에 visualize입니다.')

FILE = os.path.dirname(__file__)
FONT_PATH = os.environ.get('FONT_PATH', os.path.join(FILE, 'NanumGothic.ttf'))

############################## matplotlib : default font setting ################################
# reference: https://jehyunlee.github.io/2020/02/13/Python-DS-2-matplotlib_defaults_and_fonts/
# print('버전: ', mpl.__version__)
# print('설치 위치: ', mpl.__file__)
# print('설정 위치: ', mpl.get_configdir())
# print('캐시 위치: ', mpl.get_cachedir())
# print('설정파일 위치: ', mpl.matplotlib_fname())
# [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]
# font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# print(font_list[:100])
font_prop = fm.FontProperties(fname=FONT_PATH, size=10).get_name()
plt.rc('font', family=font_prop)
fm._rebuild()
mpl.rcParams['axes.unicode_minus'] = False
# print(fontprop)
#################################################################################################

# 우선 아래 설정으로 한글 폰트 출력 확인
mpl.rcParams['font.family'] = "AppleGothic"

def get_cloud(df, target_column, conditional_value='', conditional_column='all'):

    if conditional_column=='all':
        text = df[target_column].to_list()
    else:
        text = df[df[conditional_column]==conditional_value][target_column].to_list()

    count = Counter(text)
    words = dict(count.most_common())

    plt.figure(figsize=(14,10)) #이미지 사이즈 지정

    wordcloud = WordCloud(font_path=FONT_PATH, background_color='white').generate_from_frequencies(words)

    plt.imshow(wordcloud,interpolation='lanczos')
    plt.axis('off')
    #plt.set_title(str(target_column), fontsize=20)
    plt.show()

def get_missing_matrix(df):
    msno.matrix(df)
    plt.show()

def get_missing_bar(df):
    msno.bar(df)
    plt.show()

def get_top_counts(df, col, num):
    ax = sns.countplot(y=col, data=df, order=df[col].value_counts()[:num].index)
    plt.title(f'Top {num} counts', fontproperties = fontprop)
    plt.show()

def SentanceInspect(_column):
    maxval = 0
    list = _column.tolist()
    tokenized_list = [r.split() for r in list]
    sentence_len_by_token = [len(t) for t in tokenized_list]
    sentence_len_by_eumjeol = [len(s.replace(' ', '')) for s in list]
    for s in list:
        if len(s.replace(' ', '')) > 15000:
            if maxval < len(s):
                maxval = len(s)
                # print('len: ',len(s))
        # print('s: ',s)

    for t in tokenized_list:
        if len(t) == 0:
            print()
    print('maxval : ', maxval)
    plt.figure(figsize=(12, 5))
    plt.hist(sentence_len_by_token, bins=50, alpha=0.5, color="r", label="word")
    plt.hist(sentence_len_by_eumjeol, bins=50, alpha=0.5, color="b", label="aplt.yscallphabet")
    plt.yscale('log', nonposy='clip')
    plt.title(_column.name)
    plt.xlabel('red:token / blue:eumjeol length')
    plt.ylabel('number of sentences')
    plt.show()

    print('\n', )
    print('칼럼명 : {}'.format(_column.name))
    print('토큰 최대 길이 : {}'.format(np.max(sentence_len_by_token)))
    print('토큰 최소 길이 : {}'.format(np.min(sentence_len_by_token)))
    print('토큰 평균 길이 : {:.2f}'.format(np.mean(sentence_len_by_token)))
    print('토큰 길이 표준편차 : {:.2f}'.format(np.std(sentence_len_by_token)))
    print('토큰 중간 길이 : {}'.format(np.median(sentence_len_by_token)))
    print('제 1사분위 길이 : {}'.format(np.percentile(sentence_len_by_token, 25)))
    print('제 3사분위 길이 : {}'.format(np.percentile(sentence_len_by_token, 75)))

