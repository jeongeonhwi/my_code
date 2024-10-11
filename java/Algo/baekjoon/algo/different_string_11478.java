import java.io.*;
import java.util.*;
import java.lang.*;

public class different_string_11478 {
    static String arr;
    static int N;
    static HashSet<String> hs = new HashSet<>();

//    static String getString(int a, int b) {
//        String data = "";
//
//        for (int i=a; i<b; i++) {
//            data += arr.charAt(i);
//        }
//        return data;
//    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        arr = st.nextToken();
        N = arr.length();
        for (int i=0; i<N; i++) {
            for (int j=i+1; j<N+1; j++) {
                hs.add(arr.substring(i,j));
            }
        }
        bw.write(hs.size()+"");
        bw.flush();
    }
}
