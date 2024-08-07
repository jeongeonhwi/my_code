import java.lang.*;
import java.io.*;
import java.util.*;

public class tomato_7569 {
    static int M,N,H, after=0, before=0, non=0;
    static int[][][] arr;
    static HashSet<int[]> set = new HashSet<>();
    static HashSet<int[]> tmpset = new HashSet<>();

    public static void makeafter (int h,int i,int j) {
        if (h+1<H && arr[h+1][i][j] == 0) {
            tmpset.add(new int[]{h+1,i,j});
            arr[h+1][i][j] = 1;
            after++; before--;
        }
        if (h-1 >=0 && arr[h-1][i][j] == 0) {
            tmpset.add(new int[]{h-1,i,j});
            arr[h-1][i][j] = 1;
            after++; before--;
        }
        if (i+1<N && arr[h][i+1][j] == 0) {
            tmpset.add(new int[]{h,i+1,j});
            arr[h][i+1][j] = 1;
            after++; before--;
        }
        if (i-1>=0 && arr[h][i-1][j] == 0) {
            tmpset.add(new int[]{h,i-1,j});
            arr[h][i-1][j] = 1;
            after++; before--;
        }
        if (j+1<M && arr[h][i][j+1] == 0) {
            tmpset.add(new int[]{h,i,j+1});
            arr[h][i][j+1] = 1;
            after++; before--;
        }
        if (j-1>=0 && arr[h][i][j-1] == 0) {
            tmpset.add(new int[]{h,i,j-1});
            arr[h][i][j-1] = 1;
            after++; before--;
        }

    }

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputstring = br.readLine();
        StringTokenizer st = new StringTokenizer(inputstring);

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        arr = new int[H][N][M];

        for (int h=0; h<H; h++) {
            for (int i=0; i<N; i++) {
                inputstring = br.readLine();
                StringTokenizer stt = new StringTokenizer(inputstring);
                for (int j=0; j<M; j++) {
                    arr[h][i][j] = Integer.parseInt(stt.nextToken());
                    if (arr[h][i][j] == 1) {
                        set.add(new int[]{h,i,j});
                        after++;
                    } else if (arr[h][i][j] == 0) {
                        before++;
                    } else {
                        non++;
                    }
                }
            }
        }
        int ans = -1;
        int day = 0;
        if (after+non == H*N*M) {
            ans = 0;
        } else {
            while (true) {
                day++;
                int breakcheck = before;

                for (int[] setlist : set) {
                    makeafter(setlist[0], setlist[1], setlist[2]);
                }

                set = new HashSet<>(tmpset);
                tmpset.clear();
//                for (int[] rmvlist : rmvset) {
//                    int[] target = {rmvlist[0],rmvlist[1], rmvlist[2]};
//                    set.removeIf(array -> Arrays.equals(array, target));
//                }
//                rmvset.clear();

    //            하루가 지나고 안익은 토마토의 수가 줄지 않으면 탈출
                if (breakcheck == before) {
                    break;
                }
                if (before == 0) {
                    ans = day;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}
