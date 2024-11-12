import java.io.*;
import java.lang.*;
import java.util.*;

public class String_set_14425 {
    static int N,M;
    static HashSet<String> arr = new HashSet<>();
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);

            String d = st.nextToken();

            arr.add(d);
        }
        int count_ans = 0;
        for (int i=0; i<M; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);

            String d = st.nextToken();

            if (arr.contains(d)) count_ans++;
        }
        bw.write(count_ans+"");
        bw.flush();
    }
}
