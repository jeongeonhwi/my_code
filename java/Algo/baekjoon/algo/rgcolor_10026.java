import java.util.*;
import java.lang.*;
import java.io.*;

public class rgcolor_10026 {
    public int dfs() {
        return 0;
    }

    public static void main (String[] arg) throws IOException  {
//        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputn = br.readLine();
        StringTokenizer st = new StringTokenizer(inputn);

        int n = Integer.parseInt(st.nextToken());

        String[] arr = new String[n];
        int[][] ncvisited = new int[n][n];
        int[][] visited = new int[n][n];

        for (int i = 0; i<n; i++) {
            String inputline = br.readLine();
            arr[i] = inputline;
        }
    }
}
