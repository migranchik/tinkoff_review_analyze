import requests
from bs4 import BeautifulSoup


def get_review_links(page_num):
    req_for_get_one_page = requests.get(f"https://www.banki.ru/services/responses/bank/tcs/?page={page_num}&is_countable=off")

    review_links_from_one_page = []

    soup = BeautifulSoup(req_for_get_one_page.text, 'lxml')
    all_links = soup.find_all("a")
    for link in all_links:
        link_elements = link["href"].split('/')
        if len(link_elements) == 7 and link_elements[-3] == 'response':
            processed_link_of_response = '/'.join(link_elements[1:6])
            review_links_from_one_page.append(processed_link_of_response)

    return review_links_from_one_page


if __name__ == '__main__':
    ALL_REVIEWS = 9500
    REVIEW_IN_ONE_PAGE = 52

    pages = ALL_REVIEWS // REVIEW_IN_ONE_PAGE

    all_review_links = []

    with open("links.txt", 'w') as links_file:
        for page_num in range(1, pages + 1):
            print(f"{page_num} from {pages}")
            links_file.writelines([f"{link}\n" for link in get_review_links(page_num)])
