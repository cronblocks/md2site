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
        ln = 0
        for l in open(filename):
            ln += 1

            if filterEmptyLines == False:
                yield (l, ln)
            else:
                if len(l.strip()) > 0:
                    yield (l, ln)
