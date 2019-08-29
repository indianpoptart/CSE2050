package org.nikhilparanjape.cse2050.utils;


import java.applet.Applet;
import java.awt.*;

import javax.swing.JOptionPane;
import javax.swing.JFileChooser;
import javax.swing.JFrame;

import java.util.*;
import java.io.*;

import javax.swing.JOptionPane;
import javax.swing.UIManager;
import javax.swing.plaf.ColorUIResource;
import javax.swing.*;

/**
  Testing the values of red
  @author Nikhil Paranjape
 * @version March 2013
 */

public class ColorInputProgram {
    private static Icon icon, error;
    @SuppressWarnings("static-access")
	public static void main(String[] args){
        try{
            String ColorInput;
            UIManager UI=new UIManager();
            //final ImageIcon icon = new ImageIcon("painticon.png");
            //final ImageIcon error = new ImageIcon("error.png");
            
            //sets default window color
            UI.put("OptionPane.background",new ColorUIResource(250,235,215));
            UI.put("Panel.background",new ColorUIResource(250,235,215));
            JOptionPane.showMessageDialog(null, "Welcome to the hex to color converter", "Color Input Program", JOptionPane.INFORMATION_MESSAGE, icon);
            ColorInput = JOptionPane.showInputDialog("Tell me a hex number color and I will make a color");
            if(!ColorInput.contains("#")){
            	ColorInput = "#"+ ColorInput;
            }
            //Converts hex into rgb so the computer can use it
            Color color = Color.decode(ColorInput);
            JOptionPane.showMessageDialog(null,"Your color awaits, press OK!");
            //NExt method sets the color of the window
            UI.put("OptionPane.background",new ColorUIResource(color));
            UI.put("Panel.background",new ColorUIResource(color));
            JOptionPane.showMessageDialog(null,"YOUR BRAND NEW COLOR","Color Window", JOptionPane.INFORMATION_MESSAGE, icon);
            UI.put("OptionPane.background",new ColorUIResource(250,235,215));
            UI.put("Panel.background",new ColorUIResource(250,235,215));
            JOptionPane.showMessageDialog(null,"Check the next window for the rgb color code", "Info", JOptionPane.INFORMATION_MESSAGE,icon);
            JOptionPane.showMessageDialog(null,color);
        }
        catch(Exception e){
            JOptionPane.showMessageDialog(null, "An error has occured!", "ERROR!", JOptionPane.ERROR_MESSAGE);
        }
    }
}