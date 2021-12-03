import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Day3 {

    public static void main(String[] args) {

        // Parse input
        List<String> binaryNumbers = read_input();

        // Extract the column bits
        List<List<Character>> columnBits = new ArrayList<List<Character>>();
        for (int i = 0; i < binaryNumbers.get(0).length(); i++) {
            columnBits.add(i, extract_column(binaryNumbers, i));
        }

        // Part 1
        String gamma = "";
        String epsilon = "";
        for (List<Character> column : columnBits) {
            int zeroes = count(column, '0');
            int ones = count(column, '1');
            String mc = zeroes >= ones ? "10" : "01";
            gamma += mc.charAt(0);
            epsilon += mc.charAt(1);
        }
        System.out.println("Part 1: " + (Integer.parseInt(gamma, 2) * Integer.parseInt(epsilon, 2)));

        // Part 2
        int ogr = calc_rating(binaryNumbers, "OGR");
        int cosr = calc_rating(binaryNumbers, "COSR");
        System.out.println("Part 2: " + (ogr * cosr));

    }

    public static int calc_rating(List<String> binaryNumbers, String typeOfRating) {
        int bit = 0;
        List<String> picked = binaryNumbers;
        while (picked.size() > 1) {
            List<Character> bits = extract_column(picked, bit);
            int zeroes = count(bits, '0');
            int ones = count(bits, '1');
            int mc = typeOfRating.equals("OGR") ? ones >= zeroes ? 1 : 0 : ones >= zeroes ? 0 : 1;
            int bit_ = bit;
            picked = picked.stream().filter(bin_num -> bin_num.charAt(bit_) == (char) (mc + '0'))
                    .collect(Collectors.toList());
            bit++;
        }
        return Integer.parseInt(picked.get(0), 2);
    }

    public static int count(List<Character> li, Character k) {
        int i = 0;
        for (Character bit : li) {
            if (bit.equals(k))
                i++;
        }
        return i;
    }

    public static List<Character> extract_column(List<String> li, int column) {
        List<Character> col = new ArrayList<Character>();
        for (String bin_num : li) {
            col.add(bin_num.charAt(column));
        }
        return col;
    }

    public static List<String> read_input() {
        try {
            List<String> instructions = new ArrayList<String>();
            File fileObj = new File("day3_input.txt");
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