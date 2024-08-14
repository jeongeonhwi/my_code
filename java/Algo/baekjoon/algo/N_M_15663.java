import java.util.*;
import java.lang.*;
import java.io.*;

public class N_M_15663 {
    static int N, M, pi, factorial;
    static int[] number, perlist, visited;
    static int[][] pwlist;

    public static void permutation(int si, int ei, int[] perlist) {
        if (si >= ei) {
            if (M >= 0) System.arraycopy(perlist, 0, pwlist[pi], 0, M);
            pi++;
        } else {
            int before = 0;
            for (int i = 0; i < N; i++) {
                if (visited[i] == 0) {
                    if (before == number[i]) continue;
                    perlist[si] = number[i]; before = number[i];
                    visited[i] = 1;
                    permutation(si + 1, ei, perlist);
                    visited[i] = 0;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        pi = 0;
        factorial = 1;
        number = new int[N];
        perlist = new int[M];
        visited = new int[N];
        for (int i = N; i > (N - M); i--) factorial *= i;
        pwlist = new int[factorial][M];
        inputline = br.readLine();
        st = new StringTokenizer(inputline);
        for (int i = 0; i < N; i++) {
            number[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(number);
        permutation(0, M, perlist);

        for (int i = 0; i < pi; i++) {
            for (int j = 0; j < M; j++) {
                pw.print(pwlist[i][j] + " ");
            }
            pw.println("");
        }
        pw.flush();
    }
}
