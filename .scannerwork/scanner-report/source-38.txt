# -*- coding: utf-8 -*-
"""
Modern Toast Notifications
Replaces old QMessageBox with modern toasts
"""

from PyQt5.QtWidgets import QFrame, QLabel, QHBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import QTimer, QPropertyAnimation, QEasingCurve, Qt, QPoint
from PyQt5.QtGui import QIcon
from styles.theme_manager import get_theme_manager

class ModernToast(QFrame):
    """
    Modern toast notification with auto-dismiss
    """
    
    def __init__(self, message, toast_type='success', duration=3000, parent=None):
        super().__init__(parent)
        self.duration = duration
        self.toast_type = toast_type
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        
        self._setup_ui(message)
        self._setup_style()
        self._setup_animations()
    
    def _setup_ui(self, message):
        """Setup UI components"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        layout.setSpacing(12)
        
        # Icon (optional)
        # self.icon_label = QLabel()
        # layout.addWidget(self.icon_label)
        
        # Message
        self.message_label = QLabel(message)
        self.message_label.setWordWrap(True)
        layout.addWidget(self.message_label)
        
        self.adjustSize()
    
    def _setup_style(self):
        """Apply toast styling"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        if self.toast_type == 'success':
            bg = colors['success']
            text = 'white'
        elif self.toast_type == 'error' or self.toast_type == 'danger':
            bg = colors['danger']
            text = 'white'
        elif self.toast_type == 'warning':
            bg = colors['warning']
            text = 'white'
        elif self.toast_type == 'info':
            bg = colors['info']
            text = 'white'
        else:
            bg = colors['gray-800']
            text = colors['white']
        
        style = f"""
            QFrame {{
                background-color: {bg};
                border-radius: 12px;
            }}
            QLabel {{
                color: {text};
                font-size: 14px;
                font-weight: 500;
            }}
        """
        self.setStyleSheet(style)
    
    def _setup_animations(self):
        """Setup fade in/out animations"""
        # Opacity effect
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        
        # Fade in animation
        self.fade_in = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_in.setDuration(300)
        self.fade_in.setStartValue(0)
        self.fade_in.setEndValue(1)
        self.fade_in.setEasingCurve(QEasingCurve.InOutQuad)
        
        # Fade out animation
        self.fade_out = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_out.setDuration(300)
        self.fade_out.setStartValue(1)
        self.fade_out.setEndValue(0)
        self.fade_out.setEasingCurve(QEasingCurve.InOutQuad)
        self.fade_out.finished.connect(self.close)
    
    def show_toast(self):
        """Show toast with animation"""
        # Position at top center of parent
        if self.parent():
            parent_rect = self.parent().geometry()
            x = (parent_rect.width() - self.width()) // 2
            y = 20
            self.move(self.parent().mapToGlobal(QPoint(x, y)))
        
        # Show and animate
        self.show()
        self.fade_in.start()
        
        # Auto dismiss
        if self.duration > 0:
            QTimer.singleShot(self.duration, self.dismiss)
    
    def dismiss(self):
        """Dismiss toast with animation"""
        self.fade_out.start()


# Global function for easy usage
def show_toast(message, toast_type='success', duration=3000, parent=None):
    """
    Show a toast notification
    
    Args:
        message: Toast message text
        toast_type: 'success', 'error', 'warning', 'info'
        duration: Duration in milliseconds (0 = no auto-dismiss)
        parent: Parent widget
    
    Example:
        show_toast("Employé ajouté avec succès!", "success")
        show_toast("Erreur lors de la sauvegarde", "error")
    """
    toast = ModernToast(message, toast_type, duration, parent)
    toast.show_toast()
    return toast
