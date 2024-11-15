import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        char v= sc.next().charAt(0);
        char c=sc.next().charAt(0);
        if(v==c){
            System.out.println("NULL");
        }
        else if((v=='R' && c=='S') || (v=='P' && c=='R') || (v=='S' && c=='P')){
            System.out.println("Vignesh");
        }
        else{
            System.out.println("Charan");
        }
    }
}
