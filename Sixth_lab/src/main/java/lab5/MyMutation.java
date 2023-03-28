package lab5;

import org.uncommons.watchmaker.framework.EvolutionaryOperator;

import java.util.List;
import java.util.Random;

public class MyMutation implements EvolutionaryOperator<double[]> {
    public List<double[]> apply(List<double[]> population, Random random) {

        double mutationPercent = 0.035;
        int dimension = population.get(0).length;
        boolean[] flag = new boolean[population.size()];
        int index = random.nextInt(population.size());
        flag[index] = true;

        // initial population
        for (int i=0;i < population.size();i++) {

            if (random.nextDouble() < mutationPercent) {

                while(flag[index] != false) {
                    index = random.nextInt(population.size());
                }
                flag[index] = true;
                double[] element = new double[dimension];

                for (int j=0; j<dimension; j++) {
                    element[j] = random.nextDouble() * 10- 5;
                }

                population.set(index, element);
            }
        }

        return population;
    }
}
