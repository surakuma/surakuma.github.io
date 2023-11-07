function [C L] = normalize(A)

	
	ncols = columns(A);
	
	for i=1:ncols
		L(i) = norm(A(:,i));
		C(:,i) = A(:,i) / L(i);
	end

end
