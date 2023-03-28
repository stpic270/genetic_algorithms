package lab5;

import org.uncommons.watchmaker.framework.factories.AbstractCandidateFactory;

import java.util.Random;

public class MyFactory extends AbstractCandidateFactory<double[]> {

    private int dimension;

    public MyFactory(int dimension) {
        this.dimension = dimension;
    }

    public double[] generateRandomCandidate(Random random) {

        double[] solution = new double[dimension];
        for (int i=0;i<dimension;i++) {
            solution[i] = Math.random() * 10 - 5;
        }

        return solution;
    }
}

