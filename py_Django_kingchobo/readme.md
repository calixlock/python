## 참고

- https://www.youtube.com/@kingchobo
- https://www.youtube.com/playlist?list=PLTb3qGCzYjS0Lwc-lnQMsvbc8NPBdhRTj

---

### status :

- 2024-06-08 ~ 2024-06-10
- ( 06 / 07 )

---

### 환경 셋팅

- python 3.1 버전 이상 설치 > django 5.0 설치 가능

- python 가상머신 환경 생성

```sh
python -m venv [projectName]
```

- python 가상머신 환경 실행 및 종료 / windows 10 env

```sh
# 실행
[projectName]\Scripts\activate
# 종료
[projectName]\Scripts\deactivate
deactivate
```

- python 가상머신 내 특정 버전 설치

```sh
# 설치된 pip 리스트 확인
pip --list
# django 5.0.3 특정 버전 설치
pip install django==5.0.3
```

### django 프로젝트 생성 및 실행

- python 가상환경 접속 후 Django_project 생성

```sh
mkdir [mysite : django project folder name]
cd [mysite]
# 프로젝트의 config를 설정할 폴더위치 지정[.]
django-admin startproject config .
```

- Django_project server 실행

```sh
# manage.py가 있는 경로를 찾아 실행
py manage.py runserver
# (일반적으로) 127.0.0.1:8000에서 접근 가능
```

```sh
py .\mysite\manage.py startapp [kingchobo : appServiceName]

```

- Django shell 실행

````sh
# 가상환경에 접속 후 manage.py가 있는 경로를 찾아 실행
py manage.py shell

---

### db_sqlite3 table 생성 및 migration

- DB에 데이터 테이블 형식 셋팅

  - 1. 데이터 필드 지정

    - 특정 mysite/kingchobo/models.py 내부에 필요한 데이터 필드 지정

      ```py
      class Member(models.Model):
      name = models.CharField(max_length=50)
      email = models.CharField(max_length=100)
      profile = models.TextField()
      create_date = models.DateTimeField()
      ```

  - 2. settings에 config 작성

    - mysite/config/settings.py 내부에 추가될 config 넣기
      ```py
      INSTALLED_APPS = [
        # db에 적재할 class 등록
        'kingchobo.apps.KingchoboConfig',
        ]
      ```

  - 3. `makemigrations` 실행

    - shell에서 `py manage.py makemigrations` 명령어 실행
    - mysite/kingchobo/migrations/ 내부에 추가된 파일 확인

    - 0001_initial.py 파일 생성됨(파일명은 다를수 있음).

  - 4. `sqlmigrate` 실행

    - migration 진행 전 `py manage.py sqlmigrate kingchobo 0001` shell에 입력하여 migration 진행 전 일어날 현상 확인 가능

  - 5. `migrate` 진행
    - shell에서 `py manage.py migrate` 명령어 실행
    - migrate 진행됨
    - sqlite3 viewer로 생성된 `kingchobo_member` table 확인 가능

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
````
