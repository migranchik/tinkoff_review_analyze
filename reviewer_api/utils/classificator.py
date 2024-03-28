import numpy as np
import pandas as pd
import gc


import torch
import torch.nn as nn
from transformers import AutoModel, BertTokenizer, BertForSequenceClassification


class BERT_tune(nn.Module):
    def __init__(self, bert):
        super(BERT_tune, self).__init__()
        self.bert = bert
        self.dropout = nn.Dropout(0.1)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(768,512)
        self.fc2 = nn.Linear(512,2)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, sent_id, mask):
        _, cls_hs = self.bert(sent_id, attention_mask=mask, return_dict=False)
        x = self.fc1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x


class Classificator:
    bert = AutoModel.from_pretrained('DeepPavlov/rubert-base-cased-sentence')
    tokenizer = BertTokenizer.from_pretrained('DeepPavlov/rubert-base-cased-sentence')

    model = BERT_tune(bert)

    def classify(self, reviews_path):
        path = 'saved_weights.pt'
        self.model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
        df = pd.read_csv(reviews_path)
        reviews_content = df['message'].astype('str')
        tokens = self.tokenizer.batch_encode_plus(
            reviews_content.values,
            max_length=100,
            padding='max_length',
            truncation=True
        )

        seq = torch.tensor(tokens['input_ids'])
        mask = torch.tensor(tokens['attention_mask'])

        gc.collect()

        list_seq = np.array_split(seq, 50)
        list_mask = np.array_split(mask, 50)

        predictions = []
        for num, elem in enumerate(list_seq):
            with torch.no_grad():
                preds = self.model(elem, list_mask[num])
                predictions.append(preds)

        flat_preds = [item[1] for sublist in predictions for item in sublist]
        flat_preds = (flat_preds - min(flat_preds)) / (max(flat_preds) - min(flat_preds))
        df['confidence'] = flat_preds

        df['pred'] = df['confidence'].apply(lambda x: 1 if x > 0.88 else 0)

        return df


cls = Classificator()
cls.classify('reviews.csv')
