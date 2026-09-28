#  Hospital Patient Management System

##  Project Overview

The **Hospital Patient Management System** is a basic Python project designed to manage different activities of a hospital.

This project is developed using **basic Python concepts only**. It does not use SQL, SQLite, Streamlit, or any external libraries.

The system provides different modules for managing patients, doctors, rooms, appointments, admissions, medicines, payments, and hospital reports.

---

## Objectives

The main objectives of this project are:

* To maintain patient information.
* To manage doctors and their specializations.
* To check room availability.
* To assign rooms to patients.
* To manage patient admission and discharge.
* To book and view appointments.
* To maintain medicine records.
* To generate patient bills.
* To manage payments.
* To display basic hospital reports.
* To practice fundamental Python programming concepts.

---

## Technologies Used

* **Programming Language:** Python
* **Level:** Beginner / Basic Python
* **Database:** None
* **External Libraries:** None
* **Interface:** Console / Terminal

### Python Concepts Used

* Variables
* Lists
* Dictionaries
* Functions
* `if`, `elif`, `else`
* `for` loops
* `while` loops
* User input
* Basic calculations
* Global variables
* Searching through lists

---

# Project Modules

## 1. Patient Management

This module manages patient information.

### Features

* Add a new patient
* View all patients
* Search for a patient
* Update patient information
* Delete patient information

### Patient Information

The system stores:

* Patient ID
* Name
* Age
* Gender
* Phone number
* Address
* Health problem
* Assigned doctor
* Assigned room
* Admission status

---

## 2. Doctor Management

This module manages hospital doctors.

### Features

* View doctors
* View doctor specializations
* Assign a doctor to a patient

Example specializations include:

* General Physician
* Cardiologist
* Orthopedic
* Dermatologist

---

## 3. Room Management

This module manages hospital rooms.

### Features

* View all rooms
* Check available rooms
* Assign a room
* Release a room

The project contains different room types:

* General
* Private
* ICU

Each room has a status:

```text
Available
Occupied
```

---

## 4. Appointment Management

This module manages patient appointments.

### Features

* Book an appointment
* View appointments

Appointment information includes:

* Appointment ID
* Patient ID
* Patient name
* Doctor
* Date
* Time

---

## 5. Admission & Discharge

This module manages patient admission and discharge.

### Admission

When a patient is admitted:

1. Patient ID is entered.
2. An available room is selected.
3. The room becomes occupied.
4. The patient's admission status becomes `True`.

### Discharge

When a patient is discharged:

1. Patient ID is entered.
2. The assigned room is found.
3. The room becomes available.
4. The patient's admission status becomes `False`.

---

## 6.  Medicine Management

This module keeps track of medicines given to patients.

### Features

* Add medicine
* View medicine records
* Calculate medicine cost

Medicine information includes:

* Patient ID
* Patient name
* Medicine name
* Quantity
* Price per unit
* Total medicine cost

The total cost is calculated using:

```text
Total = Quantity × Price
```

---

## 7.  Payment & Billing

This module handles hospital bills and payments.

### Features

* Generate bill
* Calculate total bill
* Make payment
* View payment history

The bill can include:

```text
Consultation Fee
Room Charges
Medicine Charges
Other Charges
```

The total bill is calculated as:

```text
Total Bill =
Consultation Fee
+ Room Charges
+ Medicine Charges
+ Other Charges
```

Payment status can be:

```text
Pending
Paid
```

---

## 8.  Hospital Report

The hospital report provides basic statistics.

It displays:

* Total patients
* Total doctors
* Total rooms
* Occupied rooms
* Available rooms
* Total appointments
* Total paid revenue

---

#  Main Menu

When the program starts, the following menu is displayed:

```text
=============================================================
          HOSPITAL PATIENT MANAGEMENT SYSTEM
=============================================================

1. Patient Management
2. Doctor Management
3. Room Management
4. Appointment Management
5. Admission & Discharge
6. Medicine Management
7. Payment & Billing
8. Hospital Report
9. Exit
```

---

#  How to Run the Project

### Step 1: Install Python

Install Python on your computer if it is not already installed.

### Step 2: Create the Python File

Create a file named:

```text
main.py
```

### Step 3: Copy the Project Code

Paste the Hospital Patient Management System code into `main.py`.

### Step 4: Run the Program

Open the terminal in the project folder and run:

```bash
python main.py
```

The main menu will appear.

---

# Data Storage

This project **does not use a database**.

The information is temporarily stored using Python:

```python
patients = []
doctors = []
rooms = []
appointments = []
medicines = []
payments = []
```

Dictionaries are used to store individual records.

For example:

```python
patient = {
    "id": 1,
    "name": "Rahul",
    "age": 25,
    "gender": "Male",
    "problem": "Fever"
}
```

Because there is no database or file storage, the data will be lost when the program is closed.

---

#  Basic Working Flow

```text
Start
  ↓
Main Menu
  ↓
Select Module
  ↓
Perform Operation
  ↓
Display Result
  ↓
Return to Main Menu
  ↓
Exit
```

---

#  Project Structure

```text
Hospital-Patient-Management/
│
├── main.py
│
└── README.md
```

---

#  Key Features

* Simple console-based interface
* Beginner-friendly Python code
* Multiple hospital management modules
* Patient ID generation
* Room availability management
* Doctor assignment
* Appointment booking
* Admission and discharge
* Medicine cost calculation
* Hospital billing
* Payment tracking
* Hospital statistics
* No external libraries required

---

#  Limitations

Since this project is made using only basic Python:

* Data is not permanently stored.
* There is no SQL database.
* There is no login system.
* There is no graphical interface.
* The program runs through the terminal.
* Data is lost after closing the program.

These limitations are intentional because the project focuses on learning **basic Python programming concepts**.

---

#  Future Improvements

The project can be improved in the future by adding:

* File handling for permanent data storage
* Login and authentication
* GUI using Tkinter
* Database using SQLite/MySQL
* Web interface
* Automatic bill generation
* More detailed patient reports
* Doctor availability schedules
* Prescription management
* Search and filtering options

---

#  Project Type

**Academic / Educational Project**

### Subject

**Python Programming**

### Project

**Hospital Patient Management System**

### Programming Level

**Beginner / Basic Python**

---

## Conclusion

The Hospital Patient Management System demonstrates how basic Python programming concepts can be combined to create a practical hospital management application.

The project provides experience with **functions, lists, dictionaries, loops, conditional statements, user input, and basic calculations** while solving a real-world management problem.
