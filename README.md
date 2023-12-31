# IoT 저장소 소프트웨어 메뉴얼

# IoT 저장소 관리 소프트웨어

1. 실행 및 로그인

    1.1. 실행

    1.2. 로그인

    1.3. 회원가입

2. 화면 및 기능 설명

    2.1. 시스템 모니터링

    2.2. 저장소 사용 및 관리

## IoT 저장소 모듈 소프트웨어

1. 실행

# IoT 저장소 관리 소프트웨어

# 1. 실행 및 로그인

## 1.1. 실행

<aside>
⚠️ “~/App/.env” 파일의 REACT_APP_URL을 저장소 소프트웨어가 동작하고 있는 주소로 변경해주세요.

</aside>

-   소스코드 및 실행파일 레포지토리

[https://github.com/qqaazz0222/2023-IoT-Storage](https://github.com/qqaazz0222/2023-IoT-Storage)

1. 레포지토리 복사

    ```
    $ git clone https://github.com/qqaazz0222/IoT_Storage.git
    ```

2. 관리 소프트웨어 실행

    ```
    $ cd ~/App
    $ npm install
    $ npm start
    ```

3. 관리 소프트웨어 접속

    - 웹 : http://localhost:3000/
    - 프로그램

    ```
    $ cd ~/Program
    $ python program.py
    or
    $ python3 program.py
    ```

    <aside>
    💡 프로그램 실행시, pip를 통한 pywebview 라이브러리를 설치가 필요합니다.

    </aside>

![Untitled](1.png)

## 1.2. 로그인

1. 초기화면 하단 로그인 버튼을 통해 로그인 화면으로 이동
2. 아이디, 비밀번호 입력 후, 하단 로그인 버튼을 통해 로그인 진행

<aside>
💡 테스트 계정 ID : test1 / PW : password1

</aside>

![Untitled](2.png)

## 1.3 회원가입

1. 초기화면 하단 가입하기 링크를 통해 회원가입 화면으로 이동
2. 아이디, 비밀번호 입력 후, 이용약관 및 개인정보 정책에 대해 동의 체크박스를 체크
3. 하단 확인 버튼을 통해 회원가입 진행

![Untitled](3.png)

# 2. 화면 및 기능 설명

## 2.1. 시스템 모니터링 화면

![Untitled](4.png)

1. 상단 네비게이션바 : 화면간 전환이 가능합니다.
2. 시스템 정보 : CPU 및 메모리 사용률을 확인할 수 있습니다.
    - 동작속도 및 사용시간 표시가 미지원 되는 운영체제 및 프로세서가 있을 수 있습니다.
3. 저장소 요약 : 현재 디바이스에 부착된 저장소 및 정보를 확인할 수 있습니다.

## 2.2. 저장소 사용 및 관리 화면

![Untitled](5.png)

1. 파일 업로드 : 현재 표시되고 있는 저장소에 파일을 업로드할 수 있습니다.

    - 화면 중앙 영역을 클릭 또는 파일을 드래그 엔 드롭하여 파일을 업로드할 수 있습니다.

    ![Untitled](6.png)

2. 저장소 선택 : 저장소 목록을 확인하고, 표시할 저장소를 선택할 수 있습니다.
3. 저장소 정보 : 저장소에 대한 정보를 표시합니다.
4. 저장소 뷰 : 저장소에 있는 디렉터리 및 파일을 확인하고, 접근 및 다운로드 할 수 있습니다.

    - 저장소 뷰에 표시되는 폴더 클릭시, 해당 폴더로 들어갈 수 있습니다.
    - 저장소 뷰에 표시되는 파일 클릭시, 해당 파일을 다운로드 받을 수 있습니다.

    <aside>
    ⏰ 미리보기 기능 지원 예정

    </aside>

# IoT 저장소 모듈 소프트웨어

## 1. 실행

[https://github.com/qqaazz0222/2023-IoT-Storage](https://github.com/qqaazz0222/2023-IoT-Storage)

1. 레포지토리 복사

    ```
    $ git clone https://github.com/qqaazz0222/IoT_Storage.git
    ```

2. 관리 소프트웨어 실행

    ```
    $ cd ~/Server
    $ python app.py
    or
    $ python3 app.py
    ```

<aside>
⚠️ 필수 설치 라이브러리 : flask, flask_cors, dotenv, psutil

</aside>
