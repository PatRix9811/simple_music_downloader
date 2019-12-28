from selenium import webdriver

def load_title_list():
	with open('titles.txt', 'r') as file:
		return [item.strip() for item in file.readlines()]


def main():
	driver = webdriver.Firefox()
	driver.get('http://ulub.pl/')
	if "Wyszukiwarka mp3" not in driver.title:
		print("Open wrong site. Please check url adress")
		driver.close()
		exit()

	titles = load_title_list()

	driver.close()


if __name__ == '__main__':
	main()
