import java.lang.*;
import java.io.*;
import java.util.*;

public class two_liquid_2470 {
    static int N;
    static int[] arr;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken()); arr = new int[N];

        inputline = br.readLine();
        st = new StringTokenizer(inputline);

        for (int i=0; i<N; i++) arr[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(arr);

        int left = 0, right = N-1; int min_v = Math.abs(arr[left]+arr[right]); int l=arr[left], r=arr[right];

        while (left < right) {
            if (Math.abs(arr[left]+arr[right]) < min_v) {
                min_v = Math.abs(arr[left] + arr[right]); l=arr[left]; r=arr[right];
            }
            if (arr[left]+arr[right] > 0) {
                right -= 1;
            }
            else if (arr[left] + arr[right] < 0) {
                left += 1;
            }
            else {
                l= arr[left]; r = arr[right];
                break;
            }
        }
        bw.write(l+" "+r);
        bw.flush();
        bw.close();
    }
}
