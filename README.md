# LEARNING을 통한 태풍경로 예측

---

최근 태풍들의 위치정보들을 통해 3시간 후 태풍의 위치를 예측하는 머신러닝을 사용합니다.



### FACTORS

---

함수를 모델링하기 위해서 저희는 태풍의 위치(latitude, longitude)와, 그 시간대의 수온(WT)과 풍향(WD)를 이용했습니다. 공공기관에서 제공하는 데이터 특성상 시간대의 간격은 3시간 입니다. 



### LEARNING

---

향후 추가 바람.



## 파일들 목록

---

1. AccessDB.py
   - 원하시는 서버 mysql에 저장된 태풍들의 정보들을 보관할만한 sql문을 작성해줍니다.
2. InputDB.py
   * 원하시는 서버의 mysql 내부 database에 최근 태풍들의 위치정보를 input 합니다.
3. TyphoonList.py
   * 2001년부터 2019년 까지의 우리나라의 영향태풍들의 index와 이름을 크롤링합니다.
4. TyphoonListfunc.py
   * TyphoonList.py에서 받아온 태풍의 이름, index를 통해 태풍의 위치정보를 크롤링합니다.