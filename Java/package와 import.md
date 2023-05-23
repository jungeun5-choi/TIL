## package와 import
### 📌 `package` = 클래스의 일부분이면서 클래스를 식별해 주는 용도

`C++`, `C#`의 `namecase`와도 유사한 개념이라고 한다. 패키지를 선언할 때는 아래와 같은 형태로 사용한다.
```java
package {상위패키지}.{하위패키지};
```
```java
pacakge week2.day7;

public class Camp {
  public void running() {
    	System.out.println("Help!");
    }
}
```
선언한 `package`에 작성된 클래스를 해당 `package` 바깥에서 사용하려면, `import`가 필요하다.

<br><br>
### 📌 `import` = 다른 패키지에 있는 클래스를 사용하기 위해 사용

`C++`, `C#`의 `using`과도 유사한 개념이라고 한다. 패키지를 임포트 할 때는 아래와 같은 형태로 사용한다.

```java
import {상위패키지}.{하위패키지}.{클래스명};
import {상위패키지}.{하위패키지}.*;
```
```java
package week2.main;

import week2.day7.Camp;

public class Main {
  public static void main(String[] args) {
        Camp camp = new Camp();
        camp.running(); // "Help!" 출력
        
	}
}
```
`import` 할 때, 클래스명은 생략하고 `*`를 사용하여 표현하면, 패키지에 포함된 모든 클래스를 사용할 수 있다.