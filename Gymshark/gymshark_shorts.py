from bs4 import BeautifulSoup
import pandas as pd
import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


product_links = []

for page in range(1, 3):
    response = requests.get(f'https://us.shop.gymshark.com/collections/shorts/mens?page={page}')
    soup = BeautifulSoup(response.content, 'html.parser')
    product_list = soup.find_all('article', {'class': 'product-card_product-card__gB8_b'})
    for item in product_list:
        for link in item.find_all('a', href=True):
            product_links.append(link['href'])


shorts_list = []
for link in product_links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1', {'class': 'product-information_title__Wx52B'}).text
    rating = soup.find('button', {'class': 'product-information_reviews__u6MZt'}).text.strip().split(' ')[0]
    price = "$" + soup.find('span', {'data-locator-id': 'pdp-totalValue-read'}).text.strip().split("$")[1]
    try:
        original_price = soup.find('span', {'class': 'product-information_compare-at-price__VENBm'}).text
    except:
        original_price = 'No Discount'
    shorts = {
        'Title': title,
        'Rating': rating,
        'Price': price,
        'Original Price': original_price,
        'Link': link
    }

    shorts_list.append(shorts)


#Sort items from lowest price to highest
sorted_items = sorted(shorts_list, key=lambda x: float(x['Price Now'].replace('$', '').replace(',', '')))

df = pd.DataFrame(sorted_items)

excel_filename = 'gymshark_data.xlsx'
sheet_title = 'Shorts'
df.to_excel(excel_filename, sheet_name=sheet_title, index=False)

print(f'Dataframe saved to {excel_filename}')
