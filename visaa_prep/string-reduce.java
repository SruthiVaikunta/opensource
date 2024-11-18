import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        
        StringBuilder res=new StringBuilder();
        int count=1;
        
        for(int i=1;i<s.length();i++){
            if(s.charAt(i)==s.charAt(i-1)){
                count++;
            }
            else{
                res.append(s.charAt(i-1)).append(count);
                count=1;
            }
        }
        res.append(s.charAt(s.length()-1)).append(count);
        System.out.println(res);
        
    }
}
