import requests
from bs4 import BeautifulSoup

# Download the ticker, and parse using beautiful soup
sRootUrl = "https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/";
oHTML = requests.get(sRootUrl)
oSoup = BeautifulSoup(oHTML.content, 'html.parser')

for oLink in oSoup.find_all('a'):
    print(oLink.get('href'))
    
# sorry, but its all human from here - i went through it already - the HTML based transcripts are in transcript_links.py and hte PDF based transcripts are in pdf_links.py

