import numpy as np;
import dask as dd;
def DMD(X_0, X_1 = None, threshold = 10):
	
	n, m = X_0.shape
	predictions = [] 
  def preprocessing(raw_data = X_0):
		
    def regressor(reg_data = raw_data):
      pred = []; 
      j = np.arange(m)
      for i in range(n):
        slope = ((reg_data[i] @ j) - (reg_data[0, i]*j.sum()))/(j@j)
        pred.append(slope*(m+1)+reg_data[0, i]);
      pred = np.array(pred).reshape(-1, 1);
      reg_data = np.hstack((reg_data, pred));
      return reg_data;
    raw_data = regressor(raw_data)[:, 1:]
    return raw_data
  if X_1 == None:
		X_1 = preprocessing();
		
	U, S, V = np.linalg(X_0);
	A_tilde = U.T @ X_1 @ V.T @ (1/np.diag(S))
	W, L = np.eig(A_tilde)
	Phi = X_1 @ V.T @ (1/np.diag(S)) @ W
	for i in range(1, threshold):
		eigenvalues = np.diag(L**(i-1))
		x_i = Phi @ eigenvalues @ np.linalg.pinv(Phi) @ 
		
	
	
      
