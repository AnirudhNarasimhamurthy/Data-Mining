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
MatrixPower_Result=MPrime_Result * q0
%Alternate_result= M^512 * q0;



% State propagation method %


initial_value_q= M * q0;
q(:,1)=initial_value_q;
for t=2:512
    q(:,t)= M * q(:,t-1);
end


% Displaying the required answer %
State_Propagation_Result= q(:,512)



% Matrix Power Method for different q0 %


M2_prime=zeros(10,10,512);
M2_prime(:,:,1)= M;
t=1;
while (1)   
    M2_prime(:,:,t+1) = M2_prime(:,:,t) * M;
    MatrixPower_Result2=M2_prime(:,:,t+1) * q0_new;
    %if MatrixPower_Result2(3)== MatrixPower_Result(3) || MatrixPower_Result2(4)==MatrixPower_Result(4) ||  MatrixPower_Result2(5)==MatrixPower_Result(5) ||  MatrixPower_Result2(6)==MatrixPower_Result(6) ||  MatrixPower_Result2(7)==MatrixPower_Result(7) ||  MatrixPower_Result2(8)==MatrixPower_Result(8) ||  MatrixPower_Result2(9)==MatrixPower_Result(9) ||  MatrixPower_Result2(10)==MatrixPower_Result(10)
    %threshold = (MatrixPower_Result2(1)- MatrixPower_Result(1)) + (MatrixPower_Result2(2)- MatrixPower_Result(2)) + (MatrixPower_Result2(3)- MatrixPower_Result(3)) + (MatrixPower_Result2(4)- MatrixPower_Result(4)) +  (MatrixPower_Result2(5)- MatrixPower_Result(5)) +  (MatrixPower_Result2(6)- MatrixPower_Result(6)) +  (MatrixPower_Result2(7)- MatrixPower_Result(7)) +  (MatrixPower_Result2(8)- MatrixPower_Result(8)) +  (MatrixPower_Result2(9)- MatrixPower_Result(9)) +  (MatrixPower_Result2(10)- MatrixPower_Result(10));
    %threshold = (MatrixPower_Result2(1)- MatrixPower_Result(1))^2 + (MatrixPower_Result2(2)- MatrixPower_Result(2))^2 + (MatrixPower_Result2(3)- MatrixPower_Result(3))^2 + (MatrixPower_Result2(4)- MatrixPower_Result(4))^2 +  (MatrixPower_Result2(5)- MatrixPower_Result(5))^2 +  (MatrixPower_Result2(6)- MatrixPower_Result(6))^2 +  (MatrixPower_Result2(7)- MatrixPower_Result(7))^2 +  (MatrixPower_Result2(8)- MatrixPower_Result(8))^2 +  (MatrixPower_Result2(9)- MatrixPower_Result(9))^2 +  (MatrixPower_Result2(10)- MatrixPower_Result(10));
    %threshold
    threshold=norm(MatrixPower_Result2 - MatrixPower_Result, 2);
    if (threshold <= 0.0000001)
        fprintf(' t is %d', t)
        MatrixPower_Result2
        break;
    end 
    t=t+1;
end


% State propagation method for new q0%


initial_value_q= M * q0_new;
qdash(:,1)=initial_value_q;
t=2;
while (1)
     qdash(:,t)= M * qdash(:,t-1);
     %fprintf('t:%d', t)
     %threshold2= (qdash(1,t)- State_Propagation_Result(1)) + (qdash(2,t)- State_Propagation_Result(2)) + (qdash(3,t)- State_Propagation_Result(3)) +(qdash(4,t)- State_Propagation_Result(4)) + (qdash(5,t)- State_Propagation_Result(5)) + (qdash(6,t)- State_Propagation_Result(6)) + (qdash(7,t)- State_Propagation_Result(7)) + (qdash(8,t)- State_Propagation_Result(8)) + (qdash(9,t)- State_Propagation_Result(9)) + (qdash(10,t)- State_Propagation_Result(10));
     %threshold2= (qdash(1,t)- State_Propagation_Result(1))^2 + (qdash(2,t)- State_Propagation_Result(2))^2 + (qdash(3,t)- State_Propagation_Result(3))^2 +(qdash(4,t)- State_Propagation_Result(4))^2 + (qdash(5,t)- State_Propagation_Result(5))^2 + (qdash(6,t)- State_Propagation_Result(6))^2 + (qdash(7,t)- State_Propagation_Result(7))^2 + (qdash(8,t)- State_Propagation_Result(8))^2 + (qdash(9,t)- State_Propagation_Result(9))^2 + (qdash(10,t)- State_Propagation_Result(10))^2;
     threshold2 = norm(qdash(:,t) - State_Propagation_Result, 2);  
     if (threshold2 <= 0.0000001)
         fprintf('The value of t is %d', t);
         qdash(:,t)
         break
     end    
     t=t+1;
 end

% Displaying the required answer %
%State_Propagation_Result= q(:,512);

% Random Walk %

i=1;
for t0= 1:50
    u=rand;
    for r=1:10
        if (u < M(r,i))
          j_dash = r;
          break;
        else
          u = u - M(r,i);
        end
    end    
    i=j_dash; 
end

q0_dash=zeros(1,10);
q0_dash(i)=1;
q0_dash;

for t=1:512
    u=rand;
    for r=1:10
        if( u < M(r,i))
            j_doubledash=r;
            break;
        else
            u=u-M(r,i);
        end
    end
    M_dash(t)=j_doubledash;
    i=j_doubledash;
end    

% count_ones=sum(M_dash==1);
% count_twos=sum(M_dash==2);
% count_threes=sum(M_dash==3);
% count_fours=sum(M_dash==4);
% count_fives=sum(M_dash==5);
% count_sixes=sum(M_dash==6);
% count_sevens=sum(M_dash==7);
% count_eights=sum(M_dash==8);
% count_nines=sum(M_dash==9);
% count_tens=sum(M_dash==10);
% 
% count_ones=count_ones/norm(M_dash,1);
% count_twos=count_twos/norm(M_dash,1);
% count_threes=count_threes/norm(M_dash,1);
% count_fours=count_fours/norm(M_dash,1);
% count_fives=count_fives/norm(M_dash,1);
% count_sixes=count_sixes/norm(M_dash,1);
% count_sevens=count_sevens/norm(M_dash,1);
% count_eights=count_eights/norm(M_dash,1);
% count_nines=count_nines/norm(M_dash,1);
% count_tens=count_tens/norm(M_dash,1);



count_ones=sum(M_dash==1)/512;
count_twos=sum(M_dash==2)/512;
count_threes=sum(M_dash==3)/512;
count_fours=sum(M_dash==4)/512;
count_fives=sum(M_dash==5)/512;
count_sixes=sum(M_dash==6)/512;
count_sevens=sum(M_dash==7)/512;
count_eights=sum(M_dash==8)/512;
count_nines=sum(M_dash==9)/512;
count_tens=sum(M_dash==10)/512;

q_star=[count_ones count_twos count_threes count_fours count_fives count_sixes count_sevens count_eights count_nines count_tens];
q_star
sum(q_star(:))



% Eigen Analysis %
Norm_M= eig(M);
[v,d]=eig(M);
 v(:,1);
EigenAnalysis_Result=v(:,1) / norm(v(:,1),1)
sum(EigenAnalysis_Result(:))
