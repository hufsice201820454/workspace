interface InputDevice{
    void type();
}

public class keyboard implements InputDevice{
    @Override
    public void type() {
        System.out.println("키보드를 사용하여 입력합니다");
    }
}
