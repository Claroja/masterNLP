from gensim import corpora, models, similarities
import gensim

texts=[[]]
dictionary = corpora.Dictionary(texts)  # 每个单词用index代替,提高运算效率
corpus = [dictionary.doc2bow(text) for text in texts]  # 转换为数组,数组每个元素是元组,元组第一位是词语对应的index,第二位是出现次数
lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)  # lda建模
lda.print_topics(num_topics=20, num_words=5) # 打印所有主题