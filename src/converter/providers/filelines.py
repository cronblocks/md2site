# *****************************************************************************************
# * Purpose:
# *     Recursively providing text lines from specified file
# *
# *
# *****************************************************************************************
# * Author: Usama
# *
# *****************************************************************************************
# * Changes:
# *
# * Date         Changed by      Description
# * ----         ----------      -----------
# *
# *
# *
# *
# *****************************************************************************************

from os.path import isfile


def getLines(filename: str, filterEmptyLines: bool = False):
    if isfile(filename):

        lineNumber: int = 0
        
        for line in open(filename):
            lineNumber += 1

            if filterEmptyLines == False:
                yield (line, lineNumber)
            else:
                if len(line.strip()) > 0:
                    yield (line, lineNumber)
