from fastapi import FastAPI
from auth_service.db.database import get_db
from contextlib import asynccontextmanager
from auth_service.api import auth
from fastapi.middleware.cors import CORSMiddleware
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    except Exception as e:
        print(e)
    finally:
        pass


app = FastAPI(lifespan=lifespan)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
origins = [
    "http://localhost:8001", # Swagger Chat Service
    "http://localhost:8000", # Swagger Auth Service (на всяк випадок)
    "http://127.0.0.1:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Дозволяємо запити з цих адрес
    allow_credentials=True,
    allow_methods=["*"],        # Дозволяємо всі методи (GET, POST...)
    allow_headers=["*"],        # Дозволяємо всі хедери (Authorization...)
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
