import java.util.*;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean status = true;
        String[] history = new String[100];
        int index = 0;
        while(status == true){
            String S = "";
            System.out.print("첫번째 숫자: ");
            int num1 = sc.nextInt();
            sc.nextLine(); 
            
            S += Integer.toString(num1);
            System.out.print("연산자(+ - * /) 입력: ");
            String operation = sc.nextLine();
            S += operation;
            System.out.print("두번째 숫자: ");
            int num2 = sc.nextInt();
            S += Integer.toString(num2);
            sc.nextLine();  // ⭐ 여기 추가해서 버퍼 비우기

            int result = switch (operation) {
                case "+" -> {
                    yield num1 + num2;
                }
                case "-" -> {
                    yield num1 - num2;
                }
                case "*" -> {
                    yield num1 * num2;
                }
                case "/" -> {
                    if (num2 == 0) {
                        try{
                            throw new ArithmeticException("0으로 나눌 수 없습니다.");
                        }catch (ArithmeticException e){
                            System.out.println(e.getMessage());
                            e.printStackTrace();
                        }
                        yield 0;
                    } else {
                        yield num1 / num2;
                    }
                }
                default -> {
                    System.out.println("지원하지 않는 연산자입니다.");
                    yield 0;
                }
            };
            S += " = ";
            S += Integer.toString(result);
            System.out.println("결과: " + result);
            history[index] = S;
            index += 1;
            System.out.print("계속 하려면 c(continue) / 종료하려면 q(quit) 입력 : ");

            String command = sc.nextLine();
            if (command.equals("q")){
                status = false;
                System.out.println("=== 계산 기록 ===");
                for(String his : history){
                    if(his == null){
                        break;
                    }
                    System.out.println(his);
                }
            }
        }
        
        sc.close();
    }
}

