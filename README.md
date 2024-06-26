# 📌: ETRI_ADS_V2X_simulator
> 자율주행 차량의 ADS 통신 프로토콜 검증 시뮬레이터

</br>

## 1. 제작 기간 & 참여 인원 & 프로젝트 기여도
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
![시뮬레이터 설계도](https://github.com/havingforlunch/ETRI_ADS_V2X_simulator/assets/105187310/75ace104-b271-46c7-805b-04da9c5be102)

## 4. 핵심 기능
이 시뮬레이터의 핵심 기능은 협력 주행을 위한 프로토콜을 검증과 차량의 움직임을 확인 하는 기능입니다.
사용자는 J2735에서 정의한 메시지들을 기반으로 협력주행 상황에 맞도록 통신하고, 각 case만 선택하면 끝입니다.


### 4.1 전체 흐름도
![시뮬레이터 흐름도](https://github.com/havingforlunch/ETRI_ADS_V2X_simulator/assets/105187310/e317ad0d-03e8-4334-a621-1858d843a6e4)

### 4.2 차량의 움직임
![차량 움직임 구현](https://github.com/havingforlunch/ETRI_ADS_V2X_simulator/assets/105187310/b71e1c0d-146d-4a78-b17f-13b70e0d0b08)

- **차량 움직임 구현** 🚗
  -  차량은 사전에 받은 주행 기록을 바탕으로 움직입니다.
  -  주행 기록의 위도, 경도 좌표를 해당 시뮬레이터 좌표로 변환합니다.
  -  지정된 차량의 속도를 통해 실시간으로 차량의 이동 거리를 계속하여, 차량의 위치를 찍어줍니다.
  -  차량의 이동 거리가 A와 B 사이라면, A와 B 지점을 직선 상의 A로부터 이동 거리 만큼 떨어진 위치를 차량의 위치로 합니다.
  -  그 다음 이동 거리를 계산했을 때, B 지점까지의 거리를 넘는다면 B와 C 지점 사이로 차량의 위치를 측정합니다.
  -  ⚠️해당 시뮬레이터에서 사용한 차량 주행 기록은 15km/h의 낮은 속도와 0.1초 간격으로 매우 촘촘하게 찍혀있기 때문에, 각 지점의 간격은 매우 좁습니다.

### 4.3 다양한 Case 테스트

- **테스트를 위한 시나리오 구현**
  - 테스트에 맞는 시나리오를 따로 구현하였으며, 시나리오를 선택함과 동시에 차량들의 움직임과 테스트를 위한 통신 프로토콜의 전송이 시작됩니다.
  - 다양한 테스트와 성능 검증을 위해, 시뮬레이션 차량의 2가지 기능이 있습니다. (속도 변환, 위치 고정 등)

 
## 5. 프로젝트 결과
![시뮬레이터 결과1](https://github.com/havingforlunch/ETRI_ADS_V2X_simulator/assets/105187310/bb9a0306-35ef-49f0-b193-44ce008ad9f4)
![시뮬레이터 결과2](https://github.com/havingforlunch/ETRI_ADS_V2X_simulator/assets/105187310/970bdee8-776c-4414-95f1-544c84026d03)

