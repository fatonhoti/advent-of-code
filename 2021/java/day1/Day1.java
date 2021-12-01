import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Day1 {

    public static void main(String[] args) {

        // Parse input
        List<Integer> input = read_input().stream()
                .map((String num) -> Integer.valueOf(num))
                .collect(Collectors.toList());

        // Part 1
        int ctr = 0;
        for (int i = 1; i < input.size(); i++) {
            if (input.get(i) > input.get(i - 1))
                ctr += 1;
        }
        System.out.println("Part 1: " + Integer.toString(ctr));

        // Part 2
        ctr = 0;
        int lo = 0;
        int hi = 3;
        while (hi < input.size()) {
            int pre = input.subList(lo, hi).stream().mapToInt(Integer::intValue).sum();
            int next = input.subList(++lo, ++hi).stream().mapToInt(Integer::intValue).sum();
            if (next > pre)
                ctr += 1;
        }
        System.out.println("Part 2: " + Integer.toString(ctr));
    }

    public static List<String> read_input() {
        try {
            StringBuilder builder = new StringBuilder();
            File fileObj = new File("day1_input.txt");
            Scanner reader = new Scanner(fileObj);
            while (reader.hasNextLine()) {
                builder.append(reader.nextLine() + " ");
            }
            reader.close();
            return Arrays.asList(builder.toString().split(" "));
        } catch (FileNotFoundException e) {
            System.out.println("An error occured.");
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

}