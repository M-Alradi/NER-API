from fastapi import HTTPException, UploadFile
from starlette.responses import StreamingResponse

from app.core.model_loader import nlp
from app.api.models import TextInput
from app.services.files_helper import extract_entities_from_text, generate_csv


async def recognize_entities(data: TextInput) -> dict:
    if not data.text:
        raise HTTPException(status_code=400, detail="No text provided")

    try:
        entities = extract_entities_from_text(data.text)

        for entity in entities:
            print(f"Text: {entity['text']}, Entity: {entity['label']}")

        return {"text": data.text, "entities": entities}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing text")


async def process_uploaded_file(file: UploadFile) -> StreamingResponse:
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are allowed")

    try:
        contents = await file.read()
        text = contents.decode("utf-8")

        entities = extract_entities_from_text(text)
        csv_content = generate_csv(entities)

        response = StreamingResponse(iter([csv_content]), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=extracted_entities.csv"

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing uploaded file")
