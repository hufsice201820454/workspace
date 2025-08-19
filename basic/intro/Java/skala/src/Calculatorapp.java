import java.util.Scanner;
public class Calculatorapp {
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        
        int first_num = sc.nextInt(); sc.nextLine();
        String oper = sc.nextLine();
        int second_num = sc.nextInt(); sc.nextLine();
        BasicCalculator calc = new BasicCalculator(first_num, oper, second_num);
        calc.run(sc);

        sc.close();
    }
}
