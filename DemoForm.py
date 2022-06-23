# DemoForm.py 
# DemoForm.ui(디자인) + DemoForm.py(로직)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#디자인 파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]
#폼 클래스 정의
class DemoForm(QDialog, form_class):
    #생성자 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 데모~~")
#진입점 체크
if __name__ == "__main__":
    #실행프로세스 
    app = QApplication(sys.argv)
    #창을 실행 
    demoWindow = DemoForm()
    demoWindow.show() 
    #이벤트 처리 대기 
    app.exec_() 

