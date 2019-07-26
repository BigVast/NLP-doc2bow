#encoding=utf-8

from gensim import corpora, models, similarities
import jieba
from collections import defaultdict

# corpora是gensim中的一个基本概念，是文档集的表现形式，也是后续进一步处理的基础。
# jieba.load_userdict("C:/Users/yyq/Desktop/毕业论文/词典.txt") # 加载自定义字典

f1 = open('D:/test1.txt', 'r+').read()
f2 = open('D:/test2.txt', 'r+').read()

data1 = jieba.cut(f1)
data2 = jieba.cut(f2)

data11 = ""
for item in data1:
    data11 += item + " "

data21 = ""
for item in data2:
    data21 += item + " "

documents = [data11, data21]  # 存储到列表
print(data11)
print(documents)

texts = [[word for word in document.split()] for document in documents]

#print(texts)

frequency = defaultdict(int)  # 创建统计字典，统计词频

for text in texts:
    for token in text:
        frequency[token] += 1

# print(frequency)
# texts=[[word for word in text if frequency[token]>2]for text in texts] # 去掉词频少于两次的词语

dictionary = corpora.Dictionary(texts)  # corpora是 gensim 中的一个基本概念，是文档集的表现形式，也是后续进一步处理的基础。
#print(dictionary)
featureNum = len(dictionary.token2id.keys())  # 一共有228个特征词语
#print(featureNum)

# 这一步是将文档存入字典，字典有很多功能

f3 = open('D:/test3.txt', 'r+').read()

data3 = jieba.cut(f3)
data31 = ""

#print(data31)
for item in data3:
    data31 += item + "  "
new_doc = data31

new_vec = dictionary.doc2bow(new_doc.split())

#print(new_vec) # 123.txt里面有四行文字，print后也有四个二维向量,所以就是把每一行分词后向量化

corpus = [dictionary.doc2bow(text) for text in texts]  # 基于词典，将【分词列表集】转换成【稀疏向量集】，称作【语料库】

# corpora.MmCorpus.serialize("D:/4.txt", corpus)

tfidf = models.TfidfModel(corpus)  # 将上一步形成的向量载入TF-IDF模型

# featureNum = len(dictionary.token2id.keys())  # 一共有228个特征词语

index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=featureNum)  # 对【稀疏向量集】建立【索引】

sim = index[tfidf[new_vec]]  # 相似度计算

print(sim)
