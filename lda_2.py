# -*- coding: utf-8 -*-
"""LDA-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lMQURXfLhEBEbWwuW20a2oFyXniJWFja
"""

!curl ipecho.net/plain

import requests
import pandas as pd
import json
import re

from google.colab import drive
drive.mount('/content/drive')

# 코랩 내의 파일 경로 설정
base_path = "/content/drive/MyDrive/4학년_1학기_마케팅/인기도서/여성영유아.csv"

# 데이터프레임을 담을 리스트 생성
dfs = []

data = pd.read_csv(base_path)
desc = data['상세정보']

import pandas as pd

base_path = "/content/drive/MyDrive/4학년_1학기_마케팅/인기도서/여성영유아.csv"
data = pd.read_csv(base_path)

dataframes = []
for info in data['상세정보']:
    df = pd.DataFrame([info])
    dataframes.append(df)

result_df = pd.concat(dataframes, ignore_index=True)
print(result_df)

test = desc.replace("'", '"')
test = test.replace("None", "null")

df = pd.DataFrame(test)

len(test)

import ast
def extract_info(row):
    info = ast.literal_eval(row)  # 문자열을 딕셔너리로 변환
    return {
        'class_nm': info.get('class_nm'),
        'bookImageURL': info.get('bookImageURL'),
        'description': info.get('description')
    }

extracted_info = df['상세정보'].apply(extract_info)

result_df = pd.DataFrame(extracted_info.tolist())

df = pd.read_csv(base_path)

#df = pd.concat([df, result_df], axis=1)
df = pd.concat([df.reset_index(drop=True), result_df.reset_index(drop=True)], axis=1)

df.to_csv("/content/drive/MyDrive/4학년_1학기_마케팅/인기도서/test.csv", index=False)

# pip install --force-reinstall pandas

base_path = "/content/drive/MyDrive/4학년_1학기_마케팅/인기도서/여성청소년.csv"
data = pd.read_csv(base_path)
desc = data['상세정보']
test = desc.replace("'", '"')
test = test.replace("None", "null")
df = pd.DataFrame(test)
extracted_info = df['상세정보'].apply(extract_info)
result_df = pd.DataFrame(extracted_info.tolist())
df = pd.read_csv(base_path)
df = pd.concat([df.reset_index(drop=True), result_df.reset_index(drop=True)], axis=1)
df.to_csv("/content/drive/MyDrive/4학년_1학기_마케팅/인기도서/여성청소년.csv", index=False)