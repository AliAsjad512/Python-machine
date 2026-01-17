random_array_4 = np.random.randint(10, size=(5,3))
random_array_4

random_array_4.shape

# view array arrays 

np.unique(random_array_4)
k=np.unique(random_array_4)

a=array([[[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]]])

higher_var_array = np.array([1,100,200,300,4000,5000])
low_var_array = np.array([2,4,6,8,10])
np.var(higher_var_array) , np.var(low_var_array)

np.std(higher_var_array) , np.std(low_var_array)
np.mean(higher_var_array) , np.mean(low_var_array)

%matplotlib inline 
import matplotlib.pyplot as plt
plt.hist(higher_var_array)
plt.show()

plt.hist(low_var_array)
plt.show()


np.random.seed(0)
mat1 = np.random.randint(10, size=(5,3))
mat2 = np.random.randint(10, size=(5,3))
mat1, mat2

mat1.T
mat3 = np.dot(mat1,mat2.T)
mat3,mat3.shape