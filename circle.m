%Equation of circle
clc
clear all
close all
im=zeros(256);
r=20;       %Radius of the circle
[m,n]=size(im);
for i=1:m
    for j=1:n
        if (i-128)^2+(j-128)^2<r^2 %Equation of circle
            im(i,j)=255;
        end
    end
end
imshow(im)
