### 데이터 전처리

# A: 2002.06.29북_경비정_NLL침범,제2연평해전.xlsx - 김대중
# B: 2008.07.11금강산_관광객_피살_사건.xlsx - 이명박
# C: 2020.06.16남북공동연락사무소_폭파_사건.xlsx - 문재인

#%%
# 패키지
import pandas as pd
import numpy as np
import re

#%%
#  업로드 : csv파일 -> 데이터프레임
kim_pre = pd.read_excel('C:/Users/osp20/OneDrive/바탕 화면/mini project/A.xlsx')
lee_pre = pd.read_excel('C:/Users/osp20/OneDrive/바탕 화면/mini project/B.xlsx')
moon_pre = pd.read_excel('C:/Users/osp20/OneDrive/바탕 화면/mini project/C.xlsx')

kim_pre.head(2)
lee_pre.head(2)
moon_pre.head(2)
#%%
# 1. 김대중 연설문 : 열 추가 (일자, 연설자, 주제, 내용, 연설문)

df1 = pd.DataFrame(kim_pre)
df1_column_1_name = '일자'
df1_column_1_values = ['2002.06.23',
                       '2002.06.23',
                       '2002.06.24',
                       '2002.06.24',
                       '2002.06.28',
                       '2002.06.28']

df1_column_2_name = '연설자'
df1_column_2_values = ['김대중',
                       '김대중',
                       '김대중',
                       '김대중',
                       '김대중',
                       '김대중']

df1_column_3_name = '주제'
df1_column_3_values = ['햇볕정책과 한반도 평화정착',
                       '한반도에 불고 있는 긍정적 변화',
                       '참전용사들의 희생과 헌신이 아니었다면',
                       '화해자로서의 아시아',
                       '행동과 인내',
                       '한국 언론의 위상']

df1_column_4_name = '내용'
df1_column_4_values = ['6·25 제52주년 민족의 화해와 일치를 위한 대미사 축하 메시지',
                       '중국 CCTV 회견',
                       '6·25 참전용사 위로연 연설',
                       '아시아종교인평화회의(ACRP) 제6차 총회 축하 메시지',
                       '라우 독일 대통령을 위한 만찬 연설',
                       '홍석현 세계신문협회장 취임 축하 메시지']

df1.insert(1, df1_column_1_name, df1_column_1_values)
df1.insert(2, df1_column_2_name, df1_column_2_values)
df1.insert(3, df1_column_3_name, df1_column_3_values)
df1.insert(4, df1_column_4_name, df1_column_4_values)

# 열의 순서를 변경
new_order_kim_pre = ['일자', '연설자', '주제', '내용', '연설문']

# reindex() 메서드를 사용하여 열의 순서를 변경
df1 = df1.reindex(columns = new_order_kim_pre)

print(df1)   

#%%
# 2. 이명박 연설문 : 열 추가 (일자, 연설자, 주제, 내용, 연설문)

df2 = pd.DataFrame(lee_pre)
df2_column_1_name = '일자'
df2_column_1_values = ['2008.07.04',
                       '2008.07.10',
                       '2008.07.11']

df2_column_2_name = '연설자'
df2_column_2_values = ['이명박',
                       '이명박',
                       '이명박',]

df2_column_3_name = '주제'
df2_column_3_values = ['none',
                       'none',
                       'none']

df2_column_4_name = '내용'
df2_column_4_values = ['반기문 UN 사무총장 방한 만찬사',
                       'F-15K 전력화 기념행사 축사',
                       '제18 국회 개원 연설']

df2.insert(1, df2_column_1_name, df2_column_1_values)
df2.insert(2, df2_column_2_name, df2_column_2_values)
df2.insert(3, df2_column_3_name, df2_column_3_values)
df2.insert(4, df2_column_4_name, df2_column_4_values)

# 열의 순서를 변경
new_order_lee_pre = ['일자', '연설자', '주제', '내용', '연설문']

# reindex() 메서드를 사용하여 열의 순서를 변경
df2 = df2.reindex(columns = new_order_kim_pre)

print(df2)                   

#%%
# 3. 문재인 연설문 : 열 추가 (일자, 연설자, 주제, 내용, 연설문)

df3 = pd.DataFrame(moon_pre)
df3_column_1_name = '일자'
df3_column_1_values = ['2020.06.09',
                       '2020.06.10',
                       '2020.06.10',
                       '2020.06.15',
                       '2020.06.15']

df3_column_2_name = '연설자'
df3_column_2_values = ['문재인',
                       '문재인',
                       '문재인',
                       '문재인',
                       '문재인']

df3_column_3_name = '주제'
df3_column_3_values = ['none',
                       'none',
                       'none',
                       'none',
                       'none']

df3_column_4_name = '내용'
df3_column_4_values = ['제30회 국무회의',
                       '가봉 해상 피랍 국민 무사귀환 관련 메시지',
                       '제33주년 6·10민주항쟁 기념식',
                       '6·15남북공동선언 20주년 기념식 영상 축사',
                       '수석·보좌관회의']

df3.insert(1, df3_column_1_name, df3_column_1_values)
df3.insert(2, df3_column_2_name, df3_column_2_values)
df3.insert(3, df3_column_3_name, df3_column_3_values)
df3.insert(4, df3_column_4_name, df3_column_4_values)

# 열의 순서를 변경
new_order_moon_pre = ['일자', '연설자', '주제', '내용', '연설문']

# reindex() 메서드를 사용하여 열의 순서를 변경
df3 = df3.reindex(columns = new_order_moon_pre)

print(df3)
################################################################################

#%%

# 각 대통령별 사용 단어 빈도
# 1. 김대중

# 연설문 인덱싱
df1 = df1.loc[:,'연설문']
df1 = str(df1)

#%%
# 연설문의 모든 행을 'line1'에 추가
line1 = []
for i in range(len(df1)):
    line1.append(df1[i])
print(df1)

#%%
# 특수문자 제거
compile1 = re.compile("[^ ㄱ-ㅣ가-힣]+")
for i in range(len(df1)):
    a = compile.sub("",df1[i])
    df1[i] = a
print(df1)

#%%
# 리스트 -> 문자열로 변경 및 분할
df1 = str(df1)

#%%
# 명사만 추출하기
from konlpy.tag import Komoran
komoran = Komoran()
df1 = komoran.nouns(df1)

#%%
# 단어 빈도 개수 세기
from collections import Counter
df1_words_counts = Counter(df1)
print(df1_words_counts)

#%%
# 단어 빈도 개수 기준 내림차순 정렬
df1 = df1_words_counts.most_common()
# 상위 10개 항목 나열
top10 = df1[:10]
top10