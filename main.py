from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from infer import predict_disease

class Info(BaseModel):
    id: int
    diseases: List[str]


app = FastAPI()


@app.get("/")
def read_root():
    return {"Message": "VinHack 2023!!"}


@app.post("/predict")
async def text(obj: Info):
    print(obj.diseases)
    predicted_disease = predict_disease(obj.diseases)
    res = jsonable_encoder(predicted_disease[0])
    return JSONResponse(content={"predicted_disease" : res})
    
