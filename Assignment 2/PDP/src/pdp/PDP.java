/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pdp;

import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author Aditya
 */
public class PDP {
    
    ArrayList <Integer> L = new ArrayList<Integer>();
    ArrayList <Integer> X = new ArrayList<Integer>();
    int width;

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        PDP obj = new PDP();
        
        obj.createList();
        
    }
    
    public void partialDigest(ArrayList <Integer> L){
        
        width = Collections.max(L);
        
        delete(width);
        
        X.add(0);
        
        X.add(width);
        
        //System.out.println("X is " + X);
        
        place(L,X);
        
    }
    
    public void place(ArrayList <Integer> L, ArrayList <Integer> X){
        
        if( L.size() == 0 ){
            
            Collections.sort(X);
            
            System.out.println("Original set is: " + X);
            
            return;
        }
        
        int y = Collections.max(L);
        
        if(is_subset(y, X, L)){
            
            //System.out.println("First first:");
            
            //System.out.println("1. X is " + X);
            
            X.add(y);
            
            //System.out.println("2. X is " + X);
            
            remove_subSet(y, X, L);
            
            //System.out.println("L is " + L );
            
            place(L, X);
            
            //System.out.println("3. X is " + X);
            
            if(X.contains(y)){
                int index = X.indexOf(y);
                X.remove(index);
            }
            
            //System.out.println("4. X is " + X);
            
            //System.out.println("L is " + L );
            
            append_subSet(y, X, L); 
            
            //System.out.println("L is " + L );
            
        }
        
        if(is_subset( Math.abs(width-y), X, L)){
            
            //System.out.println("Second if:");
            
            //System.out.println("L is " + L );
            
            //System.out.println("1. X is " + X);
            
            X.add(Math.abs(width-y));
            
            //System.out.println("2. X is " + X);
            
            //System.out.println("L is " + L );
            
            remove_subSet(Math.abs(width-y), X, L);
            
            //System.out.println("L is " + L );
            
            place(L, X);
            
            //System.out.println("3. X is " + X);
            
            if(X.contains(Math.abs(width-y))){
                int index = X.indexOf(Math.abs(width-y));
                X.remove(index);
            }
            
            //System.out.println("4. X is " + X);
            
            //System.out.println("5. L is " + L );
            
            append_subSet(Math.abs(width-y), X, L); 
            
            //System.out.println("6. L is " + L );
            
        }
        
        return;
    }
    
    public void delete(int width){
        
        int index = L.indexOf(width);
        
        L.remove(index);
        
    }
    
    public boolean is_subset(int y, ArrayList <Integer> X, ArrayList <Integer> L){
        
        for(int i = 0; i < X.size(); i++){
            
            if( !L.contains( Math.abs( y - X.get(i) ) ) ){
                
                return false;
                
            }    
        }
        
        return true;
        
    }
    
    public void remove_subSet(int y, ArrayList <Integer> X, ArrayList <Integer> L){
        
        for(int i = 0; i < X.size(); i++){
            
            if( L.contains( Math.abs( y - X.get(i) ) ) ){
               
                int index = L.indexOf( Math.abs( y - X.get(i) ) );
               
                L.remove(index);
                
            }    
        }
    }
    
    public void append_subSet(int y, ArrayList <Integer> X, ArrayList <Integer> L){
        
        for(int i = 0; i < X.size(); i++){
               
            L.add(Math.abs( y - X.get(i) ));
                
             
        }
    }
    
    public void createList(){
       
        
        int [] list = {0, 2, 4, 7, 10};
        
        for(int i = 0; i < list.length; i++){
            L.add(list[i]);
        }
        
        
        long startTime = System.currentTimeMillis();
        
        partialDigest(L);
        
        long endTime = System.currentTimeMillis();
        
        System .out.println("Time is: " + (endTime - startTime) );
    }
}
