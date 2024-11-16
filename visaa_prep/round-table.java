import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int ways=x*fact(x-1);
        System.out.println(ways);
        sc.close();
    }
    //factorial function creation
    private static int fact(int n){
        int res=1;
        for(int i=1;i<=n;i++){
            res *=i;
            
        }
        return res;
    }
}
