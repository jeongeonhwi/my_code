import java.io.*;
import java.lang.*;
import java.util.*;

public class plus123_9095 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        int T = Integer.parseInt(st.nextToken());
        int[] dp = new int[11];
        dp[1] = 1; dp[2] = 2; dp[3] = 4;
        for (int i=4; i<11; i++) {
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3];
        }
        for (int t=0; t<T; t++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            int number = Integer.parseInt(st.nextToken());
            int ans = dp[number];
            System.out.println(ans);
        }
    }
}
