import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int x=sc.nextInt();
        int y=sc.nextInt();
        
        if( y>=0 && y<=n*x && y%x==0){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }
        
    }
}
