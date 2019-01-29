""" 


author: Atsushi Sakai

"""

import optuna


def objective(trial):
    x = trial.suggest_uniform('x', -10, 10)
    return (x - 2)**2


def main():
    print("start!!")

    study = optuna.create_study()
    study.optimize(objective, n_trials=100)
    print(study.best_params)
    print(study.best_value)
    print(study.best_trial)

    print("done!!")


if __name__ == '__main__':
    main()
