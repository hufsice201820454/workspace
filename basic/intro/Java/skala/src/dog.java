public class dog extends Animal_interface{
    public dog(String name){
        super(name);
    }

    @Override
    public void makeSound(){
        System.out.println("meow");
    }
}
