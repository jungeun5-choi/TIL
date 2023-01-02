### ▶️ [start.spring.io](https://start.spring.io/)

---

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/161294db-6322-461e-ab0e-b4f2ab37b157/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230102T145136Z&X-Amz-Expires=86400&X-Amz-Signature=72f0fce29d39a0728f8a7afe576df9f4e375d165aca59d138ec9bad6ebb74f85&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

**실습 시 설정값**

- **Project :** Gradle - Groovy
- **Language :** Java
- **Spring Boot :** 2.7.7
    - ⚠️ **주의! - 스프링 부트 3.0.x 선택 시 참고**
        1. **Java 17 이상**을 사용
        2. `javax` 패키지 이름을 `jakarta`로 변경해야함
        오라클과 자바 라이센스 문제로 모든 `javax` 패키지를 `jakarta`로 변경하기로 했습니다.
        3. **H2 데이터베이스를 2.1.214 버전 이상 사용**
    
    → 스프링 부트 3.0 관련 자세한 내용은 다음 링크를 확인해주세요: [https://bit.ly/springboot3](https://bit.ly/springboot3)
    
- **Project Metadata**
    - **Group :** hello
    - **Artifact :** hello-spring
    - **Packaging :** Jar
    - **Java :** 11
- **Dependencies**
    1. Spring Web
    2. Thymeleaf

- 실제 설정 화면 (22.12.28)
    
    ![123.PNG](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6527c6db-1db0-4fbe-bdd9-06bdd8d610ac/123.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230102T145114Z&X-Amz-Expires=86400&X-Amz-Signature=8fd8014c44ef3356bda430ba4af2775f4ecd3e24db13e2008a76ea4d01ccd859&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22123.PNG.png%22&x-id=GetObject)
    
<br/>

### IntelliJ 설정

IntelliJ에서 빌드할 때, Gradle 대신 Java 직접 실행하게 하는 방법

---

최근 IntelliJ 버전은 Gradle을 통해서 실행 하는 것이 기본 설정인데, 이렇게 하면 실행속도가 느리다.

다음과 같이 변경하면 Java를 바로 실행해서 실행속도가 더 빠르다.

- Setting → Build, Execution, Deployment → Build Tools → `Gradle`
    - `Build and run using`: Gradle → `IntelliJ IDEA`로 변경
    - `Run tests using`: Gradle → `IntelliJ IDEA`로 변경

- 참고
    
    ![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/238d7cff-eb52-4818-8ecd-9c98c5b1ff3a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230102T145533Z&X-Amz-Expires=86400&X-Amz-Signature=3a26336c04d5aac2ff39f17d355ce07ee8cc3fe9ecad4c5de2df33a9215fa609&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
