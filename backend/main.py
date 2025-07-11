from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from password_gen import generate

app = FastAPI()

# Enable frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to frontend domain
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate")
def generate_passphrase():
    data = generate()
    return {
        "password": data["password"],
        "phrases": [{"category": c, "phrase": p} for c, p in data["phrases"]]
    }

