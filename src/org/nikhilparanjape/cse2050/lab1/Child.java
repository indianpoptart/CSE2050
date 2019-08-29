package org.nikhilparanjape.cse2050.lab1;

public class Child extends Base{
    public static void main(String[] args){
        int[] array = {17, 30, 42, 22, 97, 87, 39, 123, 838, 12};

        Base prog = new Base();

        System.out.println(prog.smallest(array));

    }
}
