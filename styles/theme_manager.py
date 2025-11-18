# -*- coding: utf-8 -*-
"""
Theme Manager - Handle Light/Dark Mode Switching
"""

from PyQt5.QtWidgets import QApplication
from .modern_theme import LIGHT_THEME, DARK_THEME
from .colors import COLORS, DARK_COLORS

class ThemeManager:
    """
    Gestionnaire de thèmes pour l'application FaceSmart
    
    Usage:
        theme_manager = ThemeManager(app)
        theme_manager.set_theme('dark')  # Switch to dark mode
        theme_manager.toggle_theme()     # Toggle between themes
    """
    
    def __init__(self, app: QApplication = None):
        """
        Initialize theme manager
        
        Args:
            app: QApplication instance
        """
        self.app = app or QApplication.instance()
        self._is_dark = False
        self._callbacks = []
        
        # Apply default (light) theme
        if self.app:
            self.apply_theme()
    
    @property
    def is_dark(self):
        """Check if dark mode is enabled"""
        return self._is_dark
    
    @property
    def current_theme(self):
        """Get current theme name"""
        return 'dark' if self._is_dark else 'light'
    
    @property
    def current_colors(self):
        """Get current color palette"""
        return DARK_COLORS if self._is_dark else COLORS
    
    def set_theme(self, theme_name: str):
        """
        Set theme by name
        
        Args:
            theme_name: 'light' or 'dark'
        """
        if theme_name.lower() == 'dark':
            self._is_dark = True
        elif theme_name.lower() == 'light':
            self._is_dark = False
        else:
            raise ValueError(f"Unknown theme: {theme_name}. Use 'light' or 'dark'")
        
        self.apply_theme()
    
    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self._is_dark = not self._is_dark
        self.apply_theme()
    
    def apply_theme(self):
        """Apply current theme to the application"""
        if not self.app:
            return
        
        # Get appropriate stylesheet
        stylesheet = DARK_THEME if self._is_dark else LIGHT_THEME
        
        # Apply to application
        self.app.setStyleSheet(stylesheet)
        
        # Notify callbacks
        self._notify_callbacks()
    
    def register_callback(self, callback):
        """
        Register a callback to be called when theme changes
        
        Args:
            callback: Function to call (no arguments)
        """
        if callback not in self._callbacks:
            self._callbacks.append(callback)
    
    def unregister_callback(self, callback):
        """Remove a registered callback"""
        if callback in self._callbacks:
            self._callbacks.remove(callback)
    
    def _notify_callbacks(self):
        """Notify all registered callbacks"""
        for callback in self._callbacks:
            try:
                callback()
            except Exception as e:
                print(f"Error in theme callback: {e}")
    
    def get_color(self, color_name: str):
        """
        Get color value by name from current theme
        
        Args:
            color_name: Color key from COLORS dict
            
        Returns:
            Hex color string
        """
        return self.current_colors.get(color_name, '#000000')
    
    def create_style_dict(self):
        """
        Create a dictionary of commonly used styles
        Useful for programmatic styling
        
        Returns:
            Dictionary of style properties
        """
        colors = self.current_colors
        
        return {
            'primary_button': f"""
                background-color: {colors['primary']};
                color: {colors['text-inverse']};
                border: none;
                border-radius: 12px;
                padding: 12px 24px;
                font-weight: 600;
            """,
            'secondary_button': f"""
                background-color: {colors['bg-secondary']};
                color: {colors['text-primary']};
                border: 2px solid {colors['border']};
                border-radius: 12px;
                padding: 12px 24px;
            """,
            'input_field': f"""
                background-color: {colors['bg-primary']};
                border: 2px solid {colors['border']};
                border-radius: 10px;
                padding: 12px 16px;
                color: {colors['text-primary']};
            """,
            'card': f"""
                background-color: {colors['bg-card']};
                border: 1px solid {colors['border-light']};
                border-radius: 16px;
                padding: 24px;
            """,
        }


# Singleton instance
_theme_manager_instance = None

def get_theme_manager(app: QApplication = None) -> ThemeManager:
    """
    Get singleton ThemeManager instance
    
    Args:
        app: QApplication instance (only needed on first call)
        
    Returns:
        ThemeManager singleton
    """
    global _theme_manager_instance
    
    if _theme_manager_instance is None:
        _theme_manager_instance = ThemeManager(app)
    
    return _theme_manager_instance
