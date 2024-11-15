import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        int z=sc.nextInt();
        int total_time=z*24*60;
        int needed_time=x*y;
        if(needed_time<=total_time){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
    }
}
