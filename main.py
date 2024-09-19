from fastapi import FastAPI
# TODO: routes 패키지 내의 assignments 모듈을 import 해주세요.
from routes.assignments import router
app = FastAPI()

# TODO: app에 라우터를 추가해 주세요.
app.include_router(router)

# TODO: 아래 author 부분에 본인 이름을 적어주세요.
author = "유승원"


@app.get("/", tags=[author])
def assignment_home():
    return {"message": "본 소스는 딥러닝 서빙을 위한 FastAPI 서버입니다.",
            "author:": f"수강생 이름: {author}"}


if __name__ == "__main__":
    import uvicorn
    # uvicorn을 모듈 경로로 실행
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True)

