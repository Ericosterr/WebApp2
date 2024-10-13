import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv
import concurrent.futures
import io

class MicromaniaScraper:
    def __init__(self, url):
        self.url = url
        self.product_descriptions = []
        self.product_image_url = ''

    def scrape_product_descriptions(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all product descriptions on the page
        description_elements = soup.find_all(['div'], {'class': ['col-md-7 mb-4 product_top_right', 'product-description cms-content']})
        for element in description_elements:
            self.product_descriptions.append(element.text.strip())

    def scrape_product_image_url(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first product image URL on the page
        image_elements = soup.find_all(['img'], {'id': ['rounded img-fluid']})
        if image_elements:
            self.product_image_url = image_elements[0]['src']

    def download_to_csv(self, csvfile, row):
        writer = csv.writer(csvfile)
        writer.writerow(row)

def scrape_url(url, csvfile):
    scraper = MicromaniaScraper(url)
    scraper.scrape_product_descriptions()
    scraper.scrape_product_image_url()
    
    # Create a row with the URL, product descriptions, and image URL
    row = [url]
    row.extend(scraper.product_descriptions)
    row.append(scraper.product_image_url)  # Single image URL
    
    # Pad the row with empty strings if necessary
    max_descriptions = 5  # Maximum number of product descriptions
    row += [''] * (max_descriptions - len(scraper.product_descriptions))
    
    scraper.download_to_csv(csvfile, row)
    st.write(f"Product descriptions and image URL saved to CSV")

st.title("JoshNoaco")
st.header("Enter URL(s) (seperated by comma and no spaces) and filename:")

url_input = st.text_input("Enter URL(s) (separated by comma):")
filename_input = st.text_input("Enter filename:")

if st.button("Scrape"):
    urls = [url.strip() for url in url_input.split(',')]
    csvfile = io.StringIO()
    writer = csv.writer(csvfile)
    header_row = ["URL"]
    header_row.extend([f"Product Description {i+1}" for i in range(5)])
    header_row.append("Image URL")
    writer.writerow(header_row)
    writer.writerow([])

    for url in urls:
        scrape_url(url, csvfile)

    csvfile.seek(0)
    st.download_button("Download CSV", csvfile.read(), f"{filename_input}.csv", "text/csv")