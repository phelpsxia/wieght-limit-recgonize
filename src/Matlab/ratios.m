function [outputArg1,outputArg2] = ratios(centers)
%UNTITLED2 �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
    ratios=zeros(1,length(centers)-1);
    for i=2:1:centers(max)
        ratios(i-1) = centers(i)-centers(i-1);
    end
end