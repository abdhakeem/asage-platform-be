from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import base64
from model import Model
from engine import Engine

app = FastAPI()
model = Model()
engine = Engine()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/process_document/")
async def process_document(file: UploadFile = File(...)):
    contents = await file.read()
    file_base64 = base64.b64encode(contents).decode("utf-8")
    extracted_info = model.generate(file.filename, file_base64)
    return engine.process(extracted_info)
