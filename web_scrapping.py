import requests
from bs4 import BeautifulSoup
from csv import writer
class Web_Scrap:
	def __init__(self, url):
		self.url = url

	def to_csv(self):
		page = requests.get(self.url)

		soup = BeautifulSoup(page.content, "html.parser")
		abouts = soup.find_all('div',class_="lead-col")
		print("Data Commons: ")
		for about in abouts:
			intro = about.find('p',class_="lead").text
			print(intro)
			

		with open('Data_Commons.csv', 'w', encoding = 'utf8', newline = '') as f:
			thewriter = writer(f)
			header = ['Topic', 'How we build Connections']
			thewriter.writerow(header)  
			lists = soup.find_all('article')
			for list in lists:
				heading = list.find('h3').text
				para = list.find('p').text
				info = [heading, para]
				thewriter.writerow(info) 

output = Web_Scrap("https://www.datacommons.org/")
output.to_csv()