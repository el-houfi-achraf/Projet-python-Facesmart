# FaceSmart 🎯

**FaceSmart: Manage Your Employees with Precision and Elegance**

A comprehensive employee management system with facial recognition capabilities, built with Python and PyQt5. This desktop application enables companies to track employee attendance, manage employee information, and monitor productivity through advanced facial recognition technology.

## ✨ Features

### 🔐 Facial Recognition System

- **Automated Clock-in/Clock-out**: Employees can check in and out using facial recognition
- **Real-time Face Detection**: Live camera feed with instant face recognition
- **Secure Authentication**: Face-based employee identification system
- **Employee Photo Management**: Store and manage employee photos in the `data/` directory

### 👥 Employee Management

- **Complete Employee Database**: Store employee information including names, emails, and passwords
- **CRUD Operations**: Add, modify, delete, and view employee records
- **Employee Search**: Filter and search employees by various criteria
- **Profile Management**: Comprehensive employee profile system

### 📋 Task Management

- **Task Assignment**: Assign and manage tasks for employees
- **Task Tracking**: Monitor task status and completion
- **Task Search**: Advanced search functionality for tasks
- **Status Management**: Track task progress and completion status

### ⏱️ Time Tracking

- **Automated Time Logging**: Record working hours through facial recognition
- **Period-based Tracking**: Monitor employee attendance by date ranges
- **Work Duration Calculation**: Automatic calculation of work hours
- **Attendance Reports**: Generate detailed attendance reports

### 📊 Reporting & Analytics

- **Employee Productivity Reports**: Assess individual and collective performance
- **Attendance Analytics**: Detailed attendance tracking and reporting
- **Time-based Analysis**: Generate reports based on specific time periods
- **Search & Filter**: Advanced search capabilities across all modules

## 🛠️ Technology Stack

- **Frontend**: PyQt5 (Desktop GUI)
- **Backend**: Python 3.x
- **Database**: SQLite3
- **Computer Vision**: OpenCV, face_recognition
- **Image Processing**: NumPy, PIL
- **UI Design**: Qt Designer (.ui files)

## 🏗️ Project Structure (Reorganized)

```
Projet-python-Facesmart/
├── 🚀 run.py                    # Main application entry point (NEW)
├── 📋 fix_imports.py            # Import correction script
├── 📖 README.md                 # This file
├── 📘 QUICKSTART.md             # Quick start guide (NEW)
├── 📦 requirements.txt          # Python dependencies
├── 💾 database.db               # SQLite database
│
├── src/                         # 📦 Source Code (NEW)
│   ├── __init__.py
│   ├── main_test.py             # Login/Check-in interface
│   ├── sidebar_test.py          # Main dashboard with sidebar
│   ├── employer.py              # Employee management logic
│   ├── tache.py                 # Task management logic
│   ├── suiviTemps.py            # Time tracking logic
│   ├── face_test.py             # Facial recognition interface
│   ├── face-recog.py            # Face recognition algorithm
│   ├── afficherEmploye.py       # Display employees module
│   ├── chercher*.py             # Search modules
│   ├── gestion_tache*.py        # Advanced task management
│   ├── tache_*.py               # Task CRUD operations
│   └── screenshot*.py           # Screenshot utilities
│
├── ui/                          # 🎨 User Interface Files (NEW)
│   ├── __init__.py
│   ├── *.ui                     # Qt Designer UI files
│   └── *_ui.py                  # Generated Python UI files
│
├── data/                        # 📸 Employee Photos
│   ├── achraf_lhoufi_1.png
│   ├── ahmed_labchiri_1.png
│   └── ...
│
├── images/                      # 🖼️ UI Images & Resources
│   ├── image_background_rc.py
│   └── __pycache__/
│
├── resources/                   # 📁 Qt Resources (NEW)
│   ├── resources.qrc
│   └── resources_rc.py
│
├── learn/                       # 📚 Learning & Testing Files
│   └── ...
│
├── tests/                       # ✅ Unit Tests (NEW)
│
├── docs/                        # 📄 Documentation (NEW)
│
└── .git/                        # Git repository
```

### 📂 Directory Overview

- **`src/`**: All Python source code and business logic
- **`ui/`**: Qt Designer files and generated UI code
- **`data/`**: Employee photos for facial recognition
- **`images/`**: Application images and backgrounds
- **`resources/`**: Qt resource files (icons, images compiled)
- **`learn/`**: Experimental and learning files
- **`tests/`**: Unit and integration tests
- **`docs/`**: Additional documentation

## 🗄️ Database Schema

### Tables

- **Employe**: Employee information (id, nom, prenom, email, password, id_tache)
- **Tache**: Task management (id, libelle, Status)
- **SuiviTemps**: Time tracking (idPeriod, DateArrivee, DateDepart, id)

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.7+** (Python 3.8+ recommended)
- **pip** package manager
- **Webcam** (for facial recognition features)
- **Git** (for cloning the repository)

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/el-houfi-achraf/Projet-python-Facesmart.git
   cd Projet-python-Facesmart
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   # Recommended method (uses new structure)
   python run.py

   # Alternative: Run sidebar interface directly
   python -m src.sidebar_test

   # Alternative: Run login screen
   python -m src.main_test
   ```

### Required Dependencies

The following packages will be installed via `requirements.txt`:

- **PyQt5** - GUI framework
- **opencv-python** - Computer vision and image processing
- **face-recognition** - Facial recognition library
- **numpy** - Numerical computing
- **pillow** - Image processing
- **sqlite3** - Database (included with Python)

### Manual Installation

If you prefer to install dependencies manually:

```bash
pip install PyQt5
pip install opencv-python
pip install face-recognition
pip install numpy
pip install pillow
```

## 💻 Usage Guide

### 🚀 Starting the Application

**Option 1: Main Dashboard (Recommended)**

```bash
python run.py
```

This launches the main application with the sidebar navigation interface.

**Option 2: Login Screen**

```bash
python -m src.main_test
```

This starts with the check-in/check-out authentication screen.

**Option 3: Module-specific Launch**

```bash
python -m src.sidebar_test  # Main dashboard
python -m src.face_test     # Face recognition only
```

### 👥 Employee Management

#### Adding a New Employee

1. Launch the application and navigate to the **Create** section
2. Fill in employee details:
   - **Nom** (Last Name)
   - **Prenom** (First Name)
   - **Email**
   - **Password**
   - **Tache** (Assigned Task)
3. Click **SAVE** to register the employee
4. Add employee photo to `data/` folder with format: `firstname_lastname_1.png`

#### Updating Employee Information

1. Navigate to the **Update** section
2. Enter the employee **ID**
3. Modify the desired fields
4. Click **EDIT** to save changes

#### Deleting an Employee

1. Navigate to the **Delete** section
2. Enter employee details (ID, Nom, Prenom)
3. Click **DELETE** to remove the employee

#### Searching for Employees

- Use the search functionality to filter employees by:
  - Name
  - Task assignment
  - Date range
  - Status

### 📋 Task Management

#### Creating Tasks

1. Navigate to the task management section (📑 icon)
2. Click **Ajouter Tache** (Add Task)
3. Enter task details (Libelle, Status)
4. Save the task

#### Assigning Tasks

1. Go to **Affecter Tache** (Assign Task)
2. Select an employee
3. Select a task from the dropdown
4. Confirm assignment

### 🔐 Facial Recognition Setup

#### Preparing Employee Photos

1. **Photo Requirements**:

   - Format: PNG or JPG
   - Resolution: 640x480 or higher
   - Clear frontal face view
   - Good lighting conditions
   - Naming: `firstname_lastname_1.png`

2. **Adding Photos**:

   ```bash
   # Place photos in the data directory
   data/
   ├── john_doe_1.png
   ├── jane_smith_1.png
   └── ...
   ```

3. **Testing Recognition**:
   - Click the 📷 icon on the dashboard
   - Or run: `python -m src.face_test`
   - Allow camera access
   - Face the camera for recognition

### ⏱️ Time Tracking

#### Check-In Process

1. **Method 1: Password Authentication**

   - Enter your **Nom** (Last Name)
   - Enter your **Prenom** (First Name)
   - Enter your **Password**
   - Click **Check in**

2. **Method 2: Facial Recognition**
   - Click the camera icon (📷)
   - Face the camera
   - System automatically checks you in

#### Check-Out Process

Follow the same steps as Check-In, but click **Check Out** instead.

#### Viewing Time Reports

1. Navigate to the search section (🔍 icon)
2. Select **Période** (Period)
3. Choose date range
4. View attendance reports and work hours

### 📊 Reports & Analytics

- **Employee Productivity**: View individual employee performance
- **Attendance Reports**: Generate attendance summaries by date
- **Task Completion**: Monitor task progress across teams
- **Time Analysis**: Analyze work patterns and hours

## 📱 User Interface

The application features a modern, user-friendly interface with:

- **Sidebar Navigation**: Easy access to all modules
- **Real-time Camera Feed**: Live facial recognition display
- **Data Tables**: Organized display of employee and task information
- **Search Functionality**: Quick filtering and searching capabilities
- **Reports Dashboard**: Comprehensive analytics and reporting

## 🔒 Security Features

- **Face-based Authentication**: Secure login using facial recognition
- **Password Protection**: Additional security layer for sensitive operations
- **Data Encryption**: Secure storage of employee information
- **Access Control**: Role-based permissions for different user types

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: Open an issue with detailed reproduction steps
- 💡 **Suggest Features**: Share your ideas for new features
- 📖 **Improve Documentation**: Help make our docs clearer
- 🔧 **Submit Pull Requests**: Fix bugs or add features
- ⭐ **Star the Project**: Show your support!

### Contribution Process

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add: AmazingFeature with detailed description'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Pull Request Guidelines

- ✅ Clear description of changes
- ✅ Reference related issues
- ✅ Add tests if applicable
- ✅ Update documentation
- ✅ Follow existing code style
- ✅ Include screenshots for UI changes

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ⚠️ Liability and warranty limitations apply

## 👨‍💻 Author & Credits

### Main Developer

**Achraf El Houfi**

- 🌐 GitHub: [@el-houfi-achraf](https://github.com/el-houfi-achraf)
- 📧 Contact: via GitHub Issues
- 🔗 Repository: [Projet-python-Facesmart](https://github.com/el-houfi-achraf/Projet-python-Facesmart)

### Acknowledgments

- **PyQt5** - Qt Company for the amazing GUI framework
- **face_recognition** - Adam Geitgey for the face recognition library
- **OpenCV** - For computer vision capabilities
- **Python Community** - For extensive libraries and support

## 📊 Project Statistics

- **Language**: Python 3.x
- **Framework**: PyQt5
- **Database**: SQLite3
- **Architecture**: MVC Pattern
- **Version**: 2.0 (Reorganized Structure)

## 🌟 Star History

If you find this project helpful, please consider giving it a ⭐!

[![Star History](https://img.shields.io/github/stars/el-houfi-achraf/Projet-python-Facesmart?style=social)](https://github.com/el-houfi-achraf/Projet-python-Facesmart)

## 🐛 Troubleshooting

### Common Issues

#### Import Errors

If you encounter import errors after reorganization:

```bash
# Run the fix imports script
python fix_imports.py

# Verify Python can find the modules
python -c "import sys; import src; print('OK')"
```

#### Camera Not Working

- **Windows**: Check camera permissions in Settings → Privacy → Camera
- **Verify camera**: Test with `python -m src.face_test`
- Ensure no other application is using the camera

#### Database Errors

```bash
# Check if database exists
ls database.db

# If missing, the app will create it on first run
python run.py
```

#### PyQt5 Issues

```bash
# Reinstall PyQt5
pip uninstall PyQt5 PyQt5-sip
pip install PyQt5

# For Qt resource issues
cd resources
pyrcc5 resources.qrc -o resources_rc.py
```

#### Face Recognition Library Installation Issues

On Windows, if `face-recognition` fails to install:

```bash
# Install dlib first (may require Visual Studio Build Tools)
pip install cmake
pip install dlib
pip install face-recognition
```

### Performance Tips

- **Lighting**: Ensure good lighting for optimal face recognition
- **Photo Quality**: Use high-resolution photos (640x480 minimum)
- **Database**: For large employee bases (>1000), consider indexing
- **Camera**: Use a webcam with at least 720p resolution

### Getting Help

1. Check the [QUICKSTART.md](QUICKSTART.md) guide
2. Review error messages carefully
3. Ensure all dependencies are installed: `pip list`
4. Open an issue on GitHub with:
   - Python version (`python --version`)
   - Error message
   - Steps to reproduce

## 🔧 Development

### Project Structure Improvements (v2.0)

This project was recently reorganized for better maintainability:

**✅ What Changed:**

- All source code moved to `src/` directory
- UI files organized in `ui/` directory
- Resources centralized in `resources/`
- Added `run.py` as main entry point
- Imports updated to use `src.` prefix
- Added comprehensive documentation

**✅ Benefits:**

- Cleaner project structure
- Better separation of concerns
- Easier to navigate and maintain
- Modular and scalable architecture
- Follows Python best practices

### Running Tests

```bash
# Run all tests (when available)
python -m pytest tests/

# Run specific module tests
python -m pytest tests/test_employer.py
```

### Building Qt UI Files

If you modify `.ui` files in Qt Designer:

```bash
# Convert .ui to .py
pyuic5 ui/main_test.ui -o ui/main_test_ui.py

# Convert resources
pyrcc5 resources/resources.qrc -o resources/resources_rc.py
```

### Contributing Guidelines

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make** your changes with clear commits:
   ```bash
   git commit -m "Add: Your feature description"
   ```
4. **Test** your changes thoroughly
5. **Push** to your branch:
   ```bash
   git push origin feature/YourFeature
   ```
6. **Open** a Pull Request with:
   - Clear description
   - Screenshots (if UI changes)
   - Test results

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions/classes
- Comment complex logic
- Keep functions focused and small

## 🔮 Roadmap & Future Enhancements

### Version 2.1 (Planned)

- [ ] **Enhanced UI/UX**

  - Modern Material Design theme
  - Dark mode support
  - Responsive layouts
  - Animation improvements

- [ ] **Advanced Features**
  - Multi-face detection
  - Mask detection support
  - Real-time notifications
  - Email integration

### Version 3.0 (Future)

- [ ] **Web Interface**

  - Django/Flask backend
  - REST API
  - Web dashboard
  - Remote access

- [ ] **Mobile Application**

  - Android app
  - iOS app
  - React Native or Flutter
  - Mobile check-in/check-out

- [ ] **Cloud & Scale**

  - Cloud database (PostgreSQL/MySQL)
  - Cloud storage for photos
  - Multi-tenant support
  - Horizontal scaling

- [ ] **Analytics & AI**

  - Advanced analytics dashboard
  - Predictive analytics
  - Behavior analysis
  - Performance predictions
  - Anomaly detection

- [ ] **Integration & API**

  - REST API
  - Webhook support
  - Third-party integrations (Slack, Teams)
  - Export to Excel/PDF
  - Calendar integration

- [ ] **Localization**

  - Multi-language support (FR, EN, AR, ES)
  - RTL support for Arabic
  - Currency/date localization
  - Timezone management

- [ ] **Security Enhancements**
  - Two-factor authentication (2FA)
  - Advanced encryption
  - Audit logs
  - Role-based access control (RBAC)
  - GDPR compliance

### Community Suggestions

Want to suggest a feature? Open an issue with the `enhancement` label!

## 📚 Documentation

- 📖 [README.md](README.md) - Main documentation (you are here)
- 📘 [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- 📝 [CHANGELOG.md](CHANGELOG.md) - Version history (coming soon)
- 🔧 [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines (coming soon)

## 🎓 Learning Resources

### For Beginners

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [PyQt5 Tutorial](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Face Recognition Guide](https://github.com/ageitgey/face_recognition)

### For Advanced Users

- [Qt Designer Documentation](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [SQLite Python Tutorial](https://docs.python.org/3/library/sqlite3.html)

## 🏆 Achievements

- ✅ Clean, organized project structure
- ✅ Modular and maintainable codebase
- ✅ Comprehensive documentation
- ✅ Functional facial recognition
- ✅ Complete CRUD operations
- ✅ Time tracking system
- ✅ Search and filter capabilities

## 💖 Support This Project

If you find this project useful:

- ⭐ **Star** this repository
- 🍴 **Fork** and contribute
- 📢 **Share** with others
- 💬 **Give feedback**
- 🐛 **Report issues**

---

<div align="center">

**FaceSmart** - Smart Employee Management System

_Built with ❤️ using Python and PyQt5_

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green.svg)](https://pypi.org/project/PyQt5/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/el-houfi-achraf/Projet-python-Facesmart?style=social)](https://github.com/el-houfi-achraf/Projet-python-Facesmart)

[🏠 Home](https://github.com/el-houfi-achraf/Projet-python-Facesmart) •
[📖 Docs](README.md) •
[🐛 Issues](https://github.com/el-houfi-achraf/Projet-python-Facesmart/issues) •
[🤝 Contributing](CONTRIBUTING.md)

Copyright © 2024-2025 FaceSmart. All rights reserved.

</div>
