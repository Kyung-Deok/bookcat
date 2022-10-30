import folium
import pandas as pd
import json
from sklearn.preprocessing import MinMaxScaler

df = pd.read_excel(r'/Users/user/Downloads/2020년_서울시도서관_대출권수.xls')
df = df[["자치구", "연간대출 책수"]]
df = df.drop([0,1], axis=0)
# print(df)
seoul_latlng = pd.read_excel(r'/Users/user/Downloads/seoullatlng.xlsx')
# print(seoul_latlng['lat'][24])
library_list = pd.read_excel(r'/Users/user/Downloads/lib_list.xlsx')
print(library_list)


stand_x = df.drop(['자치구'], axis=1)
transformer = MinMaxScaler()
transformer.fit(stand_x)
stand_x = transformer.transform(stand_x)
# print(stand_x)

# print(df)
# print((df['연간대출 책수']).mean())
# normalization = (df['연간대출 책수'] - df['연간대출 책수'].mean())/df['연간대출 책수'].std()
# normalization_df = pd.DataFrame({'정규화 책수': normalization})
# print(normalization_df)
# ndf = pd.concat([df, normalization_df], axis=1)
# ndf = ndf.drop(12, axis=0)

stand_x = pd.DataFrame(stand_x)
stand_x.columns = ['정규화 책수']
# print(type(stand_x))
# stand_x.index = ["2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
stand_x.index = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

# print(stand_x)

ndf = pd.concat([df, stand_x], axis=1)
# ndf = ndf.drop([0,1], axis=0)
ndf = ndf.drop(12, axis=0)
# print(ndf)

geo_path = ('./skorea_municipalities_geo_simple.json')

geo_str = json.load(open(geo_path, encoding='utf-8'))

seoul_map = folium.Map(location=[37.56668, 126.97843], zoom_start=11)
# print(seoul_map)

# seoul_map.save('./test.html')

# folium.Choropleth(
#     geo_data = geo_str,
#     data = df,
#     columns = ['자치구', '연간대출 책수'],
#     fill_color='OrRd',
#     key_on='feature.properties.name'
# ).add_to(seoul_map)

# seoul_map.save('./map.html')
#
#


# gugunlist = []


import matplotlib.pyplot as plt

li = []
# for i in range(125):
a = library_list['gungu'].values
li2 = list(set(a))
b = library_list['gungu']
# for j in li2:
#     print(library_list.loc[j, 'bookname'])

context = {}
for j in li2:
    library_list.set_index('gungu')
    context['b'] = list(library_list.loc[j, 'bookname'])
    print(context['b'])


folium.Choropleth(
    geo_data = geo_str,
    data = ndf,
    columns = ['자치구', '연간대출 책수'],
    fill_color='OrRd',
    key_on='feature.properties.name'
).add_to(seoul_map)


for i in range(0, 25):
    folium.CircleMarker(
        location=[seoul_latlng['lat'][i], seoul_latlng['lng'][i]],
        radius=30,
        fill=True,
        color = '##18c729',
        fill_color = '#558257',
        tooltip = [seoul_latlng['gungu'][i], seoul_latlng['연간대출 책수'][i]],
        # popup = popup,
        fill_opacity=0.3
    ).add_to(seoul_map)

# plt.imshow(seoul_map)
seoul_map.save('./testcircle.html')