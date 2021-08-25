package Java.good.Break;

public class Break {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, };
        for(int i : numbers) {
            for(int x : numbers) {
                System.out.println(x + "good");
                break;
            }
            System.out.println(i);
        }
    }
}
