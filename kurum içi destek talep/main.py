import sys
import os
import csv
import json
#from PySide6.QtSvg import QSvgRenderer
from datetime import datetime
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox, QWidget,
    QTableWidgetItem, QHeaderView, QRadioButton, QButtonGroup, QStackedWidget,
    QTextEdit
)
from PySide6.QtGui import QFont, QColor, QPalette,QIcon,QPixmap

# Import the compiled UI class
from form_ui import Ui_MainWindow

# File Paths
DATA_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_CSV = os.path.join(DATA_DIR, "kullanicilar.csv")
REQUESTS_JSON = os.path.join(DATA_DIR, "talepler.json")



def init_files():
    """Initializes CSV and JSON files if they don't exist."""
    if not os.path.exists(USERS_CSV):
        with open(USERS_CSV, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password", "name", "department", "is_admin"])
            # Add some initial admin and user for quick testing
            writer.writerow(["it_admin", "1234", "Ahmet Yilmaz", "Bilgi Islem", "True"])
            writer.writerow(["user1", "1234", "Zeynep Kaya", "Bilgi Islem", "False"])
            writer.writerow(["yazi_admin", "1234", "Ayse Demir", "Yazi Isleri", "True"])
            writer.writerow(["user2", "1234", "Mehmet Sahin", "Yazi Isleri", "False"])
            
    if not os.path.exists(REQUESTS_JSON):
        with open(REQUESTS_JSON, mode='w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)

def load_users():
    """Loads users list from CSV."""
    users = []
    if os.path.exists(USERS_CSV):
        with open(USERS_CSV, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["is_admin"] = row["is_admin"] == "True"
                users.append(row)
    return users

def save_user_to_csv(username, password, name, department, is_admin):
    """Saves a new user to the CSV file."""
    with open(USERS_CSV, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([username, password, name, department, str(is_admin)])

def load_requests():
    """Loads support requests from JSON."""
    if os.path.exists(REQUESTS_JSON):
        with open(REQUESTS_JSON, mode='r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_requests(requests):
    """Saves requests to JSON."""
    with open(REQUESTS_JSON, mode='w', encoding='utf-8') as f:
        json.dump(requests, f, ensure_ascii=False, indent=4)


# Global Modern Light QSS stylesheet
MODERN_STYLE = """
QMainWindow, QDialog {
    background-color: #ffffff;
    color: #0f172a;
    font-family: 'Segoe UI', Arial, sans-serif;
}

QLabel {
    color: #334155;
    font-size: 13px;
    font-weight: 500;
}

QGroupBox {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 12px;
    margin-top: 15px;
    font-size: 14px;
    font-weight: bold;
    color: #141414;
    padding-top: 15px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 15px;
    padding: 0 5px;
}

QLineEdit, QTextEdit, QComboBox {
    background-color: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 6px;
    color: #0f172a;
    font-size: 13px;
}

QLineEdit:focus, QTextEdit:focus, QComboBox:focus {
    border: 1.5px solid #141414;
}

QComboBox::drop-down {
    border: 0px;
}

QPushButton {
    background-color: #141414;
    color: #ffffff;
    border: none;
    border-radius: 6px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #d1d5db;
}

QPushButton:pressed {
    background-color: #d1d5db;
}

QTabWidget::pane {
    border: 1px solid #d1d5db;
    background-color: #ffffff;
    border-radius: 8px;
}

QTabBar::tab {
    background-color: #f1f1f6;
    border: 1px solid #d1d5db;
    border-bottom-color: none;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    padding: 10px 16px;
    color: #a5a9ae;
    font-size: 13px;
    font-weight: bold;
}

QTabBar::tab:selected {
    background-color: #ffffff;
    border-bottom: 2px solid #141414;
    color: #141414;
}

QTabBar::tab:hover {
    color: #0f172a;
    background-color: #ffffff;
}

QTableWidget {
    background-color: #ffffff;
    border: 1px solid #ffffff;
    gridline-color: #f1f1f6;
    color: #0f172a;
    border-radius: 8px;
}

QTableWidget::item {
    padding: 5px;
}

QTableWidget::item:selected {
    background-color: #f1f1f6;
    color: #141414;
}

QHeaderView::section {
    background-color: #f1f1f6;
    color: #141414;
    padding: 6px;
    border: 1px solid #d1d5db;
    font-weight: bold;
    font-size: 12px;
}

QScrollBar:vertical {
    border: none;
    background-color: #f1f1f6;
    width: 10px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background-color: #141414;
    border-radius: 5px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #f1f1f6;
}

QDialog QLabel {
    color: #0f172a;
}
"""

class AuthDialog(QDialog):
    """A combined Login and Registration dialog with premium dark look."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sistem Giriş & Kayıt")
        self.setFixedSize(400, 480)
        self.user_data = None
        
        # Main Layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header / Title
        self.title_label = QLabel("KURUM İÇİ DESTEK SİSTEMİ", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont("Segoe UI", 16, QFont.Weight.Bold)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("font-weight: bold; color: #141414; margin-bottom: 20px;")
        self.main_layout.addWidget(self.title_label)
        
        # Stacked Widget to switch between Login and Register views
        self.stacked_widget = QStackedWidget(self)
        self.main_layout.addWidget(self.stacked_widget)
        
        # 1. Login Widget
        self.login_widget = QWidget()
        login_layout = QVBoxLayout(self.login_widget)
        login_layout.setSpacing(12)
        
        login_lbl = QLabel("Lütfen giriş yapın:")
        login_lbl.setStyleSheet("font-size: 14px; font-weight: bold; color: #141414;")
        login_layout.addWidget(login_lbl)
        
        self.login_username = QLineEdit()
        self.login_username.setPlaceholderText("Kullanıcı Adı")
        login_layout.addWidget(self.login_username)
        
        self.login_password = QLineEdit()
        self.login_password.setPlaceholderText("Şifre")
        self.login_password.setEchoMode(QLineEdit.EchoMode.Password)
        login_layout.addWidget(self.login_password)
        
        self.btn_login = QPushButton("Giriş Yap")
        self.btn_login.setFixedHeight(38)
        self.btn_login.clicked.connect(self.handle_login)
        login_layout.addWidget(self.btn_login)
        
        btn_go_register = QPushButton("Hesabınız yok mu? Kaydolun")
        btn_go_register.setStyleSheet("background-color: transparent; color: #141414; border: none; text-decoration: underline;")
        btn_go_register.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        login_layout.addWidget(btn_go_register)
        
        self.stacked_widget.addWidget(self.login_widget)
        
        # 2. Register Widget
        self.register_widget = QWidget()
        reg_layout = QVBoxLayout(self.register_widget)
        reg_layout.setSpacing(10)
        
        reg_lbl = QLabel("Yeni Hesap Oluşturun:")
        reg_lbl.setStyleSheet("font-size: 14px; font-weight: bold; color: #141414;")
        reg_layout.addWidget(reg_lbl)
        
        self.reg_username = QLineEdit()
        self.reg_username.setPlaceholderText("Kullanıcı Adı")
        reg_layout.addWidget(self.reg_username)
        
        self.reg_password = QLineEdit()
        self.reg_password.setPlaceholderText("Şifre")
        self.reg_password.setEchoMode(QLineEdit.EchoMode.Password)
        reg_layout.addWidget(self.reg_password)
        
        self.reg_name = QLineEdit()
        self.reg_name.setPlaceholderText("Ad Soyad")
        reg_layout.addWidget(self.reg_name)
        
        self.reg_dept = QComboBox()
        self.reg_dept.addItems(["Bilgi İşlem", "Yazı İşleri", "İdari Hizmetler", "Hukuk İşleri", "Genel"])
        reg_layout.addWidget(self.reg_dept)
        
        # Role Choice: Admin or Employee
        role_layout = QHBoxLayout()
        role_label = QLabel("Yetki:")
        role_layout.addWidget(role_label)
        self.role_combo = QComboBox()
        self.role_combo.addItems(["Çalışan", "Yönetici (Admin)"])
        role_layout.addWidget(self.role_combo)
        reg_layout.addLayout(role_layout)
        
        self.btn_register = QPushButton("Kaydol")
        self.btn_register.setFixedHeight(38)
        self.btn_register.clicked.connect(self.handle_register)
        reg_layout.addWidget(self.btn_register)
        
        btn_go_login = QPushButton("Zaten hesabınız var mı? Giriş Yapın")
        btn_go_login.setStyleSheet("background-color: transparent; color: #141414; border: none; text-decoration: underline;")
        btn_go_login.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        reg_layout.addWidget(btn_go_login)
        
        self.stacked_widget.addWidget(self.register_widget)
        
        # Set default active index
        self.stacked_widget.setCurrentIndex(0)
        icon_path = os.path.join(DATA_DIR, "path5.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Hata: Giriş ekranı için ikon bulunamadı! Yol: {icon_path}")

    def handle_login(self):
        username = self.login_username.text().strip()
        password = self.login_password.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun!")
            return
            
        users = load_users()
        for u in users:
            if u["username"] == username and u["password"] == password:
                self.user_data = u
                self.accept()
                return
                
        QMessageBox.critical(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

    def handle_register(self):
        username = self.reg_username.text().strip()
        password = self.reg_password.text().strip()
        name = self.reg_name.text().strip()
        dept = self.reg_dept.currentText()
        is_admin = self.role_combo.currentIndex() == 1 # Index 1 is Yönetici (Admin)
        
        if not username or not password or not name:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun!")
            return
            
        # Check if username exists
        users = load_users()
        for u in users:
            if u["username"] == username:
                QMessageBox.critical(self, "Hata", "Bu kullanıcı adı zaten alınmış!")
                return
                
        # Save user
        save_user_to_csv(username, password, name, dept, is_admin)
        QMessageBox.information(self, "Başarılı", "Kayıt işlemi tamamlandı! Şimdi giriş yapabilirsiniz.")
        
        # Clear fields and switch to login tab
        self.reg_username.clear()
        self.reg_password.clear()
        self.reg_name.clear()
        self.stacked_widget.setCurrentIndex(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_data):
        super().__init__()
        self.setupUi(self)
        self.current_user = user_data
        icon_path = os.path.join(DATA_DIR, "path5.png")
        self.setWindowIcon(QIcon(icon_path))
        # Setup window details
        self.setWindowTitle(f"Kurum İçi İstek Destek Sistemi - {self.current_user['name']} ({self.current_user['department']})")
        
        # Setup tables headers and behavior
        self.setup_tables()
        
        # Populate Comboboxes with Status Choices
        self.setup_status_combos()
        
        # Populate Tab 5 dynamic fields
        self.update_tab5_recipients()
        
        # Apply role based UI visibility rules
        self.apply_role_visibility()
        
        # Connect buttons to actions
        self.connect_events()
        
        # Load active requests into tables
        self.refresh_all_tables()

    def setup_tables(self):
        """Sets column headers, count, and resizing behavior for all tables."""
        # Tab 1: Bilgi İşlem Table
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Gönderen", "Cihaz Türü", "Problem Türü", "Açıklama", "Durum", "Tarih"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch) # Description stretch
        self.tableWidget.itemSelectionChanged.connect(lambda: self.on_row_selected(self.tableWidget, self.comboBox_3))
        
        # Tab 2: Yazı İşleri Table
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setHorizontalHeaderLabels(["ID", "Gönderen", "Konu", "Açıklama", "Durum", "Tarih"])
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_2.itemSelectionChanged.connect(lambda: self.on_row_selected(self.tableWidget_2, self.comboBox_7))
        
        # Tab 3: İdari Hizmetler Table
        self.tableWidget_3.setColumnCount(6)
        self.tableWidget_3.setHorizontalHeaderLabels(["ID", "Gönderen", "Konu", "Açıklama", "Durum", "Tarih"])
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_3.itemSelectionChanged.connect(lambda: self.on_row_selected(self.tableWidget_3, self.comboBox_8))
        
        # Tab 4: Hukuk İşleri Table
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setHorizontalHeaderLabels(["ID", "Gönderen", "Konu", "Açıklama", "Durum", "Tarih"])
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_4.itemSelectionChanged.connect(lambda: self.on_row_selected(self.tableWidget_4, self.comboBox_9))
        
        # Tab 5: Ortak Duyuru/İstek Table
        self.tableWidget_5.setColumnCount(6)
        self.tableWidget_5.setHorizontalHeaderLabels(["ID", "Gönderen", "Alıcı (Kime)", "Açıklama", "Durum", "Tarih"])
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.tableWidget_5.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.tableWidget_5.itemSelectionChanged.connect(lambda: self.on_row_selected(self.tableWidget_5, self.comboBox_11))

        # Double click handler to view full cell content (long description reading)
        for table in [self.tableWidget, self.tableWidget_2, self.tableWidget_3, self.tableWidget_4, self.tableWidget_5]:
            table.cellDoubleClicked.connect(self.show_full_cell_text)

    def show_full_cell_text(self, row, column):
        """Displays full cell text in a clean popup reader window on double-click."""
        item = self.sender().item(row, column)
        if item:
            text = item.text()
            dialog = QDialog(self)
            dialog.setWindowTitle("Detaylı Bilgi Görünümü")
            dialog.setMinimumSize(450, 320)
            
            layout = QVBoxLayout(dialog)
            layout.setContentsMargins(15, 15, 15, 15)
            layout.setSpacing(12)
            
            lbl = QLabel("Seçili Hücre İçeriği:", dialog)
            lbl.setStyleSheet("font-weight: bold; color: #141414;")
            layout.addWidget(lbl)
            
            text_edit = QTextEdit(dialog)
            text_edit.setPlainText(text)
            text_edit.setReadOnly(True)
            text_edit.setStyleSheet("background-color: #ffffff; border: 1px solid #f1f1f6; border-radius: 6px; padding: 10px; color: #0f172a; font-size: 13px;")
            layout.addWidget(text_edit)
            
            btn_close = QPushButton("Kapat", dialog)
            btn_close.clicked.connect(dialog.accept)
            btn_close.setStyleSheet("background-color: #141414; color: white; padding: 8px; font-weight: bold; border-radius: 6px;")
            layout.addWidget(btn_close)
            
            dialog.exec()

    def setup_status_combos(self):
        """Populates status comboboxes with choices."""
        status_list = ["Beklemede", "İşleme Alındı", "Tamamlandı"]
        for combo in [self.comboBox_3, self.comboBox_7, self.comboBox_8, self.comboBox_9, self.comboBox_11]:
            combo.clear()
            combo.addItems(status_list)

    def update_tab5_recipients(self):
        """Populates the Tab 5 'Kime' (To) combobox from kullanicilar.csv."""
        self.comboBox_10.clear()
        self.comboBox_10.addItem("Herkese", "Herkese")
        
        users = load_users()
        for u in users:
            # Exclude current user from their own recipient list
            if u["username"] != self.current_user["username"]:
                display_name = f"{u['name']} ({u['department']} - {'Yönetici' if u['is_admin'] else 'Çalışan'})"
                self.comboBox_10.addItem(display_name, u["username"])

    def apply_role_visibility(self):
        """
        Applies visibility rules:
        - If Admin of department X:
          - Hide request creation box for Tab X
          - Show/Enable status update panel for Tab X
          - Hide/Disable status update panels for other Tabs
        - If NOT Admin:
          - Show request creation for all Tabs
          - Hide status update panels for Tab 1, 2, 3, 4
          - Show status update panel for Tab 5 (Ortak) so anyone can complete tasks sent to them.
        """
        is_admin = self.current_user["is_admin"]
        dept = self.current_user["department"]
        
        # Default all tabs to normal employee visibility first
        self.groupBox.setVisible(True) # Tab 1 New Req
        self.frame.setVisible(False)   # Tab 1 Status update frame
        
        self.groupBox_3.setVisible(True) # Tab 2 New Req
        self.frame_2.setVisible(False)   # Tab 2 Status
        
        self.groupBox_4.setVisible(True) # Tab 3 New Req
        self.frame_3.setVisible(False)   # Tab 3 Status
        
        self.groupBox_5.setVisible(True) # Tab 4 New Req
        self.frame_4.setVisible(False)   # Tab 4 Status
        
        # Tab 5 (Ortak) is always visible and the status update frame is visible for completing/deleting tasks.
        self.groupBox_9.setVisible(True)
        self.frame_5.setVisible(True)
        
        # Auto-populate sender's department/personel line edits with current user name
        self.lineEdit.setText(f"{dept} / {self.current_user['name']}")
        self.lineEdit_2.setText(f"{dept} / {self.current_user['name']}")
        self.lineEdit_3.setText(f"{dept} / {self.current_user['name']}")
        self.lineEdit_4.setText(f"{dept} / {self.current_user['name']}")
        self.lineEdit_5.setText(f"{dept} / {self.current_user['name']}")
        
        # Lock these fields so they can't easily forge sender names
        for le in [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.lineEdit_5]:
            le.setReadOnly(True)
            
        if is_admin:
            if dept == "Bilgi İşlem":
                self.groupBox.setVisible(False)
                self.frame.setVisible(True)
            elif dept == "Yazı İşleri":
                self.groupBox_3.setVisible(False)
                self.frame_2.setVisible(True)
            elif dept == "İdari Hizmetler":
                self.groupBox_4.setVisible(False)
                self.frame_3.setVisible(True)
            elif dept == "Hukuk İşleri":
                self.groupBox_5.setVisible(False)
                self.frame_4.setVisible(True)

    def connect_events(self):
        """Connects UI buttons to their backend controller slots."""
        # Send Request buttons
        self.pushButton.clicked.connect(self.send_it_request)
        self.pushButton_3.clicked.connect(self.send_yazi_request)
        self.pushButton_4.clicked.connect(self.send_idari_request)
        self.pushButton_5.clicked.connect(self.send_hukuk_request)
        self.pushButton_9.clicked.connect(self.send_ortak_request)
        
        # Update Status buttons
        self.pushButton_2.clicked.connect(lambda: self.update_request_status(self.tableWidget, self.comboBox_3, "Bilgi İşlem"))
        self.pushButton_6.clicked.connect(lambda: self.update_request_status(self.tableWidget_2, self.comboBox_7, "Yazı İşleri"))
        self.pushButton_7.clicked.connect(lambda: self.update_request_status(self.tableWidget_3, self.comboBox_8, "İdari Hizmetler"))
        self.pushButton_8.clicked.connect(lambda: self.update_request_status(self.tableWidget_4, self.comboBox_9, "Hukuk İşleri"))
        self.pushButton_10.clicked.connect(lambda: self.update_request_status(self.tableWidget_5, self.comboBox_11, "Ortak"))

    def refresh_all_tables(self):
        """Reloads and repopulates all tables from file."""
        requests = load_requests()
        
        self.populate_table(self.tableWidget, [r for r in requests if r["department"] == "Bilgi İşlem"])
        self.populate_table(self.tableWidget_2, [r for r in requests if r["department"] == "Yazı İşleri"])
        self.populate_table(self.tableWidget_3, [r for r in requests if r["department"] == "İdari Hizmetler"])
        self.populate_table(self.tableWidget_4, [r for r in requests if r["department"] == "Hukuk İşleri"])
        
        # Tab 5 (Ortak) Filter: Show tasks sent to this user, or sent by this user, or sent to "Herkese"
        ortak_requests = []
        for r in requests:
            if r["department"] == "Ortak":
                is_sender = r["sender_username"] == self.current_user["username"]
                is_recipient = r["recipient"] == self.current_user["username"]
                is_everyone = r["recipient"] == "Herkese"
                if is_sender or is_recipient or is_everyone:
                    ortak_requests.append(r)
        self.populate_table(self.tableWidget_5, ortak_requests, is_ortak=True)

    def populate_table(self, table_widget, requests_list, is_ortak=False):
        """Fills a target table with data items."""
        table_widget.setRowCount(0)
        # Disable sorting temporarily during load
        table_widget.setSortingEnabled(False)
        
        for req in requests_list:
            row_idx = table_widget.rowCount()
            table_widget.insertRow(row_idx)
            
            # Helper to create un-editable cell item
            def make_item(text):
                item = QTableWidgetItem(str(text))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                return item
                
            if not is_ortak:
                # Normal department fields
                # ID, Gönderen, field1 (Cihaz/Konu), field2 (Problem, optional), Açıklama, Durum, Tarih
                table_widget.setItem(row_idx, 0, make_item(req["id"]))
                table_widget.setItem(row_idx, 1, make_item(req["sender_info"]))
                
                # Check column counts to determine what column holds what
                if req["department"] == "Bilgi İşlem":
                    table_widget.setItem(row_idx, 2, make_item(req.get("device_type", "")))
                    table_widget.setItem(row_idx, 3, make_item(req.get("problem_type", "")))
                    table_widget.setItem(row_idx, 4, make_item(req["description"]))
                    table_widget.setItem(row_idx, 5, make_item(req["status"]))
                    table_widget.setItem(row_idx, 6, make_item(req["created_at"]))
                else:
                    table_widget.setItem(row_idx, 2, make_item(req.get("subject", "")))
                    table_widget.setItem(row_idx, 3, make_item(req["description"]))
                    table_widget.setItem(row_idx, 4, make_item(req["status"]))
                    table_widget.setItem(row_idx, 5, make_item(req["created_at"]))
            else:
                # Ortak Duyuru / İstek Fields
                # ID, Gönderen, Alıcı (Kime), Açıklama, Durum, Tarih
                table_widget.setItem(row_idx, 0, make_item(req["id"]))
                table_widget.setItem(row_idx, 1, make_item(req["sender_info"]))
                
                # Map username recipient back to full name if possible
                recipient_val = req.get("recipient", "")
                if recipient_val != "Herkese":
                    users = load_users()
                    recipient_name = recipient_val
                    for u in users:
                        if u["username"] == recipient_val:
                            recipient_name = u["name"]
                            break
                    table_widget.setItem(row_idx, 2, make_item(recipient_name))
                else:
                    table_widget.setItem(row_idx, 2, make_item("Herkese"))
                    
                table_widget.setItem(row_idx, 3, make_item(req["description"]))
                table_widget.setItem(row_idx, 4, make_item(req["status"]))
                table_widget.setItem(row_idx, 5, make_item(req["created_at"]))

    def on_row_selected(self, table_widget, status_combo):
        """Synchronizes status combo box with the currently selected request row."""
        selected_ranges = table_widget.selectedRanges()
        if not selected_ranges:
            return
            
        row = selected_ranges[0].topRow()
        # Find the status column (second to last column before Date)
        status_col = table_widget.columnCount() - 2
        status_item = table_widget.item(row, status_col)
        if status_item:
            current_status = status_item.text()
            idx = status_combo.findText(current_status)
            if idx >= 0:
                status_combo.setCurrentIndex(idx)

    def add_new_request(self, department, form_data):
        """Helper to create and save a request to the JSON storage."""
        requests = load_requests()
        
        # Generate new ID
        new_id = 1
        if requests:
            new_id = max(r["id"] for r in requests) + 1
            
        new_request = {
            "id": new_id,
            "department": department,
            "sender_username": self.current_user["username"],
            "sender_name": self.current_user["name"],
            "status": "Beklemede",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        new_request.update(form_data)
        
        requests.append(new_request)
        save_requests(requests)
        
        QMessageBox.information(self, "Başarılı", "Talebiniz başarıyla gönderildi.")
        self.refresh_all_tables()

    # --- SEND SLOTS ---
    def send_it_request(self):
        device = self.comboBox.currentText()
        problem = self.comboBox_2.currentText()
        sender_info = self.lineEdit.text().strip()
        description = self.textEdit.toPlainText().strip()
        
        if self.comboBox.currentIndex() == 0 or self.comboBox_2.currentIndex() == 0 or not description:
            QMessageBox.warning(self, "Eksik Alan", "Lütfen tüm seçimleri yapın ve açıklama girin!")
            return
            
        form_data = {
            "sender_info": sender_info,
            "device_type": device,
            "problem_type": problem,
            "description": description
        }
        self.add_new_request("Bilgi İşlem", form_data)
        
        # Reset inputs
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.textEdit.clear()

    def send_yazi_request(self):
        subject = self.comboBox_4.currentText()
        sender_info = self.lineEdit_2.text().strip()
        description = self.textEdit_2.toPlainText().strip()
        
        if self.comboBox_4.currentIndex() == 0 or not description:
            QMessageBox.warning(self, "Eksik Alan", "Lütfen bir konu seçin ve açıklama girin!")
            return
            
        form_data = {
            "sender_info": sender_info,
            "subject": subject,
            "description": description
        }
        self.add_new_request("Yazı İşleri", form_data)
        
        self.comboBox_4.setCurrentIndex(0)
        self.textEdit_2.clear()

    def send_idari_request(self):
        subject = self.comboBox_5.currentText()
        sender_info = self.lineEdit_3.text().strip()
        description = self.textEdit_3.toPlainText().strip()
        
        if self.comboBox_5.currentIndex() == 0 or not description:
            QMessageBox.warning(self, "Eksik Alan", "Lütfen bir konu seçin ve açıklama girin!")
            return
            
        form_data = {
            "sender_info": sender_info,
            "subject": subject,
            "description": description
        }
        self.add_new_request("İdari Hizmetler", form_data)
        
        self.comboBox_5.setCurrentIndex(0)
        self.textEdit_3.clear()

    def send_hukuk_request(self):
        subject = self.comboBox_6.currentText()
        sender_info = self.lineEdit_4.text().strip()
        description = self.textEdit_4.toPlainText().strip()
        
        if self.comboBox_6.currentIndex() == 0 or not description:
            QMessageBox.warning(self, "Eksik Alan", "Lütfen bir konu seçin ve açıklama girin!")
            return
            
        form_data = {
            "sender_info": sender_info,
            "subject": subject,
            "description": description
        }
        self.add_new_request("Hukuk İşleri", form_data)
        
        self.comboBox_6.setCurrentIndex(0)
        self.textEdit_4.clear()

    def send_ortak_request(self):
        recipient_idx = self.comboBox_10.currentIndex()
        recipient_username = self.comboBox_10.itemData(recipient_idx)
        sender_info = self.lineEdit_5.text().strip()
        description = self.textEdit_5.toPlainText().strip()
        
        if not description:
            QMessageBox.warning(self, "Eksik Alan", "Lütfen bir açıklama girin!")
            return
            
        form_data = {
            "sender_info": sender_info,
            "recipient": recipient_username,
            "description": description
        }
        self.add_new_request("Ortak", form_data)
        
        self.comboBox_10.setCurrentIndex(0)
        self.textEdit_5.clear()

    # --- UPDATE STATUS SLOT ---
    def update_request_status(self, table_widget, status_combo, department):
        """Updates or completes/deletes a request status in JSON and reloads."""
        selected_ranges = table_widget.selectedRanges()
        if not selected_ranges:
            QMessageBox.warning(self, "Seçim Yok", "Lütfen durumunu güncellemek istediğiniz satırı seçin!")
            return
            
        row = selected_ranges[0].topRow()
        request_id_item = table_widget.item(row, 0)
        if not request_id_item:
            return
            
        request_id = int(request_id_item.text())
        new_status = status_combo.currentText()
        
        requests = load_requests()
        
        # Check if the status is "Tamamlandı" - if so, delete it
        if new_status == "Tamamlandı":
            # Filter out this request (deletes it)
            requests = [r for r in requests if r["id"] != request_id]
            save_requests(requests)
            QMessageBox.information(self, "İşlem Tamamlandı", "Görev başarıyla tamamlandı ve listeden kaldırıldı.")
        else:
            # Update status in json
            for r in requests:
                if r["id"] == request_id:
                    r["status"] = new_status
                    break
            save_requests(requests)
            QMessageBox.information(self, "Başarılı", "Durum başarıyla güncellendi.")
            
        self.refresh_all_tables()


def main():
    # Initialize files
    init_files()
    
    app = QApplication(sys.argv)
    app.setStyleSheet(MODERN_STYLE)
    
    # Show Login dialog
    auth = AuthDialog()
    if auth.exec() == QDialog.DialogCode.Accepted:
        user_data = auth.user_data
        window = MainWindow(user_data)
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
