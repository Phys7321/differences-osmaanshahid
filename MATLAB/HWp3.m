function [dy,xc] = HWp3(varargin)
switch nargin
    case 2
        F = varargin{1};
        x = varargin{2};
        method = 'cd' ; %default value
        n = 5 ; %default value
    case 3
        F = varargin{1};
        x = varargin{2};
        method = varargin{3};
        n = 5 ; %default value
    case 4
        F = varargin{1};
        x = varargin{2};
        method = varargin{3};
        n = varargin{4};
end

load('derdata.mat')
[dy,xc] = Der(@func,X);

end