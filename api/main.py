from fastapi import FastAPI
from .routers import products_router
import uvicorn
from dotenv import load_dotenv

load_dotenv()

router_modules = [products_router]

app = FastAPI(title="FastAPI Online Store", description="FastAPI Study Project")

for router in [getattr(module, "router") for module in router_modules]:
    app.include_router(router)


if __name__ == "main":
    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
