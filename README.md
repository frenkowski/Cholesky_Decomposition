# Methods of Scientific Calculation Project 1

# Comparison of Sparse Linear Systems solvers via Cholesky Decomposition

## Team

Ali Manan (_mohammadalimanan+github@gmail.com_)  
Francesco Porto (_francescoporto97+github@gmail.com_)  
Francesco Stranieri (_frenkowski+github@gmail.com_)

## Abstract

Linear Systems involving sparse, symmetric and positive defined ma- trices occur in many practical applications, such as in computer vision, fluid dynamics or electromagnetism.
We suppose our company needs to solve such systems via the Cholesky method, and has asked us to find the best programming environment for this task: should a reliable paid environment such as MATLAB be preferred, or is it worth investigating into free open-source alternatives? Also, does the choice of operating system matters?

## Introduction

In this report we analyze and compare four different implementations of Sparse Linear Systems solvers that make use of the Cholesky Decomposition for sparse, symmetric and positive defined matrices from the SuiteSparse Matrix Collection. We used one closed-source environment, **MATLAB**, and three different open-source environments, **C++**, **Python** and **R**. For each environment, we will take into consideration its _execution time_, _memory usage_ and _relative error_. We will also make comparisons between different operating systems, (**Windows** and **Linux**), in order to understand if the choice matters. The aim of this study is to decide whether MATLAB is worth paying for or free and open-source solutions are good enough.
