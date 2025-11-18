# -*- coding: utf-8 -*-
"""
Modern Button Components
"""

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSize, Qt
from PyQt5.QtGui import QIcon
from styles.theme_manager import get_theme_manager

class ModernButton(QPushButton):
    """
    Modern styled button with animations
    
    Variants: primary, secondary, success, danger, outline
    """
    
    def __init__(self, text='', variant='primary', icon=None, parent=None):
        super().__init__(text, parent)
        self.variant = variant
        self._setup_style()
        
        if icon:
            self.setIcon(icon)
            self.setIconSize(QSize(20, 20))
        
        # Animation
        self._animation = None
    
    def _setup_style(self):
        """Apply variant-specific styling"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        if self.variant == 'primary':
            style = f"""
                QPushButton {{
                    background-color: {colors['primary']};
                    color: {colors['text-inverse']};
                    border: none;
                    border-radius: 12px;
                    padding: 12px 24px;
                    font-size: 14px;
                    font-weight: 600;
                    min-height: 40px;
                }}
                QPushButton:hover {{
                    background-color: {colors['primary-hover']};
                }}
                QPushButton:pressed {{
                    background-color: {colors['primary-active']};
                }}
                QPushButton:disabled {{
                    background-color: {colors['gray-200']};
                    color: {colors['text-disabled']};
                }}
            """
        elif self.variant == 'secondary':
            style = f"""
                QPushButton {{
                    background-color: {colors['bg-secondary']};
                    color: {colors['text-primary']};
                    border: 2px solid {colors['border']};
                    border-radius: 12px;
                    padding: 12px 24px;
                    font-size: 14px;
                    font-weight: 600;
                    min-height: 40px;
                }}
                QPushButton:hover {{
                    background-color: {colors['bg-hover']};
                    border-color: {colors['border-dark']};
                }}
            """
        elif self.variant == 'success':
            style = f"""
                QPushButton {{
                    background-color: {colors['success']};
                    color: white;
                    border: none;
                    border-radius: 12px;
                    padding: 12px 24px;
                    font-size: 14px;
                    font-weight: 600;
                    min-height: 40px;
                }}
                QPushButton:hover {{
                    background-color: #059669;
                }}
            """
        elif self.variant == 'danger':
            style = f"""
                QPushButton {{
                    background-color: {colors['danger']};
                    color: white;
                    border: none;
                    border-radius: 12px;
                    padding: 12px 24px;
                    font-size: 14px;
                    font-weight: 600;
                    min-height: 40px;
                }}
                QPushButton:hover {{
                    background-color: #DC2626;
                }}
            """
        else:
            style = ""
        
        self.setStyleSheet(style)
    
    def animate_click(self):
        """Add click animation"""
        if self._animation:
            self._animation.stop()
        
        self._animation = QPropertyAnimation(self, b"geometry")
        self._animation.setDuration(150)
        self._animation.setEasingCurve(QEasingCurve.OutCubic)
        
        start_rect = self.geometry()
        self._animation.setStartValue(start_rect)
        
        # Slight scale down
        from PyQt5.QtCore import QRect
        scaled_rect = QRect(
            start_rect.x() + 2,
            start_rect.y() + 2,
            start_rect.width() - 4,
            start_rect.height() - 4
        )
        self._animation.setKeyValueAt(0.5, scaled_rect)
        self._animation.setEndValue(start_rect)
        self._animation.start()


class IconButton(QPushButton):
    """
    Icon-only button (no text)
    Perfect for toolbars and compact UIs
    """
    
    def __init__(self, icon=None, size=40, tooltip='', parent=None):
        super().__init__(parent)
        self.button_size = size
        
        if icon:
            self.setIcon(icon)
            self.setIconSize(QSize(size - 16, size - 16))
        
        if tooltip:
            self.setToolTip(tooltip)
        
        self._setup_style()
    
    def _setup_style(self):
        """Style for icon button"""
        theme = get_theme_manager()
        colors = theme.current_colors
        
        style = f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                border-radius: {self.button_size // 2}px;
                min-width: {self.button_size}px;
                max-width: {self.button_size}px;
                min-height: {self.button_size}px;
                max-height: {self.button_size}px;
            }}
            QPushButton:hover {{
                background-color: {colors['bg-hover']};
            }}
            QPushButton:pressed {{
                background-color: {colors['bg-tertiary']};
            }}
        """
        self.setStyleSheet(style)
