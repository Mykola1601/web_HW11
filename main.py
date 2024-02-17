import uvicorn
from fastapi import FastAPI, File, UploadFile, status
from sqlalchemy.orm import Session
from fastapi import  HTTPException, Depends
from src.database.db import get_db
from sqlalchemy import text
import pathlib


MAX_FILE_SIZE = 1_000_000  # 1Mb


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


@app.post("/upload-file/")
async def upload_file(file: UploadFile = File()):
    pathlib.Path("uploads").mkdir(exist_ok=True)
    file_path = f"uploads/{file.filename}"
    file_size = 0
    with open(file_path, "wb") as f:
        while True:
            chunk = await file.read(1024)
            if not chunk:
                break
            file_size += len(chunk)
            if file_size > MAX_FILE_SIZE:
                f.close()
                pathlib.Path(file_path).unlink()
                raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="File to big")
            f.write(chunk)
    return {"file_path": file_path}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


    