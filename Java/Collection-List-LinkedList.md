### LinkedList
`LinkedList`는 메모리에 남는 공간을 요청해 실제 데이터를 나누어서 저장하고, 실제 데이터가 위치한 `주소 값`으로 List를 구성한다. 나누어서 저장하기 때문에 조회 속도가 `ArrayList`보다 느리다. 대신, **값을 추가하거나 삭제하는 속도가 빠르다.**

#### 1) 선언 및 생성
사이즈를 지정하지 않기 때문에 초기화를 하지 않아도 된다.
```java
LinkedList<{참조 자료형}> {변수명} = new LinkedList<{참조 자료형}>(); 
```
```java
LinkedList<Integer> linkedList = new LinkedList<Integer>();
```
#### 2) 값 추가
```java
{변수명}.add({value});
```
```java
linkedList.add(1);
linkedList.add(2);
linkedList.add(3);
```
값을 도중에 추가하는 경우는 다음과 같다. (아래 1-2-4의 `set`과 유사하게 생겼다.)
```java
{변수명}.add({index}, {value});
```
```java
// 2번 index에 7을 추가
linkedList.add(2, 7); 
```
#### 3) 값 호출
```java
{변수명}.get({index});
```
```java
// 0번 index의 값을 호출
linkedList.get(0); // [결과: 1]
// 1번 index의 값을 호출
linkedList.get(1); // [결과: 2]
// 2번 index의 값을 호출
linkedList.get(2); // [결과: 4]
// 3번 index의 값을 호출
linkedList.get(3); // [결과: 3]
```
#### 4) 값 수정
```java
{변수명}.set({index}, {value});
```
```java
// 1번 index의 값을 10으로 수정
linkedList.set(1, 10);
```
#### 5) 값 삭제
```java
{변수명}.remonve({index});
```
```java
// 1번 index의 값을 삭제
linkedList.remove(1); 
```
#### 6) 값 전체 삭제
```java
{변수명}.clear();
```
```java
linkedList.clear();
```
#### 7) 값 전체 출력
```java
{변수명}.toString();
```
```java
linkedList.toString();