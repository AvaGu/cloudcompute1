#from bs4 import BeautifulSoup
#import unicodedata
import nltk
from urllib import urlopen
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn

from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import enchant
import json
import urllib2

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = {}
    in_content = False
    lemmatizer = WordNetLemmatizer()
   # if lemmatizer.lemmatize("printing") != lemmatizer.lemmatize("printed"):
    #    print "true"
    for w in text:
        w = w.upper()
        x = enchant.Dict("en_US")
 #       if x.check('YORK'):
  #          print "why???????????????"
        if len(w) != 1 and w[0] >= 'A' and w[0] <= 'Z' and x.check(w):
            if w.lower() not in stopwords:
                b = lemmatizer.lemmatize(w)
                if b in content:
                    content[b] = content[b] + 1
                else:
                    content[b] = 1
 
    return content

        
'''
soup = BeautifulSoup(open("Painting.html"))
x = soup.get_text()
print type(x)
#s = x.decode('ascii','ignore')
y = unicodedata.normalize('NFKD', x).encode('ascii','ignore')
print type(x)
#soup = BeautifulSoup("<html>data</html>")

#print soup
print y

path = r'~\eecs495\output.txt'

#Results are saved to txt file
file = open(path, 'w')
file.write(y)
file.close()

'''

search_word = "opera"
top_num_words = 10
search_result_size = 8


def analyzeWord(search_word):
    print "Searching for word : " + search_word

    search_line = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=' + str(search_result_size) + '&q='+search_word
    # print search_line
    response = urllib2.urlopen(search_line)
    search_results = json.loads(response.read())
    l = search_results['responseData']['results']
    #print(search_results['responseData']['results'])
    url = ""
    count = 0
    for link in l:
        count += 1
        url = link["url"]
        print "\tFor search result url : " + url
        html = urlopen(url).read()
        raw = nltk.clean_html(html)
        tokens = nltk.word_tokenize(raw)
    #print tokens
        my_dict = {}
        my_dict = content_fraction(tokens)
    #print my_dict

        for n in range(top_num_words):
            if my_dict:
                m = max(my_dict, key = my_dict.get)
                #print type(m)
                print "\t\t " + str(n +1) + " : " +  str(m) + " : " +  str(my_dict[m])
                # print my_dict[m]
                my_dict.pop(m, None)


analyzeWord("opera")

