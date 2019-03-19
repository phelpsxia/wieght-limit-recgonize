file_name = 'C:\Users\SHB\Desktop\����ʵ�ַ���\images.jpg';

RGB = imread(file_name);
%{
rgb2 = histeq(RGB);
I = rgb2gray(RGB);
low = 0.05;
high = 0.1;
BW = edge(I,'canny',[low ,high],1);
%imimshow(BW)
test = rgb2;
%}
%truck ���Ҫ�ѵ�һ��ʶ������ͺ��ѣ���ɫ��ʶ����ܶ���Ч���

t= RGB;
t = imresize(t, 600/size(t,1));
t = t(300:600, :,:);

se8 = strel('disk',8);
bg = imopen(t, se8);
test = t - bg;
test =histeq(test);
imshow(test);
figure;

[centers1, radii1, metric1] = imfindcircles(test,[18 54],'Sensitivity',0.93,'ObjectPolarity','dark');
[centers2, radii2, metric2] = imfindcircles(test,[18 54],'Sensitivity',0.93);
[centers3, radii3, metric3] = imfindcircles(test,[18 54],'Sensitivity',0.85,'Method','TwoStage');
[centers4, radii4, metric4] = imfindcircles(test,[18 54],'Sensitivity',0.8,'ObjectPolarity','dark','Method','TwoStage');

%93����
%Isuzu �ӶԱ�
%images93���
%44568 93 �ɺ�����

figure(2)
imshow(test)
viscircles(centers1, radii1, 'EdgeColor','b');
viscircles(centers2, radii2, 'EdgeColor','r');
viscircles(centers3, radii3, 'EdgeColor','g');
viscircles(centers4, radii4, 'EdgeColor','k');

%Below is what calculates truck type by distribution of wheels
%Distant supervision