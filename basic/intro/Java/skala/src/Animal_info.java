import java.util.*;
public class Animal_info {
    public static void main(String[] args) {
        //dog.makeSound();
        //cat.makeSound();
        List<Animal_interface> animals = new ArrayList<>();
        animals.add(new dog("dog"));
        animals.add(new cat("cat"));
        animals.add(new tiger("tiger"));
        animals.add(new pig(("pig")));

        animals.stream()
            .forEach(Animal_interface::makeSound);
    }
}
