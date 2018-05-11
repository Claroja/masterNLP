

def prepro(text):
    text = text.replace('\n', " ")  # 去掉换行符
    text = text.replace(r'-',' ')  # 将横线连接的词语去掉
    text = text.replace(r"\d+/\d+/\d+", "")  # 去除日期
    text = text.replace(r"[0-2]?[0-9]:[0-6][0-9]", "")  # 去除时间
    text = text.replace(r"[\w]+@[\.\w]+", "")  # 去除邮件地址
    text = text.replace(r"/[a-zA-Z]*[:\//\]*[A-Za-z0-9\-_]+\.+[A-Za-z0-9\.\/%&=\?\-_]+/i", "")  # 去除网址
    return text



