package org.nikhilparanjape.cse2050.experiments;
/**
 * A simple energy calculator
 *
 * Assignment 2.10
 *
 * @author Nikhil Paranjape
 *
 */

import java.util.Scanner;

public class EnergyCalculator {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.println("Enter the amount of water in kilograms:");
		double mass = scan.nextDouble();

		System.out.println("Enter the initial temperature (C):");
		double initTemp = scan.nextDouble();

		System.out.println("Enter the final temperature (C):");
		double finalTemp = scan.nextDouble();
		double diffTemp = (finalTemp - initTemp);
		//Sets constant for specific heat
		double spHeat = 4184;
		double energy = mass*diffTemp* spHeat;

		System.out.println("The energy needed is " + energy + " joules");

	}
}