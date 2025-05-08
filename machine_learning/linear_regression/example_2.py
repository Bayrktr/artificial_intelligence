from machine_learning.linear_regression.lineer_regression import run_experiment
import pandas as pd

learning_rate = 0.05
epochs = 100
batch_size = 50

# Specify the feature and the label.
features = ['reading score', 'writing score']
label = 'math score'

student_information_dataset = pd.read_csv('../datasets/StudentsPerformance.csv')
training_df = student_information_dataset[
    ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score',
     'reading score', 'writing score']]

model_1 = run_experiment(training_df, features, label, learning_rate, epochs, batch_size)