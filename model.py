import base64
import json
import time

import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
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
    def generate(self, document):
        document1 = Part.from_data(
            mime_type="application/pdf",
            data=base64.b64decode(document))
        responses = self.model.generate_content(
            [self.prompt, document1, self.context],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=False,
        )
        return json.loads(responses.text.replace("json", "").replace("\n", "").replace("```", "").replace("```", ""))
