a = 0.5; b = 0.5; I = -40;
v = -5:0.1:5;
w_1 = v-(v.^3)/3;
% w_2 = v/b + a/b;
figure(1)
for b=0.1:0.2:0.9
    for a=1-(2*b)/3:0.2:0.9
     w_2 = v/b + a/b
     plot(v,w_2)
     hold on
    end
end
title('w_1 og w_2')
plot(v,w_1)

figure(2)
% hold on
% plot(v,w_2)
for b=0.1:0.1:0.9
    for a=1-(2*b)/3:0.2:0.9
     plot(v,(b-1)*v - b/3*v.^3)
     hold on
    end
end
title(' plotting av P(v_0) for 0<b<1')




