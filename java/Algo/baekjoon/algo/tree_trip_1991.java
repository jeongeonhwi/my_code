import java.util.*;
import java.lang.*;
import java.io.*;

public class tree_trip_1991 {
    static int[] parent_tree;
    static int[][] child_tree;
    static String pre="", in="", post="";

    public static void preorder(int node) {
        pre += (char) node;
        for (int i=0; i<2; i++) {
            if (child_tree[node][i] != 0) {
                preorder(child_tree[node][i]);
            }
        }
    }

    public static void inorder(int node) {
        if (child_tree[node][0] != 0) {
            inorder(child_tree[node][0]);
        }
        in += (char) node;
        if (child_tree[node][1] != 0) {
            inorder(child_tree[node][1]);
        }
    }

    public static void postorder(int node) {
        for (int i=0; i<2; i++) {
            if (child_tree[node][i] != 0) {
                postorder(child_tree[node][i]);
            }
        }
        post += (char) node;
    }

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);

        parent_tree = new int[100];

        child_tree = new int[100][2];

        parent_tree[65] = 65;

        int node_number = Integer.parseInt(st.nextToken());

        for (int i=0; i<node_number; i++) {
            inputline = br.readLine();
            int a = inputline.charAt(0);
            char charb = inputline.charAt(2);
            if (charb != '.') {
                parent_tree[charb] = a;
                child_tree[a][0] = charb;
            }
            char charc = inputline.charAt(4);
            if (charc != '.') {
                parent_tree[charc] = a;
                child_tree[a][1] = charc;
            }
        }

        preorder(65); inorder(65); postorder(65);
        System.out.println(pre + '\n' + in + '\n' + post);
    }
}
