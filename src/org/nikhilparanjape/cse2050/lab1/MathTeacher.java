package org.nikhilparanjape.cse2050.lab1;

/**
 * This is a class for math teacher
 *
 * @author Nikhil Paranjape,
 *
 * CSE 2050
 */

public class MathTeacher extends Teacher{

    private String subject = "Calculus";
    public static void main(String[] args){
        MathTeacher teach = new MathTeacher();

        System.out.println("Hello! I am a " + teach.designation + " at " + teach.collegeName + ". " + "I teach " + teach.subject + ".");



    }
}
