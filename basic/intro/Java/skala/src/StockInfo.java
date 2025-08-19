public class StockInfo {
    public static void main(String[] args) throws Exception {
        //PreferredStock ps = new PreferredStock("삼성", 70000, 10);
        PreferredStock ps = new PreferredStock("삼성", 70000, 10);
        Stock ps2 = new Stock("한화오션", 62000);
        ps.printInfo();

        ps2.printInfo();
    }
}
