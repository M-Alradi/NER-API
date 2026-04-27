# NER-API

A FastAPI-based web service that performs **Named Entity Recognition (NER)** on text input, supports file uploads for batch processing, and includes a context-aware **spelling correction** endpoint.

---

## Features

- **`/ner`** — Extract named entities (people, organizations, locations, etc.) from raw text
- **`/uploadfile`** — Upload a `.txt` file and get a downloadable `.csv` of extracted entities
- **`/spelling_corrector`** — Detect and correct misspelled text using a neural spelling correction model

---

## Project Structure

```
NER-API/
├── main.py                         # Uvicorn entry point
├── requirements.txt
├── Apple Inc.txt                   # Sample input file
└── app/
    ├── __init__.py
    ├── core/
    │   ├── __init__.py
    │   └── model_loader.py         # Loads spaCy & Transformers models
    ├── api/
    │   ├── __init__.py
    │   ├── endpoints.py            # Route definitions (thin layer)
    │   └── models.py               # Pydantic request models
    └── services/
        ├── __init__.py
        ├── ner_service.py          # NER & file processing logic
        └── files_helper.py         # Entity extraction & CSV generation helpers
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/M-Alradi/NER-API.git
cd NER-API
```

---

### 2. Setup the enviroment

```bash
source setup.sh
```

**NOTE** 
Choose the correct command for your device:

```bash
source .venv/Scripts/activate                  # Windows
source .venv/bin/activate                      # macOS/Linux
```
---

### 3. Run the server

```bash
uvicorn main:app
```
Interactive docs (Swagger UI): **http://127.0.0.1:8000/docs**

---

## API Endpoints

### `POST /ner`
Extract named entities from a text string.

**Request body:**
```json
{
  "text": "Apple was founded by Steve Jobs in Cupertino."
}
```

**Response:**
```json
{
  "text": "Apple was founded by Steve Jobs in Cupertino.",
  "entities": [
    { "text": "Apple", "label": "ORG" },
    { "text": "Steve Jobs", "label": "PERSON" },
    { "text": "Cupertino", "label": "GPE" }
  ]
}
```

---

### `POST /uploadfile`
Upload a `.txt` file and receive a `.csv` file of extracted entities.

- **Input:** `.txt` file (form-data)
- **Output:** Downloadable `extracted_entities.csv`

```
Text,Entity
Apple,ORG
Steve Jobs,PERSON
Cupertino,GPE
```

---

### `POST /spelling_corrector`
Detect and correct misspellings in a text string.

**Request body:**
```json
{
  "text": "Ths is an exmple sentance."
}
```

**Response:**
```json
{
  "corrected_text": "This is an example sentence."
}
```
---

## Dependencies

| Package | Purpose |
|---|---|
| `fastapi` | Web framework |
| `uvicorn` | ASGI server |
| `spacy` | NER model (`en_core_web_sm`) |
| `transformers` | Spelling correction model (`oliverguhr`) |
| `torch` | Required backend for Transformers |
| `pyspellchecker` | Misspelling detection gate |
| `pydantic` | Request/response validation |
| `starlette` | Streaming file responses |

Full list in [`requirements.txt`](./requirements.txt).
