import uvicorn
from fastapi import FastAPI

from app import app_settings

project_data = app_settings.project_detail_information


app = FastAPI(**project_data)


@app.get("/api/")
async def hello():
    return {"message": "Hello, world!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
