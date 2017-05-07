import re
import pandas as pd
import numpy as np
from gensim.models import Word2Vec

# 파일읽고
file = open("C:/Users/bogard/Downloads/moby1.txt")
moby_dick = file.read()
print(moby_dick)

print("<raw_doc", "_" * 100)

# 문장별로 쪼개서
moby_dick = re.split("[\n\.?]", moby_dick)
print(moby_dick)

print("<split_doc", "_" * 100)

# 공백처리하고
while ' ' in moby_dick:
    moby_dick.remove(' ')
    moby_dick.remove('')

    print(moby_dick)
print("<remove_blank_doc", "_" * 100)

# 데이터프레임에 저장해서
df_Mobydic = pd.DataFrame()
df_Mobydic['sentences'] = np.asarray(moby_dick)

print(df_Mobydic)
print("<df_doc", "_" * 100)

# 데이터프레임 문장별 split
df_Mobydic["separates"] = df_Mobydic["sentences"].apply(lambda x: x.replace(",", ""))
df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.replace(";", ""))
df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.replace("\"", ""))
df_Mobydic["separates"] = df_Mobydic["separates"].apply(lambda x: x.split())

print(df_Mobydic)

# 문장별 word2vec 처리
model = Word2Vec(df_Mobydic["separates"], hs=1, size=300, min_count=5)
print(model)

for word, score in model.most_similar("whale".encode('utf-8')):
    print(word)
