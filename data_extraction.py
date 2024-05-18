import os
import pandas as pd
from bs4 import BeautifulSoup
from html5lib import HTMLParser
import requests

input_file = '/content/Input.xlsx'
dataframe1 = pd.read_excel(input_file)

def extract_article(url):
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    title = soup.find('h1').text.strip()
    article_text = soup.find('article').text.strip()
    return title, article_text
  except Exception as e:
    print(f"error extracting text from {url} : {e}")
    return None, None

output_dir = "extracted_articles"
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

for index, row in dataframe1.iterrows():
  url_id = row['URL_ID']
  url = row['URL']
  print(f"Processing {url_id}...")
  title, article_text = extract_article(url)
  if title and article_text:
    file_path = os.path.join(output_dir, f"{url_id}.txt")
    with open(file_path, 'w', encoding = 'utf-8') as file:
      file.write(f"{title}\n\n{article_text}")
    print(f"Article Saved: {file_path}")
  else:
    print(f"skipping {url_id} due to extraction error.")
print("Extraction complete")