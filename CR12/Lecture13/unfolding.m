function T = unfolding(X, k)

	nrows = size(X,k);
	ncols = numel(X) / nrows;
	T = zeros(nrows, ncols);
	
	dimsize = size(X);
	
	offset = dimsize;
	
	offset(k) = [];
	
	offset = [1 offset];
	
	for i=2:length(offset)
		offset(i) = offset(i) * offset(i-1);
	end
	
	for icol=1:ncols
		tindex = ones(1, ndims(X));
		id = icol-1;
		for i=ndims(X):-1:k+1
			tindex(i) += floor(id/offset(i-1));
			id = mod(id, offset(i-1));
		end
		for i=k-1:-1:1
			tindex(i) += floor(id/offset(i));
			id = mod(id, offset(i));
		end
		
			tmp2 = num2cell(tindex(k+1:ndims(X)));
			tmp1 = num2cell(tindex(1:k-1));
			T(:,icol)=X(tmp1{:},:,tmp2{:});
	%{	
		if k==1
			tmp = num2cell(tindex(k+1:ndims(X)));
			T(:,icol)=X(:,tmp{:});
		elseif k==ndims(X)
			tmp = num2cell(tindex(1:k-1));
			T(:,icol)=X(tmp{:},:);
		else
			T(:,icol)=X(tindex(1:k-1),:,tindex(k+1:ndims(X)));
		end
	%}
		
	end



end
