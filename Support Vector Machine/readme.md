# Lab 2 (Support Vector Machine)
1.
> Move the clusters around and change their sizes to make it easier or harder for the classifier to find a decent boundary. Pay attention to when the optimizer (minimize function) is not able to find a solution at all.

Answer: When the dataset is linearly separable the minimize function can find a solution, and a decision boundary is drawn. However, if the dataset is not linearly separable, then the minimize function can not find a solution and a decision boundary will not be drawn due to there does not exist a line that separetas the datasets. 

![alt-text-1](linear_lin.png "linear kernel") ![alt-text-2](nonlinear_lin.png "nonlinear kernel")

2.
> Implement the two non-linear kernels. You should be able to clas- sify very hard data sets with these.

![alt-text-3](nonlinear_pol.png "polynomial kernel") ![alt-text-4](nonlinear_RBF.png "RBF kernel")

Answer: Using the same cluster type as the non linearly separable dataset as the first figure, which the linear kernel could not find a solution to. The polynomial and radial basis function kernel solves and draws a boundary decision to.

3. 
> The non-linear kernels have parameters; explore how they influence the decision boundary. Reason about this in terms of the bias-variance trade-off.

Answer: 

![alt-text-5](p=1.png "polynomial kernel") ![alt-text-6](p=3.png "polynomial kernel")
![alt-text-7](p=7.png "polynomial kernel") ![alt-text-8](p=10.png "polynomial kernel")

![alt-text-9](sigma=1.png "RBF kernel") ![alt-text-10](sigma=3.png "RBF kernel")
![alt-text-11](p=7.png "polynomial kernel") ![alt-text-12](p=10.png "polynomial kernel")
