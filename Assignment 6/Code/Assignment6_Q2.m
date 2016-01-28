clc;
clear all;
close all;

load('M.dat')

% [V,D]=eig(M)
% sum(D(:))
% m_512=M.^512;

q0=[1 0 0 0 0 0 0 0 0 0]';
q0_new=[0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1 0.1]';
q=zeros(10,512);
%qdash=zeros(10,1024);

% Matrix Power Method %


M_prime=zeros(10,10,512);
M_prime(:,:,1)= M;
for i=1:511   
    M_prime(:,:,i+1) = M_prime(:,:,i) * M;
end


% Displaying the required answer %

MPrime_Result=M_prime(:,:,512);
MatrixPower_Result=MPrime_Result * q0;
%Alternate_result= M^512 * q0;



% State propagation method %


initial_value_q= M * q0;
q(:,1)=initial_value_q;
for t=2:512
    q(:,t)= M * q(:,t-1);
end


% Displaying the required answer %
State_Propagation_Result= q(:,512)


Q=ones(10,10);
Q=Q/10;
Q;
beta=0.85;
initial_value_q= (beta*M +(1-beta)*Q )* q0;
qddash(:,1)=initial_value_q;
for t=2:512
    qddash(:,t)= (beta*M +(1-beta)*Q ) * qddash(:,t-1);
end

% Displaying the required answer %
TaxationResult=qddash(:,512)






