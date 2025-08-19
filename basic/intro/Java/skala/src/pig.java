public class pig extends Animal_interface{
    public pig(String name){
        super(name);
    }
    @Override
    public void makeSound(){
        System.out.println("qquak");
    }
}
