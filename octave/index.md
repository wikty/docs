---
title: "Octave/Matlab"
author: "Xiao Wenbin"
date: 2017-10-08T21:40:08+08:00
draft: false
categories: ["matlab", "octave"]
---

```matlab
% basic operations

% define variable: int, float, string, vector, matrix

% comma chaining of commands
a = 1, b = 2, c = 3;

1 + 2;

3 - 2;

5 * 2;

5 / 2;

2 ^ 5; % power

1 == 2; % test equal

1 ~= 2; % test not equal

1 && 0; % logical AND

1 || 0; % logical OR

xor(1, 0); % logical XOR

% print
% suppress output with semicolon
a = 4321.1234
b = 'hello';
disp(a);
disp(sprintf('hello %0.2f', a));

% commands

pwd % print working directory
PS1('>>'); % change prompt
cd 'the target directory'; % change workding directory
ls; % list the workding direcory
who; % show variables in current Octave memory
whos; % detailed who command
clear variable_name; % delete the variable from current memory
exit; % exit command
quit; % exit command

% Octave search path: default include the working directory
addpath('the path want to be searched') % add a search path

% help

help eye; % help a command or function
help '.'; % list all of avaiable operators
help +; % show help for the operator



% long/short
format short; % enable short decimal precision
format long; % enable long decimal precision

% define matrix/vector
% semicolon means goto next row
% column element split by space or comma
A = [1 2; 3 4; 5 6];
% row vector
a = [1 2 3];
% column vector
b = [1; 2; 3];
% quick martix
A = ones(4, 5); % 4x5 matrix with element 1
a = ones(1, 3); % 1x3 matrix with element 1
b = ones(3, 1);
A = zeros(4, 5); % 4x5 matrix with element 0
A = rand(4, 5); % 4x5 matrix with uniform(0, 1) rand
A = rand(4); % 4x4 matrix with uniform(0, 1) rand
A = randn(4, 5); % 4x5 matrix with gaussian(0, 1) rand
A = eye(4); % 4x4 diagonal matrix with element 1
% magic matrix
magic(4); % 4x4

% sequence
l = 1:0.1:2; % start:step:end
l = 1:10; % start:end

% size
size(A); % dimensions of matrix A, It's a 1x2 vector(rows, columns)
size(A, 1); % the first dimension(rows)
size(A, 2); % the second dimension(columns)
v = [1 2 3 4];
length(v); % the length of vector is 4
v = [1; 2; 3; 4];
length(v); % the length of vector is 4
length(A); % the length of matrix is rows

% load/save data

load filename;
load('filename'); % create a variable via filename 
save filename variable_name; % save data in binary format
save filename variable_name -ascii; % save data in text format


% access matrix
A = [1 2 3; 4 5 6];
A(3, 2);
A(:, 1);
A(1, :); % ":" means every element along that row or column
A([1 3], :); % everything from first and third row
A(:, 2) = [1; 1]; % assign
A = [A, [1; 0]]; % append a column vector
A = [A; [7 8 9]]; % append a row vector

A(:); % put all elements of A into a single column vector
A = [1 2; 3 4; 5 6];
B = [7 8; 9 10; 11 12];
C = [A, B];
C = [A; B];


% element-wise operation
A = [1 2; 3 4; 5 6]; % 3x2
B = [11 12; 13 14; 15 16]; % 3x2
C = [1 1; 2 2]; % 2x2

A * C; % matrix multiply
A .* B; %
-2 * A; 
A .^ 2;
1 ./ A;
v = [1; 2; 3];
-1 * v;
v + 1;
1 ./ v;
log(v);
exp(v);
abs(v);
% transpose
A';
(A')';
v';

% max/min
v = [1 2 3 4];
val = max(v);
[val, idx] = max(v);
A = [1 2 3; 4 5 6];
val = max(A); % row vector [4 5 6], column-wise max value
max(rand(3), rand(3)); % max two matrix
max(A, [], 1); % column-wise max value, return as row vector
max(A, [], 2); % row-wise max value, return as column vector
max(max(A)); % the max element of matrix A
max(A(:)); % the max element of matrix A

% compare
v = [1 2 3 4];
v < 3; % 0-1 vector
find(v < 3); % return index meet condition
A = magic(3);
[r, c] = find(A >= 7); % row index and column index

% sum/product
v = [1 2.5 5.1];
sum(v);
prod(v); % product the element
floor(v);
ceil(v);
A = magic(3);
sum(A); % sum column-wise
sum(A, 1); % sum column-wise, return as row vector
sum(A, 2); % sum row-wise, retur as column vector
% sum diagnoal elements
sum(sum(A .* eye(3)));
sum(sum(A .* flipud(eye(3)))); % filp up-down diagnoal

% invert matrix
A = magic(3);
pinv(A); % pseudo-invert


% plot

hist(-6+sqrt(10)*(randn(1, 100000)), 50);
x = [0:0.01:0.98];
y = sin(4*pi*x);
plot(x, y);
hold on; % enable drawing the same figure
y = cos(4*pi*x);
plot(x, y);
hold off; % disable drawing the same figure
xlabel('x label');
ylabel('y label');
legend('sin', 'cos'); % legend for each plot
title('my new plot');
print -dpng 'filename.png';
% help plot
close; % close the figure
% draw on different figures
figure(1); plot(x, y);
figure(2); plot(x, y);
% subplot: divides figure into grid
subplot(1, 2, 1);
plot(x, y);
subplot(1, 2, 2);
plot(x, y);
% change axis range
axis([0.5 1 -1 1]);
clf; % clear figure

% visualization matrix
imagesc(magic(3));
imagesc(magic(15)), colorbar, colormap gray;


% control statements
% for
v = zeros(10, 1);
for i=1:10,
	v(i) = 2 * i;
	disp(v(i));
end;

% while
i = 1;
while i <= 5,
	v(i) = 999;
	i = i + 1;
end;

while true,

	v(i) = 100;
	i = i + 1;
	if i == 5,
		break;
	end;
end;

% if-else
if v(1) == 1,
	disp('this is 1');
elseif v(1) == 2,
	disp('this is 2');
else,
	disp('this is others');
end;

% define function

% filename should be function name plus .m

% invoke function, the file in the working directory

function y = test(x)

y = x ^ 2;

end;


% return mulitple values
function [y1, y2] = test(x)

y1 = x ^ 2;
y2 = x ^ 3;

end;

X = [1 1; 1 2; 1 3];
y = [1 2 3]
```