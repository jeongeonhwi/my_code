import java.lang.*;
import java.util.*;
import java.io.*;

public class budget_2512 {
    static int N, M;

    static int calcul_budget(int mid) {
        int m = 0;
        for (int i =0; i<N; i++) {
            m += Math.min(arr[i], mid);
        }
        return m;
    }
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken()); arr = new int[N];

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        M = Integer.parseInt(st.nextToken());
        int ans = 0;
        int left = 0, right = arr[N-1];
        while (left<=right) {
            int mid = (left+right)/2;
            int budget = calcul_budget(mid);
            if (mid == arr[N-1]) {
                ans = mid; break;
            }
            else if (budget == M) {
                ans = mid; break;
            }
            else if (budget < M) {
                if (calcul_budget(mid+1) > M) {
                    ans = mid; break;
                }
                else {
                    left = mid+1;
                }
            }
            else right = mid -1;
        }

        bw.write(ans+"");

        bw.flush();
    }
}
