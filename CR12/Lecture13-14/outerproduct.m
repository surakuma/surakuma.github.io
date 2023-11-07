function C = outerproduct(a, b, c)
	nc = length(c);
	
	for i=1:nc
		C(:,:,i) = (a*b')*c(i);
	end
end
