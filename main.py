import requests
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver

def get_request(url,filters= None,is_param=False,**kwargs):
	if is_param:
		res = requests.get(url, params='q=%s' % kwargs['title'])
	else:
		res = requests.get(url, allow_redirects = True)

	if filters != None:
		only_a_tag = SoupStrainer(filters, title = kwargs['title'])
		return BeautifulSoup(res.text, 'html.parser',parse_only = only_a_tag)
	else:
		return res
		

def download(url):
	print('Downloading...')
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk",'audio/mpeg')
	driver = webdriver.Firefox(profile)
	driver.get(f'http://ulub.pl/{url}')
	button = driver.find_element_by_class_name('rodo_go_a')
	button.click()
	button = driver.find_element_by_class_name('pobierz')
	button.click()	


def load_title_list():
	print('Loadin title list...')
	with open('titles.txt', 'r') as file:
		return [item.strip() for item in file.readlines()]


def find_track(track_title):
	print(f'Searching {track_title}')
	soup = get_request('http://ulub.pl/szukaj.html',filters ='a', is_param=True, title = track_title)
	
	if soup.a == None:
		with open('filed.txt','a') as filed:
			filed.write(track_title+'\n')
			return None
	else:
		download(soup.a['href'])



def main():
	titles = load_title_list()
	for title in titles:
		find_track(title)


if __name__ == '__main__':
	main()
