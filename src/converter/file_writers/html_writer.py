# *****************************************************************************************
# * Purpose:
# *     Writing processed data into html format
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

from providers.settings           import Settings
from file_writers.base_writer     import BaseWriter
from processing.data              import ProcessedData


class HtmlWriter(BaseWriter):
    def __init__(self, settings: Settings) -> None:
        self.settings: Settings = settings
    
    def writeData(self, originalFilename: str, data: ProcessedData) -> None:
        outputFilename: str = originalFilename.replace(self.settings.scanDirOrFile, self.settings.outputDir)
        print(f">> Outputting to {outputFilename}")
