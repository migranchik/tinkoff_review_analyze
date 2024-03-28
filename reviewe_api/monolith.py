from fastapi import FastAPI

from utils import parser, classificator, generative

app = FastAPI()


@app.get("/api/v1/analyze")
def analyze(product_name: str):
    product_name = 'Тинькофф'
    cls = classificator.Classificator()

    reviews_path = parser.parse(product_name)
    df = cls.classify(reviews_path)
    summary = generative.summarize(df)
    advises = generative.advise(summary)
    return (summary, advises)

