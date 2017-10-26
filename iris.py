import numpy as np
import matplotlib.pyplot as pl
import matplotlib.patches as mp

#load sepal length & width (cols 0 & 1). Petal length & width (cols 2 & 3) into a numpy array.
sepLen, sepWid, petLen, petWid = np.genfromtxt('IRIS.csv', delimiter = ',', usecols = (0,1,2,3), unpack = True, dtype=float)
#load the names from the 5th column
species = np.genfromtxt('IRIS.csv', delimiter=',', usecols=4, unpack = True, dtype=str)

print("Sepal\t\t| Petal\t\t | Species")
print("length | widht\t| length | width | type")
for i in range(len(petWid)):                    # print out all the data gathered
    print('{0:.1f} \t {1:.1f} \t {2:.1f} \t {3:.1f} \t {4:s}'.format(sepLen[i], sepWid[i], petLen[i], petWid[i], species[i]))


#creating a simple plot using the sepal data
pl.plot(sepLen, sepWid, 'k.')                   # set plot points 
pl.rcParams['figure.figsize'] = (16.0, 9.0)     # set dimensions of scatterplot
pl.ylabel('Sepal Widht')                        # set y label
pl.xlabel('Sepal Length')                       # set x label 
pl.title('Sepal variation in Width vs Length')  # give it a title

pl.show()                                       # draws the  scatterplot


import matplotlib.patches as mp
    
pl.rcParams['figure.figsize'] = (16.0, 9.0)     # set dimensions of a scatterplot
pl.ylabel('Sepal Widht')                        # set y label
pl.xlabel('Sepal Length')                       # set x label 
pl.title('Sepal variation in Width vs Length')  # give it a title

# create key, value pairs to bind species to different colours
pairs={'I-setosa' :'r','I-versicolor' :'g','I-virginica' :'b'} 

pl.scatter(sepLen, sepWid, c=[pairs[i] for i in species], label=[pairs[i] for i in pairs])
labels = [mp.Patch(color=cl, label=la) for la, cl in pairs.items()]


pl.legend(handles = labels)
pl.show()