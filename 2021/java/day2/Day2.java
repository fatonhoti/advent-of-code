import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Day2 {

    public static void main(String[] args) {

        // Parse input
        List<String> instructions = read_input();
        System.out.println(instructions);

        // Part 1
        int depth = 0;
        int horizontal = 0;
        for (int i = 0; i < instructions.size(); i++) {
            String[] el = instructions.get(i).split(" ");
            String instruction = el[0];
            int magnitude = Integer.valueOf(el[1]);
            if (instruction.equals("forward")) {
                horizontal += magnitude;
            } else if (instruction.equals("down")) {
                depth += magnitude;
            } else {
                depth -= magnitude;
            }
        }
        System.out.println("Part 1: " + (depth * horizontal));

        // Part 2
        depth = 0;
        horizontal = 0;
        int aim = 0;
        for (int i = 0; i < instructions.size(); i++) {
            String[] el = instructions.get(i).split(" ");
            String instruction = el[0];
            int magnitude = Integer.valueOf(el[1]);
            if (instruction.equals("forward")) {
                horizontal += magnitude;
                depth += aim * magnitude;
            } else if (instruction.equals("down")) {
                aim += magnitude;
            } else {
                aim -= magnitude;
            }
        }
        System.out.println("Part 2: " + (depth * horizontal));
    }

    public static List<String> read_input() {
        try {
            List<String> instructions = new ArrayList<String>();
            File fileObj = new File("day2_input.txt");
            Scanner reader = new Scanner(fileObj);
            while (reader.hasNextLine()) {
                instructions.add(reader.nextLine().strip());
            }
            reader.close();
            return instructions;
        } catch (FileNotFoundException e) {
            System.out.println("An error occured.");
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

}