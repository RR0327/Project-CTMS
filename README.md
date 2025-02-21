<h1 align="center">Campus Transport Management System (CTMS)</h1>

Campus Transport Management System is a web-based application designed to manage campus transportation services efficiently. This system enhances campus transportation by enabling bus schedule tracking, automated Gmail notifications, QR code-based transport cards, and staff information access. Admins get a powerful dashboard to manage transport details and user data efficiently.


## Features

### Secure User Authentication & Role-based Access
- Users (students, faculty, and admin) can register and log in securely.
- Role-based access control ensures different permissions for users and admins.

### Automated Notifications for Timely Updates
- Users receive real-time notifications about bus schedules, delays, and route changes.
- Email and in-app alerts keep passengers informed.

### QR Code Transport Cards for Easy Access
- Generates unique QR codes for digital transport passes.
- QR codes are scannable for quick check-in.

### Bus Scheduling System for Efficient Management
- Admins can create and manage transport schedules dynamically.
- Users can view available transport options.

### Admin Dashboard for Comprehensive Control
- Admins can manage routes, schedules, and users from a central panel.


## Technologies Used

### **Backend**
- **Python Django**: Framework used to build the backend.
- **PostgreSQL**: Database used for managing transport-related data.

### **Frontend**
- **HTML, CSS, JavaScript**: For building the user interface.

### **Dependencies (Python Libraries)**
```
pip install asgiref==3.8.1 Django==5.1.5 django-extensions==3.2.3 pillow==11.1.0 psycopg2==2.9.10 psycopg2-binary==2.9.10 qrcode==8.0 sqlparse==0.5.3 reportlab
```

---

## Installation & Setup


### 1. Clone the Repository:
```
git clone https://github.com/your_username/Campus-Transport-Management.git
cd Campus-Transport-Management
```

### 2. Create & Activate Virtual Environment:
```
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies:
```
pip install -r requirements.txt
```

### 4. Set Up Environment Variables:
- Create a `.env` file in the root directory.
- Add necessary variables like:
  ```
  DATABASE_URL=postgres://your_db_username:your_db_password@localhost:5432/your_db_name
  SECRET_KEY=your_django_secret_key
  DEBUG=True
  ```

### 5. Apply Migrations:
```
python manage.py migrate
```

### 6. Create a Superuser (For Admin Panel):
```
python manage.py createsuperuser
```

### 7. Run the Application:
```
python manage.py runserver
```


## Usage


1. **Register & Login Securely**  
   - Sign up as a student, faculty, or admin.  

2. **Receive Instant Transport Notifications**  
   - Get alerts for schedules, delays, and route changes.  

3. **Generate & Use QR Code Pass**  
   - Scan QR codes for quick check-in and verification.  

4. **Manage Routes & Schedules (Admin)**  
   - Add, update, or cancel bus schedules anytime.  

5. **View Reports & Analytics (Admin)**  
   - Check transport usage, occupancy, and live stats.  

6. **Monitor User & Admin Activities**  
   - Track system usage, login records, and transactions.  

7. **Ensure Secure Role-Based Access**  
   - Restrict access based on user roles and permissions.  


## Contributors

- Md Rakibul Hassan, Md Tahsin Azad Shaikat, Dipa Barua, Md Ifthakhar Alam Shams, Saima Sharmin Shama
