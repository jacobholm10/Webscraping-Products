from bs4 import BeautifulSoup
import requests
import openpyxl


url = "https://www.youngla.com/collections/shorts"


response = requests.get(url, timeout=10).text
doc = BeautifulSoup(response, 'html.parser')

page_text = doc.find(class_="Pagination__Nav").text.strip().split("1")
pages = int(page_text[-1].strip())

existing_workbook = openpyxl.load_workbook('youngla_data.xlsx')

ws_shorts = existing_workbook.create_sheet("Shorts")

headers = ['Title', 'Price', 'Link']
ws_shorts.append(headers)

for page in range(1, pages+1):
    page_url = f"{url}?page={page}"
    page = requests.get(page_url).text
    doc = BeautifulSoup(page, 'html.parser')
    div = doc.find(class_="ProductList ProductList--grid ProductList--removeMargin Grid")

    items = div.find_all("div", {"class": "Grid__Cell 1/2--phone 1/3--tablet-and-up 1/4--desk"})
    for item in items:
        item_title_element = item.find("h2", {"class": "ProductItem__Title Heading"})
        item_price_element = item.find("span", {"class": "ProductItem__Price Price Text--subdued"})
        item_link_element = item.find("h2", {"class": "ProductItem__Title Heading"}).find("a")['href']

        if item_title_element:
            item_title = item_title_element.text.strip()
        else:
            continue
                
            
        if item_price_element:
                    item_price = item_price_element.text.strip()
        else:
            continue

        if item_link_element:
            item_link = "https://www.youngla.com" + item_link_element
        else:
            continue


        if item_title and item_price and item_link:
            item_data = [item_title, item_price, item_link]
            ws_shorts.append(item_data)

    existing_workbook.save('youngla_data.xlsx')