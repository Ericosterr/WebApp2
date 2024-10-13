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
        description_elements = soup.find_all(['div'], {'class': ['col-md-6 col-xl-4', 'product_attributes_simple']})
        for element in description_elements:
            self.product_descriptions.append(element.text.strip())

    def scrape_product_image_url(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first product image URL on the page
        image_elements = soup.find_all(['img'], {'class': ['img img-fluid product_detail_img mh-100']})
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
    row.extend(scraper.product_descriptions[:5])  # Take only the first 5 descriptions
    row.append(scraper.product_image_url)  # Single image URL
    
    scraper.download_to_csv(csvfile, row)
    st.write(f"Product descriptions and image URL saved to CSV")

st.title("Lvip Web Scraper")
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

    for url in urls:
        scrape_url(url, csvfile)

    csvfile.seek(0)
    st.download_button("Download CSV", csvfile.read(), f"{filename_input}.csv", "text/csv")