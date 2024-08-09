import java.lang.*;
import java.util.*;
import java.io.*;

public class moving_knight_7562 {
    static int I,si,sj,di,dj;
    static int[][] chessfield;
    static int[][] visited;
    static ArrayDeque<int[]> deque;
    static int[] move = {2,-1,2,1,-2,-1,-2,1,-1,2,1,2,-1,-2,1,-2};

    public static int bfs() {
        while (!deque.isEmpty()) {
            int[] dequedata = deque.removeFirst();
            int cnt = dequedata[0], i = dequedata[1], j = dequedata[2];

            for (int f = 0; f<16;) {
                int ni=i+move[f], nj=j+move[f+1];
                if (check_kight(ni,nj)) {
                    if (ni == di && nj == dj) {
                        return cnt+1;
                    }
                    visited[ni][nj] = 1;
                    int[] tmp = {cnt+1,ni,nj};
                    deque.add(tmp);
                }
                f+=2;
            }
        }
        return 0;
    }

    public static boolean check_kight(int i,int j) {
        return 0 <= i && i < I && 0 <= j && j < I && visited[i][j] == 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        int T = Integer.parseInt(st.nextToken());

        for (int i=0; i<T; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            I = Integer.parseInt(st.nextToken());
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            si = Integer.parseInt(st.nextToken());
            sj = Integer.parseInt(st.nextToken());
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            di = Integer.parseInt(st.nextToken());
            dj = Integer.parseInt(st.nextToken());

            chessfield = new int[I][I];
            visited = new int[I][I];
            deque = new ArrayDeque<>();
            deque.add(new int[] {0, si,sj});
            if (si == di && sj == dj) {
                System.out.println(0);
            } else {
                System.out.println(bfs());
            }
        }
    }
}
