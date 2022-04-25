

<h1 align="center">Fast API Boilerplate <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="48px"></h1>
<p>
</p>

<center>
       Fast API Boilerplate 보일러 플레이트 입니다.
</center>

<br>

## ✨ Description

```sh

간단한 CRUD를 구현 하였습니다. pytest를 이용하여 CRUD 테스트가 가능합니다. 
GitAction을 이용하여 간단한 CI/CD를 구현하였습니다.

```

## 🏃 Run

```sh

gunicorn -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:9001 --access-logfile ../gunicorn-access/log

=============================================================================================================

-k uvicorn.workers.UvicornWorker : Uvicorn worker 클래스를 사용
–access-logfile : Gunicorn 로그 파일 기록
app:app :  app.py의 app 실행
-workers 3 : worker process 갯수 (CPU 코어 * 3)
–daemon : Gunicorn을 백그라운드 데몬 구동
–bind 0.0.0.0:9001 : 9001 포트에 서버 연결 

```


## 🔧 Tech Stack

### Tech Stack
<div>
    <center>
        <img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/>
        <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=FastAPI&logoColor=white"/>
        <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=MongoDB&logoColor=white"/>
    </center>
</div>



## ⚙️ System Architecture

<center>
    <img src="https://user-images.githubusercontent.com/61954751/165026128-e015e113-bf67-4807-97ad-4c528194cfec.png" alt="Architecture"/>
</center>
<br>


## 🤼‍ Author

 **🐯 Duhui Lee**
<br>

<hr>

## 📝 License

Copyright © 2022 Duhui Lee <br>
