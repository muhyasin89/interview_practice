package hackerRankGroup;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class javaEndOfFile {
    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner userInput = new Scanner(System.in);
        int count = 1;

        while (!(userInput.nextLine()).isEmpty()) {
            System.out.println(count + " " + userInput.nextLine());
            count++;
        }


        userInput.close();
    }
}
