import numpy as np
import matplotlib.pyplot as pl
import matplotlib.patches as mp
import seaborn as sb
from scipy import stats

#load sepal length & width (cols 0 & 1). Petal length & width (cols 2 & 3) into a numpy array.
sepLen, sepWid, petLen, petWid = np.genfromtxt('IRIS.csv', delimiter = ',', usecols = (0,1,2,3), unpack = True, dtype=float)
#load the names from the 5th column
species = np.genfromtxt('IRIS.csv', delimiter=',', usecols=4, unpack = True, dtype=str)

print(" Sepal\t\t| Petal\t\t | Species")
print(" length | widht\t| length | width | type")
for i in range(len(petWid)):                    # print out all the data gathered
    print('{0:.1f} \t {1:.1f} \t {2:.1f} \t {3:.1f} \t {4:s}'.format(sepLen[i], sepWid[i], petLen[i], petWid[i], species[i]))


#creating a simple plot using the sepal data
pl.plot(sepLen, sepWid, 'k.')                   # set plot points 
pl.rcParams['figure.figsize'] = (16.0, 9.0)     # set dimensions of scatterplot
pl.ylabel('Sepal Widht')                        # set y label
pl.xlabel('Sepal Length')                       # set x label 
pl.title('Sepal variation in Width vs Length')  # give it a title

pl.show()                                       # draws the  scatterplot
    
pl.rcParams['figure.figsize'] = (16.0, 9.0)     # set dimensions of a scatterplot
pl.ylabel('Sepal Widht')                        # set y label
pl.xlabel('Sepal Length')                       # set x label 
pl.title('Sepal variation in Width vs Length')  # give it a title

# create key, value pair dict to bind species to different colours
pairs={'I-setosa' :'r','I-versicolor' :'g','I-virginica' :'b'} 

pl.scatter(sepLen, sepWid, c=[pairs[i] for i in species], label=[pairs[i] for i in pairs])
labels = [mp.Patch(color=cl, label=la) for la, cl in pairs.items()] 
pl.legend(handles = labels)
pl.show()

sb.set(style="ticks")                           # Set aesthetic parameters in one step.
df = sb.load_dataset("iris")                    # using the iris data set from seaborns github
sb.pairplot(df, hue="species")                  # Plot pairwise relationships in a dataset.  
pl.show()

# get the best fit line
def bestFitLine(length, Width):
    pl.rcParams['figure.figsize'] = (16.0, 9.0)     # set dimensions of a scatterplot

    j = np.linspace(0, 9, 1000)
    line = np.polyfit(length, Width, 1)            # Calculate the best fit line
    lp = line[0] * j + line[1]                      # Calculate the line points

    pl.plot(length, Width, 'k.', label = 'Original Data')       # plot the points
    pl.plot(j, lp, 'b-', label = 'Best fit line')                # add the line
    pl.legend()
    pl.show()

#best fit line for all
bestFitLine(petLen, petWid)

# calculate r squared for all
rSq = stats.linregress(petLen, petWid)
print('\nR Value: ', rSq[2], '\n Slope: ', rSq[0], '\t Intercept: ', rSq[1])
# best fit line for only setosa
newLen, newWid = petLen[0:50], petWid[0:50]

bestFitLine(newLen, newWid)

# calculate r squared for setosa only
rSq = stats.linregress(newLen, newWid)
print('\nR Value: ', rSq[2], '\n Slope: ', rSq[0], '\t Intercept: ', rSq[1])


# Using gradient descent to approximate the best fit line for the petal length and petal width setosa values.
def grad_m(x, y, m, c):
  return -2.0 * np.sum(x * (y - m * x - c))

def grad_c(x, y, m , c):
  return -2.0 * np.sum(y - m * x - c)

eta = 0.0001
m, c = 1.0, 1.0
change = True

while change:
  mnew = m - eta * grad_m(newLen, newWid, m, c)
  cnew = c - eta * grad_c(newLen, newWid, m, c)
  if m == mnew and c == cnew:
    change = False
    print("m: %20.16f  c: %20.16f" % (m, c))
  else:
    m, c = mnew, cnew
    #print("m: %20.16f  c: %20.16f" % (m, c))

print('\n\n', rSq)
print('\nM difference in percentage: '+str(format((100 * (rSq[0] - m) / m), '.12f')))
print('C difference in percentage: '+str(format((100 * (rSq[1] - c) / c), '.12f')))

# End