import java.io.*;
import java.lang.*;
import java.util.*;

public class abcd_13023 {
    static boolean flag = false;
    static int N,M;
    static ArrayDeque<Integer>[] arr;
    static int[] visited;
    static void dfs (int node, int stage) {
        for (int nextnode : arr[node]) {
            if (visited[nextnode] == 1) continue;
            if (stage+1 == 5) {
                flag = true;
                return;
            }
//            System.out.println(nextnode + " " + stage);
            visited[nextnode] = 1;
            dfs(nextnode, stage+1);
            visited[nextnode] = 0;
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());
        arr = new ArrayDeque[N];
        for (int i=0; i<N; i++) {
            arr[i] = new ArrayDeque<>();
        }
        for (int i=0; i<M; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            int a = Integer.parseInt(st.nextToken()); int b = Integer.parseInt(st.nextToken());
            arr[a].add(b); arr[b].add(a);
        }
        for (int i=0; i<N; i++) {
            if (flag) break;
            visited = new int[N];
            visited[i] = 1;
            dfs(i,1);
        }
        if (flag) bw.write("1");
        else bw.write("0");
        bw.flush();
    }
}
