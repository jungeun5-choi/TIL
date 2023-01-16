DI에는 **1) 필드 주입, 2) setter 주입, 3) 생성자 주입** … 3가지 방법이 있다.

의존관계가 실행중에 동적으로 변하는 경우는 거의 없으므로 **생성자 주입을 권장**한다. <br/><br/>

1. 필드 주입 (비권장)
    
    ```java
    @Controller
    public class MemberController {
    
        @Autowired private MemberService memberService;
    }
    ```
    
2. setter 주입
    
    ```java
    @Controller
    public class MemberController {
    
        private MemberService memberService;
    
        @Autowired
        public void setMemberService(MemberService memberService) {
            this.memberService = memberService;
        }
    }
    ```
    
3. 생성자 주입
    
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
    

<br/>─

실무에서는 주로 정형화된 컨트롤러, 서비스, 리포지토리 같은 코드는 **컴포넌트 스캔을 사용**한다.

그리고 정형화 되지 않거나, 상황에 따라 구현 클래스를 변경해야 하면 **설정을 통해 스프링 빈으로 등록**한다.<br/><br/>

### ⚠️ 주의

`@Autowired`를 통한 DI는 `helloController` , `memberService` 등과 같이 스프링이 관리하는 객체에서만 동작한다.

스프링 빈으로 등록하지 않고 내가 직접 생성한 객체에서는 동작하지 않는다.