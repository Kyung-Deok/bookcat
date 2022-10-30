#!/usr/bin/env python
# coding: utf-8


import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

#자료 불러오기

#책 추천 함수 지정
def recommendations(name):
    path = 'C:/Users/ghen0/Downloads/recobooks_suran4/'
    data = pd.read_excel(path + 'yes24_data.xlsx')

    # Null 값이 존재하는 행 제거
    data = data.dropna(how='any')

    #TF-IDF 행렬의 크기 측정
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['production'])

    #코사인 유사도 연산
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # 책의 제목을 입력하면 해당 제목의 인덱스를 리턴받아 idx에 저장
    indices = pd.Series(data.index, index=data['name']).drop_duplicates()
    idx = indices[name]

    # 입력된 책과 줄거리가 유사한 책 10개 선정
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]

    # 가장 유사한 책 10권의 인덱스
    book_indices = [i[0] for i in sim_scores]

    # 전체 데이터 프레임에서 해당 인덱스의 행만 추출(10개 행만 가짐)
    recommend = data['name'].iloc[book_indices].reset_index(drop=True)

    # 책 제목만 리스트로 출력
    df = pd.DataFrame(recommend)
    name_list = df.loc[:, 'name'].to_list()
    return name_list

#'눈물 한 방울','만복이네 떡집'와 비슷한 책 추천(아까랑 다르게 이런식으로 하면 여러개 도출 가능)
