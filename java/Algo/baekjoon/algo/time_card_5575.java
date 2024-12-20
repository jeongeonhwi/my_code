import java.io.*;
import java.lang.*;
import java.util.*;

public class time_card_5575 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        int[] a = new int[6], b = new int[6], c = new int[6];
        for (int i=0; i<6; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i=0; i<6; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i=0; i<6; i++) {
            c[i] = Integer.parseInt(st.nextToken());
        }

        a[5] -= a[2]; a[4] -= a[1]; a[3] -= a[0];
        if (a[5] < 0) {
            a[5] += 60; a[4]--;
        }
        if (a[4] < 0) {
            a[4]+=60; a[3]--;
        }
        bw.write(a[3]+" "+a[4]+" "+a[5]+"\n");

        b[5] -= b[2]; b[4] -= b[1]; b[3] -= b[0];
        if (b[5] < 0) {
            b[5] += 60; b[4]--;
        }
        if (b[4] < 0) {
            b[4]+=60; b[3]--;
        }
        bw.write(b[3]+" "+b[4]+" "+b[5]+"\n");

        c[5] -= c[2]; c[4] -= c[1]; c[3] -= c[0];
        if (c[5] < 0) {
            c[5] += 60; c[4]--;
        }
        if (c[4] < 0) {
            c[4]+=60; c[3]--;
        }
        bw.write(c[3]+" "+c[4]+" "+c[5]+"\n");
        bw.flush();
        br.close(); bw.close();
    }
}
