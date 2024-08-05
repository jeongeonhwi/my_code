import java.util.*;
import java.lang.*;
import java.io.*;

public class plus_1712 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedReader br = new BufferedReader(new FileReader("input.txt")); // 파일 경로 지정
        PrintWriter pw = new PrintWriter(System.out);

        int n = 3;
        long[] numbers = new long[n];

        String inputLine = br.readLine();
        StringTokenizer st = new StringTokenizer(inputLine);

        for (int i = 0; i<n; i++) {
            numbers[i] = Long.parseLong(st.nextToken());
        }
        if (numbers[1] >= numbers[2]) {
            pw.println("-1");
        } else {
            int wi = 1;
            while (numbers[0]+numbers[1]*wi >= wi*numbers[2]) {
                wi++;
            pw.println(wi);
            }
        }

        pw.flush();
        br.close();
    }
}
