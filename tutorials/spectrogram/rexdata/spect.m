function L=spect(x)

winsize=256;
shift=20;
c=1;
clear L;
h=hamming(256);

for i=1:shift:length(x)-winsize
     X=fft(x(i:i+winsize-1).*h,winsize);
     L(:,c)=log(real(X).^2+imag(X).^2);
     c=c+1;
end

% do rescaling (4)
% find the floor of L, reset to be 0
mn=min(min(L));
L=L-mn;

% find the max of L.  Map L to a number between 0 and 128 (at first)
% and then subtract 50 (-50 to 78)
mx=max(max(L));
L=floor(L/mx*128)-50;

% map all numbers below 1 to 1, all numbers above 64 to 64
L(find(L<1))=1;
L(find(L>64))=64;

