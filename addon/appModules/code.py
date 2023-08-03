import appModuleHandler
import ui
from scriptHandler import script
import api

class AppModule(appModuleHandler.AppModule):
    @script(gesture="kb:NVDA+W", description="Report current line number in vscode.")

    def script_sayLineNumber(self, gesture):
        ui.message(self.getStatusInformation("line"))

    @script(gesture="kb:NVDA+SHIFT+W", description="Report current column (character in line) in vscode.")
    def script_sayCol(self,gesture):
        ui.message(self.getStatusInformation("col"))

    def getStatusInformation(self,mode):
        sb=api.getStatusBar().children
        if mode=="line":
            return sb[-2].name.split(",")[0]
        elif mode=="col":
            return sb[-2].name.split(",")[1]