<h1 align="center">Campus Transport Management System (CTMS)</h1>

## Overview

This is a comprehensive web-based Campus Transport Management System designed to efficiently manage campus transportation services. Built with Django, the system facilitates user registration, authentication, transport scheduling, real-time notifications, QR code-based transport cards, and staff management. It provides an admin dashboard for managing routes, schedules, and user data, ensuring a seamless transportation experience on campus.

---

## Features

### User Management & Authentication
- Secure registration and login for students, faculty, and admin roles
- Role-based access control
- Profile management and QR code generation with student/faculty IDs

### Transport & Schedule Management
- Dynamic creation and updates of bus routes and schedules
- View current and upcoming transport schedules
- Real-time notifications about delays, route changes, and timetable updates

### QR Code Transport Cards
- Generates unique QR codes for digital transport passes
- Scannable for quick check-in and validation

### Notifications & Alerts
- Automated email and in-app notifications to keep users informed about schedules, delays, and system updates

### Admin Dashboard & Control Panel
- Manage users, routes, schedules, and notifications
- View and analyze transport usage and occupancy

---

## Technologies Used

### Backend
- **Python Django** (latest stable version)
- **PostgreSQL** 
- **Libraries:** Pillow, qrcode, psycopg2, django-extensions, reportlab

### Frontend
- HTML, CSS, JavaScript (for dashboard and user interfaces)

### Dependencies
```bash
pip install asgiref==3.8.1 Django==5.1.5 django-extensions==3.2.3 pillow==11.1.0 psycopg2==2.9.10 psycopg2-binary==2.9.10 qrcode==8.0 sqlparse==0.5.3 reportlab
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your_username/Campus-Transport-Management.git
cd Campus-Transport-Management
```

### 2. Create & Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
- Create a `.env` file in the root directory
- Add variables:
```
DATABASE_URL=postgres://your_db_username:your_db_password@localhost:5432/your_db_name
SECRET_KEY=your_django_secret_key
DEBUG=True
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```

---

## Usage

### User Registration & Login
- Register as student/faculty via the signup page (`/register`)
- Login at `/login` with your credentials

### Transport Management
- View schedules at `/schedule`
- Receive notifications for delays/routes
- Use QR code cards for quick check-in

### Admin Panel
- Access at `/admin/`
- Manage users, routes, schedules, notifications, and reports

---

## Contributors

- **Md Rakibul Hassan**

  CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast
🔗 [LinkedIn](https://www.linkedin.com/in/md-rakibul-hassan-507b00308)

- **Md Tahsin Azad Shaikat**

CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast
🔗 [LinkedIn](https://www.linkedin.com/in/mdtahsinazad020/)

- **Dipa Barua**

CSE Undergraduate | Frontend Developer | UI/UX Designer
🔗 [LinkedIn](https://www.linkedin.com/in/dipa-barua-387071303/)

- **Md Ifthakhar Alam Shams**

CSE Undergraduate | Database Developer | Prompt Engineering
🔗 [LinkedIn](https://www.linkedin.com/in/md-ifthakhar-alam-shams-85080a29a/)

- **Saima Sharmin Shama**

CSE Undergraduate | UI/UX Designer | Manual Testing
🔗 [LinkedIn](https://www.linkedin.com/in/saima-sharmin-865148325/)

## License

This project is open source and available under the MIT License.
