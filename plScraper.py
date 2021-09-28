import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
ac = PrettyTable()
ac.field_names = ['#', 'Club name', 'PL', 'W', 'L', 'D','Points']
SEASON = '2021'

url = f'https://www.skysports.com/premier-league-table{SEASON}'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table', class_='standing-table__table callfn')

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
        pl_points = row.find_all('td', class_='standing-table__cell')[9].text.strip()
        position = row.find_all('td', class_='standing-table__cell')[0].text.strip()
        played = row.find_all('td', class_='standing-table__cell')[2].text.strip()
        won = row.find_all('td', class_='standing-table__cell')[3].text.strip()
        drawn = row.find_all('td', class_='standing-table__cell')[4].text.strip()
        lost = row.find_all('td', class_='standing-table__cell')[5].text.strip()
        
        # print(pl_team)
        # print(pl_points)
        ac.add_row([position ,pl_team, played, won, drawn, lost, pl_points])

ac.align = 'l'
print(ac)

