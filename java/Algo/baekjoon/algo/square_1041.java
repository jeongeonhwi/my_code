import java.io.*;
import java.lang.*;
import java.util.*;

public class square_1041 {
    static int N, min_three = 153, min_two = 102, min_one = 51;
    static int[][] arr = new int[7][4];
    static int[] alist, visited = new int[7];

    static void dfs(int step, int fin, int now, int node, int sn) {
        if (step == fin) {
            if (fin == 2) {
                min_two = Math.min(min_two, now);
            } else if (fin == 3) {
                if (now >= min_three) return;
                for (int i = 0; i<4; i++) {
                    if (arr[node][i] == sn) {
                        min_three = now;
                        break;
                    }
                }
            }
            return;
        }
        for (int i = 0; i<4; i++) {
            if (visited[arr[node][i]] == 1) continue;
            visited[arr[node][i]] = 1;
            if (step == 2) dfs(step+1, fin, now+alist[node], node, sn);
            else dfs(step+1, fin, now+alist[node], arr[node][i], sn);
            visited[arr[node][i]] = 0;
        }

    }

    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String currentDir = System.getProperty("user.dir");
        String filePath = currentDir + "/Algo/baekjoon/algo/input/1041.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
        PrintWriter pw = new PrintWriter(System.out);

        String inputstring = br.readLine();
        StringTokenizer st = new StringTokenizer(inputstring);
        N = Integer.parseInt(st.nextToken());
        alist = new int[7];
        inputstring = br.readLine();
        st = new StringTokenizer(inputstring);
        int as = 0; int amax = 0;
        for (int i = 1; i<7; i++) {
            alist[i] = Integer.parseInt(st.nextToken());
            min_one = Math.min(min_one, alist[i]);
            amax = Math.max(amax, alist[i]);
            as += alist[i];
        }

        arr[1] = new int [] {2,3,4,5};
        arr[2] = new int [] {1,3,4,6};
        arr[3] = new int [] {1,2,5,6};
        arr[4] = new int [] {1,2,5,6};
        arr[5] = new int [] {1,3,4,6};
        arr[6] = new int [] {2,3,4,5};

        for (int i=1; i<7; i++) {
            visited = new int[7];
            dfs(0,2, 0, i, i);
            visited = new int[7];
            visited[i] = 1;
            dfs(0,3, 0, i, i);
        }
//        System.out.println(min_three);
//        System.out.println(min_two);
        long ans = 0;
        if (N == 1) {
            ans = as - amax;
        } else {
            ans += min_one * ((long) (N - 2) * (N - 1) * 4 + (long) (N - 2) * (N - 2));
            ans += (long) min_two * ((N - 1) + (N - 2)) * 4;
            ans += min_three * 4L;
        }
        pw.println(ans);
        pw.flush();
    }
}
