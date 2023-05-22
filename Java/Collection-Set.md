## Set
`Set`은 순서가 보장되지 않는 데이터의 집합으로, 데이터의 중복은 허용하지 않는다. 기본 `Set`으로 사용하기 보다는 `HashSet`이나 `TreeSet` 등으로 응용하여 사용하는 경우가 많다.

`Set`도 `Queue`처럼 생성자가 없기 때문에 다른 클래스를 통하여 생성할 수 있는데, `Set`의 경우는 `HashSet`을 사용한다.

#### 1) 선언 및 생성
생성할 때 `Set`이 아닌 `HashSet`을 사용함에 주의할 것. `new Set<{참조 자료형}>();`의 형태로 생성되지 않는다.
```java
Set<{참조 자료형}> {변수명} = new HashSet<{참조 자료형}>();
```
```java
Set<Integer> intSet = new HashSet<Integer>();
```

#### 2) 값 추가
중복된 값을 추가하려고 하는 경우에는, `size`가 추가되지 않고 기존 값에 덮어쓴다.
```java
{변수명}.add({value});
```
```java
intSet.add(1);
intSet.add(2);
intSet.add(3);
intSet.add(3); // 중복된 값은 덮어쓴다.
```

#### 3) 값 조회 (포함 확인)
순서가 보장되는 집합은 아니기 때문에, `.get(index)`를 통한 조회가 불가능하다. 대신 `contatins(value)`를 통해 해당 값이 **포함되어 있는지** 확인할 수 있다.

값이 포함되어 있으면 `참(True)`을, 포함되어 있지 않으면 `거짓(False)`를 반환한다.

```java
{변수명}.contains({value});
```
```java
intSet.contains(2); // [결과: True]
intSet.contains(4); // [결과: False]
```

#### 4) 값 삭제 
```java
{변수명}.remove({value});
```
```java
intSet.remove(3); // [1, 2]만 남음
```

<br><br>
### 다양한 종류의 `Set`
▫️ `HashSet`: 이 중에서 속도가 가장 빠르지만 순서가 보장되지 않는다.

▫️ `TreeSet`: 정렬된 순서대로 보관하며, 정렬방법은 사용자가 지정할 수 있다.

▫️ `LinkedHashSet`: 추가된 순서나 가장 최근에 접근한 순서대로 접근이 가능하다. (= 순서가 보장된다)

보통 `HashSet`을 사용하지만, 순서를 보장해야한다면 대안으로 `LinkedHashSet`을 사용한다.