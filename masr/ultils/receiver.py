from fastapi import FastAPI, Request

app = FastAPI()

def gen_receiver(dtypes, listen):
    @app.post(listen)
    async def receiver(request: Request):
        ...