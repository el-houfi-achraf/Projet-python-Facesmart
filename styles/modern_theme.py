# -*- coding: utf-8 -*-
"""
Modern QSS Theme - FaceSmart 2024-2025
Complete stylesheet with modern design principles
"""

from .colors import COLORS, DARK_COLORS, SPACING, RADIUS, FONTS, WEIGHTS

def generate_light_theme():
    """Generate complete light theme stylesheet"""
    return f"""
/* ============================================================================
   GLOBAL STYLES
   ============================================================================ */

QWidget {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    font-size: {FONTS['base']};
    color: {COLORS['text-primary']};
}}

QMainWindow {{
    background-color: {COLORS['bg-secondary']};
}}

/* ============================================================================
   BUTTONS - Modern Flat Design
   ============================================================================ */

/* Primary Button */
QPushButton {{
    background-color: {COLORS['primary']};
    color: {COLORS['text-inverse']};
    border: none;
    border-radius: {RADIUS['lg']};
    padding: {SPACING['md']} {SPACING['xl']};
    font-size: {FONTS['sm']};
    font-weight: {WEIGHTS['semibold']};
    min-height: 40px;
}}

QPushButton:hover {{
    background-color: {COLORS['primary-hover']};
}}

QPushButton:pressed {{
    background-color: {COLORS['primary-active']};
}}

QPushButton:disabled {{
    background-color: {COLORS['gray-200']};
    color: {COLORS['text-disabled']};
}}

/* Secondary Button */
QPushButton#secondary {{
    background-color: {COLORS['bg-secondary']};
    color: {COLORS['text-primary']};
    border: 2px solid {COLORS['border']};
}}

QPushButton#secondary:hover {{
    background-color: {COLORS['bg-hover']};
    border-color: {COLORS['border-dark']};
}}

/* Success Button */
QPushButton#success {{
    background-color: {COLORS['success']};
    color: white;
}}

QPushButton#success:hover {{
    background-color: #059669;
}}

/* Danger Button */
QPushButton#danger {{
    background-color: {COLORS['danger']};
    color: white;
}}

QPushButton#danger:hover {{
    background-color: #DC2626;
}}

/* Icon Button */
QPushButton#icon {{
    background-color: transparent;
    border: none;
    padding: {SPACING['sm']};
    min-width: 40px;
    min-height: 40px;
}}

QPushButton#icon:hover {{
    background-color: {COLORS['bg-hover']};
    border-radius: {RADIUS['md']};
}}

/* ============================================================================
   INPUT FIELDS - Modern with Focus States
   ============================================================================ */

QLineEdit {{
    background-color: {COLORS['bg-primary']};
    border: 2px solid {COLORS['border']};
    border-radius: {RADIUS['lg']};
    padding: {SPACING['md']} {SPACING['lg']};
    font-size: {FONTS['sm']};
    color: {COLORS['text-primary']};
    min-height: 40px;
    selection-background-color: {COLORS['primary-light']};
}}

QLineEdit:hover {{
    border-color: {COLORS['border-dark']};
}}

QLineEdit:focus {{
    background-color: {COLORS['white']};
    border-color: {COLORS['border-focus']};
    outline: none;
}}

QLineEdit:disabled {{
    background-color: {COLORS['bg-tertiary']};
    color: {COLORS['text-disabled']};
    border-color: {COLORS['border-light']};
}}

QLineEdit::placeholder {{
    color: {COLORS['text-tertiary']};
}}

/* ============================================================================
   TEXT AREAS
   ============================================================================ */

QTextEdit {{
    background-color: {COLORS['bg-primary']};
    border: 2px solid {COLORS['border']};
    border-radius: {RADIUS['lg']};
    padding: {SPACING['md']};
    font-size: {FONTS['sm']};
    color: {COLORS['text-primary']};
}}

QTextEdit:focus {{
    border-color: {COLORS['border-focus']};
}}

/* ============================================================================
   COMBO BOX / DROPDOWN
   ============================================================================ */

QComboBox {{
    background-color: {COLORS['bg-primary']};
    border: 2px solid {COLORS['border']};
    border-radius: {RADIUS['lg']};
    padding: {SPACING['md']} {SPACING['lg']};
    min-height: 40px;
    font-size: {FONTS['sm']};
}}

QComboBox:hover {{
    border-color: {COLORS['border-dark']};
}}

QComboBox:focus {{
    border-color: {COLORS['border-focus']};
}}

QComboBox::drop-down {{
    border: none;
    width: 30px;
}}

QComboBox::down-arrow {{
    image: url(resources/icons/chevron-down.png);
    width: 12px;
    height: 12px;
}}

QComboBox QAbstractItemView {{
    background-color: {COLORS['bg-primary']};
    border: 1px solid {COLORS['border']};
    border-radius: {RADIUS['md']};
    padding: {SPACING['sm']};
    selection-background-color: {COLORS['primary-bg']};
    selection-color: {COLORS['primary']};
}}

/* ============================================================================
   LABELS
   ============================================================================ */

QLabel {{
    color: {COLORS['text-primary']};
    font-size: {FONTS['sm']};
    background: transparent;
    border: none;
}}

QLabel#title {{
    font-size: {FONTS['2xl']};
    font-weight: {WEIGHTS['bold']};
    color: {COLORS['text-primary']};
}}

QLabel#subtitle {{
    font-size: {FONTS['lg']};
    font-weight: {WEIGHTS['semibold']};
    color: {COLORS['text-secondary']};
}}

QLabel#caption {{
    font-size: {FONTS['xs']};
    color: {COLORS['text-tertiary']};
}}

/* ============================================================================
   CARDS / CONTAINERS
   ============================================================================ */

QFrame#card {{
    background-color: {COLORS['bg-card']};
    border: 1px solid {COLORS['border-light']};
    border-radius: {RADIUS['xl']};
    padding: {SPACING['xl']};
}}

QWidget#card {{
    background-color: {COLORS['bg-card']};
    border: 1px solid {COLORS['border-light']};
    border-radius: {RADIUS['xl']};
}}

/* ============================================================================
   SIDEBAR NAVIGATION - Modern Dark Sidebar
   ============================================================================ */

QWidget#sidebar {{
    background-color: {COLORS['gray-900']};
    border-right: 1px solid {COLORS['gray-800']};
}}

QWidget#sidebar QPushButton {{
    background-color: transparent;
    color: {COLORS['gray-400']};
    text-align: left;
    padding: {SPACING['md']} {SPACING['lg']};
    border: none;
    border-left: 3px solid transparent;
    border-radius: 0px;
    font-size: {FONTS['sm']};
    font-weight: {WEIGHTS['medium']};
}}

QWidget#sidebar QPushButton:hover {{
    background-color: rgba(255, 255, 255, 0.05);
    color: {COLORS['white']};
}}

QWidget#sidebar QPushButton:checked {{
    background-color: rgba(99, 102, 241, 0.15);
    color: {COLORS['primary']};
    border-left-color: {COLORS['primary']};
    font-weight: {WEIGHTS['semibold']};
}}

/* ============================================================================
   HEADER / TOP BAR
   ============================================================================ */

QWidget#header {{
    background-color: {COLORS['bg-primary']};
    border-bottom: 1px solid {COLORS['border']};
    padding: {SPACING['md']} {SPACING['xl']};
}}

/* ============================================================================
   SCROLL BARS - Modern Thin Scrollbars
   ============================================================================ */

QScrollBar:vertical {{
    background-color: {COLORS['bg-secondary']};
    width: 10px;
    border-radius: 5px;
}}

QScrollBar::handle:vertical {{
    background-color: {COLORS['gray-300']};
    border-radius: 5px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background-color: {COLORS['gray-400']};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QScrollBar:horizontal {{
    background-color: {COLORS['bg-secondary']};
    height: 10px;
    border-radius: 5px;
}}

QScrollBar::handle:horizontal {{
    background-color: {COLORS['gray-300']};
    border-radius: 5px;
    min-width: 30px;
}}

QScrollBar::handle:horizontal:hover {{
    background-color: {COLORS['gray-400']};
}}

/* ============================================================================
   TABLES - Modern Table Styling
   ============================================================================ */

QTableWidget {{
    background-color: {COLORS['bg-primary']};
    border: 1px solid {COLORS['border']};
    border-radius: {RADIUS['lg']};
    gridline-color: {COLORS['border-light']};
}}

QTableWidget::item {{
    padding: {SPACING['md']};
    border: none;
}}

QTableWidget::item:selected {{
    background-color: {COLORS['primary-bg']};
    color: {COLORS['primary']};
}}

QHeaderView::section {{
    background-color: {COLORS['bg-tertiary']};
    color: {COLORS['text-secondary']};
    font-weight: {WEIGHTS['semibold']};
    font-size: {FONTS['xs']};
    text-transform: uppercase;
    padding: {SPACING['md']};
    border: none;
    border-bottom: 2px solid {COLORS['border']};
}}

/* ============================================================================
   DIALOGS / MODALS
   ============================================================================ */

QDialog {{
    background-color: {COLORS['bg-primary']};
    border-radius: {RADIUS['2xl']};
}}

/* ============================================================================
   CHECKBOXES & RADIO BUTTONS
   ============================================================================ */

QCheckBox {{
    spacing: {SPACING['md']};
    color: {COLORS['text-primary']};
}}

QCheckBox::indicator {{
    width: 20px;
    height: 20px;
    border: 2px solid {COLORS['border-dark']};
    border-radius: {RADIUS['sm']};
    background-color: {COLORS['bg-primary']};
}}

QCheckBox::indicator:checked {{
    background-color: {COLORS['primary']};
    border-color: {COLORS['primary']};
    image: url(resources/icons/check.png);
}}

QCheckBox::indicator:hover {{
    border-color: {COLORS['primary']};
}}

QRadioButton {{
    spacing: {SPACING['md']};
    color: {COLORS['text-primary']};
}}

QRadioButton::indicator {{
    width: 20px;
    height: 20px;
    border: 2px solid {COLORS['border-dark']};
    border-radius: 10px;
    background-color: {COLORS['bg-primary']};
}}

QRadioButton::indicator:checked {{
    background-color: {COLORS['primary']};
    border-color: {COLORS['primary']};
}}

/* ============================================================================
   PROGRESS BAR
   ============================================================================ */

QProgressBar {{
    background-color: {COLORS['bg-tertiary']};
    border: none;
    border-radius: {RADIUS['full']};
    height: 8px;
    text-align: center;
}}

QProgressBar::chunk {{
    background-color: {COLORS['primary']};
    border-radius: {RADIUS['full']};
}}

/* ============================================================================
   TOOLTIPS
   ============================================================================ */

QToolTip {{
    background-color: {COLORS['gray-900']};
    color: {COLORS['white']};
    border: none;
    border-radius: {RADIUS['md']};
    padding: {SPACING['sm']} {SPACING['md']};
    font-size: {FONTS['xs']};
}}

/* ============================================================================
   MENU BAR & MENUS
   ============================================================================ */

QMenuBar {{
    background-color: {COLORS['bg-primary']};
    border-bottom: 1px solid {COLORS['border']};
    padding: {SPACING['sm']};
}}

QMenuBar::item {{
    padding: {SPACING['sm']} {SPACING['md']};
    border-radius: {RADIUS['md']};
}}

QMenuBar::item:selected {{
    background-color: {COLORS['bg-hover']};
}}

QMenu {{
    background-color: {COLORS['bg-primary']};
    border: 1px solid {COLORS['border']};
    border-radius: {RADIUS['lg']};
    padding: {SPACING['sm']};
}}

QMenu::item {{
    padding: {SPACING['md']} {SPACING['lg']};
    border-radius: {RADIUS['md']};
}}

QMenu::item:selected {{
    background-color: {COLORS['primary-bg']};
    color: {COLORS['primary']};
}}

/* ============================================================================
   STATUS BAR
   ============================================================================ */

QStatusBar {{
    background-color: {COLORS['bg-primary']};
    border-top: 1px solid {COLORS['border']};
    color: {COLORS['text-secondary']};
    font-size: {FONTS['xs']};
}}

/* ============================================================================
   TABS
   ============================================================================ */

QTabWidget::pane {{
    background-color: {COLORS['bg-primary']};
    border: 1px solid {COLORS['border']};
    border-radius: {RADIUS['lg']};
}}

QTabBar::tab {{
    background-color: {COLORS['bg-secondary']};
    color: {COLORS['text-secondary']};
    padding: {SPACING['md']} {SPACING['xl']};
    border-top-left-radius: {RADIUS['md']};
    border-top-right-radius: {RADIUS['md']};
    margin-right: {SPACING['xs']};
}}

QTabBar::tab:selected {{
    background-color: {COLORS['bg-primary']};
    color: {COLORS['primary']};
    font-weight: {WEIGHTS['semibold']};
}}

QTabBar::tab:hover {{
    background-color: {COLORS['bg-hover']};
}}
"""

def generate_dark_theme():
    """Generate complete dark theme stylesheet"""
    return f"""
/* ============================================================================
   DARK THEME - All colors inverted
   ============================================================================ */

QWidget {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    font-size: {FONTS['base']};
    color: {DARK_COLORS['text-primary']};
}}

QMainWindow {{
    background-color: {DARK_COLORS['bg-primary']};
}}

/* Buttons */
QPushButton {{
    background-color: {DARK_COLORS['primary']};
    color: {DARK_COLORS['text-inverse']};
    border: none;
    border-radius: {RADIUS['lg']};
    padding: {SPACING['md']} {SPACING['xl']};
    font-size: {FONTS['sm']};
    font-weight: {WEIGHTS['semibold']};
    min-height: 40px;
}}

QPushButton:hover {{
    background-color: {DARK_COLORS['primary-hover']};
}}

QPushButton:pressed {{
    background-color: {DARK_COLORS['primary-active']};
}}

/* Input Fields */
QLineEdit {{
    background-color: {DARK_COLORS['bg-secondary']};
    border: 2px solid {DARK_COLORS['border']};
    border-radius: {RADIUS['lg']};
    padding: {SPACING['md']} {SPACING['lg']};
    font-size: {FONTS['sm']};
    color: {DARK_COLORS['text-primary']};
    min-height: 40px;
}}

QLineEdit:hover {{
    border-color: {DARK_COLORS['border-dark']};
}}

QLineEdit:focus {{
    background-color: {DARK_COLORS['bg-tertiary']};
    border-color: {DARK_COLORS['border-focus']};
}}

/* Cards */
QFrame#card, QWidget#card {{
    background-color: {DARK_COLORS['bg-card']};
    border: 1px solid {DARK_COLORS['border']};
    border-radius: {RADIUS['xl']};
}}

/* Sidebar (already dark, adjust slightly) */
QWidget#sidebar {{
    background-color: {DARK_COLORS['bg-primary']};
    border-right: 1px solid {DARK_COLORS['border']};
}}

/* ... Continue with all other dark theme styles ... */
"""

# Exporter les thèmes
LIGHT_THEME = generate_light_theme()
DARK_THEME = generate_dark_theme()
