#!/user/bin/env python
# coding=utf-8
"""
@file: tfidf替换.py
@author: zwt
@time: 2021/2/1 16:23
@desc: 计算保存好相应词的tfidf，用tfidf低的词语替换当前句子中tfidf低的词语
"""
from gensim.models.tfidfmodel import TfidfModel
from gensim import corpora


if __name__ == "__main__":
    corpus = []
    tfidfdict = {}
    f_res = open('data/data_tfidf.txt', 'w', encoding='utf8')
    for line in open('data/data.txt', 'r', encoding='utf8').readlines():
        corpus.append(line.strip().split(' '))

    # 赋给语料库中每个词(不重复的词)一个整数id
    dictionary = corpora.Dictionary(corpus)
    corpus = [dictionary.doc2bow(text) for text in corpus]
    tf_idf_model = TfidfModel(corpus, normalize=False)
    word_tf_tdf = list(tf_idf_model[corpus])
    # print('词频:', corpus)
    temp = {v: k for k, v in dictionary.token2id.items()}
    for i in word_tf_tdf:
        print(i[0][1], '=', temp.get(i[0][0]))
        f_res.write(temp.get(i[0][0]).strip()+','+str(i[0][1]).strip() + '\n')