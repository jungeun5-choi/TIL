## MVC와 템플릿 엔진

### ▶️ MVC

- **MVC:** **M**odel, **V**iew, **C**ontroller

---

- **Model**:  의미있는 비즈니스 로직을 담당하는 계층
- **View**: 화면을 그리는 책임만을 담당하는 계층
- **Controller**: 클라이언트의 요청을 받아서 적절한 서비스계층을 호출하고, 그 결과를 반환하는 책임을 담당하는 계층

### ▶️ MVC 구조와 템플릿 엔진간의 연계 방식

---

1. 웹 브라우저(클라이언트)에서 컨텐츠 요청
    
    ex. localhost:8080/hello-mvc?name=catsbi
    
2. Request Path에 매핑되는 Controller 메서드 검색 후 호출
    
    ex.
    
    ```java
    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
      model.addAttribute("name", name);
      return "hello-template";
    }
    ```
    
3. 실행된 메서드는 작성된 로직 수행 후 **ViewResolver**에게 렌더링 될 View 파일 경로/이름 반환
4. 템플릿 엔진처리(ex: Thymeleaf)로 HTML 파싱된 소스파일을 클라이언트에게 반환
5. 웹 브라우저(클라이언트)는 해당 HTML 파일을 사용자에게 보여줌

<br/>

정리 도움 및 참고 → [Catsbi’s DLog](https://catsbi.oopy.io/b437f40b-c15c-45f1-adc1-113a826aa1c6)