import java.lang.*;
import java.io.*;
import java.util.*;

public class make_code_1759 {
    static int L,C;
    static String a = "",b = "";
    static char[] aa,ab;
    static List<List<Character>> ca = new ArrayList<>(), cb = new ArrayList<>();

    static void combination(int n, int r, int start, List<Character> current, List<List<Character>> ca, List<List<Character>> cb, boolean flag) {
        if (current.size() == r) {
            if (flag) ca.add(new ArrayList<>(current));
            else cb.add(new ArrayList<>(current));
            return;
        }
        for (int i = start; i<n; i++) {
            if (flag) current.add(aa[i]);
            else current.add(ab[i]);
            combination(n,r, i+1, current, ca,cb, flag);
            current.remove(current.size() - 1);
        }
    }


    public static void main (String[] arg) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);

        String inputline = br.readLine();
        StringTokenizer st = new StringTokenizer(inputline);
        L = Integer.parseInt(st.nextToken()); C = Integer.parseInt(st.nextToken());
        inputline = br.readLine();
        for (int i=0; i<inputline.length(); i++) {
            if (inputline.charAt(i) == ' ') continue;
            if (inputline.charAt(i) == 'a'
                    | inputline.charAt(i) == 'e'
                    | inputline.charAt(i) == 'i'
                    | inputline.charAt(i) == 'o'
                    | inputline.charAt(i) == 'u') {
                a += inputline.charAt(i);
            }
            else {
                b += inputline.charAt(i);
            }
        }
        aa = new char[a.length()]; ab = new char[b.length()];
        for (int i=0; i<a.length(); i++) {
            aa[i] = a.charAt(i);
        }
        for (int i=0; i<b.length(); i++) {
            ab[i] = b.charAt(i);
        }
        Arrays.sort(aa); Arrays.sort(ab);
        List<String> ans = new ArrayList<>();
        for (int i = 1; i<L-1; i++) {
            char[] tmpc = new char[L];
            int point = 0;
            combination(aa.length, i,0, new ArrayList<>(), ca, cb, true);
            combination(ab.length, L-i, 0, new ArrayList<>(), ca, cb, false);
            for (List<Character> cca : ca) {
//                System.out.println(cca.toString());
                for (List<Character> ccb : cb) {
//                    System.out.println(ccb.toString());
                    for (int j = 0; j < cca.size(); j++) {
                        tmpc[j] = cca.get(j);
                    }
                    point = cca.size();
                    for (int j = point; j < L; j++) {
                        tmpc[j] = ccb.get(j-point);
                    }
                    Arrays.sort(tmpc);
                    String ts = "";
                    for (char t : tmpc) ts += t;
                    ans.add(ts);
                }
            }
            ca.clear(); cb.clear();
        }
        Collections.sort(ans);
        for (String a : ans) pw.write(a+"\n");
        pw.flush();
    }
}
