# Metodi del Calcolo Scientifico
# Progetto_1
# Mohammad Alì Manan (817205)
# Francesco Porto (816042)
# Stranieri Francesco (816551)

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def parseResults(fileName):
    results = []
    curr_value = dict()

    with open(fileName, "r") as f:
        for line in f.readlines():
            line = line.strip(" \n")
            # print(line)

            if line != '':
                tokens = line.split()
                key = tokens[0]
                key = key[:-1]
                curr_value[key] = []

                for token in tokens[1:]:
                    curr_value[key].append(token)
            else:
                results.append(curr_value)
                curr_value = {}

    if curr_value:
        results.append(curr_value)
        curr_value = {}

    return results


def main():
    results = parseResults('./result.txt')

    matrixName = []
    platform = []
    language = []
    matrixSize = []
    nonZero = []
    relativeError = []
    executionTime = []
    memoryAllocated = []

    for result in results:
        matrixName.append(result['MatrixName'][0])
        platform.append(result['Platform'][0])
        language.append(result['Language'][0])
        matrixSize.append(result['MatrixSize'][0])
        nonZero.append(result['NonZero'][0])
        relativeError.append(result['RelativeError'][0])
        executionTime.append(result['ExecutionTime(ms)'][0])
        memoryAllocated.append(result['MemoryAllocated(KB)'][0])
        # print(nonZero)

    # print(nonZero)

    # https://wellsr.com/python/seaborn-line-plot-data-visualization/
    df = pd.DataFrame(list(zip(matrixName, platform, language, matrixSize, nonZero, relativeError, executionTime, memoryAllocated)),
                      columns=['MatrixName', 'Platform', 'Language', 'MatrixSize', 'NonZero', 'RelativeError', 'ExecutionTime', 'MemoryAllocated'])
    df.MatrixSize = df.MatrixSize.astype(float)
    df.NonZero = df.NonZero.astype(int)
    df.RelativeError = df.RelativeError.astype(float)
    df.ExecutionTime = df.ExecutionTime.astype(int)
    df.MemoryAllocated = df.MemoryAllocated.astype(float)
    # print(df.NonZero)
    
    
    # sns.set()


    def drawPlotParam(y, hue, style, param, x = 'MatrixSize'):
        plt.figure(figsize=(15, 8))
        sns.lineplot(x = x, y = y, hue = hue, style = style, err_style = "bars",
                     markers = ['o', '<', '*'], palette = 'husl', data = df.loc[df[style] == param])
        plt.yscale('log')
        plt.xlabel(x, fontsize = 12)
        plt.ylabel(y, fontsize = 12)
        plt.title(str(y) + ' vs ' + str(x) + ' on ' + str(param), fontsize = 15)
        plt.legend(title = 'Legend', bbox_to_anchor = (
            1.05, 1), loc = 2, borderaxespad = 0.)
        plt.show()

    # ### MatrixSize
    # ## SO
    # # Linux
    # drawPlotParam('RelativeError', 'Language', 'Platform', 'Linux')
    # drawPlotParam('ExecutionTime', 'Language', 'Platform', 'Linux')
    # drawPlotParam('MemoryAllocated', 'Language', 'Platform', 'Linux')

    # # Windows
    # drawPlotParam('RelativeError', 'Language', 'Platform', 'Windows')
    # drawPlotParam('ExecutionTime', 'Language', 'Platform', 'Windows')
    # drawPlotParam('MemoryAllocated', 'Language', 'Platform', 'Windows')    
    
    
    # ## Language   
    # # MatLab  
    # drawPlotParam('RelativeError', 'Platform', 'Language', 'MATLAB')
    # drawPlotParam('ExecutionTime', 'Platform', 'Language', 'MATLAB')
    # drawPlotParam('MemoryAllocated', 'Platform', 'Language', 'MATLAB')

    # # C++  
    # drawPlotParam('RelativeError', 'Platform', 'Language', 'C++')
    # drawPlotParam('ExecutionTime', 'Platform', 'Language', 'C++')
    # drawPlotParam('MemoryAllocated', 'Platform', 'Language', 'C++')  
    
    # # R 
    # drawPlotParam('RelativeError', 'Platform', 'Language', 'R')
    # drawPlotParam('ExecutionTime', 'Platform', 'Language', 'R')
    # drawPlotParam('MemoryAllocated', 'Platform', 'Language', 'R')

    # # Python
    # drawPlotParam('RelativeError', 'Platform', 'Language', 'Python')
    # drawPlotParam('ExecutionTime', 'Platform', 'Language', 'Python')
    # drawPlotParam('MemoryAllocated', 'Platform', 'Language', 'Python')
    
    # ### NonZero
    # ## SO
    # # Linux
    # drawPlotParam('RelativeError', 'Language', 'Platform', 'Linux', 'NonZero')
    # drawPlotParam('ExecutionTime', 'Language', 'Platform', 'Linux', 'NonZero')
    # drawPlotParam('MemoryAllocated', 'Language', 'Platform', 'Linux', 'NonZero')

    # # Windows
    # drawPlotParam('RelativeError', 'Language', 'Platform', 'Windows', 'NonZero')
    # drawPlotParam('ExecutionTime', 'Language', 'Platform', 'Windows', 'NonZero')
    # drawPlotParam('MemoryAllocated', 'Language', 'Platform', 'Windows', 'NonZero')  
    
    def drawPlotTotal(y, hue, style, x = 'MatrixSize'):
        plt.figure(figsize=(15,8))
        sns.lineplot(x = x, y = y, hue = hue, style = style, err_style = "bars", 
                     markers = ['o', '<', '*'], palette = 'husl', data = df)
        plt.yscale('log')
        plt.xlabel(x, fontsize= 12)
        plt.ylabel(y, fontsize = 12)
        plt.title(str(y) + ' vs ' + str(x), fontsize = 15)
        plt.legend(title = 'Legend', bbox_to_anchor = (1.05, 1), loc = 2, borderaxespad = 0.)
        plt.show()

    # ### MatrixSize
    # ## Total
    # # RelativeError
    # drawPlotTotal('RelativeError', 'Language', 'Platform')        
    # # ExecutionTime
    # drawPlotTotal('ExecutionTime', 'Language', 'Platform')
    # # MemoryAllocated
    # drawPlotTotal('MemoryAllocated', 'Language', 'Platform')
    
    ### NonZero
    ## Total
    # RelativeError
    drawPlotTotal('RelativeError', 'Language', 'Platform', x = 'NonZero')        
    # ExecutionTime
    drawPlotTotal('ExecutionTime', 'Language', 'Platform', x = 'NonZero')
    # MemoryAllocated
    drawPlotTotal('MemoryAllocated', 'Language', 'Platform', x = 'NonZero')


if __name__ == "__main__":
    main()
