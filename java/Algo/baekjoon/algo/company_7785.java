import java.io.*;
import java.lang.*;
import java.util.*;

public class company_7785 {
    static int N;
    static HashSet<String> hs = new HashSet<>();
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken());

        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);

            String name = st.nextToken();
            String now = st.nextToken();

            if (Objects.equals(now, "enter")) {
                hs.add(name);
            } else {
                hs.remove(name);
            }
        }

        String[] arr = new String[hs.size()];
        int ii = 0;
        for (String s : hs) {
            arr[ii] = s;
            ii++;
        }
        Arrays.sort(arr);
        for (int i = hs.size()-1; i>=0; i--) {
            bw.write(arr[i]+"\n");
        }
        bw.flush();
    }
}
