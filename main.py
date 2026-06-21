from fastapi import FastAPI

from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
title="Campus Placement Management System",
version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
return {
"message": "Campus Placement Management System API"
}
