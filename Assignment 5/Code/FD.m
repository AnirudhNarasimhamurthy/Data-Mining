function [B] = FD(A,l)
  [n,d] = size(A);
  B = zeros(l,d);
  for i = 1:l-1
      B(i,:) = A(i,:);
  end
  for i = l:n
      B(l,:) = A(i,:);
      [U,S,V] = svd(B);
      delta = S(min(l,d), min(l,d))^2;
      S1 = zeros(l,d);
      for k = 1:min(l,d)
          S1(k,k) = sqrt(S(k,k)^2 - delta);
      end
      B = S1*V';
  end
end