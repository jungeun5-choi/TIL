## Queue
`Queue`는 `First-In-First-Out(선입선출)` 구조로, `Stack`과는 달리 제일 밑에 저장된 데이터부터 꺼내는 형태이다.
데이터를 추가하는 `add()`와 데이터를 조회하는 `peek()`, 데이터를 꺼내는 `poll()` 기능이 주를 이룬다.
`Queue`는 생성자가 없어서 바로 생성할 수 없고, `LinkedList`를 통하여 생성할 수 있다.



#### 1) 선언 및 생성
생성할 때 `Queue`가 아닌 `LinkedList`를 사용함에 주의할 것. `new Queue<{참조 자료형}>();`의 형태가 아니다.
```java
Queue<{참조 자료형}> {변수명} = new LinkedList<{참조 자료형}>();
```
```java
Queue<Intager> intQueue = new LinkedList<Integer>();
```

#### 2) 값 추가
```java
{변수명}.add({value});
```
```java
intQueue.add(1);
intQueue.add(2);
intQueue.add(3);
```

#### 3) 값 조회
제일 아래의 값 (= 현재 시점에서 첫번째가 되는 값)을 조회한다.
```java
{변수명}.peek();
```
```java
intQueue.peek(); // [결과: 1]
```

#### 4) 값 꺼내기
단순히 지우는 것뿐만 아니라, 현재 시점에서 첫번째가 되는 값을 반환한다.
```java
{변수명}.poll();
```
```java
intStack.poll(); // [결과: 1]
intStack.poll(); // [결과: 2]
```

#### 5) `Queue`가 비어있는지
비어있으면 `참(True)`을, 비어있지 않으면 `거짓(False)`을 반환한다.
```java
{변수명}.isEmpty();
```
```java
intQueue.isEmpty(); // [결과: False]
```

#### 6) `Queue`의 크기
`Queue`의 크기 = `Queue`에 저장된 데이터의 양(개수)이다.
```java
{변수명}.size();
```
```java
intQueue.size(); // [결과: 1]
```

## Stack vs Queue


| | Stack | vs | Queue |
| --- | --- | :---: | --- |
| 입출력 순서 | LIFO (후입선출) |  | FIFO (선입선출) | 
| 생성자 유무 | O |  | X (`LinkedList` 사용) |
| 데이터 추가 | `push()` |  | `add()` |
| 데이터 조회 | `peek()` |  | `peek()` | 
| 데이터 삭제 | `pop()` |  | `poll()` | 