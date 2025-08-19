public class cat extends Animal_interface{
    public cat(String name){
        super(name);
    }
    @Override
    public void makeSound(){
        System.out.println("bow");
    }
}
