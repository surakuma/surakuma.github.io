function [U S V] = truncated_svd(A, accr)

	[U1 S1 V1] = svd(A, "ECO");
	
	[nrows ncolumns] = size(A);
	
	accr_2 = accr * accr;
   	trunc_error_2 = 0;
   	
   	r_trunc = min(nrows, ncolumns);

   	for k=r_trunc:-1:1

    		trunc_error_2 = trunc_error_2 + S1(k,k)*S1(k,k);

    		if trunc_error_2 > accr_2
    			r_trunc = k;
    			break
    		end

    	end
    	
    	U = U1(:,1:r_trunc);
    	S = S1(1:r_trunc,1:r_trunc);
    	V = V1(:,1:r_trunc);

end
