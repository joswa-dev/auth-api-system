from fastapi import FastAPI
from .database import Base, engine
from .models import User
from .auth import auth_router

app = FastAPI(title="Authify API")

# create tables
Base.metadata.create_all(bind=engine)

# include auth routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])


@app.get("/")
def root():
    return {"status": "Authify running"}
