Part 1
The first task is to collect data that can be used to train the model. Collect a single sample per
action containing, in order, the 5 distance sensor readings, the action, and whether or not a
collision occurred (0: no collision, 1: collision). This data should be saved as a .csv file with 7
untitled columns. For grading purposes, submit your ‘submission.csv’ containing 100 data
samples. For training in the future parts, you will need to collect much more than this.
Files to edit:
collect_data.py
The robot should wander around with no regard for its environment or avoiding collisions.

Part 2
Now that you have collected your training data, you can package it into an iterable PyTorch
DataLoader for ease of use. You may be required to prune your collected data to balance out
their distribution. If your dataset is 99% 0s and 1% 1s, a model that outputs only 0 would
achieve good loss, but it would not have learned anything useful. Make sure to create both a
training and testing DataLoader. Use training_data.csv collected from the previous part. Make
sure to use the PyTorch classes mentioned in the comments of Data_Loaders.py.
Files to edit:
Data_Loaders.py
saved/training_data.csv,

Part 3
For Part 3, you will be designing your own custom neural network using PyTorch’s torch.nn
class. You will need to initialize a custom architecture, define a forward pass through the
network, and build a method for evaluating the fit of a given model.
Files to edit:
Data_Loaders.py
Networks.py
saved/*

Part 4
In Part 4, you must train a model using your custom network architecture, which accurately
predicts collisions given sensor and action information. Your grade will depend on the accuracy
of the model. You may need to try many different strategies and architectures to achieve a well
fit model. Keep track of your training and testing loss throughout the epochs, and generate a
plot with these lines at the end. To see an application demo of the learning your robot has done,
run goal_seeking.py, which will have the robot seek out goals while only taking possible actions
it deems to be safe.
Files to edit:
Data_Loaders.py
Networks.py
train_model.py
saved/*
