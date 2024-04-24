import base64
import json
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


def generate(document):
    vertexai.init(project="polar-equinox-420601", location="us-central1")
    model = GenerativeModel("gemini-1.5-pro-preview-0409")

    document1 = Part.from_data(
    mime_type="application/pdf",
    data=base64.b64decode(document))
    text1 = """You are a carbon analyst accounting for carbon emissions from aluminium production. You need to 
    extract the materials from the invoice and the purchase agreement, and convert the units into SI unit.  Classify 
    the materials into the different scope and sub category using the context information below. The final output 
    should be in a table format. Add minimal justification in the table, as well as the source of the material using 
    its file name, eg. MOCK INVOICE.pdf. Output the result in JSON format."""
    responses = model.generate_content(
        [text1, document1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    for response in responses:
        print(response.text, end="")
