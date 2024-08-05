import java.util.*;

public class Main{
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int N = scanner.nextInt();

    List<Integer> result = new ArrayList<>();

    for (int i = 0; i <= N; i++) {
      int si = i;
      int tmp = i;
      while (si > 0) {
        tmp += si%10;
        si /= 10;
      }
      if (tmp == N) {
        result.add(i);
      }
    }
    if (result.isEmpty()) {
      System.out.println(0);
    } else {
      System.out.println(result.get(0));
    }
    scanner.close();
  }
}