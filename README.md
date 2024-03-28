# tinkoff_review_analyze
_There all our developments on the project_

**Files in our solution:**

- foleder "parser" for additional task /
      **1)** get_all_reviews.py - parsing links to review of tinkoff \
      **2)** get_reviews_content.py - parsing everyone review to csv 

- folder "reviewer_api" - api for mobile app \
      **1)** "monolith.py" - api on FastAPI, architecture - while monolyth \
      **2)** folder "utils" - usage of all our AI models \
            **1)** parse.py - pseudo-parsing) \
            **2)** classificator.py - BERT classification for reviews(1 - positive, 0 - negative)  \
            **3)** generative.py - for some time we will use GIGA chat: summarization and generate advise to upgrade product based on negative reviews 

- bert_classification.ipynb - research for review classificator
- review_analyze.ipynb - notebook for additional task(2 stage)
- review_analyze.pdf - presentation of our research for additional task(2 stage)
            
