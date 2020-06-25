% Metodi del Calcolo Scientifico
% Progetto_1
% Mohammad Al� Manan (817205)
% Francesco Porto (816042)
% Stranieri Francesco (816551)

clear all
close all
clc

matrixFolderSource = 'SuiteSparse/MAT/'; 
addpath(matrixFolderSource);
matrixList = dir(fullfile(matrixFolderSource, '*.mat'));

matrixFolderDestination = 'SuiteSparse/MTX/'; 
addpath(matrixFolderDestination);

fileExtension = '.mtx';

for i = 1:length(matrixList)
  load(matrixList(7).name);
    
  fileName = split(matrixList(7).name,'.');
  matrixName = fileName{1};
  matrixName = strcat(matrixFolderDestination,matrixName,fileExtension)
    
  mmwrite_SRS(matrixName,Problem.A);
    
  clearvars fileName matrixName Problem;
end
