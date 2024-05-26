import logging.config as __log_config
import logging as __logging

import uvicorn.logging
from domain.core.config import settings

import uvicorn



LOGGING_CONFIG_PRD: dict[str,] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": '{"log_level":"%(levelname)s","timestamp":"%(asctime)s","message":"%(message)s"}',
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '{"log_level":"%(levelname)s","ip_addr":"%(client_addr)s","req_line":"%(request_line)s","status_code":"%(status_code)s"}',  # noqa: E501
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "app": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": '{"log_level":"%(levelname)s","timestamp":"%(asctime)s","path":"%(filename)s/%(funcName)s;%(lineno)d","message":"%(message)s"}',
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
         "app" : {
            "formatter": "app",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
        "app" : {"handlers": ["app"], "level": "INFO",}
    },
}

LOGGING_CONFIG_DEV: dict[str,] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s | %(message)s",
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(asctime)s | %(client_addr)s | "%(request_line)s" | %(status_code)s',  # noqa: E501
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "app" : {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(asctime)s | %(filename)s/%(funcName)s | %(lineno)d | %(message)s",
            "use_colors": None,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "app" : {
            "formatter": "app",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
        "app" : {"handlers": ["app"], "level": "INFO", "propagate": False},
    },
}

def __log_setup():
    if settings.SERVER_MODE == "release":
        __log_config.dictConfig(LOGGING_CONFIG_PRD)
        logger = __logging.getLogger('app')
    else:
        __log_config.dictConfig(LOGGING_CONFIG_DEV)
        logger = __logging.getLogger('app')
    return logger

logger = __log_setup()