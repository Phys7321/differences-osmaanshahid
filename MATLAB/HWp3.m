function [dy,xc] = HWp3()


load('derdata.mat')
[dy,xc] = Der(@func,X);

end