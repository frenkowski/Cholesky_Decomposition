% Metodi del Calcolo Scientifico
% Progetto_1
% Mohammad Al� Manan (817205)
% Francesco Porto (816042)
% Stranieri Francesco (816551)

% Original File
% https://math.nist.gov/MatrixMarket/mmio/matlab/mmiomatlab.html
% Edited with Davide Marchetti

function [ err ] = mmwrite_symmetric(filename,A,comment,precision)
%
% Function: mmwrite(filename,A,comment,field,precision)
%
%    Writes the sparse, real and symmetric matrix A to a Matrix Market (MM) 
%    formatted file.
%
% Required arguments: 
%
%                 filename  -  destination file
%
%                 A         -  sparse or full matrix
%
% Optional arguments: 
%
%                 comment   -  matrix of comments to prepend to
%                              the MM file.  To build a comment matrix,
%                              use str2mat. For example:
%
%                              comment = str2mat(' Comment 1' ,...
%                                                ' Comment 2',...
%                                                ' and so on.',...
%                                                ' to attach a date:',...
%                                                [' ',date]);
%                              If ommitted, a single line date stamp comment
%                              will be included.
%
%                 precision -  number of digits to display for real 
%                              or complex values
%                              If ommitted, full working precision is used.
%

mattype = 'real';
if (nargin > 2) 
  precision = 16;
elseif (nargin == 2) 
  comment = '';
  precision = 16;
end

mmfile = fopen([filename],'w');
if (mmfile == -1)
 error('Cannot open file for output');
end;

[M,N] = size(A);
if (issparse(A))
  [I,J,V] = find(A);

  issymm = 0;
  symm = 'general';
  NZ = nnz(A);

% Sparse coordinate format:
  rep = 'coordinate';

  fprintf(mmfile, '%%%%MatrixMarket matrix %s %s %s\n', 'coordinate', mattype, symm);
  [MC,NC] = size(comment);
  if (MC == 0)
    fprintf(mmfile, '%% Generated %s\n', [date]);
  else
    for i = 1:MC,
      fprintf(mmfile, '%%%s\n', comment(i, :));
    end
  end

  fprintf(mmfile, '%d %d %d\n', M, N, NZ);
  realformat = sprintf('%%d %%d %% .%dg\n', precision);

  for i = 1:NZ
    fprintf(mmfile, realformat, I(i), J(i), V(i));
  end;
end

fclose(mmfile);
