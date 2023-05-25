## Generic
### `제네릭`을 사용하는 이유
#### 1. 중복되거나 필요없는 코드를 줄여준다.
	
예를 들어서, 숫자를 받아 덧셈하는 클래스를 만든다고 생각해보자. 하지만 숫자는 다양한 데이터 타입이 있기 때문에, 아래처럼 그 데이터 타입에 맞는 클래스를 따로 생성해주어야 한다.

```java
public class IntAdd {

	public int operate(int first, int second) {

		return first + second;
	}
}
```
```java
public class DoubleAdd {

	public double operate(double first, double second) {

		return first + second;
	}
}
```
이러면 타입만 다를 뿐, 하는 일도 같고, 형태가 같은 메서드가 반복된다. 이 때 `Generic`을 사용하면 무의미한 중복을 방지할 수 있다.
    
```java
public class NumberAdd<T> {

	public T operate(T first, T second) {

		return (T)first + (T)second;
	}
}
```

#### 2. 타입 안정성을 해치지 않는다.
모든 객체(클래스)는 `Obejct` 클래스를 상속받는다. 그러므로 `Object`를 타입으로 사용하면 그 어떤 타입이라도 받을 수 있다는 장점이 있다.

```java
public class ObjectExample {
    	
	public Object operate(Object first, Object second) {
        
		return first + second;
	}
}
```
하지만 이런 경우는 타입 안정성을 침해받게 된다. 위의 `(first + second)`를 연산한 값을 무사히 반환할 수 있을까? 한다면 어떤 타입으로 형변환을 해야할까? 내부에서 강제 형변환을 하드코딩 했는데 실제로 들어온 값의 타입이 다르다면?

### 제네릭 타입
| 타입 | 설명 |
| :---: | :---: |
| `<T>` | Type |
| `<E>` | Element |
| `<K>` | Key |
| `<V>` | Value |
| `<N>` | Number |

예를 들면 `HashMap<{Key}, {Value}>` 같은 경우는, 제네릭을 적용하면 `HashMap<K, V>`라고 작성할 수 있다.
```java
/* 일반적인 해시맵 */
HashMap<String, int> hash = new HashMap<String, int>();
```
```java
/* 제네릭을 적용한 해시맵 */
HashMap<K, V> hash = new HashMap<K, V>();
```

### 와일드 카드
와일드 카드를 사용하면 제네릭에 제한을 구체적으로 설정할 수 있다. `한정적 타입 매개변수` 라고도 한다.

- `<? extends T>` : `T`와 그의 자손들만 사용 가능. 상한 제한이라고 한다. `<T extends Class>` 형태로도 사용가능 하다.

- `<? super T>` : `T`와 그 조상들만 사용 가능. 하한 제한이라고 한다. 마찬가지로 `<T super Class>` 형태로도 사용가능 하다.

- `<?>` : 제한 없음. 모든 타입이 가능하다. (`<? extends Object>`와 동일)

### 제네릭 메서드 
메서드 선언부에 제네릭 타입이 선언된 메서드를 제네릭 메서드라고 한다. 제네릭 타입의 선언 위치는 반환 타입 바로 앞이다.

```java
static <T> void sort(List<T> list, Comparator<? super T> c) { ... }
```

메서드에 선언된 제네릭 타입은 로컬 변수를 선언한 것과 같다고 생각하면 이해하기 쉽다. 이 타입 매개변수는 메서드 내에서만 지역적으로 사용될 것이므로 메서드가 `static`이건 말건 상관이 없다. (그래서 `static 메서드`에서도 제네릭을 사용할 수 있다)

같은 이름의 변수를 사용했다고 해도 제네릭 메서드의 타입변수는 제네릭 클래스의 타입변수와 다르다.
```java
public class Generic<T, U, E> {
	
    // Generic<T,U,E>의 `T`와 아래 메서드의 `T`는
    // 이름만 같을뿐 다른 변수이다.
    static <T> void sort(List<T> list, Comparator<? super T> c) { ... }
}
```


### 제네릭을 사용할 수 없는 경우
#### 제네릭으로 배열을 생성할 수 없다.
`new` 연산자는 `heap` 영역에 충분히 공간이 있는지 확인 후, 메모리를 확보한다. 공간이 있는지 확인하려면 타입을 알아야하는데, 컴파일 시점에 타입 `T`가 무엇인지 알 수 없기 때문이다.

#### static 변수에도 제네릭을 사용할 수 없다.
`static` 변수는 인스턴스에 종속되지 않는 클래스 변수로, 모든 인스턴스가 공통된 저장공간을 공유한다. 공공적으로 사용되는 변수가, 생성되는 인스턴스에 따라 타입이 바뀐다는 개념 자체가 모순이기 때문이다. 하지만 `static` 메서드에서는 제네릭을 사용할 수 있다.

