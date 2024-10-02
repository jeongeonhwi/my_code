import java.io.*;
import java.lang.*;
import java.util.*;

class Edge implements Comparable<Edge> {
    int w;
    int cost;
    Edge(int w, int cost) {
        this.w = w;
        this.cost = cost;
    }

    @Override
    public int compareTo(Edge o) {
        return this.cost - o.cost;
    }
}

public class MST_1647 {
    static int N,M;
    static List<Edge>[] arr;

    public static int prim(int start) {
        boolean[] visit = new boolean[N+1];

        PriorityQueue<Edge> pq = new PriorityQueue<>();
        pq.offer(new Edge(start, 0));

        int total = 0;

        while(!pq.isEmpty()) {
            Edge edge = pq.poll();
            int v = edge.w;
            int cost = edge.cost;

            if (visit[v]) continue;
//            System.out.print(v);
//            System.out.println(cost);
            visit[v] = true;
            total += cost;

            for(Edge e : arr[v]) {
                if(!visit[e.w]) {
                    pq.add(e);
                }
            }
        }
        return total;
    }

    public static void main (String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String currentDir = System.getProperty("user.dir");
        String filePath = currentDir + "/Algo/baekjoon/algo/input/1647.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken());

        arr = new List[N+1];
        for (int i = 0; i < arr.length; i++) arr[i] = new ArrayList<>();

        for (int i=0; i<M; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            arr[v].add(new Edge(w, cost));
            arr[w].add(new Edge(v, cost));
        }

        int min_v = prim(1);
        for (int i = 2; i<N+1; i++) min_v = Math.min(min_v, prim(i));
//        System.out.println(min_v);
    }
}
