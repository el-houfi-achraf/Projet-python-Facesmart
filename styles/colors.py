# -*- coding: utf-8 -*-
"""
Modern Color Palette - FaceSmart 2024-2025
Inspiré par Tailwind CSS et Material Design 3.0
"""

# ============================================================================
# LIGHT THEME COLORS
# ============================================================================

COLORS = {
    # Primary Colors (Indigo - Professional & Modern)
    'primary': '#6366F1',           # Indigo-500
    'primary-hover': '#4F46E5',     # Indigo-600
    'primary-active': '#4338CA',    # Indigo-700
    'primary-light': '#A5B4FC',     # Indigo-300
    'primary-bg': '#EEF2FF',        # Indigo-50
    
    # Secondary Colors (Violet - Elegant)
    'secondary': '#8B5CF6',         # Violet-500
    'secondary-hover': '#7C3AED',   # Violet-600
    'secondary-active': '#6D28D9',  # Violet-700
    'secondary-light': '#C4B5FD',   # Violet-300
    
    # Accent Colors (Rose - Modern Touch)
    'accent': '#EC4899',            # Pink-500
    'accent-hover': '#DB2777',      # Pink-600
    'accent-light': '#F9A8D4',      # Pink-300
    
    # Status Colors
    'success': '#10B981',           # Green-500
    'success-bg': '#D1FAE5',        # Green-100
    'success-text': '#065F46',      # Green-800
    
    'warning': '#F59E0B',           # Amber-500
    'warning-bg': '#FEF3C7',        # Amber-100
    'warning-text': '#92400E',      # Amber-800
    
    'danger': '#EF4444',            # Red-500
    'danger-bg': '#FEE2E2',         # Red-100
    'danger-text': '#991B1B',       # Red-800
    
    'info': '#3B82F6',              # Blue-500
    'info-bg': '#DBEAFE',           # Blue-100
    'info-text': '#1E40AF',         # Blue-800
    
    # Neutral Colors
    'white': '#FFFFFF',
    'black': '#000000',
    
    # Gray Scale (from light to dark)
    'gray-50': '#F9FAFB',
    'gray-100': '#F3F4F6',
    'gray-200': '#E5E7EB',
    'gray-300': '#D1D5DB',
    'gray-400': '#9CA3AF',
    'gray-500': '#6B7280',
    'gray-600': '#4B5563',
    'gray-700': '#374151',
    'gray-800': '#1F2937',
    'gray-900': '#111827',
    
    # Background Colors
    'bg-primary': '#FFFFFF',
    'bg-secondary': '#F9FAFB',
    'bg-tertiary': '#F3F4F6',
    'bg-card': '#FFFFFF',
    'bg-hover': '#F3F4F6',
    
    # Text Colors
    'text-primary': '#111827',      # Gray-900
    'text-secondary': '#6B7280',    # Gray-500
    'text-tertiary': '#9CA3AF',     # Gray-400
    'text-disabled': '#D1D5DB',     # Gray-300
    'text-inverse': '#FFFFFF',
    
    # Border Colors
    'border': '#E5E7EB',            # Gray-200
    'border-light': '#F3F4F6',      # Gray-100
    'border-dark': '#D1D5DB',       # Gray-300
    'border-focus': '#6366F1',      # Primary
    
    # Shadow Colors (RGBA)
    'shadow-sm': 'rgba(0, 0, 0, 0.05)',
    'shadow-md': 'rgba(0, 0, 0, 0.1)',
    'shadow-lg': 'rgba(0, 0, 0, 0.15)',
    'shadow-xl': 'rgba(0, 0, 0, 0.25)',
}

# ============================================================================
# DARK THEME COLORS
# ============================================================================

DARK_COLORS = {
    # Primary Colors (Lighter for dark mode)
    'primary': '#818CF8',           # Indigo-400
    'primary-hover': '#6366F1',     # Indigo-500
    'primary-active': '#4F46E5',    # Indigo-600
    'primary-light': '#6366F1',     # Indigo-500
    'primary-bg': '#312E81',        # Indigo-900
    
    # Secondary Colors
    'secondary': '#A78BFA',         # Violet-400
    'secondary-hover': '#8B5CF6',   # Violet-500
    'secondary-active': '#7C3AED',  # Violet-600
    'secondary-light': '#8B5CF6',   # Violet-500
    
    # Accent Colors
    'accent': '#F472B6',            # Pink-400
    'accent-hover': '#EC4899',      # Pink-500
    'accent-light': '#EC4899',      # Pink-500
    
    # Status Colors
    'success': '#34D399',           # Green-400
    'success-bg': '#064E3B',        # Green-900
    'success-text': '#6EE7B7',      # Green-300
    
    'warning': '#FBBF24',           # Amber-400
    'warning-bg': '#78350F',        # Amber-900
    'warning-text': '#FCD34D',      # Amber-300
    
    'danger': '#F87171',            # Red-400
    'danger-bg': '#7F1D1D',         # Red-900
    'danger-text': '#FCA5A5',       # Red-300
    
    'info': '#60A5FA',              # Blue-400
    'info-bg': '#1E3A8A',           # Blue-900
    'info-text': '#93C5FD',         # Blue-300
    
    # Neutral Colors
    'white': '#FFFFFF',
    'black': '#000000',
    
    # Gray Scale (adjusted for dark mode)
    'gray-50': '#1F2937',           # Inverted
    'gray-100': '#374151',
    'gray-200': '#4B5563',
    'gray-300': '#6B7280',
    'gray-400': '#9CA3AF',
    'gray-500': '#D1D5DB',
    'gray-600': '#E5E7EB',
    'gray-700': '#F3F4F6',
    'gray-800': '#F9FAFB',
    'gray-900': '#FFFFFF',
    
    # Background Colors (Dark)
    'bg-primary': '#111827',        # Gray-900
    'bg-secondary': '#1F2937',      # Gray-800
    'bg-tertiary': '#374151',       # Gray-700
    'bg-card': '#1F2937',           # Gray-800
    'bg-hover': '#374151',          # Gray-700
    
    # Text Colors (Dark mode)
    'text-primary': '#F9FAFB',      # Gray-50
    'text-secondary': '#D1D5DB',    # Gray-300
    'text-tertiary': '#9CA3AF',     # Gray-400
    'text-disabled': '#6B7280',     # Gray-500
    'text-inverse': '#111827',      # Gray-900
    
    # Border Colors (Dark)
    'border': '#374151',            # Gray-700
    'border-light': '#4B5563',      # Gray-600
    'border-dark': '#6B7280',       # Gray-500
    'border-focus': '#818CF8',      # Primary (lighter)
    
    # Shadow Colors (RGBA for dark mode)
    'shadow-sm': 'rgba(0, 0, 0, 0.3)',
    'shadow-md': 'rgba(0, 0, 0, 0.4)',
    'shadow-lg': 'rgba(0, 0, 0, 0.5)',
    'shadow-xl': 'rgba(0, 0, 0, 0.7)',
}

# ============================================================================
# SPACING SYSTEM (8px grid)
# ============================================================================

SPACING = {
    'xs': '4px',
    'sm': '8px',
    'md': '12px',
    'lg': '16px',
    'xl': '24px',
    '2xl': '32px',
    '3xl': '48px',
    '4xl': '64px',
}

# ============================================================================
# BORDER RADIUS
# ============================================================================

RADIUS = {
    'none': '0px',
    'sm': '4px',
    'md': '8px',
    'lg': '12px',
    'xl': '16px',
    '2xl': '24px',
    'full': '9999px',
}

# ============================================================================
# FONT SIZES
# ============================================================================

FONTS = {
    'xs': '12px',
    'sm': '14px',
    'base': '16px',
    'lg': '18px',
    'xl': '20px',
    '2xl': '24px',
    '3xl': '30px',
    '4xl': '36px',
    '5xl': '48px',
}

# ============================================================================
# FONT WEIGHTS
# ============================================================================

WEIGHTS = {
    'thin': '100',
    'light': '300',
    'normal': '400',
    'medium': '500',
    'semibold': '600',
    'bold': '700',
    'extrabold': '800',
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_color(color_name, is_dark=False):
    """Get color value by name"""
    colors = DARK_COLORS if is_dark else COLORS
    return colors.get(color_name, '#000000')

def rgba(hex_color, alpha=1.0):
    """Convert hex color to rgba string"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f'rgba({r}, {g}, {b}, {alpha})'

def darken(hex_color, amount=0.1):
    """Darken a hex color by amount (0.0 to 1.0)"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = max(0, int(r * (1 - amount)))
    g = max(0, int(g * (1 - amount)))
    b = max(0, int(b * (1 - amount)))
    return f'#{r:02x}{g:02x}{b:02x}'

def lighten(hex_color, amount=0.1):
    """Lighten a hex color by amount (0.0 to 1.0)"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r = min(255, int(r + (255 - r) * amount))
    g = min(255, int(g + (255 - g) * amount))
    b = min(255, int(b + (255 - b) * amount))
    return f'#{r:02x}{g:02x}{b:02x}'
