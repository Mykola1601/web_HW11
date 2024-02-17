import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi import  HTTPException, Depends
from src.database.db import get_db
from sqlalchemy import text

from src.routes import notes, tags, contacts
from middlewares import CustomHeaderMiddleware

app = FastAPI()
app.add_middleware(CustomHeaderMiddleware)

app.include_router(contacts.router, prefix='/api')
app.include_router(tags.router, prefix='/api')
app.include_router(notes.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/api/healthchecker")
async def healthcheck(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database not config correctly")
        return {"message":"welcome to fastAPI" }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=503, detail="Database connection error")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    