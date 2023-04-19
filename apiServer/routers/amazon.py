from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from urllib.request import urlopen
import json

router = APIRouter()

app = FastAPI()
origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@router.get("/eda-get-amazon", tags=["Amazon"])
async def get_data_amazon():
  url = 'https://raw.githubusercontent.com/alanmgg/YFinance-Docs/main/Docs/data_amazon.json'
  response = urlopen(url)
  data_json = json.loads(response.read())

  return data_json

@router.get("/eda-tail-amazon", tags=["Amazon"])
async def tail_data_amazon():
  url = 'https://raw.githubusercontent.com/alanmgg/YFinance-Docs/main/Docs/data_amazon_tail.json'
  response = urlopen(url)
  data_json = json.loads(response.read())

  return data_json

@router.get("/eda-description-amazon", tags=["Amazon"])
async def description_data_amazon():
  url = 'https://raw.githubusercontent.com/alanmgg/YFinance-Docs/main/Docs/data_amazon_description.json'
  response = urlopen(url)
  data_json = json.loads(response.read())

  return data_json

@router.get("/eda-describe-amazon", tags=["Amazon"])
async def describe_data_amazon():
  url = 'https://raw.githubusercontent.com/alanmgg/YFinance-Docs/main/Docs/data_amazon_describe.json'
  response = urlopen(url)
  data_json = json.loads(response.read())

  return data_json

@router.get("/eda-corr-amazon", tags=["Amazon"])
async def corr_data_amazon():
  url = 'https://raw.githubusercontent.com/alanmgg/YFinance-Docs/main/Docs/data_amazon_corr.json'
  response = urlopen(url)
  data_json = json.loads(response.read())

  return data_json