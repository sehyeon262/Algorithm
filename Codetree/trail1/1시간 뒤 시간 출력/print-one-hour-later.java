import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] strArr = s.split(":");
        System.out.println(Integer.parseInt(strArr[0]) + 1 + ":" + strArr[1]);
    }
}