# behavioural-cloning
🤖 AI cloning the behavior of a driving simulator 🚗

## Balance data

Our data is skewed toward the middle:

![skewed](img/skewed.png)

Let's balance the data:

![balanced](img/balanced.png)

## Training & Validation Split

![split](img/split.png)

## Preprocess data

Crop the landscape and hood of the car:

![preprocess](img/preprocess.png)

Switch to YUV space:

![preprocess2](img/preprocess2.png)

Apply Gaussian Blur:

![preprocess3](img/preprocess3.png)

Resize: 

![preprocess4](img/preprocess4.png)