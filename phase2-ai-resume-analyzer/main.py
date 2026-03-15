from fastapi import FastAPI, File, UploadFile
from ai_service import analyze_resume 
from file_parser import extract_text

app = FastAPI()

@app.post("/analyze_resume/")
async def analyze_resume_endpoint(file: UploadFile = File(...)):
    resume_bytes = await file.read()
    resume_text = await extract_text(file) 

    print(resume_text[:500])

    result = await analyze_resume(resume_text)

    return result