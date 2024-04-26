## Setup
`pip install -r requirements.txt`

## Local
Backend

`uvicorn main:app --reload`

## Deploy

`gcloud app deploy frontend.yaml dispatch.yaml app.yaml`