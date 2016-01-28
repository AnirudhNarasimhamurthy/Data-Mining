clc;
clear all;
close all;


A=load('A.dat');
X=load('X.dat');
Y=load('Y.dat');
M=load('M.dat');
W=load('W.dat');
[U,S,V]= svd(A);
[n,d]=size(A);

for k = 1:10
    Uk=U(:,1:k);
    Sk=S(1:k,1:k);
    Vk=V(:,1:k);
    Ak=Uk*Sk*Vk';
    norm(A-Ak,2)
    if (0.1*norm(A,2))-norm(A-Ak,2) > 0
    fprintf('k=%d',k);
    end
    
end

temp2=norm(A,2);
temp3= 0.1 * temp2;
temp3

%Plotting in two dimensions %

for k = 1:2
    U2k=U(:,1:k);
    S2k=S(1:k,1:k);
    V2k=V(:,1:k);
    A2k=U2k*S2k*V2k';
    %Ak_values=Ak;
end


original_A=U*S*V';
%SSquare= S2k .^ S2k;


U2_S2 = U(:,1:2)*S(1:2,1:2);
U2=U(:,1:2);
[row,col]=size(U2);
row;
col;

figure(1)
scatter(U2_S2(:,1), U2_S2(:,2),60,[1,0,0])



% figure(1)
% 
% f = eye(1125) - (ones(1125,1125)/1125);
% [U,S,V] = svd(f*A);
% 
% A2 = U(:,1:2)*S(1:2,1:2)*V(1:2,1:2);
% scatter(A2(:,1), A2(:,2),[])