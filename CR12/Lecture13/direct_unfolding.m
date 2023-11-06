function T = direct_unfolding(X, k)

	pv = [k, 1:ndims(X)];

	pv(k+1) = [];
	
	T = reshape(permute(X, pv), size(X,k), []);


end
