# -*- coding: utf-8 -*-
"""
Modern Card Components
"""

from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from styles.theme_manager import get_theme_manager

class ModernCard(QFrame):
    """
    Modern card container with shadow effect
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('card')
        self._setup_style()
    
    def _setup_style(self):
        """Apply card styling"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        style = f"""
            QFrame#card {{
                background-color: {colors['bg-card']};
                border: 1px solid {colors['border-light']};
                border-radius: 16px;
                padding: 24px;
            }}
        """
        self.setStyleSheet(style)


class StatCard(ModernCard):
    """
    Statistical card with title, value, and optional badge
    Perfect for dashboards
    """
    
    def __init__(self, title='', value='', badge='', parent=None):
        super().__init__(parent)
        
        # Layout
        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        
        # Title
        self.title_label = QLabel(title)
        self.title_label.setObjectName('card_title')
        self._style_title()
        layout.addWidget(self.title_label)
        
        # Value
        self.value_label = QLabel(value)
        self.value_label.setObjectName('card_value')
        self._style_value()
        layout.addWidget(self.value_label)
        
        # Badge (optional)
        if badge:
            self.badge_label = QLabel(badge)
            self.badge_label.setObjectName('badge')
            self._style_badge()
            layout.addWidget(self.badge_label, 0, Qt.AlignLeft)
        else:
            self.badge_label = None
        
        layout.addStretch()
    
    def _style_title(self):
        """Style title label"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        style = f"""
            QLabel#card_title {{
                font-size: 12px;
                font-weight: 600;
                color: {colors['text-secondary']};
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }}
        """
        self.title_label.setStyleSheet(style)
    
    def _style_value(self):
        """Style value label"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        style = f"""
            QLabel#card_value {{
                font-size: 36px;
                font-weight: 700;
                color: {colors['text-primary']};
            }}
        """
        self.value_label.setStyleSheet(style)
    
    def _style_badge(self):
        """Style badge label"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        style = f"""
            QLabel#badge {{
                background-color: {colors['success-bg']};
                color: {colors['success-text']};
                border-radius: 12px;
                padding: 4px 12px;
                font-size: 12px;
                font-weight: 600;
            }}
        """
        if self.badge_label:
            self.badge_label.setStyleSheet(style)
    
    def set_value(self, value):
        """Update value"""
        self.value_label.setText(str(value))
    
    def set_badge(self, badge, badge_type='success'):
        """Update badge"""
        if self.badge_label:
            self.badge_label.setText(badge)
        
        # Update badge color based on type
        theme = get_theme_manager()
        colors = theme.current_colors
        
        if badge_type == 'success':
            bg = colors['success-bg']
            text = colors['success-text']
        elif badge_type == 'warning':
            bg = colors['warning-bg']
            text = colors['warning-text']
        elif badge_type == 'danger':
            bg = colors['danger-bg']
            text = colors['danger-text']
        else:
            bg = colors['info-bg']
            text = colors['info-text']
        
        style = f"""
            QLabel#badge {{
                background-color: {bg};
                color: {text};
                border-radius: 12px;
                padding: 4px 12px;
                font-size: 12px;
                font-weight: 600;
            }}
        """
        if self.badge_label:
            self.badge_label.setStyleSheet(style)
