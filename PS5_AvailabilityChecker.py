import requests
from bs4 import BeautifulSoup

def check_item_availability(item, url):
    # Make a GET request to the website
    response = requests.get(url)
    # Check the status code of the response to see if the request was successful
    if response.status_code == 200:
        # Check the page content for the item
        if item in response.text:
            return "Available"
        else:
            return "Not Available"
    else:
        return "Request Error"

def get_item_price(url):
    # Make a GET request to the website
    response = requests.get(url)
    # Check the status code of the response to see if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to extract the item price from the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        # Check different classes that may contain the price
        if soup.find("span", {"class": "price"}):
            price = soup.find("span", {"class": "price"}).text
        elif soup.find("span", {"class": "price-value"}):
            price = soup.find("span", {"class": "price-value"}).text
        elif soup.find("span", {"class": "item-price"}):
            price = soup.find("span", {"class": "item-price"}).text
        else:
            price = "Price not found"
        return price
    else:
        return "Request Error"


item = "item_name"

# URLs of top 15 top tech retail stores
urls = [
    "https://www.walmart.com/ip/Sony-PlayStation-5-Video-Game-Console/1736740710?athcpid=1736740710&athpgid=AthenaItempage&athcgid=null&athznid=PWSMT&athieid=v0&athstid=CS020&athguid=BwtQxKlfxGRNHFPYFLV75pCorrpjMJhqvbzQ&athancid=null&athena=true&athbdg=L1102",
    "https://www.bestbuy.com/site/sony-playstation-5-console/6523167.p?skuId=6523167",
    "https://www.gamestop.com/consoles-hardware/playstation-5/consoles/products/sony-playstation-5-console/11108140.html?condition=Refurbished",
    "https://www.target.com/p/playstation-5-console/-/A-87716467",
    "https://www.amazon.com/PlayStation-5-Console-CFI-1215A01X/dp/B0BCNKKZ91/ref=sr_1_1?crid=2SIYIJAJMMMZ2&keywords=ps5&qid=1676073220&s=videogames&sprefix=ps%2Cvideogames%2C216&sr=1-1",
    "https://stockx.com/sony-ps5-playstation-5-digital-edition-console-white?country=US&currencyCode=USD&g_acctid=709-098-4271&g_adgroupid=112741549393&g_adid=472683936469&g_adtype=pla&g_campaign=OD+-+Segment+-+Electronics+-+%28US%29&g_campaignid=11360176547&g_ifcreative=&g_ifproduct=product&g_keyword=&g_keywordid=pla-1012784849947&g_merchantid=111829866&g_network=g&g_partition=1012784849947&g_productchannel=online&g_productid=ee7aacf7-af0b-49f0-b0ff-9f39f46c697d&gclsrc=aw.ds&utm_source=&utm_medium=&utm_campaign=&utm_campaignid=11360176547&content=472683936469&keyword=&gclid=CjwKCAiA85efBhBbEiwAD7oLQOq7mDSWp9qCYf4u9P4TxnLiufMzk5wl59Uoc91XhBkil_bEyTFhQhoCz_kQAvD_BwE",
    "https://www.store7.com/product_page",
    "https://www.store8.com/product_page",
    "https://www.store9.com/product_page",
    "https://www.store10.com/product_page",
    "https://www.store11.com/product_page",
    "https://www.store12.com/product_page",
    "https://www.store13.com/product_page",
    "https://www.store14.com/product_page",
    "https://www.store15.com/product_page"
]

# Check availability of item in each store
for i, url in enumerate(urls):
    availability = check_item_availability(item, url)
    price = get_item_price(url)
    print("Store", i+1, ":", url, "- Price:", price, "- Availability:", availability)
