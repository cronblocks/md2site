# *****************************************************************************************
# * Purpose:
# *     Processing nodes for pipeline for file parsing
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

from processing.data import ProcessedData


class ProcessingNodesPipeline:
    def __init__(self) -> None:
        pass

    def start(self, filename: str) -> None:
        pass

    def end(self) -> None:
        pass

    def process(self, lineNumber: int, lineText: str) -> None:
        pass

    def getData(self) -> ProcessedData:
        pass
