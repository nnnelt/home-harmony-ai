from fastapi import FastAPI, UploadFile, File, Form
from image_search import search_images
from text_search import load_text_search_model, search_products
from matchmaking import match_designers

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Load text search model once
    load_text_search_model()

@app.get("/")
def read_root():
    return {"message": "Welcome to Home Harmony Full API"}

@app.post("/search/image")
async def image_search_endpoint(file: UploadFile = File(...)):
    return search_images(file)

@app.post("/search/text")
def text_search_endpoint(query: str = Form(...)):
    return search_products(query)

@app.post("/match")
def matchmaking_endpoint(style: str = Form(...), budget: str = Form(...)):
    return match_designers(style, budget)
