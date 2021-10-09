#install beautifulsoup
#---pip install beautifulsoup4

#import beautifulsoup
from bs4 import BeautifulSoup

#opening file

with open("index.html","r") as file:
    doc = BeautifulSoup(file,"html.parser")
#print(doc.prettify())   #printing all doc


#printing doc title
tag = doc.title
print(tag)

#printing title only

tag =doc.title
print(tag.string)  # .string help to print title only

#modifying title

# tag = doc.title
# tag.string = "Hello"
# print(tag)
# print(doc)

tag = doc.find("a")
print(tag.string)


tag = doc.findAll("p")[0]
print(tag.findAll("b"))