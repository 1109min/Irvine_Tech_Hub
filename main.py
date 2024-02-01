from bs4 import BeautifulSoup
import requests
import csv

# make csv file
filename = "target_etsy.csv"

# open csv file
with open(filename, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)

    # write column name
    columns_name = ["name", "review", "price"]
    writer.writerow(columns_name)

    # loop for 50 pages
    for i in range(1, 50):
        url = "https://www.etsy.com/c/home-and-living?explicit=1&category_landing_page=1&order=highest_reviews&ref=pagination&page="+str(i)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # get html
        res = requests.get(url, headers=headers)

        # check status code
        soup = BeautifulSoup(res.text, "lxml")

        # get product info
        products = soup.find_all('div', class_="v2-listing-card__info")


        # find title, review, price
        for product in products:
            title = product.find("h3", class_="wt-text-caption v2-listing-card__title wt-text-truncate").get_text(
                strip=True)
            review_element_original = product.find("span", class_="wt-text-caption wt-text-gray wt-display-inline-block wt-nudge-l-3 wt-pr-xs-1")

            # check if review is exist
            if review_element_original:
                review_element = review_element_original.get_text(strip=True)

                # remove () and split
                review = review_element[1:-1]

                # calculate review
                if review[-1] == "k":
                    review = float(review[:-1]) * 1000
                elif review[-1] == "m":
                    review = float(review[:-1]) * 1000000
                # check if review is over 1000
                elif "," in review:
                    review = float(review.replace(",", ""))
                else:
                    review = float(review)
            else:
                review_element = "N/A"

            price = product.find("span", class_="currency-value").get_text(strip=True)[1:]

            # write data
            data_rows = [title, review, price]
            writer.writerow(data_rows)
        print(f"page#{i} is done!")
