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

from datetime import datetime, timedelta

from providers.settings import Settings
from providers.pathrecursion import getDesiredFiles


class Pipeline:
    def __init__(self, settings: Settings) -> None:
        self.settings: Settings = settings
        self.isPipelineSet: bool = False
        self.processStartTime: datetime = datetime.now()
        self.processEndTime: datetime = datetime.now()

        self.setPipeline()

    def setPipeline(self) -> None:
        if self.isPipelineSet:
            self.isPipelineSet = True

            ##########
            # Pipeline Setup
            #####

    def proceed(self, headingLine: str = "Processing:", indent: str = "  > ", appendBlankLines = 0) -> None:
        indentL1 = indent
        indentL2 = " " * len(indent) * 1 + indentL1
        indentL3 = " " * len(indent) * 2 + indentL2

        print(headingLine)

        ##########
        # Starting
        #######
        self.processStartTime = datetime.now()

        ##########
        # Processing
        #######
        for f in getDesiredFiles(self.settings, ""):
            print(f"{indentL1}{f}")

        ##########
        # Ending
        #######
        self.processEndTime = datetime.now()

        dt: timedelta = self.processEndTime - self.processStartTime
        print(f"{indentL1}Time taken: {dt.total_seconds() * 1000}ms")
