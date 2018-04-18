import pandas as pd
df = pd.read_csv('Consumer_Complaints.csv')
df.head()


from io import StringIO
col = ['Product', 'Consumer complaint narrative']
df = df[col]  # 获取需要的投诉内容和产品列
df = df[pd.notnull(df['Consumer complaint narrative'])]  # 删除空列
df.columns = ['Product', 'Consumer_complaint_narrative']  # 将投诉内容列从新命名,加上下划线
df['category_id'] = df['Product'].factorize()[0]  # 将product列做整数化处理,一个数字代表一个类别
category_id_df = df[['Product', 'category_id']].drop_duplicates().sort_values('category_id')  # 获得类别编号和类别的对应关系
category_to_id = dict(category_id_df.values)   # 分类-编号字典
id_to_category = dict(category_id_df[['category_id', 'Product']].values)  # 编号分类字典
df.head()


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
df.groupby('Product').Consumer_complaint_narrative.count().plot.bar(ylim=0)  # 做类别数量统计
plt.show()



from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1',
ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.Consumer_complaint_narrative).toarray()
labels = df.category_id
features.shape


from sklearn.feature_selection import chi2
import numpy as np
N = 2
for Product, category_id in sorted(category_to_id.items()):
    features_chi2 = chi2(features, labels == category_id)
    indices = np.argsort(features_chi2[0])
    feature_names = np.array(tfidf.get_feature_names())[indices]
    unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
    bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
    print("# '{}':".format(Product))
    print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
    print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))





from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
X_train, X_test, y_train, y_test = train_test_split(df['Consumer_complaint_narrative'], df
['Product'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, y_train)


print(clf.predict(count_vect.transform(["This company refuses to provide me verification\
and validation of debt per my right under the FDCPA. I do not believe this debt is mine."
])))