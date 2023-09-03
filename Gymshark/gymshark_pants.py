from bs4 import BeautifulSoup
import pandas as pd
import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


product_links = []


response = requests.get('https://us.shop.gymshark.com/collections/joggers-sweatpants/mens')
soup = BeautifulSoup(response.content, 'html.parser')
product_list = soup.find_all('article', {'class': 'product-card_product-card__gB8_b'})
for item in product_list:
    for link in item.find_all('a', href=True):
        product_links.append(link['href'])


pants_list = []
for link in product_links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1', {'class': 'product-information_title__Wx52B'}).text
    try:
        rating = soup.find('button', {'class': 'product-information_reviews__u6MZt'}).text.strip().split(' ')[0]
    except:
        rating = 'No Rating'
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

    pants_list.append(shorts)


#Sort items from lowest price to highest
sorted_items = sorted(pants_list, key=lambda x: float(x['Price Now'].replace('$', '').replace(',', '')))

excel_filename = 'gymshark_data.xlsx'
existing_df = pd.read_excel(excel_filename)

pants_df = pd.DataFrame(sorted_items)

with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a') as writer:
    pants_df.to_excel(writer, sheet_name='Pants', index=False)

print(f'Dataframe saved to {excel_filename}')