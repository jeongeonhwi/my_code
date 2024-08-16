import java.io.*;
import java.lang.*;
import java.util.*;

public class tree_cut_2805 {
    static double N,M, now = 0, tree_count = 0, high=0;
    static double[] nlist;
    static ArrayDeque<Double> deque;
    public static void main (String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Double.parseDouble(st.nextToken()); M = Double.parseDouble(st.nextToken()); nlist = new double[N]; deque = new ArrayDeque<>();
        inputline = br.readLine();
        st = new StringTokenizer(inputline);
        for (double i=0; i<N; i++) {
            nlist[i] = Double.parseDouble(st.nextToken());
        }
        Arrays.sort(nlist); high = nlist[N-1];
        for (double i: nlist) deque.add(i);
        while (!deque.isEmpty()) {
            // 위에서부터 벌목할 나무를 계산
            double toptree = deque.removeLast();
            tree_count += 1;
            while (!deque.isEmpty()) {
                if (deque.peekLast() == toptree) {
                    deque.removeLast(); tree_count += 1;
                } else break;
            }
            double secondtree = toptree;
            if (!deque.isEmpty()) secondtree = deque.peekLast();
            if (secondtree == toptree) {
                if (M%tree_count == 0) {
                    now += M;
                    high -= M/tree_count;
                }
                else {
                    now += (M / tree_count) * (tree_count * 2);
                    high -= (M/tree_count+1);
                }
                break;
            }
            if ((toptree-secondtree)*tree_count+now >= M) {
                if (M%tree_count == 0) {
                    now += M;
                    high -= M/tree_count;
                }
                else {
                    now += (M / tree_count) * (tree_count * 2);
                    high -= (M/tree_count+1);
                }
                break;
            } else {
                M -= (toptree-secondtree)*tree_count;
                now += (toptree-secondtree)*tree_count;
                high = secondtree;
            }
            System.out.println(M+" "+now+" "+tree_count+" "+high+" "+toptree+" "+secondtree);
        }
        System.out.println(high);
    }
}
