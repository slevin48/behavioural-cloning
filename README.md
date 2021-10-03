# behavioural-cloning
🤖 AI cloning the behavior of a driving simulator 🚗

![test](img/behavioural-cloning.gif)

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

## Train NVIDIA Model
```
Model: "sequential_4"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_5 (Conv2D)            (None, 31, 98, 24)        1824      
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 14, 47, 36)        21636     
_________________________________________________________________
conv2d_7 (Conv2D)            (None, 5, 22, 48)         43248     
_________________________________________________________________
conv2d_8 (Conv2D)            (None, 3, 20, 64)         27712     
_________________________________________________________________
conv2d_9 (Conv2D)            (None, 1, 18, 64)         36928     
_________________________________________________________________
flatten (Flatten)            (None, 1152)              0         
_________________________________________________________________
dense (Dense)                (None, 100)               115300    
_________________________________________________________________
dense_1 (Dense)              (None, 50)                5050      
_________________________________________________________________
dense_2 (Dense)              (None, 10)                510       
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 11        
=================================================================
Total params: 252,219
Trainable params: 252,219
Non-trainable params: 0
```

## Test model

### Batch testing

Predicted angle:

![predicted](img/predicted.png)

Actual angle:

![steering](img/steering.png)


### Simulator in Autonomous mode

Need to downgrade engineio & socketio:

`pip install python-socketio==4.6.1`

`pip install python-engineio==3.13.2`

https://stackoverflow.com/questions/65636824/server-code-actively-refuses-to-connect-with-udacitys-self-driving-car-simulato


## Resources

* https://jefflirion.github.io/udacity_car_nanodegree_project03/index.html
* https://naokishibuya.medium.com/introduction-to-udacity-self-driving-car-simulator-4d78198d301d
* https://github.com/udacity/CarND-Behavioral-Cloning-P3