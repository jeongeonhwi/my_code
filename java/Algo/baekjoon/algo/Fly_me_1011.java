import java.io.*;
import java.util.*;
import java.lang.*;


public class Fly_me_1011 {
    static int T,x,y,start=0,end=0;
//    static ArrayDeque<Integer> start = new ArrayDeque<>(), end = new ArrayDeque<>();
    public static void main (String[] args) throws IOException {
        String currentDir = System.getProperty("user.dir");
        String filePath = currentDir + "/Algo/baekjoon/algo/input/1011.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        T = Integer.parseInt(st.nextToken());
        for (int t=0; t<T; t++) {
            start = 0;end = 0;
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            x = Integer.parseInt(st.nextToken()); y = Integer.parseInt(st.nextToken());
            int cnt = 0;
            int distance = y-x;
            while (distance > 0) {
                int point = 1;

                point += Math.min(start, end);

                if (distance >= point) {
                    start = point; distance -= point; cnt++;
                }
                if (distance >= point) {
                    end = point; distance -= point; cnt++;
                }
                if (distance < point) break;
            }
            int ans = cnt;
            if (distance > 0) ans++;
            pw.println(ans);
        }


        pw.flush();
    }
}
