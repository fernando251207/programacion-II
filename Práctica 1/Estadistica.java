import java.util.Scanner;

public class Estadistica {
    private double[] datos;

    public Estadistica(double[] datos) {
        this.datos = datos;
    }

    public double promedio() {
        double suma = 0;
        for (double v : datos) suma += v;
        return suma / datos.length;
    }

    public double desviacion() {
        if (datos.length <= 1) return 0;
        double prom = promedio();
        double sumaCuad = 0;
        for (double v : datos) {
            sumaCuad += Math.pow(v - prom, 2);
        }
        return Math.sqrt(sumaCuad / (datos.length - 1));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] nums = new double[10];
        System.out.println("Ingrese 10 números:");
        for (int i = 0; i < 10; i++) {
            nums[i] = sc.nextDouble();
        }

        Estadistica est = new Estadistica(nums);
        System.out.printf("El promedio es %.2f%n", est.promedio());
        System.out.printf("La desviación estándar es %.6f%n", est.desviacion());
        sc.close();
    }
}