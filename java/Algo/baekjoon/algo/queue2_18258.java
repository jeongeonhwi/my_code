import java.io.*;
import java.lang.*;
import java.util.*;


public class queue2_18258 {
    static ArrayDeque<Integer> arr = new ArrayDeque<>();
    public static void main (String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        int N = Integer.parseInt(st.nextToken());
        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);

            String s = st.nextToken();

            if (Objects.equals(s, "push")) {
                int n = Integer.parseInt(st.nextToken());
                arr.addLast(n);
            } else if (Objects.equals(s, "pop")) {
                if (!arr.isEmpty()) bw.write(arr.removeFirst() +"\n");
                else bw.write("-1\n");
            } else if (Objects.equals(s, "size")) bw.write(arr.size()+"\n");
            else if (Objects.equals(s, "empty")) {
                if (arr.isEmpty()) bw.write("1\n");
                else bw.write("0\n");
            } else if (Objects.equals(s, "front")) {
                if (arr.isEmpty()) bw.write("-1\n");
                else bw.write(arr.peekFirst()+"\n");
            } else if (Objects.equals(s, "back")) {
                if (arr.isEmpty()) bw.write("-1\n");
                else bw.write(arr.peekLast()+"\n");
            }
        }

        bw.flush();
    }
}
