from scraper import scrape_website

def main():
    url = "https://www.globo.com/"
    links = scrape_website(url)
    for link in links:
        print(link)

if __name__ == "__main__":
    main()
