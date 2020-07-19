R = 0;
k = 100;
n = 500;
svar = pi^2/2
t = 0
for i= 1:n
    for j=1:n
        x = (-k+((2*k*i)/n));
        y = (-k+((2*k*j)/n));
        R2 = func(x,y)*((2*k)/n)^2;
        R = R + R2;
    end
end
R
svar
abs(R - svar)
