% this script is test


tic;
maxX=100000000;
try
  x2=.01:.01:maxX;
  y2=log10(x2);
 catch
  fprintf(lasterr());
  maxX=1000000;
  x2=.01:.01:maxX;
  y2=log10(x2);
 end
toc
