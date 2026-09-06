from fastapi import FastAPI, Request
from datetime import datetime
from pathlib import Path

app = FastAPI()

AUDIO_DIR = Path("audio_uploads")
AUDIO_DIR.mkdir(exist_ok=True)


@app.get("/")
def home():
    return {
        "status": "Neighbourhood Labs AI server is alive"
    }


@app.post("/audio")
async def receive_audio(request: Request):

    audio_data = await request.body()

    size = len(audio_data)

    print(f"Received {size} bytes from ESP32")

    if size == 0:
        return {
            "status": "error",
            "message": "No audio data received"
        }

    timestamp = datetime.utcnow().strftime(
        "%Y%m%d_%H%M%S_%f"
    )

    filename = AUDIO_DIR / f"esp32_{timestamp}.bin"

    with open(filename, "wb") as f:
        f.write(audio_data)

    print(f"Saved audio to {filename}")

    return {
        "status": "audio received",
        "bytes": size,
        "file": str(filename)
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "Neighbourhood Labs AI"
    }