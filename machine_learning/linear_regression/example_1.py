# general
import io

# data
import numpy as np
import pandas as pd

# machine learning
import keras

# data visualization
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns

import matplotlib.pyplot as plt

student_information_dataset = pd.read_csv('../datasets/StudentsPerformance.csv')
training_df = student_information_dataset[
    ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course', 'math score',
     'reading score', 'writing score']]

print('Read dataset completed successfully.')
print('Total number of rows: {0}\n\n'.format(len(training_df.index)))

max_reading_score = training_df['reading score'].max()
mean_reading_score = training_df['reading score'].mean()
num_unique_gender = training_df['gender'].nunique()

print('Max reading score: {0}'.format(max_reading_score))
print('mean reading score: {0}'.format(mean_reading_score))
print('Unique gender: {0}'.format(num_unique_gender))

corr_matrix = training_df.corr(numeric_only=True)

x_vars = ["reading score", "writing score"]
y_vars = ["math score", "reading score"]
fig, axes = plt.subplots(len(y_vars), len(x_vars), figsize=(12, 12))

# Her bir alt grafiği doldurun
for i, y_var in enumerate(y_vars):
    for j, x_var in enumerate(x_vars):
        axes[i, j].scatter(training_df[x_var], training_df[y_var])
        axes[i, j].set_xlabel(x_var)
        axes[i, j].set_ylabel(y_var)

# Grafik başlığını ayarlayın
fig.suptitle("Pair Plot with Matplotlib", fontsize=16)

# Grafikleri gösterin
plt.show()

