# 📌: ETRI_ADS_V2X_simulator
> 자율주행 차량의 ADS 통신 프로토콜 검증 시뮬레이터

</br>

## 1. 제작 기간 & 참여 인원 % 프로젝트 기여도
- 2022년 3월 ~ 11월 (9개월)
- 연구실 용역 프로젝트
- BE 1명/ FE 1명/ PM 1명
- BE 기여도 85%

</br>

## 2. 사용 기술
#### 'Back-end'
  - Python 3.8
  - haversine
#### 'Front-end'
  - ursina
  - PyQT5
  - pyqtautogui
  - pyqtgraph

</br>

## 3. 시뮬레이터 설계
![시뮬레이터 설계도](https://github.com/havingforlunch/ETRI_ADS_V2X_simulator/assets/105187310/fcec0e92-4e10-4533-bd89-450ffafd3a68)

## 4. 핵심 기능
이 시뮬레이터의 핵심 기능은 협력 주행을 위한 프로토콜을 검증과 차량의 움직임을 확인 하는 것입니다.
사용자는 J2735에서 정의한 메시지들을 기반으로 협력주행 상황에 맞도록 통신하고, 각 case만 선택하면 끝입니다.
