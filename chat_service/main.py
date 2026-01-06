from fastapi import FastAPI
from contextlib import asynccontextmanager
from chat_service.api.messages import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    except Exception as e:
        print(e)
    finally:
        pass


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)