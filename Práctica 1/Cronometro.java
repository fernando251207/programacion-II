import java.time.LocalTime;
import java.time.temporal.ChronoUnit;

public class Cronometro {
    private LocalTime inicia;
    private LocalTime finaliza;

    public Cronometro() {
        inicia = LocalTime.now();
    }

    public LocalTime getInicia() {
        return inicia;
    }

    public LocalTime getFinaliza() {
        return finaliza;
    }

    public void iniciar() {
        inicia = LocalTime.now();
    }

    public void detener() {
        finaliza = LocalTime.now();
    }

    public long lapsoDeTiempo() {
        if (finaliza == null) return 0;
        return ChronoUnit.MILLIS.between(inicia, finaliza);
    }
        public static void main(String[] args) {
        Cronometro crono = new Cronometro();
        System.out.println("Cronómetro iniciado...");
        try {
            Thread.sleep(1500);
        } catch (InterruptedException e) {}
        crono.detener();
        System.out.println("Tiempo transcurrido: " + crono.lapsoDeTiempo() + " milisegundos");
    }
}