package hackerRankGroup;

import java.util.Scanner;

public class EndOfFile {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int loopInt = 0;
        
        while(scan.hasNext()){
            ++loopInt;
            System.out.println(loopInt+"."+scan.next());
            
        }

        scan.close();
    }
}