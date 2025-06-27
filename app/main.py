from fastapi import FastAPI, UploadFile, File
from app.parser import parse_resume
from app.analyser import extract_named_entities 

app = FastAPI()

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    parsed = parse_resume(file.filename, content)
    if "text" in parsed:
        entities = extract_named_entities(parsed["text"])
        parsed["entities"] = entities
    return {"parsed_resume": parsed["text"], "entities": entities}

