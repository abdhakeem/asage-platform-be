import io
from io import BytesIO
from docx import Document

import base64
import csv
import json
import time

from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai
import vertexai.preview.generative_models as generative_models

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

supported_types = {"pdf": "application/pdf", "jpg": "image/jpeg", "png": "image/png"}


def csv_to_string(decoded_data):
    decoded_data_str = decoded_data.decode("utf-8")
    csv_reader = csv.reader(io.StringIO(decoded_data_str))
    rows = list(csv_reader)
    if len(rows) > 0:
        # The decoded data is in CSV format, convert it to a string object
        csv_as_string = '\n'.join(','.join(row) for row in rows)
        return csv_as_string
    return "err: no contents uploaded"


def retry_on_error(max_retries=2, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Error occurred: {e}")
                    retries += 1
                    print(f"Retrying ({retries}/{max_retries}) after {delay} seconds...")
                    time.sleep(delay)
            raise Exception(f"Failed after {max_retries} retries.")

        return wrapper

    return decorator


class Model():
    def __init__(self):
        vertexai.init(project="polar-equinox-420601", location="us-central1")
        self.model = GenerativeModel("gemini-1.5-pro-preview-0409")

        with open('prompt/prompt.txt', 'r') as file:
            # Read the contents of the file
            self.prompt = file.read()

        with open('prompt/context.txt', 'r') as file:
            # Read the contents of the file
            self.context = file.read()

    @retry_on_error(max_retries=2, delay=1)
    def generate(self, filename, document):
        ext = filename.split(".")[-1]
        if ext in supported_types:
            document1 = Part.from_data(
                mime_type=supported_types[ext],
                data=base64.b64decode(document))
        elif ext == "csv":
            document1 = csv_to_string(base64.b64decode(document))
        elif ext == "txt":
            document1 = base64.b64decode(document).decode('utf-8')
        elif ext == "docx":
            file_stream = BytesIO(base64.b64decode(document))
            # Load the DOCX file using python-docx
            docx_file = Document(file_stream)
            # Extract text from the DOCX file
            document1 = '\n'.join([paragraph.text for paragraph in docx_file.paragraphs])
        else:
            return "err: document type not supported"
        responses = self.model.generate_content(
            [self.prompt + "The filename is " + filename, document1, self.context],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=False,
        )
        return json.loads(responses.text.replace("json", "").replace("\n", "").replace("```", "").replace("```", ""))
