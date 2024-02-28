import random, sys, time

def pearson_cor(X, y, m, n):
    v = [0] * n # Initialize the vector v to store Pearson correlation coefficients
    sum_y = sum(y) # Calculate the sum of the elements in the vector y
    sum_y2 = sum(y ** 2 for y in y) # Calculate the sum of the squares of the elements in the vector y
    
    # Loop over each column of X
    for i in range(n):
        sum_x = sum(X[i]) # Calculate the sum of the elements in the ith column of X
        sum_x2 = sum(x ** 2 for x in X[i]) # Calculate the sum of the squares of the elements in the ith column of X
        sum_xy = sum(x * y for x, y in zip(X[i], y)) # Calculate the sum of the products of the elements in the ith column of X and the vector y

        r_numerator = n * sum_xy - sum_x * sum_y # Calculate the numerator of the Pearson correlation coefficient formula
        r_denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5 # Calculate the denominator of the Pearson correlation coefficient formula
        
        v[i] = r_numerator / r_denominator # Calculate the Pearson correlation coefficient for the ith column and store it in v
    
    return v

def main():
    n = int(input("Enter the value of n: "))
    
    
    X = [[random.randint(-sys.maxsize, sys.maxsize) for _ in range(n)] for _ in range(n)] # Generate non-zero n x n matrix X with random integers
    y = [random.randint(-sys.maxsize, sys.maxsize) for _ in range(n)] # Generate non-zero n x 1 vector y with random integers

    # print("Matrix X:")
    # for row in X: print(row)
    # print("\nVector y:", y)
    
    time_before = time.time() # Record start time
    
    v = pearson_cor(X, y, n, n) # Calculate Pearson correlation coefficient vector
    
    time_after = time.time() # Record end time
    time_elapsed = time_after - time_before # Calculate elapsed time
    
    # print("Pearson correlation coefficient vector:", v)
    print("Time elapsed:", time_elapsed, "seconds")

main()