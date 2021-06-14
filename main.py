import nltk
nltk.download('punkt')
from newspaper import Article

#A new article from TOI
url = "https://www.ndtv.com/mumbai-news/watch-shiv-sena-mla-punishes-contractor-in-mumbai-for-not-getting-drains-cleaned-2462770?pfrom=home-ndtv_topscroll"

#For different language newspaper refer above table
toi_article = Article(url, language="en") # en for English

#To download the article
toi_article.download()

#To parse the article
toi_article.parse()

#To perform natural language processing ie..nlp
toi_article.nlp()

#To extract title
print("Article's Title:")
print(toi_article.title)
print("n")

#To extract text
print("Article's Text:")
print(toi_article.text)
print("n")

#To extract summary
print("Article's Summary:")
print(toi_article.summary)
print("n")

#To extract keywords
print("Article's Keywords:")
print(toi_article.keywords)

print(toi_article.images)
print(toi_article.movies)
