import java.util.*;
import java.io.*;
import java.lang.*;

public class checkin_5524 {
    static int N;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken());
        for (int i=0; i<N; i++) {
            inputline = br.readLine().trim();
            bw.write(inputline.toLowerCase()+"\n");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}
