
from bs4 import BeautifulSoup
import requests

import pandas as pd

df = pd.DataFrame(columns=["header", "created_date", "rating", "message"])


def remove_duplicate():
    links_with_duplicate = []
    with open("links.txt", "r") as links_file:
        for link in links_file.readlines():
            links_with_duplicate.append(link.strip())

        links = set(links_with_duplicate)
        links = list(links)

    return links


def get_review_content(links):
    global df

    for i in range(0, len(links)):
        print(i + 1, len(links) + 1)
        req_for_get_review_content = requests.get(f"https://www.banki.ru/{links[i]}/")
        try:
            soup = BeautifulSoup(req_for_get_review_content.text, 'lxml')
            header = get_review_header(soup)
            created_date = get_review_created_date(soup)
            rating = get_review_rate(soup)
            message = get_review_message(soup)
            df.loc[len(df.index)] = [header, created_date, rating, message]
        except Exception:
            print("Failed(")


def get_review_header(soup):
    return soup.select_one(".text-header-0.le856f50c").text.strip()


def get_review_created_date(soup):
    return soup.select_one(".l10fac986").text.strip()


def get_review_rate(soup):
    return soup.select_one(".rating-grade").text.strip()


def get_review_message(soup):
    return soup.select_one("body > div.page-container > main > div:nth-child(2) > section:nth-child(1) > main > div > "
                           "section > div:nth-child(3) > div:nth-child(2) > div > div.lf4cbd87d.ld6d46e58.lfd76152f > "
                           "div:nth-child(2) > div > div > p").text.strip()


if __name__ == '__main__':
    # firstly remove duplicate of link
    links = remove_duplicate()
    get_review_content(links)
    df.to_csv('reviews.csv', encoding='utf-8')
