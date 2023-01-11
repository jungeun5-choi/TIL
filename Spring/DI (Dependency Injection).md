### DI (Dependency Injection) - 의존성 주입, 의존관계 주입

서비스와 서비스 테스트가 repository 인스턴스를 같이 사용하게 하려면…?

---

📌**참조** [의존관계 주입](https://tecoble.techcourse.co.kr/post/2021-04-27-dependency-injection/)

기존에는 회원 서비스와 서비스 테스트가 `MemoryMemberRepository`를 각자 직접 생성했다.

```java
public class MemberService {

  private final MemberRepository memberRepository = new MemoryMemberRepository();
}
```

```java
class MemberServiceTest {

  MemberService memberService = new MemberSerivce();
  MemoryMemberRepository memberRepository = new MemeoryMemberRepository();
}
```

하지만 이렇게 하면, 서비스와 서비스 테스트가 서로 다른 DB가 되는 문제가 생긴다.

해결하기 위해 (같은 Repository를 사용하게 하기 위해) 리포지토리의 코드가 서비스를 DI 가능하게 변경한다.

```java
public class MemberService {

  private final MemberRepository memberRepository;

    // 생성자를 사용한다
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
}
```

```java
class MemberServiceTest {

  MemberService memberService;
  MemoryMemberRepository memberRepository;

  @BeforeEach
  public void beforeEach() {
  
    // 서비스를 생성할 때 명시적으로 리포지토리를 전달한다
    memberRepository = new MemoryMemberRepository();
    memberService = new MemberService(memberRepository);
  }

}
```

이렇게 하면 서비스와 서비스 테스트는 같은 리포지토리를 사용할 수 있다.

<br/>

### 자동 의존관계 설정

---

생성된 Member Controller가 회원 서비스를 통해서 회원가입과 회원정보열람을 할 수 있도록 해야한다.

→ Member Controller가 회원 서비스를 의존하게 하도록 하자.

<br/>

Member Controller에 의존관계를 추가

```java
@Controller
public class MemberController {

  private final MemberService memberService;

  @Autowired
  public MemberController(MemberService memberService) {
    this.memberService = memberService;
  }
}
```

💡 `**@Autowired**` : 스프링이 (스프링 컨테이너와) 연관된 객체를 찾아서 스프링 컨테이너에 넣어준다.

[테스트](https://github.com/jungeun5-choi/TIL/blob/main/Spring/DI%20(Dependency%20Injection).md#di-dependency-injection---%EC%9D%98%EC%A1%B4%EC%84%B1-%EC%A3%BC%EC%9E%85-%EC%9D%98%EC%A1%B4%EA%B4%80%EA%B3%84-%EC%A3%BC%EC%9E%85)에서는 개발자가 명시적으로 의존성을 주입했고, 여기서는 `@Autowired`에 의해 스프링이 의존성을 주입했다.

<br/>

```
⚠️ 회원 서비스와 리포지토리를 스프링 빈으로 등록해주어야한다.
```

그렇지 않으면 오류가 발생한다…

<br/>

- 회원 서비스 (Member Service) : `@Service` 사용
    
    ```java
    @Service
    public class MemberService {
    
      @Autowired
      public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
      }
    }
    ```
    
    생성자에 `@Autowired`를 사용하면 객체 생성 시점에 스프링 컨테이너에서 해당 스프링 빈을 찾아서 주입한다.
    
    생성자가 1개만 있으면 `@Autowired`를 생략할 수 있다.
    
<br/>
    
- 회원 리포지토리 (Member Repository) : `@Repository` 사용
    
    ```java
    @Repository
    public class MemoryMemberRepository implements MemberRepository { ... }
    ```

<br/>

- 컨트롤러 (Controller)의 경우에는 `@Controller`를 사용하여 스프링 빈에 등록한다.

<br/>

- 위의 세가지 모두는 구분하지 않고 `@Component`를 사용하여 등록할 수 있다.
    - `@Controller`, `@Service`, `@Repository`는 `@Component`를 포함하고 있기 때문이다…

<br/>

**스프링 빈 등록 이미지**

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3253dea9-ef2e-4081-a961-643ddd524db8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230111T025046Z&X-Amz-Expires=86400&X-Amz-Signature=cb09d435cf7eb437f0dc059154da058f7fba91d5fb76c7e6eee96a92861595b7&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

- Controller는 Service를 의존하고, Serivce는 Repository를 의존하는 형태로 등록되어 있다.


<br/>

스프링은 스프링 컨테이너에 스프링 빈을 등록할 때, 기본으로 싱글톤으로 등록한다 (= 유일하게 하나만 등록해서 공유한다)

따라서, 같은 스프링 빈이면 모두 같은 인스턴스다.

설정으로 싱글톤이 아니게 설정할 수 있지만, 특별한 경우를 제외하면 대부분 싱글톤을 사용한다.
