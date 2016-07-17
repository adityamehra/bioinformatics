/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package assignment4cs6660;

import java.io.*;


/**
 *
 * @author Aditya
 */
public class Assignment4CS6660 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        
        Assignment4CS6660 obj = new Assignment4CS6660();
        
        //str1 stores string 1 before "->".
        //str2 stores string 2 after "->".
        //str stores each line in the input.txt. 
        String str1, str2, str;
        
        //variable index stores the index of seprator "->".
        int index = 0;
        
        //Reading word pairs from file "input.txt".
        FileInputStream fr = new FileInputStream("input.txt");
        BufferedReader br = new BufferedReader(new InputStreamReader(fr));
        
        while((str = br.readLine()) != null){
            
            index = str.indexOf("->");
            
            str1 = str.substring(0, index);
            
            str2 = str.substring(index+2);
            
            System.out.println("For " + str1 + " " + str2);
            
            int rec_result = obj.rec_med(str1.toLowerCase().toCharArray(), str2.toLowerCase().toCharArray(), str1.length(), str2.length());
        
            int dynamic_result = obj.dynamic_med(str1.toLowerCase().toCharArray(), str2.toLowerCase().toCharArray());
    
            System.out.println("Minimum Edit Distance via recursion: " + rec_result);
        
            System.out.println("Minimum Edit Distance via dynamic: " + dynamic_result);
            
            System.out.println("-------X-------");
            
        }
        
        
        
        
        
    }
    
    int rec_med(char[] str1, char[] str2, int i, int j){
        
        if(i == 0)
            return j;
        
        if(j == 0)
            return i;
        
        return Math.min( rec_med(str1, str2, i-1, j-1) + (str1[i-1] == str2[j-1] ? 0:1), Math.min(rec_med(str1, str2, i-1, j) + 1, rec_med(str1, str2, i, j-1) + 1));
        
    }
    
    int dynamic_med(char[] str1, char[] str2){

        int[][] temp = new int[str1.length+1][str2.length+1];

        for(int i = 0; i < temp[0].length; i++){
            temp[0][i] = i;
        }

        for(int i = 0; i < temp.length; i++){
            temp[i][0] = i;
        }

        for(int i = 1; i < temp.length; i++){
            for(int j = 1; j < temp[0].length; j++){

                if(str1[i-1] == str2[j-1]){
                    temp[i][j] = temp[i-1][j-1];
                }else{
                    temp[i][j] = Math.min( temp[i][j-1], Math.min(temp[i-1][j-1], temp[i-1][j])) + 1;
                }
            }
        }
        
        traceBack(temp, str1, str2);
        
        return temp[str1.length][str2.length];
    }
    
    public void traceBack(int[][] temp, char[] str1, char[] str2){
        
        System.out.println("Traceback is: ");
        
        int j = temp[0].length - 1;
        
        int i = temp.length - 1;
        
        while(true){
            
            if(i == 0 && j == 0){
            break;
            }
        
        if( str1[i-1] == str2[j-1] ){
            i = i - 1;
            j = j - 1;            
        }else if(temp[i][j] == temp[i-1][j-1] + 1){
            System.out.println("Replace " + str1[j-1] + " in string1 to " + str2[i-1] + " at " + i);
            i = i - 1;
            j = j - 1;
        }else if(temp[i][j] == temp[i-1][j] + 1){
            System.out.println("Delete " + str1[i-1] + " from string1 at " + i );
            i = i - 1;
        }else if(temp[i][j] == temp[i][j-1] + 1){
            System.out.println("Insert " + str2[j-1] + " in string1 at " + j);
            j = j - 1;
        }
            
        }
        
    }

    
    
}
