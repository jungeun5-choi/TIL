### Java에서 User Input 받기 : `Scanner`

---

- **전처리**

```java
import java.util.Scanner;
```

Scanner를 사용하려면 Scanner를 import 해주어야한다

<br/>

- **기본형**

```java
// Type obj = new Type(argument);
Scanner scanner = new Scanner(System.in);
```

Scanner를 통해 값의 출처를 정할 수 있는데, 우리는 사용자의 입력이 출처이기 때문에 `Scanner(System.in)`을 사용한다.

※ `System.in`이 사용자 입력값, `System.out`은 사용자의 출력값을 뜻한다

<br/>

- **예시**

```java
public static void main(String[] args) {

    // Type obj = new Type(argument);
    Scanner scanner = new Scanner(System.in);
    
    System.out.println("Enter... Number1: ");
    int number1 = scanner.nextInt();
    
    System.out.println("The number you entered is - " + number1);

}
```

`scanner.nextInt();`는 정수값을 읽는다.

<br/>

### 📝 **스캐너(Scanner)의 주요 메서드**

| 메소드 | 설명 |
| --- | --- |
| String next() | 다음 토큰을 문자열로 리턴 |
| byte nextByte() | 다음 토큰을 byte 타입으로 리턴 |
| short nextShort() | 다음 토큰을 short 타입으로 리턴 |
| int nextInt() | 다음 토큰을 int 타입으로 리턴 |
| long nextLong() | 다음 토큰을 long 타입으로 리턴 |
| float nextFloat() | 다음 토큰을 float 타입으로 리턴 |
| double nextDouble() | 다음 토큰을 double 타입으로 리턴 |
| String nextLine() | ' \n '을 포함하는 한 라인을 읽고 ' \n '을 버린 나머지만 리턴 |
| void close() | Scanner의 사용 종료 |
| boolean hasNext() | 현재 입력된 토큰이 있으면 true, 아니면 새로운 입력이 들어올 때까지 무한정 기다려서, 새로운 입력이 들어오면 그 때 true 리턴. ctrl + z 키가 입력되면 입력 끝이므로 false 리턴 |

<br/>

추가 참고: [[JAVA] 자바_스캐너(Scanner)](https://mine-it-record.tistory.com/103)
