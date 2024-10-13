import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv
import concurrent.futures
import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class MicromaniaScraper:
    def __init__(self, url):
        self.url = url
        self.product_name = ''
        self.product_descriptions = []
        self.product_image_url = ''

    # Product Name
    def scrape_product_name(self, soup):
        name_element = soup.find('h1', {'class': 'prd__nome'})
        if name_element:
            self.product_name = name_element.text.strip()

    # Product Descriptions
    def scrape_product_descriptions(self, soup):
        description_elements = soup.find_all('p', {'class': 'prd__desc'})
        for element in description_elements:
            self.product_descriptions.append(element.text.strip())

    # Product Image URL
    def scrape_product_image_url(self, soup):
        image_element = soup.find('img', {'class': 'prd__img'})
        if image_element:
            self.product_image_url = image_element['src']

    def download_to_csv(self, csvfile, row):
        writer = csv.writer(csvfile)
        writer.writerow(row)

def scrape_url(url, csvfile):
    scraper = MicromaniaScraper(url)
    
    # Set up selenium
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    
    # Get the HTML content
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Scrape the data
    scraper.scrape_product_name(soup)
    scraper.scrape_product_descriptions(soup)
    scraper.scrape_product_image_url(soup)
    
    # Close the selenium driver
    driver.quit()
    
    # Create a row with the URL, product name, product descriptions, and image URL
    row = [url, scraper.product_name]
    row.extend(scraper.product_descriptions)
    row.append(scraper.product_image_url)  # Single image URL
    
    # Pad the row with empty strings if necessary
    max_descriptions = 5  # Maximum number of product descriptions
    row += [''] * (max_descriptions - len(scraper.product_descriptions))
    
    scraper.download_to_csv(csvfile, row)
    st.write(f"Product information saved to CSV")

st.title("Cdiscount (NOT AVAILABLE)")
st.header("Enter URL(s) and filename:")

url_input = st.text_input("Enter URL(s) (separated by comma):")
filename_input = st.text_input("Enter filename:")

if st.button("Scrape"):
    urls = [url.strip() for url in url_input.split(',')]
    csvfile = io.StringIO()
    writer = csv.writer(csvfile)
    header_row = ["URL", "Product Name"]
    header_row.extend([f"Product Description {i+1}" for i in range(5)])
    header_row.append("Image URL")
    writer.writerow(header_row)
    writer.writerow([])

    for url in urls:
        scrape_url(url, csvfile)

    csvfile.seek(0)
    st.download_button("Download CSV", csvfile.read(), f"{filename_input}.csv", "text/csv")