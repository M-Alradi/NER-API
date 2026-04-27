import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")

nlp_oliverguhr = pipeline(
    "text2text-generation",
    model="oliverguhr/spelling-correction-english-base"
)
