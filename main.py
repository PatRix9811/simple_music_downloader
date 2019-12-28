#from selenium import webdriver
import requests
from bs4 import BeautifulSoup, SoupStrainer
from pprint import pprint as pp

def load_title_list():
	with open('titles.txt', 'r') as file:
		return [item.strip() for item in file.readlines()]


def find_track(track_title):
	res = requests.get('http://ulub.pl/szukaj.html', params='q=%s' % track_title)
	only_a_tag = SoupStrainer('a', title = track_title)
	soup = BeautifulSoup(res.text, 'html.parser',parse_only = only_a_tag)
	if soup.a == None:
		with open('filed.txt','a') as filed:
			filed.write(track_title)
			return None
	else:
		return soup.a['href']



def main():
	titles = load_title_list()
	for title in titles:
		find_track(title)


if __name__ == '__main__':
	main()
