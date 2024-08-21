import java.util.*;
import java.lang.*;
import java.io.*;

public class color_paper_2630 {
    static int N, white_cnt=0, blue_cnt=0;
    static int [][] arr, visited;

    public static void find_color_paper(int n, int si,int sj) {
        if (n == 1) {
//            System.out.println(arr[si][sj]+" "+si+" "+sj+" "+n);
            if (arr[si][sj] == 0) white_cnt++;
            else blue_cnt++;
            return;
        }
        if (check_paper(si,sj,si+n,sj+n)) {
//            System.out.println(arr[si][sj]+" "+si+" "+sj+" "+di+" "+dj);
            if (arr[si][sj] == 0) white_cnt++;
            else blue_cnt++;
            return;
        }
        find_color_paper(n/2, si,sj);
        find_color_paper(n/2, si,sj+n/2);
        find_color_paper(n/2, si+n/2,sj);
        find_color_paper(n/2, si+n/2,sj+n/2);
    }
    public static boolean check_paper(int si, int sj, int di, int dj) {
        int paper_color = arr[si][sj];
        for (int i=si; i<di; i++) {
            for (int j=sj; j<dj; j++) {
                if (arr[i][j] != paper_color) return false;
            }
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken()); arr = new int[N][N]; visited = new int[N][N];
        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            for (int j=0; j<N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        find_color_paper(N, 0,0);
//        System.out.println(white_cnt+"\n"+blue_cnt);
        pw.write(white_cnt+"\n"+blue_cnt);
        pw.flush();
    }
}
