import java.io.*;
import java.util.*;
public class Solution {

    public static void main(String[] args) {
     Scanner sc=new Scanner(System.in);
     int x=sc.nextInt();
     int y=sc.nextInt();
     int z=sc.nextInt();
     if(z<x){
         System.out.println("0");
     }
     else if(z<x+y){
         System.out.println("1");
     }
     else{
         System.out.println("2");
     }
    }
}
