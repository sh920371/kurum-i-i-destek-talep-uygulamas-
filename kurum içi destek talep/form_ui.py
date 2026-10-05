# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 650)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        
        # --- TAB 1: Bilgi İşlem ---
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab1_layout = QHBoxLayout(self.tab)
        self.tab1_layout.setContentsMargins(10, 10, 10, 10)
        self.tab1_layout.setSpacing(15)
        
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumWidth(260)
        self.groupBox.setMaximumWidth(320)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSpacing(8)
        
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.groupBox)
        for _ in range(6): self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.verticalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.groupBox)
        for _ in range(6): self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.verticalLayout.addWidget(self.comboBox_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.tab1_layout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_gb2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_gb2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_gb2.setSpacing(10)
        
        self.tableWidget = QTableWidget(self.groupBox_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.verticalLayout_gb2.addWidget(self.tableWidget)
        
        self.frame = QFrame(self.groupBox_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        
        self.horizontalLayout_frame1 = QHBoxLayout(self.frame)
        self.horizontalLayout_frame1.setContentsMargins(5, 5, 5, 5)
        
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.horizontalLayout_frame1.addWidget(self.label_5)
        
        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.horizontalLayout_frame1.addWidget(self.comboBox_3)
        
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.horizontalLayout_frame1.addWidget(self.pushButton_2)
        
        self.verticalLayout_gb2.addWidget(self.frame)
        self.tab1_layout.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")

        # --- TAB 2: Yazı İşleri ---
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab2_layout = QHBoxLayout(self.tab_2)
        self.tab2_layout.setContentsMargins(10, 10, 10, 10)
        self.tab2_layout.setSpacing(15)
        
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumWidth(260)
        self.groupBox_3.setMaximumWidth(320)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSpacing(8)
        
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.verticalLayout_2.addWidget(self.label_6)

        self.comboBox_4 = QComboBox(self.groupBox_3)
        for _ in range(6): self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.verticalLayout_2.addWidget(self.comboBox_4)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.verticalLayout_2.addWidget(self.label_7)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.verticalLayout_2.addWidget(self.label_9)

        self.textEdit_2 = QTextEdit(self.groupBox_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.tab2_layout.addWidget(self.groupBox_3)

        self.groupBox_6 = QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_gb6 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_gb6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_gb6.setSpacing(10)
        
        self.tableWidget_2 = QTableWidget(self.groupBox_6)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.verticalLayout_gb6.addWidget(self.tableWidget_2)
        
        self.frame_2 = QFrame(self.groupBox_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        
        self.horizontalLayout_frame2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_frame2.setContentsMargins(5, 5, 5, 5)
        
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.horizontalLayout_frame2.addWidget(self.label_15)
        
        self.comboBox_7 = QComboBox(self.frame_2)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.horizontalLayout_frame2.addWidget(self.comboBox_7)
        
        self.pushButton_6 = QPushButton(self.frame_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.horizontalLayout_frame2.addWidget(self.pushButton_6)
        
        self.verticalLayout_gb6.addWidget(self.frame_2)
        self.tab2_layout.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.tab_2, "")

        # --- TAB 3: İdari Hizmetler ---
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab3_layout = QHBoxLayout(self.tab_3)
        self.tab3_layout.setContentsMargins(10, 10, 10, 10)
        self.tab3_layout.setSpacing(15)
        
        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumWidth(260)
        self.groupBox_4.setMaximumWidth(320)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSpacing(8)
        
        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.verticalLayout_3.addWidget(self.label_8)

        self.comboBox_5 = QComboBox(self.groupBox_4)
        for _ in range(11): self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.verticalLayout_3.addWidget(self.comboBox_5)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.verticalLayout_3.addWidget(self.label_10)

        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        self.verticalLayout_3.addWidget(self.label_11)

        self.textEdit_3 = QTextEdit(self.groupBox_4)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.verticalLayout_3.addWidget(self.textEdit_3)

        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.tab3_layout.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_gb7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_gb7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_gb7.setSpacing(10)
        
        self.tableWidget_3 = QTableWidget(self.groupBox_7)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.verticalLayout_gb7.addWidget(self.tableWidget_3)
        
        self.frame_3 = QFrame(self.groupBox_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        
        self.horizontalLayout_frame3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_frame3.setContentsMargins(5, 5, 5, 5)
        
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.horizontalLayout_frame3.addWidget(self.label_16)
        
        self.comboBox_8 = QComboBox(self.frame_3)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.horizontalLayout_frame3.addWidget(self.comboBox_8)
        
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.horizontalLayout_frame3.addWidget(self.pushButton_7)
        
        self.verticalLayout_gb7.addWidget(self.frame_3)
        self.tab3_layout.addWidget(self.groupBox_7)
        self.tabWidget.addTab(self.tab_3, "")

        # --- TAB 4: Hukuk İşleri ---
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab4_layout = QHBoxLayout(self.tab_4)
        self.tab4_layout.setContentsMargins(10, 10, 10, 10)
        self.tab4_layout.setSpacing(15)
        
        self.groupBox_5 = QGroupBox(self.tab_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumWidth(260)
        self.groupBox_5.setMaximumWidth(320)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSpacing(8)
        
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        self.verticalLayout_4.addWidget(self.label_12)

        self.comboBox_6 = QComboBox(self.groupBox_5)
        for _ in range(7): self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.verticalLayout_4.addWidget(self.comboBox_6)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")
        self.verticalLayout_4.addWidget(self.label_13)

        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.verticalLayout_4.addWidget(self.lineEdit_4)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        self.verticalLayout_4.addWidget(self.label_14)

        self.textEdit_4 = QTextEdit(self.groupBox_5)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.verticalLayout_4.addWidget(self.textEdit_4)

        self.pushButton_5 = QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.tab4_layout.addWidget(self.groupBox_5)

        self.groupBox_8 = QGroupBox(self.tab_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_gb8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_gb8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_gb8.setSpacing(10)
        
        self.tableWidget_4 = QTableWidget(self.groupBox_8)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.verticalLayout_gb8.addWidget(self.tableWidget_4)
        
        self.frame_4 = QFrame(self.groupBox_8)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        
        self.horizontalLayout_frame4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_frame4.setContentsMargins(5, 5, 5, 5)
        
        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.horizontalLayout_frame4.addWidget(self.label_17)
        
        self.comboBox_9 = QComboBox(self.frame_4)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.horizontalLayout_frame4.addWidget(self.comboBox_9)
        
        self.pushButton_8 = QPushButton(self.frame_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.horizontalLayout_frame4.addWidget(self.pushButton_8)
        
        self.verticalLayout_gb8.addWidget(self.frame_4)
        self.tab4_layout.addWidget(self.groupBox_8)
        self.tabWidget.addTab(self.tab_4, "")

        # --- TAB 5: Ortak Duyuru/İstek ---
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab5_layout = QHBoxLayout(self.tab_5)
        self.tab5_layout.setContentsMargins(10, 10, 10, 10)
        self.tab5_layout.setSpacing(15)
        
        self.groupBox_9 = QGroupBox(self.tab_5)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumWidth(260)
        self.groupBox_9.setMaximumWidth(320)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSpacing(8)
        
        self.label_18 = QLabel(self.groupBox_9)
        self.label_18.setObjectName(u"label_18")
        self.verticalLayout_5.addWidget(self.label_18)

        self.comboBox_10 = QComboBox(self.groupBox_9)
        for _ in range(7): self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.verticalLayout_5.addWidget(self.comboBox_10)

        self.label_19 = QLabel(self.groupBox_9)
        self.label_19.setObjectName(u"label_19")
        self.verticalLayout_5.addWidget(self.label_19)

        self.lineEdit_5 = QLineEdit(self.groupBox_9)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.verticalLayout_5.addWidget(self.lineEdit_5)

        self.label_20 = QLabel(self.groupBox_9)
        self.label_20.setObjectName(u"label_20")
        self.verticalLayout_5.addWidget(self.label_20)

        self.textEdit_5 = QTextEdit(self.groupBox_9)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.verticalLayout_5.addWidget(self.textEdit_5)

        self.pushButton_9 = QPushButton(self.groupBox_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.verticalLayout_5.addWidget(self.pushButton_9)

        self.tab5_layout.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.tab_5)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_gb10 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_gb10.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_gb10.setSpacing(10)
        
        self.tableWidget_5 = QTableWidget(self.groupBox_10)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.verticalLayout_gb10.addWidget(self.tableWidget_5)
        
        self.frame_5 = QFrame(self.groupBox_10)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        
        self.horizontalLayout_frame5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_frame5.setContentsMargins(5, 5, 5, 5)
        
        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.horizontalLayout_frame5.addWidget(self.label_21)
        
        self.comboBox_11 = QComboBox(self.frame_5)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.horizontalLayout_frame5.addWidget(self.comboBox_11)
        
        self.pushButton_10 = QPushButton(self.frame_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.horizontalLayout_frame5.addWidget(self.pushButton_10)
        
        self.verticalLayout_gb10.addWidget(self.frame_5)
        self.tab5_layout.addWidget(self.groupBox_10)
        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Yeni Destek Talebi", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cihaz T\u00fcr\u00fc:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Se\u00e7iniz", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Masa\u00fcst\u00fc Bilgisayar ", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Diz\u00fcst\u00fc Bilgisayar ", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Yaz\u0131c\u0131/Taray\u0131c\u0131", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"A\u011f/\u0130nternet", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Di\u011fer", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Departman/Personel:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Problem T\u00fcr\u00fc:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Se\u00e7iniz", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Yaz\u0131l\u0131msal Hata ", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Donan\u0131m Ar\u0131zas\u0131", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Ba\u011flant\u0131 Sorunu ", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Kurulum Talebi", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Di\u011fer", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131klama:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Destek Talebini G\u00f6nder", None))
        self.groupBox_2.setTitle("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Talebin Durumu:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Durumu G\u00fcncelle ve Kaydet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Bilgi \u0130\u015flem", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Yeni Destek Talebi", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Konu:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Se\u00e7iniz", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Gelen/Giden Evrak Kayd\u0131", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Ar\u015fiv/Dosyalama Talebi", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Resmi Yaz\u0131\u015fma \u0130\u015flemleri", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Tebligat/Posta \u0130\u015flemleri", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Di\u011fer", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Departman/Personel:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131klama:", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Destek Talebini G\u00f6nder", None))
        self.groupBox_6.setTitle("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Talebin Durumu:", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Durumu G\u00fcncelle ve Kaydet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Yaz\u0131 \u0130\u015fleri", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Yeni Destek Talebi", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Konu:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Se\u00e7iniz", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"Teknik Bak\u0131m/Onar\u0131m", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Sarf Malzeme/K\u0131rtasiye Talebi", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"Temizlik /Hijyen Talepleri", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"Demirba\u015f/Ofis Mobilyas\u0131 Talebi", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"Lojistik/Ta\u015f\u0131ma \u0130\u015flemleri", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"Yemekhane/ Kafeterya Hizmetleri", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"Resmi Ara\u00e7/\u015eof\u00f6r Talebi", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("MainWindow", u"G\u00fcvenlik/Kartl\u0131 Ge\u00e7i\u015f Sistemleri", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("MainWindow", u"Toplant\u0131/Konferans Salonu Rezervasyonu", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("MainWindow", u"Di\u011fer", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Departman/Personel:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131klama:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Destek Talebini G\u00f6nder", None))
        self.groupBox_7.setTitle("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Talebin Durumu:", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Durumu G\u00fcncelle ve Kaydet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0130dari Hizmetler", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Yeni Destek Talebi", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Konu:", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Se\u00e7iniz", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Hukuki M\u00fctalaa/G\u00f6r\u00fc\u015f Talebi ", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Dava \u0130tiraz/Savunma  Haz\u0131rl\u0131\u011f\u0131", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"S\u00f6zle\u015fme /Protokol \u0130ncelemesi ", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0130dari Soru\u015fturma/\u0130nceleme", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"Mevzuat/Y\u00f6netmelik De\u011fi\u015fikli\u011fi", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("MainWindow", u"Di\u011fer ", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Departman/Personel:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131klama:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Destek Talebini G\u00f6nder", None))
        self.groupBox_8.setTitle("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Talebin Durumu:", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Durumu G\u00fcncelle ve Kaydet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Hukuk \u0130\u015fleri", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Yeni Destek Talebi", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Kime:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Departman/Personel:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"A\u00e7\u0131klama:", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Destek Talebini G\u00f6nder", None))
        self.groupBox_10.setTitle("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7ili Talebin Durumu:", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Durumu G\u00fcncelle ve Kaydet", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Ortak Duyuru/\u0130stek", None))
    # retranslateUi
