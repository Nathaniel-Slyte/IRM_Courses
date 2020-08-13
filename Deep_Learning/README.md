# Deep Learning: a Modern Approach to Artificial Intelligence

[Deep Learning - Ian Goodfellow and Yoshua Bengio and Aaron Courville](https://www.deeplearningbook.org/)
[Dive into Deep Learning - Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola](https://d2l.ai/index.html)

## Table of Content

* I. Introduction
    * 1. History
    * 2. Automatic Differentiation
* II. Basic Components
    * 1. Perceptron
    * 2. MultiLayer Perceptron
    * 3. Convolution and Pooling
    * 4. Recurrent Neural Network
    * 5. Underfitting and Overfitting
    * 6. Regularization
* III. Simple Architectures
    * 1. CNN Architectures
    * 2. Gated Recurrent Neural Networks
    * 3. Bidirectional Recurrent Neural Networks
    * 4. Auto-Encoders
    * 5. Sequence to Sequence
    * 6. Attention Mechanism 
* IV. Complex Systems
    * 1. Computer Vision
        * a. Augmentation
        * b. Fine-Tuning
        * c. Object and Box Detection
        * d. Sementic Segmentation
        * e. Style Transfer
        * f. Triplet Loss
        * h. Generative Networks
    * 2. Natural Language Processing
        * a. Word Embeddings
        * b. BERT Family
    * 3. Reinforcement Learning
        * a. Q Learning
        * b. Deep Q Learning
* V. Workshop
* VI. Assignement

---

## I. Introduction

### 1. History

![Deep Learning Time Line](https://cdn-images-1.medium.com/max/2000/1*Z_DnCyKt18RM0aCCrFzaIQ.png)

* [Yoshua Bengio TEDx Talk](https://www.youtube.com/watch?v=uawLjkSI7Mo)
* [Quand la machine apprend: La révolution des neurones artificiels et de l'apprentissage profond - Yann Le Cun](https://www.amazon.fr/Quand-machine-apprend-artificiels-lapprentissage/dp/2738149316)
* [The Male Only History of Deep Learning - Yannic Kilcher](https://www.youtube.com/watch?v=yPjuAo53uNI)

### 2. Automatic Differentiation

- Chain Rule
- Computation Graph
- Auto Grad Library
- Practice with Pytorch

* [Livecoding an AutoGrad Library - Joel Gruss](https://www.youtube.com/watch?v=RxmBukb-Om4)
* [PyTorch Autograd Explained - In-depth Tutorial - Elliot Waite](https://www.youtube.com/watch?v=MswxJw-8PvE)
* [Pytorch](https://pytorch.org/)

## II. Basic Concepts

### 1. Perceptron

![Perceptron](https://miro.medium.com/max/645/0*LJBO8UbtzK_SKMog)

- Linear Classifier with Activation Function
- Threshold, Tanh, Sigmoid, ...
- Linearly Separable
- Fails at XOR


### 2. MultiLayer Perceptron

![MultiLayer Perceptron](https://www.allaboutcircuits.com/uploads/articles/an-introduction-to-training-theory-for-neural-networks_rk_aac_image2.jpg)

- MultiLayer Perceptron
- Universal Approximators
- Fold The Space by Applying Linear Transformation and Non-Linear Activation
- Activation Functions: Tanh, Sigmoid, ReLU, LeakyReLU, pReLU, Mish, Swish

### 3. Convolution and Pooling

![Convolution](https://miro.medium.com/max/790/1*1okwhewf5KCtIPaFib4XaA.gif)
![Feature Maps](https://miro.medium.com/max/4426/1*_uk1cKXslKo1gDHOWzljXA.png)
![Pooling](https://media.giphy.com/media/jnbNCPUT0w161qn0hb/giphy.gif)

- Kernel Filter
- Feature Maps
- Pooling Layers
- Low Level and Hight Level Filters

### 4. Recurrent Neural Network

![Recurrent Neural Net](https://miro.medium.com/max/1000/1*JhL58UYgnMXeXBkLhjPFQg.png)
![RNN Configs](https://gblobscdn.gitbook.com/assets%2F-LIA3amopGH9NC6Rf0mA%2F-M4bJ-IWAKzglR0XHFwU%2F-M4bJ3Kh_oCL1b6-9iX9%2Fsequence.png?alt=media)

- Recurrent Neural Network
- Shared Weights but Backprop Through Time
- Sequence Input
- One To Many, Many to One, Many to Many

### 5. Underfitting and Overfitting

![Overfitting](https://i.pinimg.com/originals/72/e2/22/72e222c1542539754df1d914cb671bd7.png)

### 6. Regularization

![Dropout](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2018/04/1IrdJ5PghD9YoOyVAQ73MJw.gif)

- L1/L2 Regularization
- Penalize Weight Cost
- Dropout
- Normalization (Batch, ...)


## III. Advanced Concepts

### 1. CNN Architectures

![TimeLine](https://miro.medium.com/max/1000/1*dc07I4_N_IWDJVb6cM-KsQ.png)
![Benchmark](https://miro.medium.com/max/700/1*IPBwL5yb04_hc_zX08C-Rg.png)

### 2. Gated Recurrent Neural Networks

![Gated RNN](https://penseeartificielle.fr/wp-content/uploads/2019/10/lstm-vs-gru.png)

### 3. Bidirectional Recurrent Neural Networks

![BRNN](https://miro.medium.com/max/764/1*6QnPUSv_t9BY9Fv8_aLb-Q.png)

- Bidrectional for Forward and Backward Correlations
- Great for Encoding Not for Generation (you do not have access to future)

#### 4. Auto-Encoders

![AutoEncoder](https://miro.medium.com/max/600/1*nqzWupxC60iAH2dYrFT78Q.png)

- Encoder to Encode Input Space into A Latent Space (Dimensionality Reduction)
- Decoder to Decoder Latent Space into Output Space
- Latent Space is like mp3 for Audio
- Latent Space Interpolation

### 5. Sequence to Sequence

![Seq2Seq](https://miro.medium.com/max/1598/1*x4wsJobiSC7zlTkP8yv40A.png)

### 6. Attention Mechanism

![Attention Mechanism](https://miro.medium.com/max/1200/1*1V221DO9QIafh4htkwVBYw.jpeg)
![CNN Attention](https://weave.eu/app/uploads/2018/01/captioning_and_attention.png)

## IV. Research and Applications

### 1. Computer Vision

#### a. Augmentation

![Img Aug](https://miro.medium.com/max/3564/1*bqNylp7FcqIBWg0DrcimUw.png)
![Spec Aug](https://neurohive.io/wp-content/uploads/2019/04/Snimok-ekrana-2019-04-23-v-14.01.33-min-e1556019107842-1.png)

#### b. Fine-Tuning

![FineTuning](https://d2l.ai/_images/finetune.svg)

#### c. Object and Box Detection

![Yolov4](https://blog.roboflow.ai/content/images/2020/06/yolov4-results.png)
![Box Detection](https://pic1.zhimg.com/v2-41541d68d0d43b598f63170666d100cc_b.gif)

#### d. Sementic Segmentation

![Sementic Segmentation](https://thumbs.gfycat.com/DimSarcasticCockerspaniel-size_restricted.gif)

#### e. Style Transfer

![Style Transfer](https://user-images.githubusercontent.com/37034031/42068549-97588fc0-7b87-11e8-8110-93796a42a293.png)

- Gram Matrix
- Iterative vs Real Time

#### f. Triplet Loss

![Triplet Loss](https://www.researchgate.net/profile/Jie_Liu190/publication/320885314/figure/fig3/AS:557870018199552@1510017985050/Triplet-Loss-Learning-Process.png)

#### h. Generative Networks

![GAN GIF](https://www.smalltechnews.com/wp-content/uploads/2019/12/frc-581faea96a1dc9364bb3601f874b0912.gif)
![GAN](https://www.mdpi.com/remotesensing/remotesensing-12-01149/article_deploy/html/images/remotesensing-12-01149-g001.png)

- VAE / cVAE
- GAN / cGAN
- WGAN / WGAN-GP

### 2. Natural Language Processing

#### a. Word Embeddings

![Word Embedding](https://miro.medium.com/max/2456/1*gcC7b_v7OKWutYN1NAHyMQ.png)

#### b. BERT Family

![BERT TimeLine](https://miro.medium.com/max/3900/1*ff_bprXLuTueAx7-5-MHew.png)
![Transformer](https://jalammar.github.io/images/t/transformer_decoding_2.gif)
![Self Attention](https://miro.medium.com/max/1084/1*4q2LVXBfVKUZ3cn2y10U7w.png)
![Transformer Architecture](https://miro.medium.com/max/1000/1*o0pS0LbXVw7i41vSISrw1A.png)

#### 3. Reinforcement Learning

#### a. Q Learning

![Q Learning](https://www.mlq.ai/content/images/2020/04/q-tables.gif)
![Bellman Equation](https://image.slidesharecdn.com/ai-bellmanintro-170909235039/95/ai-introduction-to-bellman-equations-6-638.jpg?cb=1505001199)

#### b. Deep Q Learning

![Deep Q learning](https://lh3.googleusercontent.com/KhHK28tjPj70KrRIsjmYgtOnyRPcrFjuxSXRlCzmi5Wv-7DWSssD3VSJ_FNHWVnq5LfywwMCQa7M7mGC-An6793gluSK6AsNwDpd=w1440)

## V. Workshop

## VI. Assignement


---

## . Workshop

**Requirements**:

**Tasks**:

---

## . Assignements

**Requirements**:

**Objectives**: