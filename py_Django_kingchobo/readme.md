## 참고

#### 참고 영상

- https://www.youtube.com/@kingchobo
- https://www.youtube.com/playlist?list=PLTb3qGCzYjS0Lwc-lnQMsvbc8NPBdhRTj

#### 장고 docs / db

- https://docs.djangoproject.com/en/5.0/topics/db/queries/

---

### status :

- 2024-06-08 ~ 2024-06-10
- ( 07 / 07 )

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

```sh
# 가상환경에 접속 후 manage.py가 있는 경로를 찾아 실행
py manage.py shell

```

---

### db_sqlite3 table 생성 및 migration

- DB에 데이터 테이블 형식 셋팅

  - 1. 데이터 필드 지정

    - 특정 mysite/kingchobo/models.py 내부에 필요한 데이터 필드 지정

  ```sh
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

### db_data 접근 방식 query

```sh
# django shell 접근
py manage.py shell
```

#### data 조회

```py
from kingchobo.models import Member
Member.objects.all() # 객체 내 전체 data 조회
Member.objects.filter(id=1) # id가 1인 객체 list적 조회 / 없을 경우 빈 list 반환
Member.objects.get(id=1) # 특정 객체(id=1) 하나 조회 / 없을 경우 오류 발생
Member.objects.filter(name__contains="x") # 특정 이니셜을 포함한 데이터 조회
```

#### data CRUD

```py
from kingchobo.models import Member
from django.utils import timezone
# data create
m = Member(name="ex_name",email="ex_email",profile="ex_profile",create_date=timezone.now())
m.save()
# data read & delete
m = Member.objects.get(id=1) # id가 1인 객체 read
m.delete()

# data modify
m = Member.objects.get(id=1)
## 수정하고자 하는 값 변환
m.name = "another_name"
m.email = "another_email"
m.profile = "another_email"
m.save()

```

---

## ※ 주의

### python 파일 gitignore 적용

```sh
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
