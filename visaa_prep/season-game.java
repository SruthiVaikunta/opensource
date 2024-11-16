import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        if(1<=n && n<=12){
            if(3<=n && n<=5){
                System.out.println("Spring");
            }
            else if(6<=n && n<=8){
                System.out.println("Summer");
            }
            else if(9<=n && n<=11){
                System.out.println("Autumn");
            }
            else{
                System.out.println("Winter");
            }
        }
        else{
            System.out.println("Invalid");
        }
    }
}
