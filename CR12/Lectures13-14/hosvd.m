function [G F] = hosvd(X, tol)
% Ensures ||X- approx(X)|| <= tol

	d= ndims(X);
	dimsize = size(X);
	threshold_per_dim = tol/sqrt(d);
	F = cell(d,1);
	
	for i=1:1:d
		x_i = unfolding(X,i);
		[U S V] = truncated_svd(x_i, threshold_per_dim);
		F{i} = U;		
	end
	if d==3
		r1 = size(F{1}, 2);
		r2 = size(F{2}, 2);
		r3 = size(F{3}, 2);
		
		n1 = dimsize(1);
		n2 = dimsize(2);
		n3 = dimsize(3);
		
		G=zeros(r1, r2, r3);
		
		for i1=1:n1
		  for i2=1:n2
		    for i3=1:n3
		      for j1=1:r1
		        for j2=1:r2
		          for j3=1:r3
		            G(j1,j2,j3) += X(i1,i2,i3)*F{1}(i1,j1)* F{2}(i2,j2) * F{3}(i3,j3);
		          end
		        end
		      end
		    end
		  end
		end
		
	else
		 G = X;
		 for i=1:1:d
		 	G = tensorproduct(G, 1, F{i}, 1);
		 end
		 
	end
	

end

