# Lab 3 

1.
> Write a function, mlParams(X,labels), that computes the ML- estimates of μk and Σk for the different classes in the dataset. X here is a set of row vectors, and labels are the class labels for each of the data points (again, ignore the W argument for now). The function should return a C × d-array mu that contains the class means, a C × d × d-array sigma that contains the class covariances. The covariance should be implemented using your own code and not by applying a library function.

Use the provided function, genBlobs(), that returns Gaussian distributed data points together with class labels, to generate some test data. Compute the ML-estimates for the data and plot the 95%-confidence interval using the function plotGaussians.

Answer:
```python
    # Iterate over both index and value
    for jdx, classes in enumerate(classes):
        idx = labels == classes # Returns a true or false with the length of y
        # Or more compactly extract the indices for which y==class is true,
        # analogous to MATLAB’s find
        idx = np.where(labels == classes)[0]

        xlc = X[idx,:] # Get the x for the class labels. Vectors are rows.
        """
        xlc contains the vectors for each indivual class which is looped through
        hence the mean vector is obtain through sum_i xlc_i/N for each class. axis = 0
        takes the mean of each column.
        """
        mu[jdx] += np.mean(xlc, axis = 0) 
        """
        Assuming the first column is the x-values and the second column is the
        y-values.
        """
        for i in range(2): 
            temp = []
            for rows in range(0,xlc.shape[0]):
                temp.append(pow(xlc[rows][i]-mu[jdx][i],2))
            sigma[jdx][i][i] = np.mean(temp)
```

<p>
    <img src="a1.png" width="400" />
    <em>Plot for 95%-confidence interval.</em>

</p>

2. 

> a) Write a function computePrior(labels) that estimates and returns the class prior in X (ignore the W argument).

Answer:
```python
    # Iterate over both index and value
    for jdx,classes in enumerate(classes):
        idx = labels == classes # Returns a true or false with the length of y
        # Or more compactly extract the indices for which y==class is true,
        # analogous to MATLAB’s find
        idx = np.where(labels==classes)[0]
        prior[jdx] = len(idx)/len(labels)
```
> b) Write a function classifyBayes(X,prior,mu,sigma) that computes the dis- criminant function values for all classes and data points, and classifies each point to belong to the max discriminant value. The function should return a length N vector containing the predicted class value for each point.
```python

# For each class 
for classes in range (0,Nclasses):
    # np.log is ln, whereas np.log10 is your standard base 10 log. - Stack Overflow
    ln_sigma = -0.5 * np.log(np.linalg.det(sigma[classes]))
    ln_class_prior = np.log(prior[classes])
    sub_mean = X - mu[classes] 
    # For each data point logProb = np.zeros((Nclasses, Npts))
    for data_points in range(0,Npts):
        # In reference to logProb = np.zeros((Nclasses, Npts))
        # Note that sigma only has values on the diagonal
        logProb[classes][data_points] = ln_sigma
        - 0.5 * np.inner(sub_mean[data_points]/np.diag(sigma[classes]), sub_mean[data_points])
        + ln_class_prior

```













```python



```




