from bs4 import BeautifulSoup
import pandas as pd
import requests



base_url = 'https://byltbasics.com'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' 
    
}


product_links = []

response = requests.get('https://byltbasics.com/collections/short-sleeve-shirts')
soup = BeautifulSoup(response.content, 'html.parser')
product_list = soup.find_all('div', {'class': 'column is-one-quarter-desktop is-half-tablet is-half-touch'})
for item in product_list:
    for link in item.find_all('a', href=True):
        product_links.append(base_url + link['href'])


shirts_list = []
for link in product_links:
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1', {'class': 'product-title nacelle'}).text
    price_now = soup.find('span', {'class': 'product-price nacelle has-compared'}).text.split('e')[1].strip()
    original_price = soup.find('span', {'class': 'product-price nacelle compared'}).text.split('e')[2].strip()
    reviews = soup.find('span', {'class': 'rating-total'}).text.strip()

    shirts = {
        'Title': title,
        'Price Now': price_now,
        'Original Price': original_price,
        'Reviews': reviews,
        'Link': link
        
    }

    shirts_list.append(shirts)


#Sort items from lowest price to highest
sorted_items = sorted(shirts_list, key=lambda x: float(x['Price Now'].replace('$', '').replace(',', '')))


#Filename
excel_filename = 'bylt_data.xlsx'
existing_df = pd.read_excel(excel_filename)

#Create DataFrame
shirts_df = pd.DataFrame(sorted_items)

with pd.ExcelWriter(excel_filename, engine='openpyxl', mode='a') as writer:
    shirts_df.to_excel(writer, sheet_name='Shirts', index=False)


#Make sure the data actually saves
print(f'Dataframe saved to {excel_filename}')