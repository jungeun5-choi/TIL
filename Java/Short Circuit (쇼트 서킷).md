### Boolean 계산의 Short Circuit (쇼트 서킷)

---

**🍤 And 논리 연산자의 쇼트 서킷**

- **case 1 :** `&&`
    
    ```java
    > j > 15 && i++ > 5
    > false
    
    > i
    i ==> 10
    
    > j
    j ==> 15
    ```
    
- **case 2 :** `&`
    
    ```java
    > j > 15 & i++ > 5
    > false
    
    > i
    i ==> 11
    
    > j
    j ==> 15
    ```

<br/>

→ **case 1의 경우,** `&&` 연산의 앞 부분이 `false` 이기에 뒷 부분의 연산은 수행되지 않는다
즉, `i++` 연산이 수행되지 않는다.

→ **case 2의 경우,** `&` 연산의 앞 부분이 `false` 이지만, 뒷 부분의 `i++` 연산이 수행되었다.

<br/>

```
📝 [쇼트 서킷]에서는 && 앞의 boolean 값이 false 일 때, && 뒤를 굳이 실행하지 않음으로써, 불필요한 연산을 생략한다.
```

<br/>

내용 참고: [[Java] 자바 쇼트 서킷 (short-circuit)[Java] 자바 쇼트 서킷 (short-circuit)](https://junior-datalist.tistory.com/214)