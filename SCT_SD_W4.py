import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def get_rating_value(rating_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating_class, 0)

def scrape_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")

    products = []

    for book in books:
        name = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        rating_class = book.p["class"][1]  
        rating = get_rating_value(rating_class)

        products.append({
            "Name": name,
            "Price": price,
            "Rating": rating
        })

    return products

def scrape_books(num_pages=3, output_file="books.csv"):
    all_books = []
    for page in range(1, num_pages + 1):
        print(f"Scraping page {page}...")
        books = scrape_page(page)
        all_books.extend(books)

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Name", "Price", "Rating"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for book in all_books:
            writer.writerow(book)

    print(f"\n✅ Scraped {len(all_books)} products. Data saved to '{output_file}'.")

if __name__ == "__main__":
    scrape_books(num_pages=5)  
