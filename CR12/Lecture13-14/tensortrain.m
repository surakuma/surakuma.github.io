function [G] = tensortrain(X, tol)
% Ensures ||X- approx(X)|| <= tol
    dims = size(X);
    d= ndims(X);

    C=X;
    r=1;
    threshold_per_decomp = tol/sqrt(d-1);
    for k=1:1:d-1

    C= reshape(C, r*dims(k), numel(C)/(r*dims(k)));
    [U S V] = truncated_svd(C, threshold_per_decomp);
    
    r2 = columns(U);
   
    G{k} = reshape(U, r, dims(k), r2);
    C = S*V';
    r=r2;
    end

    G{d} = reshape(C, r, dims(d), 1);

end
