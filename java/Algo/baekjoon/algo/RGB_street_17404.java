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
            for (int i = 0; i<N; i++) {
                if (i == 0) {
                    for (int z = 0; z<3; z++) {
                        if (j == z) rgb[z] = rgbhouse[i][z];
                        else rgb[z] = 100000000;
                    }
                } else {
                    rgb[0] += Math.min(rgbhouse[i][1],rgbhouse[i][2]);
                    rgb[1] += Math.min(rgbhouse[i][0],rgbhouse[i][2]);
                    rgb[2] += Math.min(rgbhouse[i][1],rgbhouse[i][0]);
                }
                System.out.println(Arrays.toString(rgb));
            }
            System.out.println(Arrays.toString(rgb));
            for (int i : rgb) ans = Math.min(ans,i);
        }

//        for (int[] ilist : rgbhouse) {efefe
//            ans = Math.min(ilist[0], ans);
//        }
        System.out.println(ans);
    }
}
