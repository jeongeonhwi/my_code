import java.util.*;
import java.lang.*;
import java.io.*;

public class rgcolor_10026 {
    static int n = 0, ncnt=0, ccnt=0;
    static int[][] ncvisited = new int[n][n];
    static int[][] visited = new int[n][n];

    public static void dfs(char c, int i, int j, String[]arr) {
        int[] di = {-1,1,0,0};
        int[] dj = {0,0,-1,1};

        visited[i][j] = 1;

        for (int d = 0; d<4; d++) {
            int ni = i+di[d];
            int nj = j+dj[d];

            if (ni>=0 && nj>=0 && ni<n && nj<n) {
                if (visited[ni][nj] == 0 && arr[ni].charAt(nj) == c) {
                    dfs(c,ni,nj,arr);
                }
            }
        }
    }

    public static void ndfs(char c, int i, int j, String[]arr) {
        int[] di = {-1,1,0,0};
        int[] dj = {0,0,-1,1};

        ncvisited[i][j] = 1;

        for (int d = 0; d<4; d++) {
            int ni = i+di[d];
            int nj = j+dj[d];

            if (ni>=0 && nj>=0 && ni<n && nj<n) {
                if (c == 'R' || c == 'G') {
                    if (ncvisited[ni][nj] == 0 && (arr[ni].charAt(nj) == 'R' || arr[ni].charAt(nj) == 'G')) {
                        ndfs(c,ni,nj,arr);
                    }
                }
                else  {
                    if (ncvisited[ni][nj] == 0 && arr[ni].charAt(nj) == c) {
                        ndfs(c,ni,nj,arr);
                        }
                    }
            }
        }
    }

    public static void main (String[] arg) throws IOException  {
//        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputn = br.readLine();
        StringTokenizer st = new StringTokenizer(inputn);

        n = Integer.parseInt(st.nextToken());

        ncvisited = new int[n][n];
        visited = new int[n][n];

        String[] arr = new String[n];


        for (int i = 0; i<n; i++) {
            String inputline = br.readLine();
            arr[i] = inputline;
        }

        for (int i = 0; i<n; i++) {
            for (int j = 0; j<n; j++) {
                if (visited[i][j] == 0) {
                    dfs(arr[i].charAt(j), i ,j, arr);
                    ccnt++;
                }
                if (ncvisited[i][j] == 0) {
                    ndfs(arr[i].charAt(j), i,j, arr);
                    ncnt++;
                }
            }
        }
        System.out.print(ccnt);
        System.out.print(' ');
        System.out.print(ncnt);
    }
}
