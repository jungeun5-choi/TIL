### ▶️ 테스트는 이 틀을 기반으로… given, when, then (권장)

---

1. **`given`** : 기반 데이터 (무엇이 주어졌을 때) 
2. **`when`** : 검증 요건 (이런 것을 실행했을 때)
3. **`then`** : 검증 결과 (결과가 이렇게 나와야한다)

의 순서로 틀을 짜고 시작하면 테스트를 작성하기 편하다

당연히 테스트가 복잡해 질수록 구조는 이 형태에서 많이 벗어난다 <br/><br/>

- 예시
    
    ```java
    class MemberServiceTest {
    
        MemberService memberService = new MemberService();
    
        @Test
        void 회원가입() {
            // given (무엇이 주어졌을 때) - 기반 데이터
            Member member = new Member();
            member.setName("Hello");
    
            // when (이런 것을 실행했을 때) - 검증 요건
            Long saveId = memberService.join(member);
    
            // then (결과가 이렇게 나와야한다) - 결과
            Member findMember = memberService.findOne(saveId).get();
            Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());
        }
    }
    ```