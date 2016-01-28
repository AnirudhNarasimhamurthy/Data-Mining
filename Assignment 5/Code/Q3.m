%A = load('A.dat');
clc;
clear all;
close all;

X = load('X.dat');
Y = load('Y.dat');
svalues = [0.1, 0.3, 0.5, 1.0, 2.0];
for s = svalues
    Cs = inv(X'*X+s^2*eye(12) )*X'*Y;
    fprintf('s=%f error=%f\n',s,norm(Y -X*Cs,2));
end
C = inv(X'*X)*X'*Y;
fprintf('Error via least squares=%f\n',norm(Y-(X*C),2));
%fprintf('Linear error=%f\n',norm(Y(9:10) -X(9:10,:)*C,2));

fprintf('X1,Y1');
X1 = X(1:66,:);
Y1 = Y(1:66);
for s = svalues
    Cs1 = inv(X1'*X1+s^2*eye(12) )*X1'*Y1;
    fprintf('s=%f error=%f\n',s,norm(Y(67:100)-(X(67:100,:)*Cs1),2));
end
C1 = inv(X1'*X1)*X1'*Y1;
fprintf('Error via Least Squares=%f\n',norm(Y(67:100) -X(67:100,:)*C1,2));


fprintf('X2,Y2');

X2 = X(34:100,:);
Y2 = Y(34:100);
for s = svalues
    Cs2 = inv(X2'*X2+s^2*eye(12) )*X2'*Y2;
    fprintf('s=%f error=%f\n',s,norm(Y(1:33)-(X(1:33,:)*Cs2),2));
end
C2 = inv(X2'*X2)*X2'*Y2;
fprintf('Error via Least Squares=%f\n',norm(Y(1:33)-X(1:33,:)*C2,2));

fprintf('X3,Y3');

X3 = [X(1:33,:); X(67:100,:)];
Y3 = [Y(1:33); Y(67:100)];
for s = svalues
    Cs3 = inv(X3'*X3+s^2*eye(12) )*X3'*Y3;
    fprintf('s=%f error=%f\n',s,norm(Y(34:66)-(X(34:66,:)*Cs3),2));
end
C3 = inv(X3'*X3)*X3'*Y3;
fprintf('Error via Least Squares=%f\n',norm(Y(34:66)-X(34:66,:)*C3,2));

%norm(Y(9:10) -X(9:10,:)*A,2)
%A = (X'*X)'*X'*Y;
%A = (transpose(X) * X)' * transpose(X) * Y;
