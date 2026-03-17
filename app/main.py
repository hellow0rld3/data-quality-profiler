from fastapi import FastAPI, File, UploadFile, HTTPException
from app.services.analyzer import analyze_csv

app = FastAPI(title="Data Quality Profiler")


@app.get("/")
async def root():
    return {"status" : "serwer zyje"}

@app.post("/upload")
async def upload_csv(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Plik musi być w formacie CSV.")
    result = analyze_csv(file.file)
    return result
