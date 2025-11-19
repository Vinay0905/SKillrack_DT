// The program must accept N string values as the input. The given N string values are aligned vertically or horizontally as shown in the Example Input/Output section. The empty spaces at the end of each string are denoted as asterisks (*). The program must change the alignment (vertical to horizontal or horizontal to vertical) of the given N string values and print them as the output.

// Note: At least one string value is always longer than N.

// Boundary Condition(s):

// 3
// ≤
// N
// ≤
// 50
// 3≤N≤50

// 1
// ≤
// 1≤ Length of each string 
// ≤
// 100
// ≤100

// Input Format:
// The first line contains N.
// The next lines contain the N string values vertically or horizontally.

// Output Format:
// The lines contain the N string values vertically or horizontally.

// Example Input/Output 1:

// Input:

// text
// 4
// book**
// pencil
// car***
// cycle*
// Output:

// text
// bpcc
// oeay
// onrc
// kc*l
// *i*e
// *l**
// Explanation:
// Here N = 4 and the string values are aligned horizontally. So they are printed vertically.

// Example Input/Output 2:

// Input:

// text
// 4
// bpcc
// oeay
// onrc
// kcl
// wiwe
// Output:

// text
// book**
// pencil
// car***
// cycle
// Explanation:
// Here N = 4 and the string values are aligned vertically. So they are printed horizontally.
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String first = br.readLine();
        if (first == null || first.trim().isEmpty()) {
            return;
        }
        int N = Integer.parseInt(first.trim());
        List<String> lines = new ArrayList<>();
        String line;
        while ((line = br.readLine()) != null) {
            line = line.replaceAll("\\r", ""); // guard for CRLF
            if (line.length() == 0 && br.ready() == false) break;
            lines.add(line);
        }

        // If exactly N lines -> horizontal input (N strings). Convert to vertical.
        if (lines.size() == N) {
            int maxLen = 0;
            for (String s : lines) if (s.length() > maxLen) maxLen = s.length();

            StringBuilder out = new StringBuilder();
            for (int col = 0; col < maxLen; col++) {
                for (int row = 0; row < N; row++) {
                    String s = lines.get(row);
                    char ch = (col < s.length()) ? s.charAt(col) : '*';
                    out.append(ch);
                }
                System.out.println(out.toString());
                out.setLength(0);
            }
        } else {
            // vertical input: number of lines > N -> convert to horizontal (N strings)
            int M = lines.size();
            StringBuilder out = new StringBuilder();
            for (int col = 0; col < N; col++) {
                for (int row = 0; row < M; row++) {
                    String s = lines.get(row);
                    char ch = (col < s.length()) ? s.charAt(col) : '*';
                    out.append(ch);
                }
                System.out.println(out.toString());
                out.setLength(0);
            }
        }
    }
}


