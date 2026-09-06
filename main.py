from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI server is alive"}

@app.post("/audio")
async def receive_audio():
    print("Audio received from ESP32!")
    return {"status": "audio received"}