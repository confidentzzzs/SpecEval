package test;
import java.util.*;

public class AddDigits {



    /**
     * Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
     *
     * @param num the number to process
     * @return the result after repeatedly adding digits until one digit remains
     */
    public int addDigits(int num) {
 
 

        // Perform the operation
        int result = num == 0 ? 0 : 1 + (num - 1) % 9;


        return result;
    }
    // Unit tests
    public static void main(String[] args) {
        AddDigits solution = new AddDigits();

        // Test cases with int values
        assert solution.addDigits(9) == 9 : "Test case 1 failed";
        assert solution.addDigits(3) == 3 : "Test case 2 failed";
        assert solution.addDigits(7) == 7 : "Test case 3 failed";
        assert solution.addDigits(123456789) == 9 : "Test case 4 failed";
        assert solution.addDigits(1111) == 4 : "Test case 5 failed";
        assert solution.addDigits(231000000) == 6 : "Test case 6 failed";
        assert solution.addDigits(231) == 6 : "Test case 7 failed";
        assert solution.addDigits(123456789) == 9 : "Test case 8 failed";
        assert solution.addDigits(111111111) == 9 : "Test case 9 failed";
        assert solution.addDigits(231000) == 6 : "Test case 10 failed";
        assert solution.addDigits(5) == 5 : "Test case 11 failed";
        assert solution.addDigits(999999999) == 9 : "Test case 12 failed";
        assert solution.addDigits(12) == 3 : "Test case 13 failed";
        assert solution.addDigits(987654321) == 9 : "Test case 14 failed";
        assert solution.addDigits(2310) == 6 : "Test case 15 failed";
        assert solution.addDigits(38) == 2 : "Test case 16 failed";
        assert solution.addDigits(4) == 4 : "Test case 17 failed";
        assert solution.addDigits(98765432) == 8 : "Test case 18 failed";
        assert solution.addDigits(6) == 6 : "Test case 19 failed";
        assert solution.addDigits(99) == 9 : "Test case 20 failed";
        assert solution.addDigits(100000000) == 1 : "Test case 21 failed";
        assert solution.addDigits(123) == 6 : "Test case 22 failed";
        assert solution.addDigits(23100000) == 6 : "Test case 23 failed";
        assert solution.addDigits(87654321) == 9 : "Test case 24 failed";
        assert solution.addDigits(123456789) == 9 : "Test case 25 failed";
        assert solution.addDigits(999999999) == 9 : "Test case 26 failed";
        assert solution.addDigits(23100) == 6 : "Test case 27 failed";
        assert solution.addDigits(18) == 9 : "Test case 28 failed";
        assert solution.addDigits(1000000000) == 1 : "Test case 29 failed";
        assert solution.addDigits(456) == 6 : "Test case 30 failed";
        assert solution.addDigits(123456789) == 9 : "Test case 31 failed";
        assert solution.addDigits(8) == 8 : "Test case 32 failed";
        assert solution.addDigits(789) == 6 : "Test case 33 failed";


    }
}

