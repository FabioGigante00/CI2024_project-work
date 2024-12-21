# Pruning the solution space
maybe it's hard to implement these, but let's consider them at some point
- `div` should not be able to divide a value by itself, since it just becomes a 1 and we already have it in the constants
- try allowing for only sinusoids and paraboloids to reduce overfitting

# Known Bugs
Generando un albero di altezza 1 con operazione unaria (quindi una sola radice accompagnata da una sola foglia) tipo `cos` o `sqrt` esce `UserWarning: Drawing not available (`np.alltrue` was removed in the NumPy 2.0 release. Use `np.all` instead.)`, e la foglia viene disegnata a fanculo giu senza linea a collegarle radice e foglia