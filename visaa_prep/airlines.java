import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int n=sc.nextInt();// e=extra_people p=extra_planes
        int e=n-(x*100);
        int p=0;
        if(e>0){
            p=e/100;
            if(e%100!=0){
                p+=1;
            }
        }
        System.out.println(p);
    }
    
}
