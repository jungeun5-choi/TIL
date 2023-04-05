## Java는 언제나 Call By Value

📌 [https://reinvestment.tistory.com/68](https://reinvestment.tistory.com/68)

…

Java는 기본적으로 `call-by-value` 방식을 지원한다. 그런데 왜 원본의 값이 변할까?

`Java는 인자를 넘겨줄 때, 해당 객체의 주소값의 복사값을 넘겨주기 때문`이다.


<br><br>
_<br>

📌 [https://loosie.tistory.com/486](https://loosie.tistory.com/486)

…

Java 또한 참조 객체를 다른 객체에게 주소값을 전달하여 값을 변경할 수 있는 구조를 가지고 있다. 이러한 동작 때문에 **Call By Reference로 착각할 수 있지만,** 이는 `같은 주소값을 가지고 있는 보조객체가 주소값을 통해 접근하여, 주소값이 가리키는 내용을 변경시키는 것이기 때문에 Call By Value`이다.

```java
import java.util.Arrays;

public class CallByEx {

	public static void main(String[] args) {
		
		int[] src = {1,2,3};

		foo(src);
		System.out.println(Arrays.toString(src));

		boo(src);
		System.out.println(Arrays.toString(src));
	}

	static void foo(int[] arr) {

		arr = new int[]{3,4,5};
		arr[0] = 9;
	}

	static void boo(int[] arr) {
		arr[0] = 2; // 주소값이 가리키는 변수를 바꾼 것
	}

}
```

다음과 같이 원래 `[1,2,3]`의 값을 지는 배열 원소가 `boo(int[] arr)`의 보조객체인 `arr`을 통해 값이 변경되는 것을 볼 수 있다.

```java
[1,2,3]
[2,2,3]
```

### `foo(int[] arr);`

새로운 배열을 생성하여 값을 변경하면 **원본 객체(`src`)에게는 전혀 영향이 가지 않는다.**

### `boo(int[] arr);`

Java의 참조타입 객체는 주소값을 가지고 있다. 때문에, **①보조객체(`arr`)가 주소값을 통해 주소값이 가리키고 있는 값을 변경하면** → **②같은 주소값을 가리키고 있는 원본 객체(`src`)의 값도 변경**이 되는 것이다.