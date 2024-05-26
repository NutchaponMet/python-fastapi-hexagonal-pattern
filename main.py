from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.main import root
from domain.core.config import settings
from logs.logs import logger, LOGGING_CONFIG_PRD, LOGGING_CONFIG_DEV

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(root, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    if settings.SERVER_MODE == "release":
        logger.info("Server started production mode at port 8000")
        uvicorn.run(
            "main:app", 
            host="0.0.0.0", 
            port=settings.SERVER_PORT, 
            workers=5, 
            reload=False, 
            log_config=LOGGING_CONFIG_PRD,
        ) # for production
    else:
        logger.info("Server started development mode at port 8000")
        uvicorn.run(
            "main:app",
            host="127.0.0.1",
            port=settings.SERVER_PORT, 
            reload=True, 
            log_config=LOGGING_CONFIG_DEV,
        ) # for dev