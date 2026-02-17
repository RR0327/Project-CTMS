<h1 align="center">Campus Transport Management System (CTMS)</h1>

## Overview

The Campus Transport Management System (CTMS) is a professional, glassmorphism-themed web application developed for BAIUST to digitize campus transit. It streamlines the commute for students and staff through real-time searchable schedules, digital transport passes, and automated administrative controls.

---

## Features

### Transport and Schedule Management

- **Public Central Schedule**: A comprehensive, searchable timetable accessible without login for easy trip planning.
- **Trip Categorization**: Specifically tracks and filters for Up-trips (To Campus) and Down-trips (From Campus).
- **Real-time Route Search**: Instant filtering for specific routes (e.g., Kandirpar, Sasason) or bus numbers.
- **Administrative Posting**: Admins can publish live route updates directly through a dedicated web form.

### Digital Pass and Profile

- **Digital Transport Pass**: Automated generation of student and faculty transport cards using unique university IDs.
- **Profile Dashboard**: Personal interface to view academic details and transport card status.

### Admin and Export Tools

- **User Management**: A high-level dashboard for administrators to view and manage all registered campus members.
- **PDF Export Utility**: Enables users to generate and download official offline versions of the transport schedule.

### Communication and Support

- **Automated Alerts**: Email notifications for schedule updates, delays, and secure password resets.
- **Support Interface**: Integrated contact form with automated routing to the transport office for queries.

---

## Technologies Used

### Backend and Database

- **Python Django 5.1.5**
- **SQLite3** (Current development database)
- **Libraries**: ReportLab (PDF), Pillow (Images), Django-Extensions.

### Frontend

- **Bootstrap 5 and Font Awesome 6.5.1** for responsive UI.
- **Glassmorphism CSS**: Custom modern UI design system with blur and transparency effects.
- **Animate.css**: For smooth page transitions and entry animations.

---

## Installation and Setup

### 1. Clone and Environment

```bash
git clone https://github.com/your_username/CTMS-BAIUST.git
cd CTMS-BAIUST
python -m venv venv
venv\Scripts\activate  # Windows

```

### 2. Install Dependencies

```bash
pip install django reportlab pillow django-extensions

```

### 3. Database and Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```

### 4. Run the Server

```bash
python manage.py runserver

```

---

## Credits and Contributions

### Current Updated Project (Phase II)

- **Md Rakibul Hassan**: Backend Development
- **Md Tahsin Azad Shaikat**: Backend Development
- **Dipa Barua**: Frontend Development
- **Saima Sharmin Shama**: Frontend Development

### Previous Version Credits (Phase I)

- **Md Rakibul Hassan**: Backend Development
- **Md Tahsin Azad Shaikat**: Backend Development
- **Dipa Barua**: Frontend Development
- **Saima Sharmin Shama**: Manual Testing
- **Md Ifthakhar Alam Shams**: Database Sector Contribution Only

---

## Contributors

- _Md Rakibul Hassan_

  CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast
  [LinkedIn](https://www.linkedin.com/in/md-rakibul-hassan-507b00308)

- _Md Tahsin Azad Shaikat_

  CSE Undergraduate | Backend Developer | Robotics & IoT Enthusiast
  [LinkedIn](https://www.linkedin.com/in/mdtahsinazad020/)

- _Dipa Barua_

  CSE Undergraduate | Frontend Developer | UI/UX Designer
  [LinkedIn](https://www.linkedin.com/in/dipa-barua-387071303/)

- _Md Ifthakhar Alam Shams_

  CSE Undergraduate | Database Developer | Prompt Engineering
  [LinkedIn](https://www.linkedin.com/in/md-ifthakhar-alam-shams-85080a29a/)

- _Saima Sharmin Shama_

  CSE Undergraduate | UI/UX Designer | Manual Testing
  [LinkedIn](https://www.linkedin.com/in/saima-sharmin-865148325/)

---

## License

This project is open source and available under the **MIT License**.

---
