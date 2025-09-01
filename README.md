# 🏥 Hospital Management System  

A **Python + MySQL based Hospital Management System** that helps manage patients, doctors, nurses, and workers.  
It includes **user authentication, patient admission/discharge, and admin tasks** like adding, viewing, and deleting staff details.  

---

## ✨ Features  

- **User Authentication**
  - Sign Up (New User Registration)
  - Login with username & password  

- **Admin Tasks**
  - Show details of doctors, nurses, and workers  
  - Add new members (Doctors, Nurses, Workers)  
  - Delete existing members  

- **Patient Management**
  - Show all patient records  
  - Admit new patients (auto-generates patient ID)  
  - Discharge patients after bill payment  

---

## 🛠️ Technologies Used  

- **Programming Language:** Python 3  
- **Database:** MySQL  
- **Connector:** `mysql.connector` (Python MySQL driver)  

---

## 📂 Database Schema  

### Patients Table  
| Column   | Type        | Description              |  
|----------|------------|--------------------------|  
| pid      | INT(10)    | Patient ID (Primary Key) |  
| name     | VARCHAR(30)| Patient Name             |  
| mobile   | VARCHAR(10)| Mobile Number            |  
| age      | INT(3)     | Age                      |  
| city     | VARCHAR(50)| City                     |  
| doc_rec  | VARCHAR(30)| Doctor Recommended       |  

### Doctors Table  
| Column      | Type         | Description             |  
|-------------|-------------|-------------------------|  
| name        | VARCHAR(30) | Doctor Name (Primary Key)|  
| department  | VARCHAR(40) | Department              |  
| age         | INT(2)      | Age                     |  
| city        | VARCHAR(30) | City                    |  
| mobile      | VARCHAR(15) | Mobile Number           |  
| fees        | INT(10)     | Consultation Fees       |  
| salary      | INT(10)     | Salary                  |  

### Nurses & Workers Tables  
- Contain: `name, age, city, mobile, salary`  

### Users Table  
| Column    | Type         | Description             |  
|-----------|-------------|-------------------------|  
| username  | VARCHAR(30) | User login ID (Primary) |  
| password  | VARCHAR(30) | User password           |  

---

## ⚙️ Installation & Setup  

1. **Clone this repository**  
   ```bash
   git clone https://github.com/prattyan/Hospital-Management-System.git
   cd Hospital-Management-System
   ```

2. **Install required Python package**  
   ```bash
   pip install mysql-connector-python
   ```

3. **Setup MySQL Database**  
   - Make sure MySQL server is running.  
   - Use MySQL root user (or update script with your DB user).  
   - The program will **auto-create `hospital` database and required tables**.  

4. **Run the project**  
   ```bash
   python main.py
   ```

---

## 🚀 Usage  

1. Start the application → Enter your MySQL password.  
2. Choose from main menu:  
   - **1. Sign Up** → Register a new user.  
   - **2. Login** → Enter credentials to access system.  
   - **3. Exit** → Quit program.  
3. Once logged in:  
   - **Admin Tasks** → Manage doctors, nurses, workers.  
   - **Patient Management** → Admit, view, or discharge patients.  

---

## 📸 Example Output  

```
================================
     Welcome to Hospital
================================

1. Sign Up (New User)
2. Log In
3. Exit
************************
```

---

## 📌 Notes  

- Default database password must be entered correctly at startup.  
- Patient IDs are auto-generated.  
- Admin can add, view, and delete hospital staff.  

---

## 🤝 Contribution  

Contributions are welcome! If you’d like to improve this project, feel free to fork and submit a PR.  

---

## 📜 License  

This project is licensed under the **MIT License**.  
