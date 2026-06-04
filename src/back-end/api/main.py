# import fastapi library
from fastapi import FASTAPI

# create a fastapi application
app = FASTAPI()

# create a endpoint called /health
@app.get("/health")

# endpoint return message status
def health():
    return{"status":"ok"}