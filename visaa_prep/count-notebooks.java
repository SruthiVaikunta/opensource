import java.io.*;
import java.util.*;
public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int books=10*n; 
        /* total pages = 1000*n  ==> then books possible = total pages/100 = 10*n; */
        System.out.println(books);
    }
}
