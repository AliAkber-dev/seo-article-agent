from fastapi import FastAPI

app = FastAPI(title="SEO Article Generation Agent")


@app.get("/")
def root():
    return {"message": "SEO Article Agent Running"}