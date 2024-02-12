# Generator
[CRM (고객관리 솔루션) 프로젝트](https://github.com/etesongg/Flask) 개발을 위해 필요한 데이터 생성기 개발
- 생성 가능한 데이터 : User, Store, Item, Order, OrderItem

### 사용법
1. 파일 실행 후 원하는 데이터 갯수와 출력될 결과물 타입을 선택한다.
```python
python main.py
```
````
user 데이터를 생성할 개수를 입력해주세요: 10000
출력될 결과물 타입을 입력해주세요(console, csv): csv
user.csv write done
store 데이터를 생성할 개수를 입력해주세요: 150
출력될 결과물 타입을 입력해주세요(console, csv): csv
store.csv write done
order 데이터를 생성할 개수를 입력해주세요: 100000
...
````

<br/>

2. sqlite3를 통해 생성된 csv파일을 db 테이블로 옮겨주는 작업을 한다.
```
sqlite3 crm.db
.mode csv
.import user.csv user
```

### 기술 스택
- 언어 : Python 
- 데이터베이스 : sqlite3

