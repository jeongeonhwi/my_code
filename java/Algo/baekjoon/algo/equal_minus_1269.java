import java.io.*;
import java.lang.*;
import java.util.*;

public class equal_minus_1269 {
    static int N,M;
    static HashSet<Integer> left = new HashSet<>(), right = new HashSet<>();
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i = 0; i<N; i++) left.add(Integer.parseInt(st.nextToken()));

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i = 0; i<M; i++) {
            int d = Integer.parseInt(st.nextToken());
            if (left.contains(d)) {
                left.remove(d);
            } else right.add(d);
        }
        int ans = left.size() + right.size();
        bw.write(ans+"");
        bw.flush();
    }
}
