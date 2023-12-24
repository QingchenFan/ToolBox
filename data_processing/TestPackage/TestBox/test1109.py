from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

documents = ["机器学习是人工智能的一部分","我喜欢看电影和听音乐", "人工智能在我们生活中的应用越来越广泛"]

# 使用TF-IDF将文本转化为矩阵：用TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents)
print(vectorizer)
print(tfidf)

# 执行NMF
nmf = NMF(n_components=2)  # 这里我们告诉NMF我们希望得到2个主题
W = nmf.fit_transform(tfidf)
H = nmf.components_

print("TF-IDF矩阵：", tfidf.toarray())
print("W矩阵：", W)
print("H矩阵：", H)
