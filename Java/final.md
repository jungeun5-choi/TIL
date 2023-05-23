## final
### 상수를 정의할 때
숫자를 코드에 때려박아야 할 때(?)가 종종 생기는데, 이럴 땐 여러가지를 고려해서 상수를 애용한다. 그런데 이상하게 `Java`에서는 상수 키워드가 빨리 익숙해지지 않아서 인터넷 서핑을 하는 일이 잦다. (`const`에 익숙하다보니...)

> `final`은 해당 `entity`가 오로지 한 번 할당될 수 있음을 의미한다.

`final` 키워드를 잊지 말자!

final int COST = 10000;
final String TAG = "MELON";
```

#### 왜 `static final`?
그런데 상수를 설명할 때 `static final` 키워드로 설명하는 예제가 많아서 관련하여 추가로 찾아보았다.

> 출처: [왜 자바에서 final 멤버 변수는 관례적으로 static을 붙일까?](https://djkeh.github.io/articles/Why-should-final-member-variables-be-conventionally-static-in-Java-kor/)

상수를 선언할 때 `final` 앞에 `static`을 붙여서 `static fianl`이라고 작성하는 것은 관례라고 한다. (아래부터 설명 추가)

<br><br>
### final의 정의는 '한 번만 초기화 가능하다' 이다. (≠ 상수)

실제로 '상수'를 정의할 때만 사용하는 것이 아니다. `final`은 변수 뿐만 아니라, 메서드나 클래스를 선언할 때도 사용된다.

#### final 메서드
주로 메서드 오버라이딩을 금지할 때 사용된다.
```java
class Example {
	final void sum() {}
}

class Test extends Example {
	void sum() {} // 컴파일 에러
}
```
#### final 클래스
`class` 앞에 `final` 키워드를 붙이면 더 이상 상속이 불가능하다는 것을 의미한다.
```java
final class Example {}
class Test extends Example {} // 컴파일 에러
```
#### 객체마다 다른 값을 갖게 된다?
아래의 코드에서 `final`로 선언된 변수인 `value`는 **생성자를 통해 초기화 된다.**
```java
public class Test {
	private final int value;
  
	public Test(int value) {
  		this.value = value;
	}
}
```
즉, 이 클래스의 객체들은 각기 다른 `value` 값을 갖게 되는 것이고, (객체 내에서는 값이 변하지 않지만) 클래스 레벨에서 통용되는 상수라고는 볼 수 없다.

<br><br>
### static
> `static`은 해당 데이터의 메모리 할당을 컴파일 시간에 할 것임을 의미한다.

그래서 `static` 데이터는 동적 데이터＊와는 기능과 역할이 구분된다. 동적 데이터와는 달리, `static` 데이터는 프로그램 실행 직후부터 끝날 때까지 메모리 수명이 유지된다.

*＊동적 데이터: 런타임 중에 필요할 때마다 동적으로 할당 및 해제되는 데이터.*

<br><br>
### 그래서 왜 static final이라고 써요?

보통 `final` 키워드를 쓰는 이유는, 해당 클래스를 사용할 때 변하지 않고 일관된 값으로 데이터를 사용하기 위함일 것이다.

그렇다면 위의 [`final`의 정의는 '한 번만 초기화 가능하다' 이다. (≠ 상수)](#final의-정의는-'한-번만-초기화-가능하다'-이다.-(≠-상수))의 예제인 [객체마다 다른 값을 갖게 된다?]의 케이스를 피하고 싶을 것이다. 

이를 피하기 위해서는 **인스턴스가 만들어질 때마다 새로 메모리를 잡아서 초기화 시키지 말고, 클래스 레벨에서 한 번만 잡아서 하나의 메모리 공간을 쭉 쓰도록 하면 된다.** 이 때 `static` 키워드를 사용하는 것이다.

```java
static final int COST = 10000;
static final String TAG = "MELON";
```

아마 이런 흐름으로 `static final`이 관례가 되었을지도 모른다 (추측)