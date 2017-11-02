from bs4 import BeautifulSoup
import requests
import winsound

page = 1
flag = 0
rank = 0
max_pages = 100000
username = 'nealzane'         # Enter your username/handle here.

# ------------- PRINT THE NAME OF THE USER ------------- #

url = 'https://www.hackerearth.com/@' + username
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
for i in soup.findAll('h1', {'class': 'name ellipsis larger'}):
    print("\nYou searched for " + i.string + ".\n")

# --------------- BASIC PROGRAMMING ------------------ #

while page <= max_pages:
    url = 'https://www.hackerearth.com/practice/basic-programming/leaderboard/' + str(page) + '/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for i in soup.findAll('p', {'class': 'light small weight-400'}):
        rank += 1
        if i.string == username:
            print("Rank in Basic Programming : " + str(rank))
            print()
            flag = 1
            break
    if flag == 1:
        break
    page += 1


page = 1
flag = 0
rank = 0
max_pages = 100000

# --------------- DATA STRUCTURES ---------------- #

while page <= max_pages:
    url = 'https://www.hackerearth.com/practice/data-structures/leaderboard/' + str(page) + '/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for i in soup.findAll('p', {'class': 'light small weight-400'}):
        rank += 1
        if i.string == username:
            print("Rank in Data Structures : " + str(rank))
            print()
            flag = 1
            break
    if flag == 1:
        break
    page += 1

page = 1
flag = 0
rank = 0
max_pages = 100000

# --------------- ALGORITHMS ---------------- #

while page <= max_pages:
    url = 'https://www.hackerearth.com/practice/algorithms/leaderboard/' + str(page) + '/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for i in soup.findAll('p', {'class': 'light small weight-400'}):
        rank += 1
        if i.string == username:
            print("Rank in Algorithms : " + str(rank))
            print()
            flag = 1
            break
    if flag == 1:
        break
    page += 1


page = 1
flag = 0
rank = 0
max_pages = 100000

# --------------- MATH ---------------- #

while page <= max_pages:
    url = 'https://www.hackerearth.com/practice/math/leaderboard/' + str(page) + '/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for i in soup.findAll('p', {'class': 'light small weight-400'}):
        rank += 1
        if i.string == username:
            print("Rank in Math : " + str(rank))
            print()
            flag = 1
            break
    if flag == 1:
        break
    page += 1

# --------------- PLAY A SOUND ALERT ON PROCESS COMPLETION ------------ #

print("Task completed!!")
duration = 2000
freq = 440
winsound.Beep(freq, duration)
