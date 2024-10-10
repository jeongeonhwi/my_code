import java.io.*;
import java.lang.*;
import java.util.*;

public class dokie_dokie_12789 {
    static int N;
    static ArrayDeque<Integer> arr = new ArrayDeque<>();
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken());

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i=0; i<N; i++) {
            int a = Integer.parseInt(st.nextToken());
            arr.add(a);
        }
    }
}
