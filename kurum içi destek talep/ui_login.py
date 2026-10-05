# ui_login.py
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QStackedWidget
)

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget: QWidget):
        LoginWidget.setObjectName("LoginWidget")
        LoginWidget.resize(400, 480)
        LoginWidget.setMinimumSize(QSize(400, 480))
        
        # Arka plan ve şık tasarım için stil tanımlamaları
        LoginWidget.setStyleSheet("""
            QWidget {
                background-color: #f5f6fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QLabel {
                color: #2f3640;
                font-size: 13px;
                font-weight: bold;
            }
            QLineEdit {
                border: 2px solid #dcdde1;
                border-radius: 6px;
                padding: 10px;
                background-color: #ffffff;
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton#btn_kayit_ekrani, QPushButton#btn_giris_ekrani {
                background-color: transparent;
                color: #7f8c8d;
                font-size: 12px;
                text-decoration: underline;
                padding: 5px;
            }
            QPushButton#btn_kayit_ekrani:hover, QPushButton#btn_giris_ekrani:hover {
                color: #2c3e50;
            }
        """)

        # Giriş ve kayıt ekranları arasında geçiş için StackedWidget kullanıyoruz
        self.stackedWidget = QStackedWidget(LoginWidget)
        
        # ----- GİRİŞ SAYFASI -----
        self.page_giris = QWidget()
        self.layout_giris = QVBoxLayout(self.page_giris)
        self.layout_giris.setSpacing(12)
        self.layout_giris.setContentsMargins(30, 40, 30, 40)
        
        self.lbl_giris_baslik = QLabel("BİLGİ İŞLEM PORTALİ")
        self.lbl_giris_baslik.setStyleSheet("font-size: 20px; color: #2c3e50; margin-bottom: 15px;")
        self.lbl_giris_baslik.setAlignment(Qt.AlignCenter)
        self.layout_giris.addWidget(self.lbl_giris_baslik)

        self.layout_giris.addWidget(QLabel("Kullanıcı Adı:"))
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Kullanıcı adınızı girin...")
        self.layout_giris.addWidget(self.input_username)

        self.layout_giris.addWidget(QLabel("Şifre:"))
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setPlaceholderText("Şifrenizi girin...")
        self.layout_giris.addWidget(self.input_password)

        self.btn_giris = QPushButton("Sisteme Giriş Yap")
        self.layout_giris.addWidget(self.btn_giris)

        self.btn_goto_kayit = QPushButton("Hesabın yok mu? Kayıt Ol")
        self.btn_goto_kayit.setObjectName("btn_kayit_ekrani")
        self.layout_giris.addWidget(self.btn_goto_kayit)
        
        self.stackedWidget.addWidget(self.page_giris)

        # ----- KAYIT SAYFASI -----
        self.page_kayit = QWidget()
        self.layout_kayit = QVBoxLayout(self.page_kayit)
        self.layout_kayit.setSpacing(12)
        self.layout_kayit.setContentsMargins(30, 40, 30, 40)

        self.lbl_kayit_baslik = QLabel("YENİ KULLANICI KAYDI")
        self.lbl_kayit_baslik.setStyleSheet("font-size: 18px; color: #27ae60; margin-bottom: 15px;")
        self.lbl_kayit_baslik.setAlignment(Qt.AlignCenter)
        self.layout_kayit.addWidget(self.lbl_kayit_baslik)

        self.layout_kayit.addWidget(QLabel("Kullanıcı Adı Belirleyin:"))
        self.reg_username = QLineEdit()
        self.reg_username.setPlaceholderText("Örn: ahmet")
        self.layout_kayit.addWidget(self.reg_username)

        self.layout_kayit.addWidget(QLabel("Şifre Belirleyin:"))
        self.reg_password = QLineEdit()
        self.reg_password.setEchoMode(QLineEdit.Password)
        self.reg_password.setPlaceholderText("Güçlü bir şifre girin...")
        self.layout_kayit.addWidget(self.reg_password)

        self.btn_kayit = QPushButton("Hesabı Oluştur ve Kaydet")
        self.layout_kayit.addWidget(self.btn_kayit)

        self.btn_goto_giris = QPushButton("Zaten hesabım var, Giriş Yap")
        self.btn_goto_giris.setObjectName("btn_giris_ekrani")
        self.layout_kayit.addWidget(self.btn_goto_giris)

        self.stackedWidget.addWidget(self.page_kayit)

        # Ana widget layoutu
        main_layout = QVBoxLayout(LoginWidget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.stackedWidget)