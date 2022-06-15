from fastapi import FastAPI
import uvicorn


app = FastAPI(title="FastAPI Online Store", description="FastAPI Study Project")


if __name__ == 'main':
  uvicorn.run("main:app", reload=True)