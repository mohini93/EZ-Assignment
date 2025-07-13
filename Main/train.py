import torch
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

def load_summarizer():
    return pipeline("summarization", model="google/flan-t5-small")

def load_qna():
    model_name = "distilbert-base-uncased-distilled-squad"
    return pipeline("question-answering", model=model_name, tokenizer=model_name)

def load_embedder():
    model = "sentence-transformers/all-MiniLM-L6-v2"
    return pipeline("feature-extraction", model=model)
