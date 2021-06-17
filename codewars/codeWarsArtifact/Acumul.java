public class Acumul {
    
    public static String accum(String s) {
     // your code
      char[] ch=new char[s.length()];
      String result_string;
      
      for(int  i =0; i <= s.length(); i++){
        ch[i] = s.charAt(i);
        
        String repeat_char = new String(new char[i]).replace("\0", ch[i]);
        //last character
        if(i == (s.length() - 1)){
          result_string+=  repeat_char.toUpperCase();
        }else{
          result_string+= repeat_char.toUpperCase() + '-';
        }
         
        
      }
    }   
}

/****
 * https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/java
 * 
 */