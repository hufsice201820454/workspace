interface InputDevice {
    void type();

}

interface Display{
    void type();

}

public class computer {
    private final InputDevice inputdeivce;
    private final Display display;

    public computer(InputDevice inputdeivce, Display display){
        this.inputdeivce = inputdeivce;
        this.display = display;
    }

    public void operate(){
        inputdeivce.type();
        display.type();
    }
}
