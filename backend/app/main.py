from fastapi import FastAPI

app = FastAPI(title="Campus Byte")

@app.get("/")
def home():
    return {"message": "Campus Byte is running"}
