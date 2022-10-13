# *****************************************************************************************
# * Purpose:
# *     Base / provider for file writers
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

from providers.settings import Settings
from processing.data    import ProcessedData


class BaseWriter:
    def __init__(self, settings: Settings) -> None:
        self.settings: Settings = settings
    
    def writeData(self, data: ProcessedData) -> None:
        pass
