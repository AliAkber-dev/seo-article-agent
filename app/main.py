from fastapi import FastAPI
from app.routers import jobs_router

app = FastAPI(title="SEO Article Generation Agent")
app.include_router(prefix="/api", router=jobs_router.router, tags=["Article Jobs"])

@app.get("/health")
def root():
    return {"message": "SEO Article Agent Running"}