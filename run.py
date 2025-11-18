# -*- coding: utf-8 -*-
"""
Point d'entrée principal de l'application FaceSmart
"""
import sys
import os

# Ajouter le répertoire parent au PYTHONPATH pour permettre les imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Ajouter le dossier `src/` au PYTHONPATH pour permettre les imports de modules
# qui utilisent des imports sans le préfixe `src.` (compatibilité avec l'ancien code)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from src.sidebar_test import Ui_MainWindow as SidebarUI

# Import du gestionnaire de thème moderne
from styles.theme_manager import get_theme_manager

def main():
    """Lance l'application FaceSmart avec le thème moderne"""
    app = QApplication(sys.argv)
    
    # Configuration de l'application
    app.setApplicationName("FaceSmart")
    app.setOrganizationName("FaceSmart")
    
    # Activer le thème moderne
    theme_manager = get_theme_manager(app)
    
    # Par défaut en mode clair - décommentez pour mode sombre
    # theme_manager.set_theme('dark')
    
    # Fenêtre principale avec sidebar
    MainWindow = QMainWindow()
    ui = SidebarUI()
    ui.setupUi(MainWindow)
    
    # Icône de la fenêtre (optionnel)
    try:
        icon = QIcon("resources/profile_pic.png")
        MainWindow.setWindowIcon(icon)
    except:
        pass
    
    # Titre de la fenêtre
    MainWindow.setWindowTitle("FaceSmart - Gestion des Employés")
    
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
