import java.lang.*;
import java.io.*;
import java.util.*;

public class fire_4179 {
    static int N,M;
    static ArrayDeque<int []> deq = new ArrayDeque<>(), fire = new ArrayDeque<>();
    static String[] map;
    static boolean[][] visited,fvisited;
    static int[] d = new int[] {1,0,0,1,-1,0,0,-1};

    static int move_man (int[] sp) {
        deq.addLast(new int[]{sp[0],sp[1],0});
        visited[sp[0]][sp[1]] = true;
        while (!deq.isEmpty()) {
            int[] ij = deq.removeFirst();
            int i = ij[0], j = ij[1], c = ij[2];
            if (reach(i,j)) return c;

            for (int ii=0; ii<8; ii+=2) {
                int ni = i+d[ii]; int nj = j+d[ii+1];
                if (0<=ni && ni<N && 0<=nj && nj<M && !visited[ni][nj] && !fvisited[ni][nj] && map[ni].charAt(nj) == '.') {
                    deq.addLast(new int[]{ni, nj, c + 1});
                    visited[ni][nj] = true;
                }
            }

            fire_visited(c);
        }
        return -2;
    }

    static void fire_visited (int c) {
        while (!fire.isEmpty() && fire.peekFirst()[2] == c) {
            int[] f = fire.removeFirst();
            for (int ii=0; ii<8; ii+=2) {
                int ni = f[0]+d[ii], nj = f[1]+d[ii+1];
                if (0<=ni && ni<N && 0<=nj && nj <M && map[ni].charAt(nj) != '#' && !fvisited[ni][nj]) {
                    fvisited[f[0]][f[1]] = true;
                    fire.addLast(new int[]{ni,nj,c+1});
                }
            }
        }
    }

    static boolean reach(int i, int j) {
        return i == 0 || i == N - 1 || j == 0 || j == M - 1;
    }

    static int[] find_position () {
        int[] m = new int[2];
        for (int i = 0; i<N; i++) {
            for (int j = 0; j<M; j++) {
                if (map[i].charAt(j) == 'J') {
                    m[0] = i; m[1] = j;
                }
                if (map[i].charAt(j) == 'F') {
                    fire.addLast(new int[] {i,j,0});
                    fvisited[i][j] = true;
                }
            }
        }

        return new int[]{m[0],m[1]};
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken()); visited = new boolean[N][M]; fvisited = new boolean[N][M];

        map = new String[N];

        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);

            String d = st.nextToken();

            map[i] = d;
        }

        int ans = move_man(find_position())+1;
        if (ans == -1) bw.write("IMPOSSIBLE");
        else bw.write(ans+"");

        bw.flush();

    }
}
