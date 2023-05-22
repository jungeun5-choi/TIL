## Map

`Map`은 `key-value`의 구조로 구성되어, `key` 값을 기준으로 `value`를 저장하고 조회할 수 있도록 한다. 그렇기 때문에 `value`의 중복은 허용할지라도 `key`의 중복은 허용하지 않는다.

일반 `Map`으로도 사용할 수 있지만, `HashMap`, `TreeMap` 등으로 응용하여 사용하기도 한다.


#### 1) 선언 및 생성
```java
Map<{key 자료형}, {value 자료형}> {변수명} = new HashMap<>();
```
```java
Map<String, Integer> intMap = new HashMap<>();
```

#### 2) 값 추가
`key` 값이 중복되는 것은 허용하지 않으므로, `key`를 중복된 값으로 추가하려는 경우에는 가장 최근의 `key` 값으로 덮어쓴다.
```java
{변수명}.put({key}, {value});
```
```java
intMap.put("일", 11);
intMap.put("이", 12);
intMap.put("삼", 13);
intMap.put("삼", 14); // 중복 Key값은 덮어쓴다.
intMap.put("삼", 15); // 중복 Key값은 덮어슨다.
```
#### 3) 값 조회
전달한 `key` 값으로 `value`를 조회한다.
```java
{변수명}.get({key});
```
```java
intMap.get("일"); // value = 11
intMap.get("이"); // value = 12
intMap.get("삼"); // value = 15
```

#### 4) 전체 `key` 조회
```java
{변수명}.keySet();
```
```java
intMap.keySet(); // "일", "이", "삼"
```
#### 5) 전체 `value` 조회
```java
{변수명}.values();
```
```java
intMap.values(); // 11, 12, 15
```

#### 6) 값 삭제
```java
{변수명}.remove({key});
```
```java
intMap.remove("일");
// 남은 데이터: {"이", 12}, {"삼", 15}
```

<br><br>

### 다양한 종류의 `Map`
▫️ `HashMap`: 중복을 허용하지 않고, 순서도 보장하지 않는다. `key`와 `value`로 `null`을 지정하는 것이 허용된다.

▫️ `TreeMap`: `key` 값을 기준으로 정렬이 가능하다. 저장할 때 오름차순 정렬을 하기 때문에 값을 저장(추가)할 때 시간이 상대적으로 오래 걸리는 편.