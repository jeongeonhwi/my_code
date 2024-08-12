import java.util.*;
import java.lang.*;
import java.io.*;

public class tree_trip_1991 {
    static int[] tree;
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        tree = new int[100];

        tree[65] = 65;

        int node_number = Integer.parseInt(st.nextToken());

        for (int i=0; i<node_number; i++) {
            inputline = br.readLine();
            String[] data = inputline.split(" ");
//            int a = (int) data[1];
        }
    }
}
