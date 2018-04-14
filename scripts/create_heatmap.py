import pandas as pd
from gmplot import gmplot
import os
import time
from selenium import webdriver

filepath = os.path.abspath('assets/heatmap.html')

# Load dataset
df = pd.read_csv("data/listings_bali_201804.csv")
# Heatmap on Google Maps
gmap = gmplot.GoogleMapPlotter(-8.41, 115.07, 10)
gmap.heatmap(df.latitude, df.longitude)
gmap.draw(filepath)

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
browser = webdriver.Firefox(firefox_options=options)
browser.get(f"file://{filepath}")
time.sleep(3)
browser.save_screenshot("assets/heatmap.png")
browser.quit()
