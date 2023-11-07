function T = tensorproduct(X, k1, Y, k2)

	dimsize1 = size(X);
	pv1 = [1:ndims(X), k1];

	pv1(k1) = [];
	dimsize1(k1) = [];
	A = reshape(permute(X, pv1), numel(X)/size(X,k1), []);
	
	dimsize2 = size(Y);
	pv2 = [k2, 1:ndims(Y)];

	pv2(k2+1) = [];
	dimsize2(k2) = [];
	
	B = reshape(permute(Y, pv2), size(Y,k2), []);
	
	
	finaldim = [dimsize1 dimsize2];
	
	T = reshape(A*B, finaldim);

end
