function C = krproduct(A,B)

	n1 = rows(A);
	n2 = rows(B);
	
	r = columns(A);
	
	for i=1:r
		a=A(:,i); b=B(:,i);
		C(:,i) = vec(b*a');
	end

end
