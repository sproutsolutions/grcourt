from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup (open("loadCase.do?caseSequence=01"))

datum = soup.find_all(class_="medium")

for data in datum:
  print (data.prettify())


