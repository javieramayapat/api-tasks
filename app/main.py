from fastapi import FastAPI, status

app = FastAPI(title="📑 Task API 📑",
              version="1.0",
              description="Personal task api to manage user's tasks")


@app.get(path="/", tags=['Root'], status_code=status.HTTP_200_OK)
def index():
    return {"Hello": "Welcome to Task API 📑"}

