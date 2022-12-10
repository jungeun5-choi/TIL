### 이클립스에서 첫 프로젝트 : 구구단 출력하기

---

- **MultiplicationTable.java**
    
    ```java
    package com.in28minutes.firstjavaproject;
    
    public class MultiplicationTable {
    
    	public void print() {
    		for(int i = 1; i <= 10; i++) {
    			System.out.printf("%d * %d = %d", 5, i, 5 * i).println();
    		}
    	}
    }
    ```
    
- **MultiplicationTableRunner.java**
    
    ```java
    package com.in28minutes.firstjavaproject;
    
    public class MultiplicationTableRunner {
    
    	public static void main(String[] args) {
    		MultiplicationTable table = new MultiplicationTable();
    		table.print();
    	}
    
    }
    ```

<br/>

- **실행 결과**
    
    ![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cd6ed717-f2ef-4ffc-b578-1133503726cf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221210T145516Z&X-Amz-Expires=86400&X-Amz-Signature=78142dc0838a72a0916bd58173b8299abcbd46db24bd6780aa927c3f887dff20&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)