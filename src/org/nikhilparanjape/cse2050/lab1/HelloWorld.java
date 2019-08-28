package org.nikhilparanjape.cse2050.lab1;

public class HelloWorld {
    public static void main(String[] args){
        int z = 0;
        for(int i = 0; i < 10; i++){
            System.out.println(i);
            z -= i;
            System.out.println(z);
        }
    }
}
