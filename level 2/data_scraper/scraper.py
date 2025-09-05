import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Define the target website
URL = "https://quotes.toscrape.com/"   # demo site for web scraping

def scrape_data():
    # Step 2: Send an HTTP request to the website
    response = requests.get(URL)
    
    if response.status_code != 200:
        print("❌ Failed to retrieve page")
        return
    
    # Step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step 4: Extract the data we want (quotes and authors)
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    # Step 5: Save the data into a CSV file
    with open("level 2/data_scraper/scraped_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])  # Header row

        for quote, author in zip(quotes, authors):
            writer.writerow([quote.get_text(), author.get_text()])

    print("✅ Data successfully scraped and saved to scraped_data.csv")


# Run the scraper
if __name__ == "__main__":
    scrape_data()
