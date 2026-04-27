from io import StringIO
import csv

from app.core.model_loader import nlp


def extract_entities_from_text(text: str) -> list:
    processed_text = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in processed_text.ents]
    return entities


def generate_csv(entities: list) -> str:
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)
    csv_writer.writerow(["Text", "Entity"])

    for entity in entities:
        csv_writer.writerow([entity["text"], entity["label"]])

    return csv_data.getvalue()
