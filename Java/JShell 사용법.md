### JShell 사용법/명령어
---

- 명령프롬프트 cmd에서 명령어를 입력
    
    ```
    > jshell
    ```
    
- 도움말
        
    ```
    > /help intro
    ```
        
- 종료하려면 아래의 명령어를 입력
    
    ```
    > /exit
    ```

- JShell에서 생성한 method들 확인하기
    
    ```
    > /methods
    |    void sayHelloWorld()
    ```
    
- JShell 기록 저장하기
    
    ```
    > /save backup.txt
    ```
    
    - 백업 파일이 Shell이 작동 중인 디렉토리에 저장된다

- 편집
    
    ```java
    > /edit sayHelloWorld()
    
    // 수정 후...
    |    modified method sayHelloWorld()
    ```
    
    - `/edit` + `(편집하고자 하는 method 등)` 명령어를 실행하면 **“JShell Edit Pad”** 창이 나타나고, 작성한 내용 편집이 가능하다.


- 내용 불러오기
    
    ```java
    > /list printNumbers
    
    28 : void printNumbers(int n) {
           for(int i = 0; i <= n; i++) {
               System.out.println(i);
           }
       }
    ```
    
    - `/list` + `(확인하고자 하는 method 등)` 명령어를 입력하면 내용을 확인할 수 있다.