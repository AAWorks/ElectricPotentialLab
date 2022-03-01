import pandas as pd
import numpy as np

# Get the data 
data = pd.read_csv('e_field.csv')
 
# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# Transform the spreadsheet rows and columns into centimeters
df['X']=pd.Categorical(df['X'])

df['X']=df['X'].cat.codes*2 +1

df['Y']=pd.Categorical(df['Y'])

df['Y']=df['Y'].cat.codes*2 +1

Z = df.pivot_table(index='X', columns='Y', values='Z').T.values

X_unique = np.sort(df.X.unique())
Y_unique = np.sort(df.Y.unique())
X, Y = np.meshgrid(X_unique, Y_unique)

import matplotlib.pyplot as plt
try:
    get_ipython().magic("matplotlib inline")
    get_ipython().magic("config InlineBackend.figure_formats = ['svg']")
except:
    plt.ion()

from matplotlib import rcParams

# Initialize plot objects
rcParams['figure.figsize'] = 5, 5 # sets plot size
fig = plt.figure()
ax = fig.add_subplot(111)

# Generate a contour plot
cp = ax.contour(X, Y, Z)

#----------------------------------------------------------------
# Initialize plot objects
rcParams['figure.figsize'] = 5, 5 # sets plot size
fig = plt.figure()
ax = fig.add_subplot(111)

# Define levels in z-axis where we want lines to appear
levels = np.array([0,1,2,3,4,5])

# Generate a color mapping of the levels we've specified
import matplotlib.cm as cm # matplotlib's color map library
cpf = ax.contourf(X,Y,Z, len(levels), cmap=cm.Reds)

# Set all level lines to black
line_colors = ['black' for l in cpf.levels]

# Make plot and customize axes
cp = ax.contour(X, Y, Z, levels=levels, colors=line_colors)
ax.clabel(cp, fontsize=10, colors=line_colors)
plt.xticks(df['X'])
plt.yticks(df['Y'])
ax.set_xlabel('X coordinate (cm)')
ax.set_ylabel('Y coordinate (cm)')

plt.title('Electric Potential Scalar Field')
plt.savefig('Contour_Plot.pdf')
