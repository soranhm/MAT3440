b = 1.1:0.1:2.9;

R = (3*(b-1))./b;
la = -(b-1+R)+sqrt((b-1+R).^2 - 4.*(1-b+b.*R));
la2 = -(b-1+R)-sqrt((b-1+R).^2 - 4.*(1-b+b.*R));

lambda = la/2
lambda2 = la2/2
