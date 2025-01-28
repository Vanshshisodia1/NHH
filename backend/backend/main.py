from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ocr import router as ocr_router

app = FastAPI()

# CORS setup to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include OCR routes
app.include_router(ocr_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to SmartRx Backend!"}
