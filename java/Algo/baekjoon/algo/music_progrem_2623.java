import java.io.*;
import java.lang.*;
import java.util.*;

public class music_progrem_2623 {
    static int N,M;
    static ArrayDeque<Integer>[] arr;
    static ArrayDeque<Integer> topologic = new ArrayDeque<>();
    static int[] nodeLevel,visited;
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new ArrayDeque[N+1];
        nodeLevel = new int[N+1]; visited = new int[N+1];
        for (int i=0; i<N+1; i++) {
            arr[i] = new ArrayDeque<>();
        }
        for (int i=0; i<M; i++){
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            int a = Integer.parseInt(st.nextToken());
            int[] al = new int[a];
            for (int ii=0; ii<a; ii++) al[ii] = Integer.parseInt((st.nextToken()));
            for (int ii=0; ii<a-1; ii++) {
                nodeLevel[al[ii+1]]++;
                arr[al[ii]].add(al[ii + 1]);
            }
        }
        System.out.println(Arrays.toString(nodeLevel));
        for (int i = 1; i<N+1; i++) {
            if (nodeLevel[i] == 0) {
                topologic.add(i);
                visited[i] = 1;
            }
        }
        String ans = "";
        while (!topologic.isEmpty()) {
            int a = topologic.removeFirst();
            ans += a+"\n";
            for (int aa : arr[a]) {
                nodeLevel[aa]--;
            }
            for (int i=1; i<N+1; i++) {
                if (visited[i] == 0 && nodeLevel[i] == 0) {
                    topologic.addLast(i);
                    visited[i] = 1;
                }
            }
        }
        for (int i=1; i<N+1; i++) {
            if (visited[i] == 0) {
                ans = "0";
                break;
            }
        }
        bw.write(ans);
        bw.flush();
    }
}
