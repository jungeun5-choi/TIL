### ArrayList
`ArrayList`는 **동적배열**로 데이터를 추가 및 삭제할 때 메모리를 재할당하기 때문에 **정적배열**인 `Array`와 달리 크기가 **가변적**이다. `Array`는 초기화시 할당받은 메모리를 재할당하지 않는다.

#### 1) 선언 및 생성
사이즈를 지정하지 않기 때문에 초기화를 하지 않아도 된다.
```java
ArrayList<{참조 자료형}> {변수명} = new ArrayList<{참조 자료형}>(); 
```
```java
ArrayList<Integer> intList = new ArrayList<Integer>(); 
```

#### 2) 값 추가
```java
{변수명}.add({value});
```
```java
intList.add(1);
intList.add(2);
intList.add(3);
```
#### 3) 값 호출
```java
{변수명}.get({index});
```
```java
// 0번 index의 값을 호출
intList.get(0); // [결과: 1]
// 1번 index의 값을 호출
intList.get(1); // [결과: 2]
// 2번 index의 값을 호출
intList.get(2); // [결과: 3]
```
#### 4) 값 수정
```java
{변수명}.set({index}, {value});
```
```java
// 1번 index의 값을 10으로 수정
intList.set(1, 10);
```
#### 5) 값 삭제
```java
{변수명}.remonve({index});
```
```java
// 1번 index의 값을 삭제
intList.remove(1); 
```
#### 6) 값 전체 삭제
```java
{변수명}.clear();
```
```java
intList.clear();
```
#### 7) 값 전체 출력
```java
{변수명}.toString();
```
```java
intList.toString();
```