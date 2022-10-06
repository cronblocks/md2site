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

    def proceed(self) -> None:
        self.processStartTime = datetime.now()

        self.processEndTime = datetime.now()
        dt: timedelta = self.processEndTime - self.processStartTime
        print(f"Time taken: {dt.total_seconds() * 1000}ms")
