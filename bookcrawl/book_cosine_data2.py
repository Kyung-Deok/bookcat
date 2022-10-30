#!/usr/bin/env python
# coding: utf-8

# In[54]:


import urllib.request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import sys
import re
from PIL import Image
from io import BytesIO
from nltk.tokenize import RegexpTokenizer
import nltk
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt

# In[63]:


path = 'C:/Users/ghen0/Downloads/recobooks_suran4/'

df0 = pd.read_excel(path + '예스24.xlsx')
df1 = pd.read_excel(path + '예스24_1.xlsx')
df2 = pd.read_excel(path + '예스24_2.xlsx')
df3 = pd.read_excel(path + '예스24_3.xlsx')

# In[64]:


#합병한 결과를 담을 객체
dataframe = pd.concat([df0, df1, df2, df3],axis=0)

# In[65]:


dataframe.to_excel('C:/Users/ghen0/Downloads/recobooks_suran4/yes24_data.xlsx', index=False)

# In[66]:


# path = 'C:/Users/ghen0/Downloads/recobooks_suran4'

data = pd.read_excel(path + 'yes24_data.xlsx')
data.head(3)

# In[67]:


# 개수 출력

print(len(data))

# In[68]:


# NULL 값 존재 유무

print(data.isnull().values.any())

# In[69]:


# Null 값이 존재하는 행 제거
data = data.dropna(how = 'any')

# Null 값이 존재하는지 확인
print(data.isnull().values.any())

# In[70]:


print(len(data))

# In[88]:


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['production'])
print('TF-IDF 행렬의 크기(shape) :',tfidf_matrix.shape)

# In[89]:


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print('코사인 유사도 연산 결과 :',cosine_sim.shape)

# In[90]:


name_to_index = dict(zip(data['name'], data.index))

# 268번째줄 책 제목'보도 섀퍼의 돈' 인덱스를 리턴
idx = name_to_index['보도 섀퍼의 돈']
print(idx)

# In[91]:


def get_recommendations(name, cosine_sim=cosine_sim):
    # 선택한 책의 제목으로부터 해당 책의 인덱스를 받아온다.
    idx = name_to_index[name]

    # 해당 책과 모든 책의 유사도를 가져온다.
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 책들을 정렬한다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 책을 받아온다.
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개의 영화의 인덱스를 얻는다.
    book_indices = [idx[0] for idx in sim_scores]

    # 가장 유사한 10개의 책의 제목을 리턴한다.
    return data['name'].iloc[book_indices]

# In[92]:


#75번째줄
get_recommendations('수박 수영장')

# In[93]:


#182번째줄
get_recommendations('해커스 토익 실전 1000제 1 RC Reading 문제집 (리딩)')

# In[94]:


#190번째줄(어린이책)
get_recommendations('만복이네 떡집')

# In[95]:


#302번째줄(에세이)
get_recommendations('똥 쌀 때 읽는 책')
