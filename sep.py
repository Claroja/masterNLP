stoplist = []
import jieba
stopwords = [line.strip() for line in open("./stopwords.txt", 'r', encoding='utf-8').readlines()] # 获得停词表，停词表可以在网上搜集
def word_counts(text):
    seg_list = jieba.cut(text)  # 使用结巴对文本分词
    words_list=[]
    for word in seg_list:
        if word not in stopwords: # 去除停用词
            if not word.isspace() and len(word)>1: # 去除空白以及单个的词
                words_list.append(word)
    counts=pd.Series(words_list).value_counts() # 统计词频
    return counts # 返回的是Series所以可以直接用to_csv来保存