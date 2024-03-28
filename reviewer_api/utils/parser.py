# времени на крутой парсер не хватило, поэтому пока на костылях только для трех банков

def parse(product_name: str) -> str:
    if 'тинькофф' in product_name:
        return 'tinkoff_reviews.csv'
    elif 'альфа' in product_name:
        return 'alfa_reviews.csv'
    else:
        return 'sber_reviews.csv'
