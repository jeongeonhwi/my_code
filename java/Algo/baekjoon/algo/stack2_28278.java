import java.io.*;
import java.lang.*;
import java.util.*;

public class stack2_28278 {
    static int N;
    static ArrayDeque<Integer> stack = new ArrayDeque<>();

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken());
        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            int a = Integer.parseInt(st.nextToken());
            if (a == 1) {
                int b = Integer.parseInt(st.nextToken());
                stack.add(b);
            } else if (a == 2) {
                if (stack.isEmpty()) {
                    pw.println("-1");
                } else {
                    pw.println(stack.removeLast());
                }
            } else if (a == 3) {
                pw.println(stack.size());
            } else if (a == 4) {
                if (stack.isEmpty()) {
                    pw.println("1");
                } else {
                    pw.println("0");
                }
            } else if (a == 5) {
                if (stack.isEmpty()) {
                    pw.println("-1");
                } else {
                    pw.println(stack.peekLast());
                }
            }
        }

        pw.flush();
    }

}
