# tinkoff_review_analyze
There all our developments on the project

foleder "parser" for additional task/
      get_all_reviews.py - parsing links to review of tinkoff
      get_reviews_content.py - parsing everyone review to csv

folder "reviewer_api" - api for mobile app /
      "monolith.py" - api on FastAPI, architecture - while monolyth
      folder "utils" - usage of all our AI models /
            parse.py - pseudo parsin)
            classificator.py - BERT classification for reviews(1 - positive, 0 - negative)
            generative.py - for some time we will use GIGA chat: summarization and generate advise to upgrade product based on negative reviews

bert_classification.ipynb - research for review classificator
review_analyze.ipynb - notebook for additional task(2 stage)
review_analyze.pdf - presentation of our research for additional task(2 stage)
            
