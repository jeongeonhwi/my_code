import java.io.*;
import java.lang.*;
import java.util.*;

public class MST_1647 {
    static int N,M;
    static int[][] arr;
    public static void main (String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String currentDir = System.getProperty("user.dir");
        String filePath = currentDir + "/Algo/baekjoon/algo/input/1647.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());

        arr = new int[N+1][1];

        for (int i=0; i<M; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
        }
    }
}
