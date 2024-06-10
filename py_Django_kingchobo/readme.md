---
start - end: 2024-06-08 ~ 2024-06-
---

참고

- https://www.youtube.com/@kingchobo
- https://www.youtube.com/playlist?list=PLTb3qGCzYjS0Lwc-lnQMsvbc8NPBdhRTj

---

- python 가상머신 환경 생성

```sh
python -m venv [projectName]
```

- python 가상머신 환경 실행 / windows 10 env

```sh
[projectName]\Scripts\activate
```

- python 가상머신 내 특정 버젼 설치

```sh
pip install django==5.0.3
```

- python 가상머신 종료

```sh
deactivate
```

- python 가상환경 접속 후 Django_project 생성

```sh
mkdir [mysite : django project folder name]
cd [mysite]
# 프로젝트의 config를 설정할 폴더위치 지정[.]
django-admin startproject config .
```

- Django_project 실행

```sh
# manage.py가 있는 경로를 찾아 실행
py manage.py runserver
# (일반적으로) 127.0.0.1:8000에서 접근 가능
```

- Django_project

```sh
py .\mysite\manage.py startapp [kingchobo : appServiceName]

```

---

### ※ 주의

python 파일 gitignore 적용

```shell
# add된 상태에서 .gitignore가 안통하기 때문에 스테이징 된 것들 일단 모두 되돌려 다시 설정
출처: https://inpa.tistory.com/entry/GIT-⚡️-gitignore-자동-생성 [Inpa Dev 👨‍💻:티스토리]
git rm -r --cached .
git add .
git commit -m "Apply .gitignore"

----------------------------------------------
# ignore 처리된 파일 확인
git status --ignored

▶ 출처: https://inpa.tistory.com/entry/GIT-⚡️-gitignore-자동-생성 [Inpa Dev 👨‍💻:티스토리]`
```
