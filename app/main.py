from fastapi import FastAPI
from app.routes import notes
from app.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app = FastAPI(debug=True)

app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(notes.router,prefix='/notes',tags=['Notes'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allows requests from the frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
