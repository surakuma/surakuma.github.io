function T = approxTensor(L, U1, U2, U3)

	ncols  = length(L);
	
	n1 = rows(U1);
	n2 = rows(U2);
	n3 = rows(U3);
	
	T = zeros(n1, n2, n3);

	
	
	for i=1:ncols
		T += L(i) * outerproduct(U1(:,i), U2(:,i), U3(:,i));
	end

end
