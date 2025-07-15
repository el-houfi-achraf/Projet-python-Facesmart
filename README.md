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

## 🏗️ Project Structure

```
Projet-python-Facesmart/
├── main_test.py                 # Main application entry point
├── sidebar_test.py              # Main sidebar interface
├── database.db                  # SQLite database
├── employer.py                  # Employee management logic
├── tache.py                     # Task management logic
├── suiviTemps.py               # Time tracking logic
├── face_test.py                # Facial recognition interface
├── face-recog.py               # Face recognition implementation
├── data/                       # Employee photos storage
│   ├── achraf_lhoufi_1.png
│   ├── ahmed_labchiri_1.png
│   └── ...
├── images/                     # UI images and resources
├── learn/                      # Learning and testing files
└── UI Files/
    ├── *.ui                    # Qt Designer UI files
    └── *_ui.py                 # Generated UI Python files
```

## 🗄️ Database Schema

### Tables

- **Employe**: Employee information (id, nom, prenom, email, password, id_tache)
- **Tache**: Task management (id, libelle, Status)
- **SuiviTemps**: Time tracking (idPeriod, DateArrivee, DateDepart, id)

## 🚀 Installation

### Prerequisites

- Python 3.7+
- pip package manager
- Webcam (for facial recognition)

### Required Dependencies

```bash
pip install PyQt5
pip install opencv-python
pip install face-recognition
pip install numpy
pip install sqlite3
```

### Setup Instructions

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
   python main_test.py
   ```

## 💻 Usage

### Starting the Application

1. Launch the main application: `python main_test.py`
2. Use the sidebar navigation to access different modules
3. Login with employee credentials or admin access

### Employee Management

- **Add Employee**: Navigate to employee management → Add new employee
- **Search Employee**: Use the search functionality to find specific employees
- **Update Information**: Edit employee details and save changes

### Facial Recognition Setup

1. **Add Employee Photo**: Place employee photos in the `data/` directory
2. **Format**: Use naming convention: `firstname_lastname_1.png`
3. **Test Recognition**: Use the face test module to verify recognition

### Task Management

- **Create Tasks**: Add new tasks with status tracking
- **Assign Tasks**: Link tasks to specific employees
- **Monitor Progress**: Track task completion and status updates

### Time Tracking

- **Clock In**: Use facial recognition to start work session
- **Clock Out**: End work session with face recognition
- **View Reports**: Generate attendance and productivity reports

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

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Achraf El Houfi** - [GitHub Profile](https://github.com/el-houfi-achraf)

## 🐛 Known Issues

- Ensure proper lighting for optimal facial recognition
- Camera permissions may need to be granted on first run
- Some UI elements may require PyQt5 specific versions

## 🔮 Future Enhancements

- [ ] Web-based interface
- [ ] Mobile application
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Cloud synchronization
- [ ] Advanced reporting features

---

_Built with ❤️ using Python and PyQt5_
