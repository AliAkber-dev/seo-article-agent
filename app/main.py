from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="SEO Article Generation Agent")
app.include_router(router)

@app.get("/health")
def root():
    return {"message": "SEO Article Agent Running"}