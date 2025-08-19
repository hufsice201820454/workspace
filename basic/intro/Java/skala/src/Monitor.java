interface Display{
    void type();

}

public class Monitor implements Display{
    @Override
    public void type() {
        System.out.println("모니터에 화면을 입력합니다");
    }
}
