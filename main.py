from collections.abc import Callable
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.operations import add, divide, multiply, subtract

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class CalculationRequest(BaseModel):
    a: float
    b: float


def calculate(
    operation: Callable[[float, float], float | int],
    values: CalculationRequest,
) -> dict[str, float | int] | JSONResponse:
    try:
        result = operation(values.a, values.b)
    except ValueError as error:
        return JSONResponse(status_code=400, content={"error": str(error)})
    return {"result": result}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/add")
def add_numbers(values: CalculationRequest):
    return calculate(add, values)


@app.post("/subtract")
def subtract_numbers(values: CalculationRequest):
    return calculate(subtract, values)


@app.post("/multiply")
def multiply_numbers(values: CalculationRequest):
    return calculate(multiply, values)


@app.post("/divide")
def divide_numbers(values: CalculationRequest):
    return calculate(divide, values)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
