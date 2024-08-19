import java.io.*;
import java.lang.*;
import java.util.*;

public class tree_cut_2805 {
    static int N,M, now = 0, tree_count = 0, high=0;
    static int[] nlist;
    static ArrayDeque<Integer> deque;
    public static void main (String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken()); M = Integer.parseInt(st.nextToken()); nlist = new int[N]; deque = new ArrayDeque<>();
        inputline = br.readLine();
        st = new StringTokenizer(inputline);
        for (int i=0; i<N; i++) {
            nlist[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nlist); high = nlist[N-1];
        for (int i: nlist) deque.add(i);
//        System.out.println(now);
        while (!deque.isEmpty()) {
            // 위에서부터 벌목할 나무를 계산
            int toptree = deque.removeLast();
            tree_count += 1;
            while (!deque.isEmpty()) {
                if (deque.peekLast() == toptree) {
                    deque.removeLast(); tree_count += 1;
                } else break;
            }
            int secondtree = 0;
            if (!deque.isEmpty()) secondtree = deque.peekLast();
            if (toptree-secondtree >= (M)/(tree_count)) {
//                System.out.println(M+" "+tree_count+" "+toptree+" "+secondtree+" "+now);
                if (M%tree_count == 0) {
                    now += M;
                    high -= M/tree_count;
                }
                else {
                    now += (M / tree_count) * (tree_count * 2);
                    high -= (M/tree_count)+1;
                }
                break;
            } else {
                M -= (toptree-secondtree)*tree_count;
                now += (toptree-secondtree)*tree_count;
//                System.out.println(now);
                high = secondtree;
            }
//            System.out.println(toptree+" "+secondtree+" "+tree_count+" "+now);
        }
        System.out.println(high);
    }
}