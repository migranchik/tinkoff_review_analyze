import requests
import json

url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"


def summarize(df) -> str:
    negative_reviews = df[df["pred"] == 0]
    negative_reviews = negative_reviews["message"].values
    negative_reviews = ' '.join(negative_reviews)

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": f"Выдели основные недостатки продукта по этим отзывам {negative_reviews}"
            }
        ],
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer <токен_доступа>'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)
    return response.choices.message.content


def advise(summary) -> str:
    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": f"Какие способы решения этих проблем можешь предложить {summary}"
            }
        ],
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer <токен_доступа>'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)
    return response.choices.message.content



