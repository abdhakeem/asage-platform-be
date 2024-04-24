from fastapi import FastAPI, UploadFile, File
import base64
from model import Model

app = FastAPI()
model = Model()


@app.post("/process_document/")
async def process_document(file: UploadFile = File(...)):
    contents = await file.read()
    file_base64 = base64.b64encode(contents).decode("utf-8")
    return model.generate(file.filename, file_base64)
