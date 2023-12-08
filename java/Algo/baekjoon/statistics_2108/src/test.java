import java.io.*;
import java.util.*;

public class test {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // String filePath = "src/input.txt";
        // BufferedReader br = new BufferedReader(new FileReader(filePath));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] numbers = new int[N];
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int n = 0; n < N; n++) {
            numbers[n] = Integer.parseInt(br.readLine());
            countMap.put(numbers[n], countMap.getOrDefault(numbers[n], 0) + 1);
        }

        Arrays.sort(numbers);

        int sum = 0;
        int maxFrequency = 0;
        int maxFrequencyNumber = 0;
        List<Integer> maxFrequencyNumbers = new ArrayList<>();

        for (int n = 0; n < N; n++) {
            int num = numbers[n];
            sum += num;

            int frequency = countMap.get(num);

            if (maxFrequency < frequency) {
                maxFrequency = frequency;
                maxFrequencyNumber = num;
                maxFrequencyNumbers.clear();
                maxFrequencyNumbers.add(num);
            } else if (maxFrequency == frequency) {
                if (!maxFrequencyNumbers.contains(num)) {
                  maxFrequencyNumbers.add(num);
              }
            }
        }

        Collections.sort(maxFrequencyNumbers);
        


        int average = (int) Math.round((double) sum / N);
        int median = numbers[N / 2];
        int mode = (maxFrequencyNumbers.size() > 1) ? maxFrequencyNumbers.get(1) : maxFrequencyNumber;
        int range = numbers[N - 1] - numbers[0];

        bw.write(average + "\n");
        bw.write(median + "\n");
        bw.write(mode + "\n");
        bw.write(range + "\n");

        bw.flush();
        bw.close();
    }
}
