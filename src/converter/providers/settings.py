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
        self.elementTemplatesDir = join(templatesDir, "element-templates")
        self.siteTemplateDir = join(templatesDir, "site-template-001-default")

        self.outputDir = join(workingDir, "..", "..", "generated-site")

        self.scriptName: str = ""
        self.scriptDir: str = workingDir
        self.scanDirOrFile: str = workingDir
        self.isRecursive: bool = True
        self.recursionDepth: int = Settings.infinite
        self.baseUrl: str = "file:///" + self.outputDir

        self.parseArguments()

    def parseArguments(self):

        # Script name
        if argv:
            self.scriptName = argv.pop(0).replace(self.scriptDir, "").replace(sep, "")
        
        # 1 => path-to-scan          => file or directory full-path
        if argv:
            try:
                self.scanDirOrFile = argv.pop(0)
            except: pass
        
        # 2 => recursion-enabled     => [true] / false
        if argv:
            value = argv.pop(0).lstrip().rstrip().lower()

            if(value == "false" or value.startswith("0")):
                self.isRecursive = False
            else:
                self.isRecursive = True

        # 3 => recursion-depth       => number / [infinite]
        if argv:
            try:
                self.recursionDepth = int(argv.pop(0))
            except: pass
        
        # 4 => dir-element-templates => - for default
        if argv:
            value = argv.pop(0)

            if value != "-":
                self.elementTemplatesDir = value

        # 5 => dir-site-template     => - for default
        if argv:
            value = argv.pop(0)

            if value != "-":
                self.siteTemplateDir = value

        # 6 => dir-output            => - for default
        if argv:
            value = argv.pop(0)

            if value != "-":
                self.outputDir = value
        
        # 7 => base-url              => - for local files
        if argv:
            value = argv.pop(0)

            if value != "-":
                self.baseUrl = value

        # Spoiling remaining elements
        while argv:
            argv.pop()
        

    def print(self, headingLine: str = "Settings:", indent: str = "  > ", appendBlankLines = 0):

        indentL1 = indent
        indentL2 = " " * len(indent) * 1 + indentL1
        indentL3 = " " * len(indent) * 2 + indentL2
        
        recursion = "Disabled"
        if self.isRecursive:
            recursion = "Enabled"
        
        recursionDepth = self.recursionDepth
        if recursionDepth >= Settings.infinite:
            recursionDepth = "Infinite"
        
        print(headingLine)
        print(f"{indent}Script Directory       -> {self.scriptDir}")
        print(f"{indent}Script Name            -> {self.scriptName}")
        print(f"{indent}Scan Path              *> {self.scanDirOrFile}")
        print(f"{indent}Recursion              *> {recursion}")
        print(f"{indent}Recursion Depth        *> {recursionDepth}")
        print(f"{indent}Element Templates Path *> {self.elementTemplatesDir}")
        print(f"{indent}Site Template Path     *> {self.siteTemplateDir}")
        print(f"{indent}Output Path            *> {self.outputDir}")
        print(f"{indent}Base URL               *> {self.baseUrl}")
        
        while appendBlankLines > 0:
            print("")
            appendBlankLines = appendBlankLines - 1

        return
