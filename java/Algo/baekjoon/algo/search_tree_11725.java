import java.lang.*;
import java.util.*;
import java.io.*;


public class search_tree_11725 {
    static int N;
    static int[] tree;
    static ArrayList<Integer>[] arr;
    static Deque<Integer> deque = new ArrayDeque<>();

    public static boolean fine_parent(int node) {
        return tree[node] != 0;
    }

    public static void bfs(int rootnode) {

        for (int arrdata : arr[rootnode]) {
            deque.add(arrdata);
            tree[arrdata] = rootnode;
        }

        while (!deque.isEmpty()) {
            int node = deque.removeFirst();
            for (int arrdata : arr[node]) {
                if (!fine_parent(arrdata)) {
                    deque.add(arrdata);
                    tree[arrdata] = node;
                }
            }
        }
    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        N = Integer.parseInt(st.nextToken());
        tree = new int[N+1];
        arr = new ArrayList[N+1];
        for (int i=0; i<N+1; i++) {
            arr[i] = new ArrayList<>();
        }
        tree[1] = 1;
        for (int i=0; i<N-1; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[a].add(b);
            arr[b].add(a);
        }

        bfs(1);

        StringBuilder ans = new StringBuilder();
        for (int i=2; i<N+1; i++) {
            ans.append(tree[i]).append("\n");
        }
        pw.print(ans);
    }
}
