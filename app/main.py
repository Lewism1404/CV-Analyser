from fastapi import FastAPI, UploadFile, File
from app.parser import parse_resume

app = FastAPI()

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    content = await file.read()
    result = parse_resume(file.filename, content)
    return {"parsed_resume": result}
