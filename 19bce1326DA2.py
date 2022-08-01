


## 19BCE1326  DA2



C:\Users\Sriman>python
Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

import nltk
nltk.download ()

from nltk.tokenize import sent_tokenize, word_tokenizefrom

data="Recent times have witnessed an explosion in the amount of biological data generated. There are millions of research articles with pivotal information on human health and disease, spanning from single molecule resolution to the level of the whole organism. However, this information is scattered in different databases, repositories and in the text of journal articles. This makes the seamless extraction of scientific information an extremely challenging and time-consuming (yet incomplete) process. With 100+ databases and millions of data points (combined) from just human cells/tissue and disease, there is a pressing need to collate this information in such a way that users like academic/industrial/clinical researcher as well as teachers and students can easily access information that is relevant to them from a common and modular platform. Although there are ambitious ongoing efforts like the Recon X, The Virtual Physiological Human, Human Cell Atlas, none of these projects aim to build the map of the whole human body simultaneously comparing both macro(organ/tissue/cell) and micro (molecular interaction networks) level details. Manav-Human Atlas Initiative aims to construct a comprehensive map of the entire human body which will explicitly document macro to micro level information. The project Manav will dramatically accelerate our understanding of the working of the human body and help design better therapeutic targets for treating diseases like cancer, diabetes and more. This project will require understanding, extracting and collating information from millions of scientific papers which would need a massive investment of time, effort and manpower. The large pool of scientifically literate population in India pursuing a bachelors /masters / Ph.D. is a great resource that will be trained and engaged as part of this project to use the annotation tool being developed to collate, curate, manage and visualize this scientific information. This project is funded by Department of Biotechnology (DBT), Government of India as a collaboration between Persistent Systems, NCCS and IISER, Pune."

#TOKENIZATION :
#Sentence Tokenizer
sentences=sent_tokenize(data)
print(sentences)
#Word Tokenizer
words=word_tokenize(data)
print(words)

import re
from nltk.corpus import stopwords

data = data.lower()
data = data.split()
data = [word for word in data if not word in set(stopwords.words('english'))]
data = ' '.join(data)
print(data)

#Create object of PorterStemmer
stemmer=PorterStemmer()

for i in range(len(sentences)):
    words=word_tokenize(sentences[i])
    #List comprehension
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)
print(sentences)

#Stemming with lemmatization to get proper meaning words after stemming
#Create obj of Lemmatizer
lemmmatizer=WordNetLemmatizer()

for i in range(len(sentences)):
    words=word_tokenize(sentences[i])
    #List comprehension
    words = [lemmmatizer.lemmatize(word.lower()) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)
print(sentences)

words=word_tokenize(data)
for word in words: 
   print(nltk.pos_tag([word]))
