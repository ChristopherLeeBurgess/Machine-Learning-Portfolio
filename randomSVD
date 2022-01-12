def rSVD(mat, k=10, random_seed = 32, p_iteration = 3, osv_threshold = False):

  """Takes arbitrary input matrix, and uses random SVD with power iteration for the output."""

  np.random.seed(random_seed)                                #random seed for reproducibility.
  P = np.random.randn(mat.shape[1], k)                     #random matrix
  M = mat @ P                                           #multiplying the matrix input by the random matrix.
  for i in range(p_iteration):  #Using the power-iteration method to more accurately retrieve a reliable matrix M.
    M = mat @ (mat.T @ M);
  Q, _ = np.linalg.qr(M)               #Finding Q.
  B = Q.T @ mat                        #Projecting the input matrix into a smaller, more manageable matrix.
  U_ , S, V_T = np.linalg.svd(B, full_matrices = False) #Computing the SVD of smaller matrix B.  
  U = Q @ U_                          #Mapping U_ into the left singular matrix.

  if osv_threshold == True:
    sigma = np.median(S)
    n, m = mat.shape
    beta = float(n/m)
    la_beta = np.sqrt(2*(beta + 1) + ((8*beta)/((beta+1)+np.sqrt(beta**2 +14*beta+1))))
    thresh = la_beta * np.sqrt(n)*sigma
  elif osv_threshold == False:
    continue





  return U, S, V_T;
