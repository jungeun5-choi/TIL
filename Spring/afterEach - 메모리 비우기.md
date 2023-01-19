### ▶️ 메모리 비우기 - `afterEach`

---

- 테스트는 실행순서를 보장하지 않는다.
    
    예를 들어, `member.setName();`을 사용하여 이름을 등록하면, DB에는 테스트가 끝나도 이름이 지워지지 않는다.
    
    즉, 다음 테스트에 영향을 끼칠 수도 있다. <br/><br/>
    

- 메모리를 비워주자
    
    ```java
    MemoryMemberRepository memberRepository = new MemoryMemberRepository();
    
    @AfterEach
    public void afterEach() {
        // 데이터 클리어
        memberRepository.clearStore();
    }
    ```