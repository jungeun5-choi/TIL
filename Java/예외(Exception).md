## 예외(Exception)
### 오류와 예외 : Error & Exception
`오류(Error)`는 일반적으로 회복이 불가능한 문제를 일컫는다. 이는 시스템 레벨이나, 환경적인 이유로 발생하기 때문이다. `오류`가 발생한 경우, 어떠한 오류로 프로그램이 종료되었는지 확인하고 대응해야한다.

유사하지만 `예외(Exception)`는 일반적으로 회복이 가능한 문제를 말한다. 우리는 코드레벨에서 `예외처리`를 통해 문제상황에 대응해야한다.

### 예외처리 흐름
일반적인 예외처리의 흐름은 다음과 같다. 이는 `Checked Exception(확인된 예외)`을 다루는 것이다.

1. 발생 가능한 예외를 정의한다
2. 예외가 발생할 수 있음을 알린다
3. 사용자가 예외를 핸들링한다

#### (1) 예외 정의: exception class
아래와 같이 `예외 클래스`를 정의하는 것으로 사용자만의 예외를 정의할 수 있다.
```java
// Exception 클래스를 상속
class ExampleBadException extends Exception {

    public ExampleBadException() {
        	
        super("위험한 행동을 하면 예외처리를 꼭 해야합니다!");
    }
}
```
#### (2) 예외가 발생할 수 있음을 알리기: throws, throw
메서드를 선언 할 때, 이 메서드의 위험성을 미리 예측해야한다. 예측된 위험이 있다면, `throw` 키워드와 함께 이 메서드가 위험하다고 미리 알려야한다.
```java
class ExampleClass {

    private final Boolean just = true;
		
    // throws: 메서드가 어떤 예외사항을 던질 수 있는지 알림
    public void thisMethodIsDangerous() throws ExampleException {
    
        if (just) {
          // throw: 예외 객체를 던질 때 사용 (메서드 안에서 사용)
          throw new ExampleException();
        }
    }
}
```
    
|  | throws | vs | throw |
| :---: | --- | :---: | --- |
| 위치 | 메서드 이름 뒤 |  | 메서드 안 |
| 용도 | 이 메서드가 어떠한 예외사항을 던질 수 있음을 알림 | | 실제로 예외 객체를 던질 때 사용 |
| 예외 개수 | 여러 종류의 예외사항을 적을 수 있음 |  | 실제로 던지는 예외 객체 한 개와 같이 작성해야 함 |
| 특징 |  | | 일반 메서드의 `return` 키워드처럼 `throw` 아래의 구문들은 실행되지 않고, `throw` 문과 함께 메서드가 종료됨 |


#### (3) 예외 핸들링: try-catch
예외를 핸들링(handling)할 때는 일반적으로 `try-catch (finally)` 문을 사용한다. `try-catch (finally)` 문은 아래와 같은 형태로 사용한다.
```java
try {
    // try something...
    
} catch({exception}) {

    // catch exeption...

} finally {
    // finally do...
    // finally는 무조건 실행된다
}
```
`try` 블럭 내에서는 위험이 예측된 메서드를 실행시킨다. 예측된 위험이 실제로 발생하면, 예외(exception)가 발생한 것이다. 그러면 구문을 실행하던 위치에서 더 이상 다른 구문을 실행하지 않고 멈춘다.

멈춘 상태에서 끝나는 것이 아니라 `catch` 블럭으로 순서가 넘어간다. `catch` 블럭 내의 구문을 실행하는데, 이를 핸들링(handling)한다고 말한다.

무조건 실행해야하는 구문이 있다면 `finally` 블럭에 작성한다. `finally`는 예외 발생 여부와는 관계없이 블럭 내의 구문을 무조건 실행시키는 키워드이다.

예문은 아래와 같다.
```java
public class PracticeException {
    public static void main(String[] args) {
    
        ExampleClass exClass = new ExampleClass();

        try {
            // 1. 위험한 메서드 실행을 "시도" 해본다. (try)
            exClass.thisMethodIsDangerous();
            
        } catch (ExampleException e) {
           
            // 2. 예외가 발생하면, "잡아서" handling한다 (catch)
            // try 블럭 내의 구문을 실행하다가
            // 예외가 발생하면, (해당 위치에서) 코드 실행을 멈추고
            // catch 블럭의 구문이 실행된다.
            System.out.println(e.getMessage()); // 에러 메세지 출력
            
        } finally {
            // 3. 예외 발생 여부와는 관계 없이,
            // finally 블럭 내의 구문은 무조건 실행된다.
            // = 무조건 실행시킬 구문을 작성
            System.out.println("우리는 방금 예외를 handling 했습니다!");
        }

    }
}
```

### Throwable Class 구조
`Throwable` 클래스는 가장 상위에 있는 클래스인 `Object` 클래스의 자식 클래스로, `Object` 클래스를 상속한다.

`Throwable` 클래스의 자식 클래스로는 `Error(에러)`와 `Exception(예외)` 클래스가 있고, `Error` 클래스와 `Exception` 클래스도 구현체 클래스를 각각 자식으로 두고 있다.

![Throwable](https://velog.velcdn.com/images/temprmn/post/4bf18882-12d3-4981-8f42-e5913ed5954a/image.png)

[여기](https://programming.guide/java/list-of-java-exceptions.html)에서 더 많은 `Exception의 구현체 클래스`들을 확인할 수 있다.

모두 익힐 필요는 없고, 기능이 필요할 때마다 필요할 때마다 참고하여 적절하게 사용하자. 특정 에러(예외)를 구체화하고 싶다면 [위의 예시처럼](https://velog.io/@temprmn/Java-%EC%98%88%EC%99%B8Exception#%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC-%ED%9D%90%EB%A6%84) 직접 `정의`하고 `구현`하면 된다. 

### Chained Exception: 연결된 예외
예외는 또 다른 예외를 유발할 수 있다. 그래서 예외를 연결(chaining) 할 수 있는 것이다. 

`예외 연결`은 여러가지 예외를 하나의 큰 분류로 묶어서 다루기 위해 사용되기도 하고, `checked exception`을 `unchecked exception`으로 `wrapping`하는데 유용하게 사용되기도 한다.

#### {원인 예외}를 다루기 위한 메서드들
1) `initCause()` 메서드를 사용하면 특정 예외를 원인 예외로 등록할 수 있다.
```java
{예외 객체 변수}.initCause({원인 예외로 지정할 객체});
```
```java
e.initCause(new NullPointerException("원인 예외"));
```
2) `getCause()` 메서드는 지정된 원인 예외를 반환한다.
```java
{예외 객체 변수}.initCause();
```
```java
e.initCause();
e.initCause().printStackTrace(); // 원인 조회 후 출력
```

예제를 살펴보자. 전체적인 흐름은 [위의 예시](https://velog.io/@temprmn/Java-%EC%98%88%EC%99%B8Exception#%EC%98%88%EC%99%B8%EC%B2%98%EB%A6%AC-%ED%9D%90%EB%A6%84)와 유사하다.
```java
public class Main {

    public static void main(String[] args) {
        try {
            // 예외 생성
            NumberFormatException e = new NumberFormatException("가짜 예외 사유 입력");

            // 지정한 예외를 원인 예외로 등록
            e.initCause(new NullPointerException("진짜 예외 사유 입력"));

            // 예외를 직접 던진다.
            throw e;

        } catch (NumberFormatException e) {
            
            // 예외 로그 출력            
            e.printStackTrace();
            
            // 예외 원인 조회 후 출력
            e.getCause().printStackTrace();
        }

        // checked exception을 
        // unchecked exception으로 wrapping
        throw new RuntimeException(new Exception("이것이 진짜 예외 이유 입니다."));
    }
}
```
##### 출력 결과
```
Caused by: java.lang.NullPointerException: {진짜 예외 사유}
```

### 실제로 예외 처리하기: 예외를 처리하는 3가지 방법
예외를 처리하는 방법으로는 `예외 복구`, `예외 처리 회피`, `예외 전환`이 있다.

#### 1) 예외 복구
`try-catch`로 예외를 처리하여 정상 상태로 복구하는 방법으로, 가장 기본적인 방식이다. 하지만 실제로는 복구가 가능하지 않은 경우도 많아서 자주 사용되지는 않는다.

```java
public String getDataFromAnotherServer(String dataPath) {
	
    try {
    
        // 만약 여기서 오류가 발생했다면
        return anotherServerClient.getData(dataPath).toString();
        
    } catch (GetDataException e) {
    
        // defaultData (=기존 데이터)를 받아옴으로써
        // 프로그램을 정상 상태로 복구한다.
        return defaultData;
    }
}
```
#### 2) 예외 처리 회피
말 그대로 에러(예외) 처리를 회피하고, 호출한 쪽으로 예외 처리를 담당하라고 던져버리는 방법이다. 호출한 쪽에서 예외를 핸들링하는 것이 더 바람직하다는 확신이 있거나, 회피하는 것이 최선일 때만 사용해야한다.

아래의 예제처럼

```java
public void someMethod() throws Exception { ... }

public void someIrresponsibleMethod() throws Exception {

    // 위에 있는 someMethod()를 향해
    // 처리할 예외를 던져버린다
    this.someMethod();
}
```
*같은 객체(클래스) 내에서 이런 식으로 처리하지는 않으니, 예제는 참고용으로만 보자.*

#### 3) 예외 전환하기
위의 `예외 처리 회피`와 비슷하지만, 적절한 예외로 필터링해서 넘기는 방법이다. 적합한 의미를 가진 예외로 변경하여 던지는 것이라 볼 수 있다. 예외 처리에 더 신경을 쓰고 싶거나, 일괄적으로 처리하기 편한 예외로 바꿔서 던지고 싶은 경우 사용한다.

```java
public void someMethod() throws IOException { ... }


public void someResponsibleMethod() throws MoreSpecificException {
    try {        	
        this.someMethod();
        
    // 위 메서드에서 알려준 IOException 예외가 발생하면
    } catch (IOException e) {
    
        // 좀 더 상세한 exception으로 변경한다
        throw new MoreSpecificException(e.getMessage());
    }
}
```