import tensorflow as tf

# Define two matrices A and B
A = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)
B = tf.constant([[5, 6], [7, 8]], dtype=tf.float32)

print("Matrix A:")
print(A.numpy())

print("Matrix B:")
print(B.numpy())

# Matrix addition
C = tf.add(A, B)
print("Matrix C (A + B):")
print(C.numpy())

# Matrix multiplication
D = tf.matmul(A, B)
print("Matrix D (A * B):")
print(D.numpy())

# Matrix transposition
A_transposed = tf.transpose(A)
print("Transposed Matrix A:")
print(A_transposed.numpy())

# Element-wise multiplication
E = tf.multiply(A, B)
print("Element-wise multiplication (A .* B):")
print(E.numpy())


# Calculate the determinant of the 2x2 A matrix
det_2x2 = tf.linalg.det(A)
print("Determinant of 2x2 A matrix:")
print(det_2x2)

