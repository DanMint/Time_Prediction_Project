import sys
sys.path.insert
import requests
from bs4 import BeautifulSoup
import Testing.test_url
url = 'https://www.mbta.com/schedules/CR-Worcester/timetable' 


# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# timetable_div = soup.find('div', id='timetable')

# print(type(timetable_div))

# time_table = timetable_div.text.split()

# print(time_table)


# if timetable_div:
#     print(timetable_div.text)
# else:
#     print("No div with id 'timetable' found")
