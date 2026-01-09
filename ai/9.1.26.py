# Remove HTML tags
from bs4 import BeautifulSoup

str = '<div>Beautiful Soup is a library that makes it easy to scrape information from web pages.</div>'

cleaned_str = BeautifulSoup(str, 'html.parser').get_text()

print(cleaned_str)

# Remove Url

import re

str = 'Check out the trailer at http://youtube.com/7812'

cleaned_str = re.sub(r'http\S+|www\S+', '', str) # Substitute

print(cleaned_str)

# Remove Emojis / NON ASCII Characters

str = 'I had an amazing experience at this restaurant 🍽️✨ The biryani was super flavorful and perfectly cooked 🍗🍚. The staff was friendly and quick to help 😊🙌. The place was clean and had a nice ambiance 🪑🎶. I will definitely come back again with my family 👨‍👩‍👧‍👦❤️. Highly recommended! ⭐⭐⭐⭐⭐'

cleaned_str = re.sub(r'[^\x00-\x7f]+', '', str)

print(cleaned_str)

# Remove special characters

str = 'Movie was amazing!!! #excited manikanta'

cleaned_str = re.sub(r'[^A-Za-z0-9\s]', '', str)

print(cleaned_str)

# Remove extra spaces

str = 'Programming   languages   to work  with text'

cleaned_str = re.sub(r'\s+', ' ', str)

print(cleaned_str)

def clean_str(str):
    str = BeautifulSoup(str, 'html.parser').get_text()
    str = re.sub(r'http\S+|www\S+', '', str)
    str = re.sub(r'[^\x00-\x7f]+', '', str)
    str = re.sub(r'[^A-Za-z0-9\s]', '', str)
    str = re.sub(r'\s+', ' ', str)
    return str

raw_str = 'I had an amazing experience at this restaurant 🍽️✨    The biryani was http://youtube.com/ganesh super flavorful and   perfectly cooked 🍗🍚. <div>The staff was friendly and quick to help </div> 😊🙌. The place was clean and had a nice ambiance 🪑🎶. I will definitely come ## &&  back again with my family 👨‍👩‍👧‍👦❤️. Highly @@ recommended! ⭐⭐⭐⭐⭐'

cleaned_str = clean_str(raw_str)

print(cleaned_str)