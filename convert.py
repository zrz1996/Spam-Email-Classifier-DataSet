import os
from bs4 import BeautifulSoup
dirs = os.listdir("./email/")
path = "./emailPlain/"
for fname in dirs:
    f = open("./email/" + fname, "r")
    html = f.read()
    f.close()
    soup = BeautifulSoup(html, 'html.parser')
    s = soup.get_text()
    s = s.encode('UTF-8')
    f = open(path + fname + ".txt", "w")
    f.write(s)
    f.close()

