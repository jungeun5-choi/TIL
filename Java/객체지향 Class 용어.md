### 용어 - Class, Obj

---

- Class
- Objects/Instances    
    ```java
    /* 객체와 인스턴스 */
    public class Main {
    
      public static void main(String[] args) {
    
        Animal cat, dog; // 'object'
    
        // Instantiation 인스턴스화
        cat = new Animal(); // cat은 Animal Class의 'instance'(객체를 메모리에 할당)
        dog = new Animal(); // dog은 Animal Class의 'instance'(객체를 메모리에 할당)
      }
    }
    ```
    - [객체와 인스턴스 참고](https://gmlwjd9405.github.io/2018/09/17/class-object-instance.html)
    
- Member Data/State/Fields
- Actions/Methods/Behaviour
    
    ```java
    class Planet {
    
        name, location, distanceFromSun // *data/state/fields*
        revolve(), rotate() // *action/behaviour/methods*
    }
    ```