# *****************************************************************************************
# * Purpose:
# *     Defining defaults and loading settings for other application components
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

from sys        import argv
from os         import getcwd
from os.path    import join
from os.path    import sep

# ***********
# Command-line arguments:
#     1 => path-to-scan          => file or directory full-path
#     2 => recursion-enabled     => [true] / false
#     3 => recursion-depth       => number / [infinite]
#     4 => dir-element-templates => - for default
#     5 => dir-site-template     => - for default
#     6 => dir-output            => - for default
#     7 => base-url              => - for local files
# ********
class Settings:
    infinite: int = 1000000

    def __init__(self):
        workingDir = getcwd()

        templatesDir = join(workingDir, "..", "templates")
        elementTemplatesDir = join(templatesDir, "element-templates")
        siteTemplateDir = join(templatesDir, "site-template-001-default")

        outputDir = join(workingDir, "..", "..", "generated-site")

        self.scriptName: str = ""
        self.scriptDir: str = workingDir
        self.scanDirOrFile: str = workingDir
        self.isRecursive: bool = True
        self.recursionDepth: int = Settings.infinite
        self.baseUrl: str = "file:///" + outputDir

        self.parseArguments()

    def parseArguments(self):

        # Script name
        if(argv):
            self.scriptName = argv.pop(0).replace(self.scriptDir, "").replace(sep, "")
        
        # 1 => path-to-scan          => file or directory full-path
        if(argv):
            try:
                self.scanDirOrFile = argv.pop(0)
            except: pass
        
        # 2 => recursion-enabled     => [true] / false
        if(argv):
            value = argv.pop(0).lstrip().rstrip().lower()

            if(value == "false" or value.startswith("0")):
                self.isRecursive = False
            else:
                self.isRecursive = True

        # 3 => recursion-depth       => number / [infinite]
        if(argv):
            try:
                self.recursionDepth = int(argv.pop(0))
            except: pass
        
        # 4 => dir-element-templates => - for default
        if(argv):
            value = argv.pop(0)

            if value != "-":
                self.elementTemplatesDir = value

        # 5 => dir-site-template     => - for default
        if(argv):
            value = argv.pop(0)

            if value != "-":
                self.siteTemplateDir = value

        # 6 => dir-output            => - for default
        if(argv):
            value = argv.pop(0)

            if value != "-":
                self.outputDir = value
        
        # 7 => base-url              => - for local files
        if(argv):
            value = argv.pop(0)

            if value != "-":
                self.baseUrl = value

        # Spoiling remaining elements
        while(argv):
            argv.pop()
        

    def print(self, headingLine: str, indent: str = "  > ", appendBlankLines = 0):

        indentL1 = indent
        indentL2 = " " * len(indent) * 1 + indentL1
        indentL3 = " " * len(indent) * 2 + indentL2
        
        recursion = "Disabled"
        if(self.isRecursive):
            recursion = "Enabled"
        
        recursionDepth = self.recursionDepth
        if(recursionDepth >= 1000000):
            recursionDepth = "Infinite"
        
        scriptDirInd = "<script-dir>"
        outputDir = self.outputDir.replace(self.scriptDir, scriptDirInd)
        
        libCssBootstrapFile = self.libCssBootstrapFile.replace(self.scriptDir, scriptDirInd)
        libCssSiteStylesFile = self.libCssSiteStylesFile.replace(self.scriptDir, scriptDirInd)
        libJsJQueryFile = self.libJsJQueryFile.replace(self.scriptDir, scriptDirInd)
        libJsBootstrapFile = self.libJsBootstrapFile.replace(self.scriptDir, scriptDirInd)
        libJsSiteScriptFile = self.libJsSiteScriptFile.replace(self.scriptDir, scriptDirInd)

        templateContentHeading1File              = self.templateContentHeading1File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading2File              = self.templateContentHeading2File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading3File              = self.templateContentHeading3File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading4File              = self.templateContentHeading4File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading5File              = self.templateContentHeading5File.replace(self.scriptDir, scriptDirInd)
        templateContentHeading6File              = self.templateContentHeading6File.replace(self.scriptDir, scriptDirInd)
        templateContentImageFile                 = self.templateContentImageFile.replace(self.scriptDir, scriptDirInd)
        templateContentCodeFile                  = self.templateContentCodeFile.replace(self.scriptDir, scriptDirInd)
        templateContentConsoleFile               = self.templateContentConsoleFile.replace(self.scriptDir, scriptDirInd)
        templateContentListUnorderedFile         = self.templateContentListUnorderedFile.replace(self.scriptDir, scriptDirInd)
        templateContentListUnorderedItemFile     = self.templateContentListUnorderedItemFile.replace(self.scriptDir, scriptDirInd)
        templateContentParaFile                  = self.templateContentParaFile.replace(self.scriptDir, scriptDirInd)
        templateContentQuestionFile              = self.templateContentQuestionFile.replace(self.scriptDir, scriptDirInd)
        templateContentSectionFile               = self.templateContentSectionFile.replace(self.scriptDir, scriptDirInd)
        templateSideMajorItemFile                = self.templateSideMajorItemFile.replace(self.scriptDir, scriptDirInd)
        templateSideMinorItemFile                = self.templateSideMinorItemFile.replace(self.scriptDir, scriptDirInd)
        templateSideSectionItemFile              = self.templateSideSectionItemFile.replace(self.scriptDir, scriptDirInd)
        templateSidePageItemFile                 = self.templateSidePageItemFile.replace(self.scriptDir, scriptDirInd)
        templateSiteFile                         = self.templateSiteFile.replace(self.scriptDir, scriptDirInd)
        
        print(headingLine)
        print(f"{indent}Script Directory       -> {self.scriptDir}")
        print(f"{indent}Script Name            -> {self.scriptName}")
        print(f"{indent}Scan Directory         *> {self.scanDir}")
        print(f"{indent}Recursion              *> {recursion}")
        print(f"{indent}Recursion Depth        *> {recursionDepth}")
        print(f"{indent}Output Path            *> {outputDir}")
        print(f"{indent}Base URL               *> {self.baseUrl}")
        
        print(f"{indent}Library:")
        print(f"{indent2}(Bootstrap)    -> {libCssBootstrapFile}")
        print(f"{indent2}(jQuery)       -> {libJsJQueryFile}")
        print(f"{indent2}(Bootstrap JS) -> {libJsBootstrapFile}")
        print(f"{indent2}(Site CSS)     -> {libCssSiteStylesFile}")
        print(f"{indent2}(Site JS)      -> {libJsSiteScriptFile}")

        print(f"{indent}Templates:")
        print(f"{indent2}(Content - Heading 1) -> {templateContentHeading1File}")
        print(f"{indent2}(Content - Heading 2) -> {templateContentHeading2File}")
        print(f"{indent2}(Content - Heading 3) -> {templateContentHeading3File}")
        print(f"{indent2}(Content - Heading 4) -> {templateContentHeading4File}")
        print(f"{indent2}(Content - Heading 5) -> {templateContentHeading5File}")
        print(f"{indent2}(Content - Heading 6) -> {templateContentHeading6File}")
        print(f"{indent2}(Content - Image)     -> {templateContentImageFile}")
        print(f"{indent2}(Content - Code)      -> {templateContentCodeFile}")
        print(f"{indent2}(Content - Console)   -> {templateContentConsoleFile}")
        print(f"{indent2}(Content - List - Unordered)      -> {templateContentListUnorderedFile}")
        print(f"{indent2}(Content - List - Unordered Item) -> {templateContentListUnorderedItemFile}")
        print(f"{indent2}(Content - Para)      -> {templateContentParaFile}")
        print(f"{indent2}(Content - Question)  -> {templateContentQuestionFile}")
        print(f"{indent2}(Content - Section)   -> {templateContentSectionFile}")
        print(f"{indent2}(Side - Major Item)   -> {templateSideMajorItemFile}")
        print(f"{indent2}(Side - Minor Item)   -> {templateSideMinorItemFile}")
        print(f"{indent2}(Side - Section Item) -> {templateSideSectionItemFile}")
        print(f"{indent2}(Side - Page Item)    -> {templateSidePageItemFile}")
        print(f"{indent2}(Site)                -> {templateSiteFile}")

        while (appendBlankLines > 0):
            print("")
            appendBlankLines = appendBlankLines - 1

        return
