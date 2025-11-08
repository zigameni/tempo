import sys
from PySide6.QtCore import QPoint
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget

class TempoTimer(QWidget):


    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.drag_position = QPoint()
    
    
    def init_ui(self):
        
        # Frameless window 
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowShadeButtonHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        # container widget for background
        container = QWidget()
        container.setStyleSheet("""
        QWidget {
            background.color: #2C3E50;
            border-radius: 15px;
        }
        """)
        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(20)

        # timer display
        self.time_label = QLabel("25:00")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Arial", 72)
        font.setBold(True)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: #ECF0F1;")
        container_layout.addWidget(self.time_label)

        # Status label
        self.status_label = QLabel("Ready to focus!")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        status_font = QFont("Arial", 14)
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet("color: #95A5A6")
        container_layout.addWidget(self.status_label)
        
        # Control buttons 
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.start_button = QPushButton("Start")
        self.pause_button = QPushButton("Pause")
        self.reset_button = QPushButton("Reset")
        self.close_button = QPushButton("x")

        button_style = """
            QPushButton {
                background-color: #3498DB;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #21618C;
            }
            QPushButton:disabled {
                background-color: #7F8C8D;
            }
        """
        
        close_button_style = """
            QPushButton {
                background-color: #E74C3C;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 16px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """

        self.start_button.setStyleSheet(button_style)
        self.pause_button.setStyleSheet(button_style)
        self.reset_button.setStyleSheet(button_style)
        self.close_button.setStyleSheet(close_button_style)
        
        self.pause_button.setEnabled(False)
        
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.reset_button)
        button_layout.addStretch()
        button_layout.addWidget(self.close_button)
        
        container_layout.addLayout(button_layout)
        
        layout.addWidget(container)
        self.setLayout(layout)
        
        # Connect buttons
        self.start_button.clicked.connect(self.start_timer)
        self.pause_button.clicked.connect(self.pause_timer)
        self.reset_button.clicked.connect(self.reset_timer)
        self.close_button.clicked.connect(self.close)
        
        # Window properties
        self.setFixedSize(400, 300)
        self.center_window()




    def center_window(self):
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width())//2
        y = (screen.height() - self.height())//2
        self.move(x, y)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
            
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_position:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()
             

    def start_timer(self):
        self.status_label.setText("Focus time!")
        self.start_button.setEnabled(False)
        self.pause_button.setEnabled(True)
        # Timer logic

    def pause_timer(self):
        self.status_label.setText("Paused")
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)


    def reset_timer(self):
        self.time_label.setText("25:00")
        self.status_label.setText("Ready to focus!")
        self.start_button.setEnabled(True)
        self.pause_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # noqa: F821
    timer = TempoTimer()
    timer.show()
    sys.exit(app.exec())
