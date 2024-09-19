# TODO : 여기에 지시사항에 맞게 라우터를 작성하여 app에 추가해 주세요
from fastapi import APIRouter, Query
# TODO : 라우터의 태그는 "assignments"로 지정해 주세요.
router = APIRouter(tags=["assignments"])

# TODO: 단순 요청에 대한 응답을 하는 EndPoint 작성


@router.get("/hello")
def hello():
    return {"message": "Hello World!"}


# TODO: 쿼리 파라미터를 받아서 응답을 하는 EndPoint 작성

@router.get("/sum")
def sum_numbers(num1: int = Query(...), num2: int = Query(...)):
    return {"num1": num1, "num2": num2, "sum": num1 + num2}


# TODO: Path Parameter를 받아서 응답을 하는 EndPoint 작성

@router.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
