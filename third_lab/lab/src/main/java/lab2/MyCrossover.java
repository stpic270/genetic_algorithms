package lab2;

import org.uncommons.watchmaker.framework.operators.AbstractCrossover;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MyCrossover extends AbstractCrossover<double[]> {
    protected MyCrossover() {
        super(1);
    }

    protected List<double[]> mate(double[] p1, double[] p2, int i, Random random) {
        List<double[]> children = new ArrayList<double[]>();
        // your implementation:
        int dimension = p1.length;
        int part = dimension / 2;

        double[] gen1 = p1.clone();
        double[] gen2 = p2.clone();

        double  l = 4;
        l = random.nextDouble();
        for (int j=0;j<p1.length;j++) {

            if (random.nextBoolean()) {
                gen1[j] = l * p1[j] + (1 - l) * p2[j];
                gen2[j] = l * p2[j] + (1 - l) * p1[j];
            }
            else {

                gen1[j] = p1[j];
                gen2[j] = p2[j];
            }
            gen1[j] = Math.min(Math.max(gen1[j], -5), 5);
            gen2[j] = Math.min(Math.max(gen2[j], -5), 5);
        }

        children.add(gen1);
        children.add(gen2);
        return children;
    }
}
