# requests is basically asking a website permission to extract data
# import requests
# print("version: ", requests.__version__)
# url = "https://www.bbc.com/news"
# headers = {"User-Agent": "Mozilla"}# Headers specifies the name of the function, and any arguments (inputs, or parameters) into the function
# response = requests.get(url)

# print("Response: ", response)
# print("Status-code: ", response.status_code)
# print("Header: ", response.headers)
# print("Content: ", response.content)

import requests
from bs4 import BeautifulSoup
url = "https://edition.cnn.com/"
headers= {"User-Agent": "Mozilla"}
response = requests.get(url, headers=headers)
print(response)

html_data = BeautifulSoup(response.text, features="html.parser")
web_title = html_data.find("title")
print("web_title", web_title)

list_article =html_data.find("body").find_all("article")
print("list_article: ", len(list_article))
print(list_article)

list_title = []
for article in list_article:
    title = article.find("h3").find("a")["title"]
    list_title.append(title)
print("list title; ", list_title, len(list_title))