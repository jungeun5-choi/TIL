### Method/함수

---

- 문법
    
    ```java
    (Return Type) nameOfTheMethod(Type argumentName) {
    	// Body of the method
    }
    ```
    
    ```java
    > void sayHelloWorld() {
    >     System.out.println("Hello World");
    > }
    |  created method sayHelloWorld()
    
    > void sayNumberOne(int num) {
    >     System.out.printf("%d", num).println();
    > }
    |  created method sayNumberOne()
    ```
    
    - 이름 생성 규칙은 변수와 동일하다 <br/><br/>


- **📝 연습문제**
    
    **Quiz 1.** 함수를 만들고 그 함수에서 `1`부터 매개변수 `n`까지의 숫자를 출력하라
    
    ```java
    > void printNumbers(int n) {
    >     for(int i = 1; i <= n; i++) {
    >         System.out.println(i);
    >     }
    > }
    |  created method printNumbers(int)
    
    > printNumbers(5)
    1
    2
    3
    4
    5
    ```
    
    **Quiz 2.** 함수를 만들고 그 함수에서 1부터 매개변수 `n`까지의 각 숫자의 제곱을 출력하라
    
    ```java
    > void printSquares(int m) {
    >     for(int i = 1; i <= m; i++) {
    >         System.out.printf("%d", i*i).println();
    >     }
    > }
    |  created method printSquares(int)
    
    > printNumbers(5)
    1
    4
    9
    16
    25
    ```
    

### Method 오버로딩

---

- 오버로딩 예제

```java
> void sayNumberOne() {
>     System.out.print.println(1);
> }

> void sayNumberOne(int num) {
>     System.out.printf("%d with overloading", num).println();
> }
```

```java
> sayNumberOne(1)
1 with overloading

> sayNumberOne()
1
```

### Method `return` (반환)

---

- `return` 예제

```java
> int sum (int first, int second) {
>     int temp = first+second;
>     return temp;
> }
|  created method sum(int,int)
```

```java
> sum(1, 3)
$6 ==> 4

> int add = sum(1,3)
add ==> 4
```
<br/>

- **📝 연습문제**
    
    **Quiz 1.** 세 수의 합을 계산하여 `return`하는 method를 만들어라
    
    ```java
    > int thrice (int first, int second, int third) {
    >     int sum = first + second + third;
    >     return sum;
    > }
    |  created method thrice(int,int,int)
    
    > int i = thrice(1,3,5)
    i ==> 9
    ```
    
    **Quiz 2.** 삼각형의 두 각의 값이 주어졌을 때, 나머지 한 개의 각의 값을 `return`하는 method를 작성하라
    
    ```java
    > int triangles (int one, int two) {
    >     int other = 180 - (one + two);
    >     return other;
    > }
    |  created method triangles(int,int)
    
    > int t = triangles(90, 30);
    t ==> 60
    ```
