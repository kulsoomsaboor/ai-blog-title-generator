from fastapi import FastAPI
from app.routes import generator
from fastapi.middleware.cors import CORSMiddleware

import logging

logging.basicConfig(
    level=logging.INFO)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods: POST, GET, etc.
    allow_headers=["*"],  # allow all headers
)

app.include_router(generator.router)




