참고

- https://www.youtube.com/@kingchobo
- https://www.youtube.com/playlist?list=PLTb3qGCzYjS0Lwc-lnQMsvbc8NPBdhRTj

---

- python 가상환경 생성

```shell
python -m venv [projectName]
```

- python 가상환경 실행 / windows 10 env

```shell
[projectName]\Scripts\activate
```

- python 가상환경 특정 버젼 설치

```shell
pip install django==5.0.3
```

- python 가상환경 종료

```python
deactivate
```

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
