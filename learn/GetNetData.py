# coding=utf-8
import os
import re
import jieba
default_encoding = 'utf-8'

def getNetData(disease_name):

    dir="/home/DataSet/data_"+disease_name
    f_all=open(disease_name+".txt","w",encoding='utf-8') #python就是用的utf-8格式，必须注明，不然文件写的时候默认gbk就会对不上

    for root,dirs,files in os.walk(dir):
        for file in files:
            postfix=file[-3:]
            if postfix=='txt':
                f = open(os.path.join(root,file), "r",encoding='utf-8')  # 设置文件对象
                str = f.read()  # 将txt文件的所有内容读入到字符串str中
                f_all.write(str)
                f.close()  # 将文件关闭
    f_all.close()

    stopwords=[]
    for word in open('/home/DataSet/chinesestopword.txt','r',encoding='utf-8'):
        stopwords.append(word.strip())

    word_dict={}
    with open(disease_name+".txt", 'r',encoding='utf-8') as f:
        for line in f:
            if line[:2]=="内容" :
                text=line[3:]
                # print('new_line:  '+text, end='')
                seg_list = list(jieba.cut(text))
                # print(u"[全模式]: ", "/ ".join(seg_list))

                for word in seg_list:
                    # print('word=',word)
                    if bool(re.search('[a-z]', word)):
                        continue
                    if word in stopwords:
                        continue

                    if word not in word_dict:
                        word_dict[word] =1
                    else:
                        word_dict[word] += 1

    # print('word_dict=',word_dict)
    sorted_dict = sorted(word_dict.items(), key = lambda x:x[1],reverse=True)
    sorted_dict=sorted_dict[1:21] #取前20个
    # print('sorted_dict=',sorted_dict)

    key_list=[]
    value_list=[]
    for key,value in sorted_dict:
         key_list.append(key)
         value_list.append(value)
    # print(key_list)
    # print(value_list)
    return key_list,value_list