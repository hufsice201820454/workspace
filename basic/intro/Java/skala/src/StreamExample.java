import java.util.*;

public class StreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>(List.of(1, 2, 3, 4, 5));

        numbers.stream()
               .map(n -> n * n)
               .filter(n -> n > 5)
               .forEach(System.out::println);

        System.out.println("");

        for (int i = 0; i < numbers.size(); i++) {
            numbers.set(i, numbers.get(i) * numbers.get(i)); 
            if (numbers.get(i) > 5) {
                System.out.println(numbers.get(i));
            }
        }
    }
}


