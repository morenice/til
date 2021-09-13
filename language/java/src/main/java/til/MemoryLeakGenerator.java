package til;

import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

import java.io.File;
import java.io.FileNotFoundException;

import til.common.*;

public class MemoryLeakGenerator {
    public static List<Double> list = new ArrayList<>();

    /**
     * Unclose stream file or network
     * @throws FileNotFoundException
     */
    public static void makeLeak1() {        
        for (int i = 0; i < 100000; i++) {
            try {
                Scanner scanner = new Scanner(new File("README.md"));
            } catch (FileNotFoundException e) {
                // TODO Auto-generated catch block
                // e.printStackTrace();
            }
        }

        System.gc();
        System.out.println("Waiting...");            

        try {
            Thread.sleep(30_000);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    
    /**
     * make leak with static variable
     * @param loopCount
     */
    public static void makeLeak2() {    
        for (int i = 0; i < 10000000; i++) {
            list.add(Math.random());
        }            
        System.gc();    
        System.gc();

        System.out.println("Waiting...");    

        try {               
            Thread.sleep(30_000);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }        
    }

    
    /**
     * Improper equals() and hashCode() Implementations
     */
    public static void makeLeak3() {    
        Map<Person, Integer> map = new HashMap<>();
        // Map<Person2, Integer> map = new HashMap<>();
        for(int i=0; i<10000000; i++) {
            map.put(new Person("jon"), 1);
            // map.put(new Person2("jon"), 1);
        }
        System.out.println(map.size());

        System.gc();

        System.out.println("Waiting...");

        try {               
            Thread.sleep(30_000);
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } 
    }
}