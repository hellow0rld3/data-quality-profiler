import io
import pandas as pd
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from app.services.analyzer import analyze_csv
from app.services.cleaner import clean_csv

app = FastAPI(title="Data Quality Profiler")


@app.get("/")
async def root():
    return {"status" : "serwer zyje"}

@app.post("/upload")
async def upload_csv(file: UploadFile):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Plik musi być w formacie CSV.")
    df = pd.read_csv(file.file)
    result = analyze_csv(df)
    return result

@app.post("/clean")
async def return_csv(file: UploadFile):
    df = pd.read_csv(file.file)
    cleaned_df = clean_csv(df)

    stream = io.StringIO()
    cleaned_df.to_csv(stream, index=False)
    stream.seek(0)

    return StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition" : f"attachment; filename=cleaned_{file.filename}"}
    )

