import nltk
import csv
nltk.download('punkt')
from newspaper import Article

with open('fourth.csv', mode='w') as employee_file:
    my_file = open("small.txt", "r")
    content_list = my_file.readlines()
    test_list = list(set(content_list))
    length = len(test_list)

    print(length)

    for i in test_list:
        print(i)
        toi_article = Article(i, language="en") # en for English
        toi_article.download()
        toi_article.parse()
        toi_article.nlp()
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([toi_article.title])
