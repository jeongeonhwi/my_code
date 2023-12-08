import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws IOException {
    // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    String filePath = "src/input.txt";
    BufferedReader br = new BufferedReader(new FileReader(filePath));
    
    
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    int N = Integer.parseInt(br.readLine());

    int[] numbers = new int[N];
    for (int n=0; n<N; n++) {
        numbers[n] = Integer.parseInt(br.readLine());
    }
    Arrays.sort(numbers);

    Map<Integer, Integer> many = new HashMap<>();

    int max_v = 0;
    int max_k = 10000;
    int second = 10000;
    boolean check = true;

    for (int n=0; n<N; n++) {
        int target = numbers[n];
        long ncount = Arrays.stream(numbers).filter(element -> element == target).count();
        int inncount = (int) ncount;
        many.put(target, inncount);
        
        if (max_v <= inncount) {
            max_v = inncount;
            max_k = target;
        }
    }
    List<Integer> result = new ArrayList<>();
    for (int n=0; n<N; n++) {
        int target = numbers[n];
        long ncount = Arrays.stream(numbers).filter(element -> element == target).count();
        int inncount = (int) ncount;

        if (inncount != max_v) {
            continue;
        }
        // System.out.println(target);
        if (!result.contains(target)) {
            result.add(target);
        }
    }
    Collections.sort(result);
    int numbers_many = 0;
    

    if (many.size() == 2) {
        numbers_many = result.get(0);
    }
    else {
        // System.out.println("안녕");
        // System.out.println(result.get(2));
        numbers_many = result.get(1);
    }

    int numbers_length = numbers.length;
    int numbers_sum = Arrays.stream(numbers).sum();
    int numbers_center = numbers[numbers_length/2];
    int numbers_max = Arrays.stream(numbers).max().orElse(0);
    int numbers_min = Arrays.stream(numbers).min().orElse(0);
    
    if (numbers_sum/numbers_length < 0) {
        bw.write(Integer.toString(numbers_sum/numbers_length-1));
    }
    else {
        bw.write(Integer.toString(numbers_sum/numbers_length));
    }
    bw.write("\n");
    bw.write(Integer.toString(numbers_center));
    bw.write("\n");
    bw.write(Integer.toString(numbers_many));
    bw.write("\n");
    bw.write(Integer.toString(numbers_max-numbers_min));
    bw.flush();
    bw.close();
    
  }
}