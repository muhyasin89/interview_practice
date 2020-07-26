package codeWars;

import java.util.*;

/**
 * Hello world!
 *
 */
public class App 
{
    // public static void main( String[] args )
    // {
    //     System.out.println( "Hello World!" );
    // }

    static int sum(List<Integer> int_list){
        int sum = 0;
        int i;

        for(i=0; i< int_list.size(); i++){
        sum += int_list.get(i);
        }

        return sum;
    }

    public static int main(int n) {
        
        
        String temp = Integer.toString(n);
         
        List<Integer> int_list = new ArrayList<Integer>();
        for (int i = 0; i < temp.length(); i++) {
            int_list.add(temp.charAt(i) - '0');
        }

        return sum(int_list);
    }
}




