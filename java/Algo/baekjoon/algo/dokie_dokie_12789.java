import java.io.*;
import java.lang.*;
import java.util.*;

public class dokie_dokie_12789 {
    static int N, now = 1;
    static ArrayDeque<Integer> arr = new ArrayDeque<>(), side = new ArrayDeque<>();
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken());

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i=0; i<N; i++) {
            int c = Integer.parseInt(st.nextToken());
            side.addLast(c);
        }

        boolean flag = true;

        for (int i=0; i<N; i++) {
            int a = side.removeFirst();
            if (now == a) now++;
            else if (!arr.isEmpty() && arr.peekLast() == now) {
                arr.removeLast(); now++;
                side.addFirst(a);
            }
            else {
                if (arr.isEmpty()) arr.add(a);
                else {
                    if (arr.peekLast() < a) {
                        flag = false;
                        break;
                    }
                    else arr.add(a);
                }
            }
        }
        if (flag) pw.println("Nice");
        else pw.println("Sad");
        pw.flush();
    }
}
