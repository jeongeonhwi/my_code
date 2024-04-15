import java.util.List;
class Person {
  private String name;
  public Person(String val) {
    name = val;
  }

  public static String get() {
    return name;
  }
  public void print() {
    System.out.println(name);
  }
}
public class Main {
  public static void main(String[] args) {
    Person obj = new Person("Kim");
    obj.print();
  }
}