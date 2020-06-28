package hackerRankGroup;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class Solution {
    public static void main(String[] args) {
        // Write your code here
        Scanner firstNumber = new Scanner(System.in);

        Int secondNumber=firstNumber.nextInt();

        if((firstNumber*secondNumber)<0)
        {
            throw new Exception("java.lang.Exception: Breadth and height must be positive");
        }else
        {
            System.out.println(secondNumber);
        }
    }
}
