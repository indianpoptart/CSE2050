package org.nikhilparanjape.cse2050.lab1;

import java.util.*;

class Base {

    int smallest(int[] array){
        int smallestVal = array[0];

        for(int i = 1; i < array.length; i++){
            if((array[i]) < smallestVal){
                smallestVal = array[i];
            }
        }

        return smallestVal;
    }
}
