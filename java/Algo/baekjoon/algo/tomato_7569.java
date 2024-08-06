import java.lang.*;
import java.io.*;
import java.util.*;

public class tomato_7569 {
    static int M,N,H;
    static int[][][] arr;

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputstring = br.readLine();
        StringTokenizer st = new StringTokenizer(inputstring);

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        arr = new int[H][N][M];

        for (int h=0; h<N; h++) {
            for (int i=0; i<N; i++) {
                inputstring = br.readLine();
                for (int j=0; j<M; j++) {
                    arr[h][i][j] = inputstring.charAt(j);
                }
            }
        }
    }
}
