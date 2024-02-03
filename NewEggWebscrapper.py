from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

# URL Link that we have used for this workshop
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

# Other parts of Beautiful Soup and Web Scraping
# opening up connection, grabbing the page.
uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

#HTML parser
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})

# Creates a new csv file so we can store it from there. We'll call it products
filename = "products.csv"
f = open(filename, "w")
headers="brand, product_name, shipping\n"
f.write(headers)
# https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card

# This is the web scraper. Its purpose is to grab the important information that we need from each container that we have got. 
# Then, we place them to the csv file with File I/O
for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name " + product_name)
	print("Shipping " + shipping)

	f.write(brand + ", " + product_name.replace(",","|") + ", " + shipping + "\n")
f.close()