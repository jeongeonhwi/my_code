import java.util.List;

public class Main {
  public static void main(String[] args) {
    int[] a = {5,6,7,8,9};
    int[] b = a;
    a[0] = 10;
    System.out.println(b[0]);
    int i = -1;
//    for (int aa : a) {
//      i++;
//      System.out.println(i);
//      System.out.println(aa);
//    }
  }
}