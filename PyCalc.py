import sys
from PyQt5 import QtWidgets, QtCore
import mainwindow
ERROR_MSG = 'ERROR'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainwindow.Ui_PyCalc()
        self.ui.setupUi(self)
        self.ui.display.setAlignment(QtCore.Qt.AlignRight)
        self.ui.clearAll.clicked.connect(self.clearDisplay)
        
        self.ui.one.clicked.connect(lambda: self.setDisplayText(self.displayText()+"1"))
        self.ui.two.clicked.connect(lambda: self.setDisplayText(self.displayText()+"2"))
        self.ui.three.clicked.connect(lambda: self.setDisplayText(self.displayText()+"3"))
        self.ui.four.clicked.connect(lambda: self.setDisplayText(self.displayText()+"4"))
        self.ui.five.clicked.connect(lambda: self.setDisplayText(self.displayText()+"5"))
        self.ui.six.clicked.connect(lambda: self.setDisplayText(self.displayText()+"6"))
        self.ui.seven.clicked.connect(lambda: self.setDisplayText(self.displayText()+"7"))
        self.ui.eight.clicked.connect(lambda: self.setDisplayText(self.displayText()+"8"))
        self.ui.nine.clicked.connect(lambda: self.setDisplayText(self.displayText()+"9"))
        self.ui.plus.clicked.connect(lambda: self.setDisplayText(self.displayText()+"+"))
        self.ui.divideBy.clicked.connect(lambda: self.setDisplayText(self.displayText()+"/"))
        self.ui.minus.clicked.connect(lambda: self.setDisplayText(self.displayText()+"-"))
        self.ui.multiply.clicked.connect(lambda: self.setDisplayText(self.displayText()+"*"))
        self.ui.leftBracket.clicked.connect(lambda: self.setDisplayText(self.displayText()+"("))
        self.ui.rightBracket.clicked.connect(lambda: self.setDisplayText(self.displayText()+")"))
        self.ui.pointer.clicked.connect(lambda: self.setDisplayText(self.displayText()+"."))
        
        self.ui.doubleZero.clicked.connect(lambda: self.setZero('00'))
        self.ui.zero.clicked.connect(lambda: self.setZero('0'))
        
        self.ui.equalTo.clicked.connect(lambda: self.setDisplayText(evaluateExpression(self.displayText())))
    def advanceSlider(self):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
    
    #Function to clear display
    def clearDisplay(self):
        self.ui.display.setText("")
    
    #Function to set display setText
    def setDisplayText(self, text):
        self.ui.display.setText(text)
        self.ui.display.setFocus()
    
    #return display Text
    def displayText(self):
        return self.ui.display.text()
    
    #Function to set 00
    def setZero(self,text):
        currentText = self.displayText().strip()
        if currentText != '' and currentText[len(currentText)-1] not in ["(", ")","+","-","*","/"]:
            self.setDisplayText(currentText+text)

#Evaluate expressions
def evaluateExpression(expression):
    try:
        result = str(eval(expression,{},{}))
    except Exception:
        result = ERROR_MSG
    return result

app = QtWidgets.QApplication(sys.argv)

my_mainWindow = MainWindow()
my_mainWindow.show()

sys.exit(app.exec_())
