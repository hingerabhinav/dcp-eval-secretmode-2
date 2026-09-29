from fastapi import FastAPI

app = FastAPI(title="dcp-eval-secretmode-2")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "dcp-eval-secretmode-2", "owner": "harness"}
