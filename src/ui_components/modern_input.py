# -*- coding: utf-8 -*-
"""
Modern Input Components
"""

from PyQt5.QtWidgets import QLineEdit, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from styles.theme_manager import get_theme_manager

class ModernInput(QLineEdit):
    """
    Modern styled input field with focus effects
    """
    
    def __init__(self, placeholder='', password=False, parent=None):
        super().__init__(parent)
        
        if placeholder:
            self.setPlaceholderText(placeholder)
        
        if password:
            self.setEchoMode(QLineEdit.Password)
        
        self._setup_style()
    
    def _setup_style(self):
        """Apply modern styling"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        style = f"""
            QLineEdit {{
                background-color: {colors['bg-primary']};
                border: 2px solid {colors['border']};
                border-radius: 10px;
                padding: 12px 16px;
                font-size: 14px;
                color: {colors['text-primary']};
                min-height: 40px;
                selection-background-color: {colors['primary-light']};
            }}
            QLineEdit:hover {{
                border-color: {colors['border-dark']};
            }}
            QLineEdit:focus {{
                background-color: {colors['white']};
                border-color: {colors['border-focus']};
            }}
            QLineEdit:disabled {{
                background-color: {colors['bg-tertiary']};
                color: {colors['text-disabled']};
            }}
        """
        self.setStyleSheet(style)
    
    def set_error(self, error=True):
        """Set error state (red border)"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        if error:
            self.setStyleSheet(self.styleSheet() + f"""
                QLineEdit {{
                    border-color: {colors['danger']} !important;
                }}
            """)
        else:
            self._setup_style()
    
    def set_success(self, success=True):
        """Set success state (green border)"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        if success:
            self.setStyleSheet(self.styleSheet() + f"""
                QLineEdit {{
                    border-color: {colors['success']} !important;
                }}
            """)
        else:
            self._setup_style()


class ModernTextArea(QTextEdit):
    """
    Modern styled text area
    """
    
    def __init__(self, placeholder='', parent=None):
        super().__init__(parent)
        
        if placeholder:
            self.setPlaceholderText(placeholder)
        
        self._setup_style()
    
    def _setup_style(self):
        """Apply modern styling"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        style = f"""
            QTextEdit {{
                background-color: {colors['bg-primary']};
                border: 2px solid {colors['border']};
                border-radius: 10px;
                padding: 12px;
                font-size: 14px;
                color: {colors['text-primary']};
                selection-background-color: {colors['primary-light']};
            }}
            QTextEdit:hover {{
                border-color: {colors['border-dark']};
            }}
            QTextEdit:focus {{
                border-color: {colors['border-focus']};
            }}
        """
        self.setStyleSheet(style)
