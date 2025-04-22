import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Target URL
url = 'http://books.toscrape.com/catalogue/page-1.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

book_data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    
    star_rating = book.p.get('class')[1]  
    
    book_data.append({
        'Title': title,
        'Price': price,
        'Availability': availability,
        'Rating': star_rating
    })

df = pd.DataFrame(book_data)

df.to_csv('books.csv', index=False)

print("Book data saved to 'books.csv'")
