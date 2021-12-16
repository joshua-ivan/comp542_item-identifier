
import requests
from bs4 import BeautifulSoup
import csv


def get_page(url):
	response = requests.get(url)

	if not response.ok:
		print('Server responded:', response.status_code)
		soup = ''
	else:
		soup = BeautifulSoup(response.text, 'lxml')
	return soup



def get_detail_data(soup):
	#title
	#price
	#item sold
	#condition
	try:
		title = soup.find('h1', id='itemTitle').text.strip("Details about ").replace('\xa0', '')
	except:
		title = ''


	try:
		p = soup.find('span', id = 'prcIsum').text.strip()
		currency, price = p.split(' ')
	except:
		currency = ''
		price = ''

	try:
		sold = soup.find('span', class_='vi-qtyS-hot-red').find('a').text.strip().split(' ')[0]

	except:
		sold = ''

	try:
		condition = soup.find('span', class_='ux-expandable-textual-display-block-inline').find('span').text.strip()
	except:
		condition = ''

	try:
		color = soup.find(text = "Color:").findNext('span').text.strip()
	except:
		color = ''

	try:
		theme = soup.find(text = "Theme:").findNext('span').text.strip()
	except:
		theme = ''

	try:
		features = soup.find(text = "Features:").findNext('span').text.strip()
	except:
		features = ''

	data = {
		'title': title,
		'price': price,
		'currency': currency,
		'total sold': sold,
		'condition': condition,
		'color': color,
		'theme': theme,
		'features': features
	}
	return data

def get_index_data(soup):
	try:
		links = soup.find_all('a', class_ = 's-item__link')
	except:
		links = []

	urls = [item.get('href') for item in links]

	return urls




def write_csv(data, url):
	with open('output1.csv', 'a') as csvfile:
		writer = csv.writer(csvfile)
		headerList = ['title', 'price', 'currency', 'total sold', 'condition', 'color', 'theme', 'features'] 
		row = [data['title'], data['price'], data['currency'], data['total sold'], 
		data['condition'], data['color'], data['theme'], data['features'], url]

		writer.writerow(row)




def main():
	url = 'https://www.ebay.com/sch/i.html?_nkw=vintage+shirts&_pgn=1'

	products = get_index_data(get_page(url))

	for link in products:
		data = get_detail_data(get_page(link))
		write_csv(data, link)

if __name__ == '__main__':
	main()