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

from datetime                    import datetime, timedelta
from os.path                     import isfile

from providers.settings          import Settings
from providers.pathrecursion     import getDesiredFiles
from providers.filelines         import getLines
from processing.processing_nodes import ProcessingNodesPipeline
from file_writers.base_writer    import BaseWriter
from file_writers.html_writer    import HtmlWriter


class Pipeline:
    def __init__(self, settings: Settings) -> None:
        self.settings: Settings = settings
        self.isPipelineSet: bool = False
        self.processStartTime: datetime = datetime.now()
        self.processEndTime: datetime = datetime.now()
        self.processingNodesPipeline: ProcessingNodesPipeline = ProcessingNodesPipeline()
        self.fileWriter: BaseWriter = HtmlWriter(self.settings)

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
        for filename in getDesiredFiles(self.settings, ".md"):
            if isfile(filename):

                print(f"{indentL1}{filename}")
                self.processingNodesPipeline.start(filename)

                try:
                    for l, ln in getLines(filename):
                        self.processingNodesPipeline.process(ln, l)
                except:
                    print(f"{indentL2}ERROR: cannot read file")

                self.processingNodesPipeline.end()
                self.fileWriter.writeData(self.processingNodesPipeline.getData())

            else:
                print(f"{indentL1}ERROR: {filename}")

        ##########
        # Ending
        #######
        self.processEndTime = datetime.now()

        dt: timedelta = self.processEndTime - self.processStartTime
        print(f"{indentL2}Time taken: {dt.total_seconds() * 1000}ms")
