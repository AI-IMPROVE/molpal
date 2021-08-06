import argparse
from itertools import repeat

import utils
import curves

def cost(it: int) -> int:
    if it < 1:
        raise ValueError(f'no cost for iterations less than 1. got {it}')

    TRAIN_COST = 568
    INFERENCE_COST = 152
    return TRAIN_COST + INFERENCE_COST*it

def utility(experiment: str):
    chkpts = curves.get_checkpoints(experiment)[1:]
    Y_preds, Y_vars = curves.gather_experiment_predss(experiment)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--experiments', '--expts', nargs='+',
                        help='the top-level directory generated by the MolPAL run. I.e., the directory with the "data" and "chkpts" directories')
    parser.add_argument('-m', '--metrics', nargs='+', default=repeat('greedy'),
                        help='the respective acquisition metric used for each experiment')
    parser.add_argument('--reps', type=int, nargs='+',
                        help='the number of reps for each configuration. I.e., you passed in the arguments: --expts e1_a e1_b e1_c e2_a e2_b where there are three reps of the first configuration and two reps of the seecond. In this case, you should pass in: --reps 3 2. By default, the program assumed each experiment is a unique configuration.')
    parser.add_argument('--labels', nargs='+',
                        help='the label of each trace on the plot. Will use the metric labels if not specified. NOTE: the labels correspond the number of *different* configurations. I.e., if you pass in the args: --expts e1_a e1_b e1_c --reps 3, you only need to specify one label: --labels l1')
    parser.add_argument('--name',
                        help='the filepath to which the plot should be saved')
    


if __name__ == '__main__':
    main()