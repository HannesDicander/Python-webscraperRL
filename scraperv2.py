from bs4 import BeautifulSoup
import requests

url = "https://rocketleague.tracker.network/profile/steam/76561198376035244"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
match = soup.find('div', class_='season-table')
print(match.text)