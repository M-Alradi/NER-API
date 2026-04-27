import re

from fastapi import APIRouter, File, UploadFile
from spellchecker import SpellChecker

from app.core.model_loader import nlp_oliverguhr
from app.api.models import TextInput
from app.services.ner_service import recognize_entities, process_uploaded_file

router = APIRouter()
spell = SpellChecker()


@router.post("/ner")
async def ner_endpoint(data: TextInput):
    return await recognize_entities(data)


@router.post("/uploadfile")
async def upload_file_endpoint(file: UploadFile = File(...)):
    return await process_uploaded_file(file)


@router.post("/spelling_corrector")
async def spelling_corrector_endpoint(input: TextInput):
    words = re.findall(r"\b[a-zA-Z']+\b", input.text.lower())
    misspelled = spell.unknown(words)
    
    if misspelled:
        corrected = nlp_oliverguhr(
            input.text,
            max_length=50,
            num_return_sequences=1,
            clean_up_tokenization_spaces=True
        )[0]["generated_text"]
        return {"corrected_text": corrected}

    return {"message": "Text is correct", "text": input.text}
