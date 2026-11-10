import logging
import os

from flask import Flask

logging.basicConfig(
    level=logging.INFO,
    format='{"time":"%(asctime)s","level":"%(levelname)s","app":"app1","msg":"%(message)s"}',
)

app = Flask(__name__)
APP_VERSION = os.getenv("APP_VERSION", "dev")


@app.get("/")
def index() -> str:
    app.logger.info("index requested")
    return "Hello World 1"


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "app": "app1", "version": APP_VERSION}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
