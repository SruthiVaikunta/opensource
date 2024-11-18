import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       Scanner sc=new Scanner(System.in);
        Long n=sc.nextLong();
        int k=sc.nextInt();
        if ((n & (1L <<(k-1))) !=0){
            System.out.println("true");
        }
        else{
            System.out.println("false");
        }
    }
}
