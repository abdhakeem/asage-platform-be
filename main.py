from fastapi import FastAPI, UploadFile, File
import base64

app = FastAPI()


@app.post("/process_document/")
async def process_document(file: UploadFile = File(...)):
    contents = await file.read()
    file_base64 = base64.b64encode(contents).decode("utf-8")
    return {"filename": file.filename, "content": file_base64}

