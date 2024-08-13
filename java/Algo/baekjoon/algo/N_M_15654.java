import java.util.*;
import java.lang.*;
import java.io.*;

public class N_M_15654 {
    static int N,M, pi=0;
    static int[] arr, perlist, visited;
    static int[][] permutation;

    public static void permutationvoid (int si, int ei, int[] perlist) {
        if (si >= ei) {
            for (int j =0; j<M; j++) {
                permutation[pi][j] = perlist[j];
            }
            pi++;
        } else {
            for (int i=0; i<N; i++) {
                perlist[si] = arr[i];
                if (visited[i] == 0) {
                    visited[i] = 1;
                    permutationvoid(si+1, ei, perlist);
                    visited[i] = 0;
                }
            }
        }
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());
        int factorialN = 1;

        for (int i=N; i>(N-M); i--) {
            factorialN *= i;
        }

        perlist = new int[M]; visited = new int[N];
        permutation = new int[factorialN][M];
        arr = new int[N];
        inputline = br.readLine();
        st = new StringTokenizer(inputline);
        for (int i=0; i<(N); i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        permutationvoid(0,M,perlist);


        for (int i=0; i<pi; i++) {
            for (int j=0; j<M; j++) {
                pw.print(permutation[i][j]+" ");
            }
            pw.println(" ");
        }
        pw.flush();
    }
}
