from fastapi import FastAPI, UploadFile, File
from app.parser import parse_resume
from app.analyser import extract_named_entities

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "CV Analyser API is running!"}

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    parsed = parse_resume(file.filename, content)

    entities = {}
    if "text" in parsed and parsed["text"].strip():
        entities = extract_named_entities(parsed["text"])
        parsed["entities"] = entities

    return {
        "parsed_resume": parsed.get("text", ""),
        "entities": entities
    }
