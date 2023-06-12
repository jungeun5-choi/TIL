## 🐘 Gradle 

> `Gradle` = 빌드 자동화 시스템

- 우리가 작성한 `Java` 코드를 설정에 맞게 자동으로 `Build` 해준다.

- `Gradle`을 사용하면 간편하게 `Java` 소스 코드를 실행한 가능한 `jar` 파일로 만들어준다.


#### build.gradle

> `build.gradle` = `Gradle` 기반의 빌드 스크립트

- 이 스크립트를 작성하면 소스 코드를 빌드하고 `라이브러리들의 의존성을 쉽게 관리`할 수 있다.
  - 의존성을 자동으로 관리해 주기 때문에 라이브러리들간의 충돌 걱정 없이 개발에만 집중할 수 있다.

- `groovy` 혹은 `kotlin` 언어로 스크립트를 작성할 수 있다.

<br><br>

##### `dependencies`

(1) 필요한 외부 라이브러리들을 `dependencies`에 작성

→ (2) `Gradle`이 라이브러리들을 Maven Repository＊와 같은 외부 저장소에서 자동으로 다운로드<br><br>

＊[Maven Repository](https://mvnrepository.com/): 라이브러리들을 모아둔 저장소. 필요한 라이브러리가 있다면 검색해서 사용해보세요 (^^)

```groovy
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter'
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```