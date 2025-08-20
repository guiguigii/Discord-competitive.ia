import os
import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from rag import answer_question

app = FastAPI()

DISCORD_PUBLIC_KEY = os.getenv("DISCORD_PUBLIC_KEY")

verify_key = VerifyKey(bytes.fromhex(DISCORD_PUBLIC_KEY))

def verify_signature(request: Request, body: bytes):
    signature = request.headers["x-signature-ed25519"]
    timestamp = request.headers["x-signature-timestamp"]
    message = timestamp.encode() + body
    try:
        verify_key.verify(message, bytes.fromhex(signature))
    except BadSignatureError:
        return False
    return True

@app.post("/interactions")
async def interactions(request: Request):
    body = await request.body()
    if not verify_signature(request, body):
        return JSONResponse(content={"error": "Invalid request"}, status_code=401)

    data = json.loads(body)
    if data["type"] == 1:  # PING
        return JSONResponse(content={"type": 1})

    if data["type"] == 2:  # SLASH COMMAND
        if data["data"]["name"] == "ask":
            question = data["data"]["options"][0]["value"]
            answer = answer_question(question)
            return JSONResponse(content={"type": 4, "data": {"content": answer}})
