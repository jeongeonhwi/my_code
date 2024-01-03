# java 알고리즘 정리
## 기본적으로 외워야 할 것들
### input
* 숫자 하나
```java
import java.util.Scanner

Scanner scanner = new Scanner(System.in);

int a = scanner.nextInt();

scanner.close();
```
* 숫자 하나 (빠르게 인풋 받음)
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        br.close();
    }
}
```
* 여러줄 인풋받기
    - br.readLine() 쓰면 한줄 입력받음
    - 내가 N값을 받았으면 포문을 돌려서 br.readLine()으로 받으면 됨
### sort
* 배열 정렬
```java
import java.util.Arrays;

public class ArraySortExample {
    public static void main(String[] args) {
        int[] array = {5, 2, 8, 1, 7};

        // 배열 정렬
        Arrays.sort(array);

        // 정렬된 배열 출력
        System.out.println(Arrays.toString(array));
    }
}
```
* 컬렉션 정렬
```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CollectionSortExample {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(5);
        list.add(2);
        list.add(8);
        list.add(1);
        list.add(7);

        // 컬렉션 정렬
        Collections.sort(list);

        // 컬렉션 내림차순 정렬
        Collections.sort(list, Comparator.reverseOrder());

        // 정렬된 컬렉션 출력
        System.out.println(list);
    }
}
```
* 컬렉션 접근은 대괄호가 아닌 .get으로 접근
* 컬렉션의 해당 인덱스 내용을 변경하고 싶으면 set(index, 변경하고 싶은 내용) 사용
