# Machine Learning: Learning from Data

[Pattern Recognition And Machine Learning - Christopher M. Bishop](http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf)

## Table of Content

* I. Introduction
* II. Mathematics
    * a. Linear Algebra
    * b. Probabilities
    * c. Optimization
* III. Dimenstionality Reduction
    * a. Principal Component Analysis
    * b. t-Distributed Stochastic Neighbour Embedding
* IV. Supervised
    * a. Linear Regression
    * b. Logistic Regression
    * c. Discriminant Analysis
    * d. Random Forest
    * e. Gradient Boosting
    * f. Support Vector Machine
* V. Unspervised
    * a. Clustering
    * b. Gaussian Mixture Models
* VI. Workshop
* VII. Assignement

---

## I. Introduction

* Introduction the Domain of Pattern Recognition
* Data-Driven Techniques
* Supervised, Unsupervised and Reinforcement Technics
* Regression, Classification and Clustering
* AI > Machine Learning > Deep Learning
* Machine Learning requires Feature Engineering

## II. Mathematics

### a. Linear Algebra

* Vectors
* Matrices
* Tensors
* Operations:
    * Addition (Scalars, Tensors), Substraction (Scalars, Tensors)
    * Multiplication (Scalars), Division (Scalars)
    * Transpose
    * Dot Product (Vectors), Cross Product (Vectors)
    * Matrix Multiplication (Tensors), Hadamard Product (Tensors)
* Transformation Matrices:
    * Scaling
    * Rotation
    * Shearing
    * Reflection
    * Translation (Affine Transformation)

[Essence of Linear Algebra preview](https://www.youtube.com/watch?v=kjBOesZCoqc)

### b. Probabilities

* Random Variable
* Distributions
* Sum Rule, Product Rule
* Expectation, Variance, Covariance
* Bayes Theorem

[Introduction to Probability](https://www.youtube.com/watch?v=SkidyDQuupA),
[Multiplication & Addition Rule](https://www.youtube.com/watch?v=94AmzeR9n2w),
[Bayes Theorem](https://www.youtube.com/watch?v=HZGCoVF3YvM)

### c. Optimization

* Derivatives, Gradient, Laplacian
* Jacobian, Hessian
* Least Squared Methods
* Gradient Descent
* Train, Test, Validation
* Cross-Validation

[Gradient](https://www.youtube.com/watch?v=tIpKfDc295M),
[Jacobian](https://www.youtube.com/watch?v=bohL918kXQk),
[Hessian](https://www.youtube.com/watch?v=LbBcuZukCAw),
[Gradient Descent](https://www.youtube.com/watch?v=sDv4f4s2SB8)

## III. Dimenstionality Reduction

* How to express High Dimensional data with Less Dimensions
* Traid of between Dimensionaly and Variation Encoding
* Embedding Visualization

### a. Principal Component Analysis

* Singular Value Decomposition
* Ordered by Variational Explanation
* Projection along Principal Components

[PCA](https://www.youtube.com/watch?v=FgakZw6K1QQ)

### b. t-Distributed Stochastic Neighbour Embedding

* Geoffrey Hinton & Laurens Van Der Mateen
* Infomation Theory (Shannon) Criteria (Close in High Dimension -> Close in Embedding)
* Minimizing Kullback-Leibler Divergence
* Stoastic/Iterative Process

[t-SNE](https://www.youtube.com/watch?v=NEaUSP4YerM)

## IV. Supervised

* Regression Analysis
* Estimate Relationship between a Dependent Variables and Multiple Independent Variables
* Regression Model is defined by:
    * Unkonw Parameters (Scalars, Vectors)
    * Independent Variables (Observed Data)
    * Dependent Variable (Observed Data)
    * Error Term (Random Statistical Noise)
    * $Y_{i} = f(X_{i}, \beta) + \epsilon_{i}$
* Often Minimized using Ordinal Least Squares Method
    * $\sum_{i}(Y_{i} - f(X_{i}, \beta))^{2}$
* Classify Data Points into Discrete Classes
* Regression can also be used for Classification

### a. Linear Regression

* Exploit Linear Dependency
    * $y = X \beta + \epsilon$
* Study Conditional Probability Distribution of the Response Given the Values of the Predictor
* Simple and Multi Linear Regression (Univariate and Multivariate)
* MAE, MSE, MPE, R² (avoid)

[Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo)

### b. Logistic Regression

* Also called Logit Model
* Binary classification
* Non Linear Regression
* Represent $log(\frac{y}{1 - y})$ as a Linear Regression Model $\sum_{k} X \beta_{k} + \epsilon$
* $log$ or Logisitic Function is also called Sigmoid $\sigma(x) = \frac{1}{1 + e^{-x}}$
* Maximum Likelihood Estimation

[logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)

### c. Discriminant Analysis

* Used for Multi Classes classification
* Less stable than Logistic Regression in Some Cases
* Bayes Theorem: $P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(B | A) P(A)}{P(B)}$
    * P(A|B): Posteriror Probability
    * P(A): Prior
    * P(B): Likelihood
* Chose Density Function and Drawn Linear Boundaries (Often Gaussian or $\beta$-Distribution)
* Using Softmax of the Discriminants for Prediction
* Implying Different Prior Constraint on the Convariance Parametric Matrices
    * Different for each Class: Quadratic
    * Diagonal: Naive Bayes

[Linear Discriminant Analysis](https://www.youtube.com/watch?v=azXCzI57Yfc)

### d. Random Forest

* Random Decision Tree
    * Splitting into Subsets
    * Splitting rules based on Classification Features (Greedy Top-Down Algorithm)
    * Recursive Process
* Random Decision Forest
    * Ensemble Classification/Regression Method
    * Training ensemble of Decision Trees
    * Aggregation when Prediction (Average, Mode, ...)
    * Random Feature Selection, Random Bagging

[Random Forest](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)

### e. Gradient Boosting

* Uses Gradient Descent and an Objective/Cost Function
* Iterative Model Building trying to Overcome Residual $F_{m + 1}(x) = F_{m}(x) + h_{m}(x) = y$
* Uses Mean Squared Error

[Gradient Boost](https://www.youtube.com/watch?v=3CC4N4z3GJc)

### f. Support Vector Machine

* Linear Setup and non-Linear Setup (Kernel Trick)
* How to Sperate the $p$ Vector Data with a $p-1$ Hyperplan ?
    * Hyperplan: $\vec{w} . \vec{x} - b = 0$
* Maximum-Margin Classifier
* Map Data Features to Higher Dimensionnal Space using Kernels to be Linearly Separable
* Hard and Soft Margins
* Grid Search Initial Parameter Selection

[Support Vector Machine](https://www.youtube.com/watch?v=efR1C6CvhmE)

## V. Unspervised

### a. Clustering

* Grouping Data with Common Features into Clusters
* Learn from the Common Features of each Clusters
* Good for Behaviours and Outliers
* k-Mean Clustering
    * Fit $k$ Centroids to Define $k$ Clusters
    * $k$ Chosen by Finding the Graph's Elbow
    * Dependent on the Prior Distance (Euclidean, Manathan, ...)
    * Iterative Mean Refinement -> Moving Centroids
    * Voronoi Partitioning

[k-Means](https://www.youtube.com/watch?v=4b5d3muPQmA)

### b. Gaussian Mixture Models

* Define $k$ Guassians
* Refine Gaussian Parameters ($\mu$ and $\sum$) using Expectation Maximization

[Gaussian Mixture Model](https://www.youtube.com/watch?v=JNlEIEwe-Cg)

---

## VI. Workshop

**Requirements**: 
* Libraries: [Python3](https://www.python.org/), [Pip3](https://pypi.org/), [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/3.1.1/index.html), [Scikit Learn](https://scikit-learn.org/stable/)
* Dataset: [Spotify Songs](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21/readme.md)

**Tasks**:
* Explore the Dataset using Pandas an Data Visualization
* Predict Song Popularity Based on the Provided Features
* Predict Song Genre Based on the Provided Features
* Embedding Visualization
* For Each Exercise Explore Multiple Approches and Compare (Model Selection)

---

## VII. Assignements

**Requirements**:
* Libraries: [Python3](https://www.python.org/), [Pip3](https://pypi.org/), [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/3.1.1/index.html), [Scikit Learn](https://scikit-learn.org/stable/)

**Objectives**:
* Find a Dataset to Explore
* Latex Report with Analysis
* Perform a Prediction
* Example: Predict the Likelihood of Winning a Round based on Current Game Stats