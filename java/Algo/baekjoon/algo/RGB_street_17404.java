import java.util.*;
import java.lang.*;
import java.io.*;

public class RGB_street_17404 {
    static int[] rgb;
    static int N, red, green, blue;
    static int[][] rgbhouse;

    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        N = Integer.parseInt(st.nextToken()); rgbhouse = new int[N][3]; rgb = new int[3];
        for (int i=0; i<N; i++) {
            inputline = br.readLine();
            st = new StringTokenizer(inputline);
            red = Integer.parseInt(st.nextToken()); green = Integer.parseInt(st.nextToken()); blue = Integer.parseInt(st.nextToken());
            rgbhouse[i] = new int[] {red, green, blue};
        }
        int ans = 10000000;

        for (int j = 0; j<3; j++) {
            int[] flag = {0,0,0};
            for (int i = 0; i<N; i++) {
                if (i == 0) {
                    for (int z = 0; z<3; z++) {
                        if (j == z) {
                            rgb[z] = rgbhouse[i][z];
                            flag[z] = 1;
                        }
                        else rgb[z] = 100000000;
                    }
                } else {
                    int[] tmp = {0,0,0};
                    tmp[0] += Math.min(rgb[1],rgb[2]) + rgbhouse[i][0];
                    tmp[1] += Math.min(rgb[0],rgb[2]) + rgbhouse[i][1];
                    tmp[2] += Math.min(rgb[1],rgb[0]) + rgbhouse[i][2];
                    System.arraycopy(tmp, 0, rgb, 0, 3);
                    if (i==N-1) {
//                        System.out.println(Arrays.toString(flag));
                        for (int f=0; f<3; f++) {
                            if (flag[f] == 1) {
                                rgb[f] += 100000000;
                            }
                        }
                    }
                }
//                System.out.println(Arrays.toString(rgb));
            }
//            System.out.println(Arrays.toString(rgb));
            for (int i : rgb) ans = Math.min(ans,i);
//            System.out.println(ans);
        }

//        for (int[] ilist : rgbhouse) {efefe
//            ans = Math.min(ilist[0], ans);
//        }
        System.out.println(ans);
    }
}
