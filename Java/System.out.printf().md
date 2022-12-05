### **`System.out.printf()`**

* `System`: 자바 표준 입출력 클래스

---

- `System.out.printf()`의 괄호`()` 안에도 “매개변수”가 들어간다

```java
> System.out.printf("5*4=20")
5*4=20$11 ==> java.io.PrintStream@6d21714c
```

- 문자열을 정상적으로 출력하려면 `.println()`도 함께 작성해야한다
    
    ```java
    > System.out.printf("5*4=20").println()
    5*4=20
    ```
    
- `printf()`는 계산된 값을 출력할 수 있다
    
    ```java
    > System.out.printf("5*4=%d",5*4).println()
    5*4=20
    ```
    
    ```java
    > System.out.printf("%d*%d=%d", 5, 4, 5*4).println()
    5*4=20
    ```
    
    → 이렇게도 된다
    <br/><br/>
    
- 부동 소수점을 출력하려면…
    
    ```java
    > System.out.printf("%f+%f=%f", 1.1, 2.2, 1.1+2.2).println()
    1.100000+2.200000=3.300000
    ```
