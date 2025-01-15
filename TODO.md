# Pruning the solution space
maybe it's hard to implement these, but let's consider them at some point
- `div` should not be able to divide a value by itself, since it just becomes a 1 and we already have it in the constants
- try allowing for only sinusoids and paraboloids to reduce overfitting
- try implementing fitness holes, but try not to increase computation time

# Known Bugs
Generando un albero di altezza 1 con operazione unaria (quindi una sola radice accompagnata da una sola foglia) tipo `cos` o `sqrt` esce `UserWarning: Drawing not available (`np.alltrue` was removed in the NumPy 2.0 release. Use `np.all` instead.)`, e la foglia viene disegnata a fanculo giu senza linea a collegarle radice e foglia

# Hyperparams/Configurations to try
- Mutations
    - Try all the mutations, one by one, and see which ones work best
    - Then see if it's worth trying more of them at random (e.g. 50% of times you use point_mutation, the other you use hoist_mutation)
- Hyperparameters
    - ...