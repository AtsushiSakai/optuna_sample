""" 

Himmlblau Function Optimization

author: Atsushi Sakai

"""

import optuna
import numpy as np
import matplotlib.pyplot as plt


def HimmelblauFunction(x, y):
    """
    Himmelblau's function
    see Himmelblau's function - Wikipedia, the free encyclopedia 
    http://en.wikipedia.org/wiki/Himmelblau%27s_function
    """
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def objective(trial):
    x = trial.suggest_uniform('x', -5, 5)
    y = trial.suggest_uniform('y', -5, 5)
    return HimmelblauFunction(x, y)


def CreateMeshData():
    minXY = -5.0
    maxXY = 5.0
    delta = 0.1
    x = np.arange(minXY, maxXY, delta)
    y = np.arange(minXY, maxXY, delta)
    X, Y = np.meshgrid(x, y)
    Z = [HimmelblauFunction(x, y) for (x, y) in zip(X, Y)]
    return(X, Y, Z)


def main():
    print("start!!")

    # plot Himmelblau Function
    (X, Y, Z) = CreateMeshData()
    CS = plt.contour(X, Y, Z, 50)

    # optimize
    study = optuna.create_study(
        study_name="himmelblau_function_opt3",
        # storage="mysql://root@localhost/optuna"
    )

    # study = optuna.Study(
    # study_name="himmelblau_function_opt3",
    # storage="mysql://root@localhost/optuna"
    # )

    study.optimize(objective,
                   n_trials=100,
                   n_jobs=1)
    print(len(study.trials))
    print(study.best_params)

    for t in study.trials:
        plt.plot(t.params["x"], t.params["y"], "xb")

    # plot optimize result
    plt.plot(study.best_params["x"], study.best_params["y"], "xr")

    plt.show()

    print("done!!")


if __name__ == '__main__':
    main()
