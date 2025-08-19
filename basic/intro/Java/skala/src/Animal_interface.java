public abstract class Animal_interface {
    protected String name;
    public Animal_interface(String name) { this.name = name; }

    public abstract void makeSound();

    private void helperMethod() {
        System.out.println("this is private method");
    }
    private void sleep() {
        helperMethod();
        System.out.println("Sleeping...");
    }
}

