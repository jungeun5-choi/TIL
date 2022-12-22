### BigDecimal

---

소수점을 저장할 수 있는 가장 크기가 큰 자료형인 `double`은, 소수점의 정밀도에 한계가 있어 값이 유실될 수 있다.

**BigDecimal**은 Java에서 숫자를 정밀하게 저장하고 표현할 수 있는 유일한 방법이다.

<br/>

- **발단:** double 값 연산의 문제점
    
    ```java
    > 34.56789876 + 34.2234
    > 68.79129875999999
    ```
    
    → 결과값 뒤에 999999가 생겼다 = 값이 유실되었다
    

<br/>

- **BigDecimal을 사용해보자**
    
    ```java
    > BigDecimal number1 = new BigDecimal("34.56789876");
    number1 ==> 34.56789876
    
    > BigDecimal number2 = new BigDecimal("34.2234");
    number2 ==> 34.2234
    ```
    
    ```java
    > number1.add(number2);
    > 68.79129876
    
    > BigDecimal number3 = number1.add(number2);
    number3 ==> 68.79129876
    ```


<br/>

**📝 BigDecimal의 멤버함수들** (jshell에서 `(decimal 변수명)` + `.` + `Tab 키`를 눌러 확인할 수 있다)

```
abs(                     add(                     byteValue()              byteValueExact()
compareTo(               divide(                  divideAndRemainder(      divideToIntegralValue(
doubleValue()            equals(                  floatValue()             getClass()
hashCode()               intValue()               intValueExact()          longValue()
longValueExact()         max(                     min(                     movePointLeft(
movePointRight(          multiply(                negate(                  notify()
notifyAll()              plus(                    pow(                     precision()
remainder(               round(                   scale()                  scaleByPowerOfTen(
setScale(                shortValue()             shortValueExact()        signum()
sqrt(                    stripTrailingZeros()     subtract(                toBigInteger()
toBigIntegerExact()      toEngineeringString()    toPlainString()          toString()
ulp()                    unscaledValue()          wait(
```

**📝 이클립스 IDE에서 사용하려면 import 필요 ↓**

```java
import java.math.BigDecimal;
```

내용 일부 참고: [Java, BigDecimal 사용법 정리](https://jsonobject.tistory.com/466)

<br/>

### BigDecimal로 Integer형 계산하기

---

```java
> BigDecimal number = new BigDecimal("11.5");
number ==> 11.5

> int i =5;
i ==> 5
```

⚠️ double형인 `number`와 int형인 `i`를 계산하려면 `i`로 새로운 `BigDecimal`를 만들어야한다 ↓

```java
> number.add(new BigDecimal(i));
> 16.5

> number.multiply(new BigDecimal(i));
> 57.5

> number.divide(new BigDecimal(100));  // 일반 정수도 가능하다
> 0.115
```

<br/>

### BigDecimal로 단리 계산

---

- **SimpleInterestCalculatorRunner.java**

```java
public class SimpleInterestCalculatorRunner {

  public static void main(String[] args) {

  SimpleInterestCalculator calculator = new SimpleInterestCalculator("4500.00", "7.5");
  // 4500달러를 7.5퍼센트 이율로 대출

  BigDecimal totalValue = calculator.cacluateTotalValue(5);
  // 5년동안

  System.out.println(totalValue);
  }
}
```

- **SimpleInterestCalculator.java**

```java
public class SimpleInterestCalculator {

  BigDecimal principal;
  BigDecimal interest;

  public SimpleInterestCalculator(String principal, String interest) {
    this.principal = new BigDecimal(principal);
    this.interest = new BigDecimal(interest).divide(new BigDecimal(100));
  }

  public BigDecimal cacluateTotalValue(int noOfYears) {

    // TotalValue = principal + principal * interest * noOfYears;

    BigDecimal noOfYearsBigDecimal = new BigDecimal(noOfYears);

    BigDecimal totalValue = principal.add(
                                        principal.multiply(interest)
                                        .multiply(noOfYearsBigDecimal)
                                        );

    return totalValue;
  }
}
```