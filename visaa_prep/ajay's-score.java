import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        
        int[] scores =new int[n];
        for(int i=0;i<n;i++){
            int total_points=sc.nextInt();
            int passed_cases=sc.nextInt();
            int tc_points=total_points/10;
            scores[i]=tc_points*passed_cases;
        }
        for(int score:scores){
            System.out.println(score);
        }
    }
}
