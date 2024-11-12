import java.io.*;
import java.lang.*;
import java.util.*;

public class deque2_28279 {
    static int N;
    static ArrayDeque<Integer> arr = new ArrayDeque<>();
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);

            int a = Integer.parseInt(st.nextToken());

            if (a == 1) {
                int b = Integer.parseInt(st.nextToken());
                arr.addFirst(b);
            }
            else if (a == 2) {
                int b = Integer.parseInt(st.nextToken());
                arr.addLast(b);
            }
            else if (a == 3) {
                if (arr.isEmpty()) bw.write("-1\n");
                else bw.write(arr.removeFirst()+"\n");
            }
            else if (a == 4) {
                if (arr.isEmpty()) bw.write("-1\n");
                else bw.write(arr.removeLast()+"\n");
            }
            else if (a == 5) {
                bw.write(arr.size()+"\n");
            }
            else if (a == 6) {
                if (arr.isEmpty()) bw.write("1\n");
                else bw.write("0\n");
            }
            else if (a == 7) {
                if (arr.isEmpty()) bw.write("-1\n");
                else bw.write(arr.peekFirst()+"\n");
            }
            else if (a == 8) {
                if (arr.isEmpty()) bw.write("-1\n");
                else bw.write(arr.peekLast()+"\n");
            }
        }
    }
}
