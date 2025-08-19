import java.util.Scanner;

public abstract class AbCalculator {
    protected String[] history = new String[100];
    protected int historyCount = 0;
    protected boolean status = true;

    protected int firstNumber;
    protected int secondNumber;
    protected String operator;

    protected AbCalculator(int firstNumber, String operator, int secondNumber) {
        this.firstNumber = firstNumber;
        this.operator = operator;
        this.secondNumber = secondNumber;
    }

    public void run(Scanner sc) {
        while (status) {
            String record = calculate(firstNumber, operator, secondNumber);
            if (historyCount < history.length) history[historyCount++] = record;

            System.out.print("계속(c) / 종료(q): ");
            String cmd = sc.nextLine();
            if ("q".equals(cmd)) {
                status = false;
                printHistory();
            } else if("c".equals(cmd)){
                // 다음 입력을 이어서 받도록 설계
                System.out.print("첫번째 숫자: ");
                firstNumber = sc.nextInt(); sc.nextLine();

                System.out.print("연산자(+ - * /) 입력: ");
                operator = sc.nextLine();

                System.out.print("두번째 숫자: ");
                secondNumber = sc.nextInt(); sc.nextLine();
            } else {
                System.out.print("Error");
                break;
            }
        }
    }

    protected void printHistory() {
        System.out.println("=== 계산 기록 ===");
        for (int i = 0; i < historyCount; i++) System.out.println(history[i]);
    }

    protected abstract String calculate(int firstNumber, String operator, int secondNumber);
}
