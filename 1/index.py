# coding=utf8
import jieba
import jieba.analyse
import urllib.request
import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from os import path
import matplotlib.pyplot as plt
font_path = path.join('SimHei.ttf')


def getHTMLContent():
    url = "https://juejin.im/post/5d8d9eeaf265da5b783ef45c"
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    reg = re.compile('<[^>]*>')
    html = reg.sub('', html)
    return html


def analyseContent(sentence):
    # https://gist.github.com/luw2007/6016931
    keywords = jieba.analyse.extract_tags(
        sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    return keywords


def makeImage(text):
    wc = WordCloud(font_path=font_path,
                   background_color="white", max_words=1000)
    wc.generate_from_frequencies(text)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


sentence = getHTMLContent()
keywords = analyseContent(sentence)

dict = {}
for item in keywords:
    dict[item[0]] = item[1]

makeImage(dict)
