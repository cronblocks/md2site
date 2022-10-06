# *****************************************************************************************
# * Purpose:
# *     Processing pipeline for file parsing
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


class Pipeline:
    def __init__(self, settings: Settings) -> None:
        self.settings: Settings = settings
        self.isPipelineSet: bool = False

        self.setPipeline()

    def setPipeline(self) -> None:
        if self.isPipelineSet:
            self.isPipelineSet = True

            ##########
            # Pipeline Setup
            #####

    def proceed(self) -> None:
        pass
