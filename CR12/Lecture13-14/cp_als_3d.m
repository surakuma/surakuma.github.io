function [L U1 U2 U3] = cp_als_3d(T, r)
	
	dimsize = size(T);
	
	U1=rand(dimsize(1),r);
	U2=rand(dimsize(2),r);
	U3=rand(dimsize(3),r);
	
	approx_error = 1.0;
	niterations = 0;

	 while(approx_error > 0.00000001)
	 
	 	tmp2 = U2' * U2;
	 	tmp3 = U3' * U3;
	 	tmp = tmp2 .* tmp3;
	 	U1 = unfolding(T,1)* krproduct(U3,U2);
	 	U1 = U1 * pinv(tmp);
	 	[U1 L] = normalize(U1);
	 	
	 	tmp1 = U1' * U1;
	 	tmp3 = U3' * U3;
	 	tmp = tmp1 .* tmp3;
	 	U2 = unfolding(T,2)* krproduct(U3,U1);
	 	U2 = U2 * pinv(tmp);
	 	[U2 L] = normalize(U2);
	 	
	 	tmp1 = U1' * U1;
	 	tmp2 = U2' * U2;
	 	tmp = tmp1 .* tmp2;
		U3 = unfolding(T,3)* krproduct(U2,U1);
	 	U3 = U3 * pinv(tmp);
	 	[U3 L] = normalize(U3);
	 		
	 	approxT = approxTensor(L, U1, U2, U3);
	 	approx_error = tensorfronorm(T, approxT)
	 	niterations += 1;	 	
	 end
 
 end
 
