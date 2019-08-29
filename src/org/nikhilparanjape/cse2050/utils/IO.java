package org.nikhilparanjape.cse2050.utils;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Scanner;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
/**
 * Use as a windowed Input/Output file chooser
 * 
 * Use by initializing in different classes such as IO.saveFile(save);
 * or String file = IO.openFile();
 * 
 * @author Nikhil Paranjape (indianpoptart)
 * @version April 5 2013 - v3.1.1
 * 
 * USE WITH COPYRIGHTS, nah you can use it, but my name should be in it (GPL3)
 */
public class IO {
    public static void saveFile(String message){
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JFileChooser fc = new JFileChooser();
        fc.setDialogTitle("Choose the directory to save your binary text file ");
        fc.setFileSelectionMode(JFileChooser.FILES_ONLY);
        if(fc.showSaveDialog(frame) != JFileChooser.CANCEL_OPTION){
            File f = fc.getSelectedFile();
            try{
                BufferedWriter output = new BufferedWriter(new FileWriter(f.getAbsolutePath() + ".txt"));
                output.write(message);
                output.close();
            }
            catch(Exception e){
                JOptionPane.showMessageDialog(null, "Error saving file");
            }
        }
        frame.dispose();
    }

    public static String openFile(){
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JFileChooser fc = new JFileChooser();
        fc.setDialogTitle("Choose the binary text file");
        fc.setFileSelectionMode(JFileChooser.FILES_ONLY);
        if(fc.showOpenDialog(frame) != JFileChooser.CANCEL_OPTION){
            File f = fc.getSelectedFile();
            try{
                Scanner scan = new Scanner(new BufferedReader(new FileReader(f.getAbsolutePath())));
                StringBuilder text = new StringBuilder();
                while(scan.hasNextLine()) {
                    text.append(scan.nextLine()).append("\n");
                }
                frame.dispose();
                return text.toString();
            }
            catch(Exception e){
                JOptionPane.showMessageDialog(null, "Error opening file");
            }
        }
        frame.dispose();
        return null;
    }
}