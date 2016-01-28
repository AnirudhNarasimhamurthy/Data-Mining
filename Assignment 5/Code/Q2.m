load A.dat

[n, d] = size(A)

norm(A, 'fro')^2

for l = 1:10
    B = FD(A,l);
    [l, norm(A'*A - B'*B, 2)]
end


for k = [1, 2, 3, 4, 5, 6, 7]
    l = 11*k;
    [U,S,V] = svd(A);
    for l1 = k+1:l
        B = FD(A,l1);
        Bk = B(1:k,:);
        R = A*pinv(Bk)*Bk;
        Ak = U(:,1:k)*S(1:k,1:k)*V(:,1:k)';
        if R <= 1.1*norm(A - Ak, 2)
            [k, l, l1]
            break
        end
    end
end