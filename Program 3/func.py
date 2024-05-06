sports_url = "https://en.wikipedia.org/wiki/Sports"
sports_url2 = "https://en.wikipedia.org/wiki/Cricket"
education_url = "https://en.wikipedia.org/wiki/Education"
education_url2 = "https://en.wikipedia.org/wiki/School"


# Scrape Wikipedia pages
sports_text1 = scrape_wikipedia(sports_url)
sports_text2 = scrape_wikipedia(sports_url2)
sports_text = sports_text1 + sports_text2
print(sports_text)
education_text = scrape_wikipedia(education_url)
