public class BasicCalculator extends AbCalculator {
    public BasicCalculator(int firstNumber, String operator, int secondNumber) {
        super(firstNumber, operator, secondNumber); 
    }

    @Override
    protected String calculate(int firstNumber, String operator, int secondNumber) {
        int result = switch (operator) {
            case "+" -> firstNumber + secondNumber;
            case "-" -> firstNumber - secondNumber;
            case "*" -> firstNumber * secondNumber;
            case "/" -> {
                if (secondNumber == 0) throw new ArithmeticException("0으로 나눌 수 없습니다.");
                yield firstNumber / secondNumber;
            }
            default -> throw new IllegalArgumentException("지원하지 않는 연산자: " + operator); 
        };
        String rec = firstNumber + " " + operator + " " + secondNumber + " = " + result;
        System.out.println("결과: " + result);
        return rec;
    }
}
