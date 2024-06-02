import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
# data = soup.find_all(string = re.compile('galaxy'))
# pd.DataFrame = ({"head" : list},{"head" : list},{"head" : list}).
# df = pd.DataFram(columns = titles)
# num_of_week = input("Enter the number of week : ")
contest_round = input('please input contest_round : ')
result = requests.get(
    f"https://codeforces.com/contest/{contest_round}/ratings")
soup = BeautifulSoup(result.text, "lxml")

pages_num = soup.find('div', class_='custom-links-pagination')
nobr = pages_num.find_all('nobr')
size = len(nobr)

rank = []
name = []
points = []
rating = []
transform = []

for i in range(int(size / 4)):
    c = int(i + 1)
    stri = str(c)
    resultt = requests.get(
        f"https://codeforces.com/contest/{contest_round}/ratings/page/{stri}")
    soupp = BeautifulSoup(resultt.text, "lxml")
    table = soupp.find('table', class_='')
    trr = table.find_all('tr')

    for i in trr[1:]:
        tdd = i.find_all('td')
        rank.append(tdd[0].text.strip())
        name.append(tdd[1].text.strip())
        points.append(tdd[3].text.strip())
        rating.append(tdd[4].text.strip())
        transform.append(tdd[5].text.strip())

data = {"rank": rank, "name": name, "points": points,
        "rating": rating, "transform": transform}
df = pd.DataFrame(data)
csv_filename = input('please input filename : ')
df.to_csv(f"{csv_filename}.csv", index=False)
print("File created")
