from fastapi import FastAPI
from app.routes import notes
from app.auth import router as auth_router

app = FastAPI()

app = FastAPI(debug=True)

app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(notes.router,prefix='/notes',tags=['Notes'])

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
