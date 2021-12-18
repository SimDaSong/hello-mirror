# hello-mirror 

> 헬로 미러 프로젝트
> 
> https://github.com/HackerShackOfficial/Smart-Mirror 를 참고하여 제작 하였습니다.

Raspberry powered mirror which can display the news, weather, bus time table and time.

### 헬로미러란?
헬로미러는 스마트미러 기반의 프로젝트입니다.

### 스마트미러란?
스마트미러는 거울(Mirror)과 디스플레이(Display)가 합쳐진 차세대 디스플레이로, 날씨, 시간, 뉴스 등 사용자가 필요로 하는 간단한 정보들을 거울 속에 띄워줍니다.

**사용 예시**

![image](https://user-images.githubusercontent.com/35736920/146646175-c00660b9-4a6f-4424-94d7-4f3fa1a69fac.png)

**소프트웨어 구상도**

![image](https://user-images.githubusercontent.com/35736920/146646178-63f5849e-22be-4446-aeb0-bee6f7ff66f4.png)

**하드웨어 구상도**

![image](https://user-images.githubusercontent.com/35736920/146646186-4797c458-77da-479e-925e-82fe0dbc8f36.png)

---

## Installation and Updating
```
git clone https://github.com/SimDaSong/hello-mirror.git
```
Alternatively, you can download a zip file containing the project (green button on the repository page)

## Navigate to the folder for the repository
```
cd hello-mirror
```

## Install your dependencies
make sure you have pip installed before doing this
```
sudo pip install -r requirements.txt
sudo apt-get install python-imaging-tk
```

## Add your api token
Copy the .env.sample to create a .env file and add content.

In the root directory, rename the json file issued by https://developers.google.com/workspace/guides/create-credentials to credentials.json and save it.

## Running
To run the application run the following command in this folder
```
python3 hello-mirror/__main__.py
```

## Demo

![image](https://user-images.githubusercontent.com/35736920/146646212-a3f98f14-9781-4ae6-8771-c16e9fdbea5e.png)

