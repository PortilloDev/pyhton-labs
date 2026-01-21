from fastapi import FastAPI


app = FastAPI(title='Python - labs')

@app.get("/health-check")
async def health():
    return {"status": "ok"}