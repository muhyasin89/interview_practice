package codeWars;

import java.util.*;   

/**
 * step 1: convert int to list
 * step 2: sum list value
 */
public class App 
{
    // public static void main( String[] args )
    // {
    //     System.out.println( "Hello World!" );
    // }

    public static void main() {
        
        int n = 123;
        String temp = Integer.toString(n);
         
        List<Integer> int_list = new ArrayList<Integer>();
        for (int i = 0; i < temp.length(); i++) {
            int_list.add(temp.charAt(i) - '0');
        }

        System.out.println("The Sum is "+ sumList(int_list));
    }

    static int sumList(List<Integer> int_list) {
        int sum = 0;
        int i;

        for (i = 0; i < int_list.size(); i++) {
            sum += int_list.get(i);
        }

        return sum;
    }

}




