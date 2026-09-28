# ============================================================
#          HOSPITAL PATIENT MANAGEMENT SYSTEM
#          Basic Python Project
# ============================================================

# -------------------- DATA STORAGE ---------------------------

patients = []
doctors = [
    {"id": 1, "name": "Dr. Sharma", "specialization": "General Physician"},
    {"id": 2, "name": "Dr. Verma", "specialization": "Cardiologist"},
    {"id": 3, "name": "Dr. Khan", "specialization": "Orthopedic"},
    {"id": 4, "name": "Dr. Singh", "specialization": "Dermatologist"}
]

rooms = [
    {"room_no": 101, "type": "General", "status": "Available", "patient_id": None},
    {"room_no": 102, "type": "General", "status": "Available", "patient_id": None},
    {"room_no": 103, "type": "General", "status": "Available", "patient_id": None},
    {"room_no": 201, "type": "Private", "status": "Available", "patient_id": None},
    {"room_no": 202, "type": "Private", "status": "Available", "patient_id": None},
    {"room_no": 301, "type": "ICU", "status": "Available", "patient_id": None},
    {"room_no": 302, "type": "ICU", "status": "Available", "patient_id": None}
]

appointments = []
medicines = []
payments = []

patient_counter = 1
appointment_counter = 1
payment_counter = 1


# ============================================================
#                    UTILITY FUNCTIONS
# ============================================================

def line():
    print("=" * 65)


def pause():
    input("\nPress Enter to continue...")


def find_patient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


def find_doctor(doctor_id):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor
    return None


def find_room(room_no):
    for room in rooms:
        if room["room_no"] == room_no:
            return room
    return None


# ============================================================
#                    PATIENT MODULE
# ============================================================

def add_patient():
    global patient_counter

    line()
    print("                 ADD NEW PATIENT")
    line()

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    problem = input("Enter health problem: ")

    patient = {
        "id": patient_counter,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "address": address,
        "problem": problem,
        "doctor": None,
        "room": None,
        "admitted": False
    }

    patients.append(patient)

    print("\nPatient added successfully!")
    print("Patient ID:", patient_counter)

    patient_counter += 1


def view_patients():
    line()
    print("                 ALL PATIENTS")
    line()

    if len(patients) == 0:
        print("No patient records found.")
        return

    for patient in patients:
        print("\nPatient ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Phone:", patient["phone"])
        print("Address:", patient["address"])
        print("Problem:", patient["problem"])

        if patient["doctor"] is not None:
            print("Doctor:", patient["doctor"])
        else:
            print("Doctor: Not assigned")

        if patient["room"] is not None:
            print("Room:", patient["room"])
        else:
            print("Room: Not assigned")

        print("Admitted:", patient["admitted"])
        print("-" * 50)


def search_patient():
    line()
    print("                 SEARCH PATIENT")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    print("\nPatient Found!")
    print("ID:", patient["id"])
    print("Name:", patient["name"])
    print("Age:", patient["age"])
    print("Gender:", patient["gender"])
    print("Phone:", patient["phone"])
    print("Address:", patient["address"])
    print("Problem:", patient["problem"])

    if patient["doctor"]:
        print("Doctor:", patient["doctor"])
    else:
        print("Doctor: Not assigned")

    if patient["room"]:
        print("Room:", patient["room"])
    else:
        print("Room: Not assigned")


def update_patient():
    line()
    print("                 UPDATE PATIENT")
    line()

    patient_id = int(input("Enter patient ID: "))
    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    print("\nCurrent Name:", patient["name"])
    patient["name"] = input("Enter new name: ")

    print("Current Age:", patient["age"])
    patient["age"] = int(input("Enter new age: "))

    print("Current Phone:", patient["phone"])
    patient["phone"] = input("Enter new phone: ")

    print("Current Problem:", patient["problem"])
    patient["problem"] = input("Enter new problem: ")

    print("\nPatient information updated successfully!")


def delete_patient():
    line()
    print("                 DELETE PATIENT")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    patients.remove(patient)

    print("Patient deleted successfully.")


# ============================================================
#                    DOCTOR MODULE
# ============================================================

def view_doctors():
    line()
    print("                 DOCTOR LIST")
    line()

    for doctor in doctors:
        print("Doctor ID:", doctor["id"])
        print("Name:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("-" * 50)


def assign_doctor():
    line()
    print("                 ASSIGN DOCTOR")
    line()

    patient_id = int(input("Enter patient ID: "))
    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    view_doctors()

    doctor_id = int(input("\nEnter doctor ID: "))
    doctor = find_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found.")
        return

    patient["doctor"] = doctor["name"]

    print("Doctor assigned successfully!")


# ============================================================
#                    ROOM MODULE
# ============================================================

def view_rooms():
    line()
    print("                 ROOM INFORMATION")
    line()

    for room in rooms:
        print("Room Number:", room["room_no"])
        print("Room Type:", room["type"])
        print("Status:", room["status"])

        if room["patient_id"] is not None:
            print("Patient ID:", room["patient_id"])
        else:
            print("Patient ID: None")

        print("-" * 50)


def available_rooms():
    line()
    print("                 AVAILABLE ROOMS")
    line()

    found = False

    for room in rooms:
        if room["status"] == "Available":
            print(
                "Room:", room["room_no"],
                "| Type:", room["type"]
            )
            found = True

    if not found:
        print("No rooms are currently available.")


def assign_room():
    line()
    print("                 ASSIGN ROOM")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    available_rooms()

    room_no = int(input("\nEnter room number: "))

    room = find_room(room_no)

    if room is None:
        print("Room not found.")
        return

    if room["status"] == "Occupied":
        print("This room is already occupied.")
        return

    room["status"] = "Occupied"
    room["patient_id"] = patient_id

    patient["room"] = room_no
    patient["admitted"] = True

    print("Room assigned successfully!")


def release_room():
    line()
    print("                 RELEASE ROOM")
    line()

    room_no = int(input("Enter room number: "))

    room = find_room(room_no)

    if room is None:
        print("Room not found.")
        return

    if room["status"] == "Available":
        print("Room is already available.")
        return

    patient_id = room["patient_id"]

    patient = find_patient(patient_id)

    if patient is not None:
        patient["room"] = None
        patient["admitted"] = False

    room["status"] = "Available"
    room["patient_id"] = None

    print("Room released successfully.")


# ============================================================
#                  APPOINTMENT MODULE
# ============================================================

def book_appointment():
    global appointment_counter

    line()
    print("                 BOOK APPOINTMENT")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    view_doctors()

    doctor_id = int(input("\nEnter doctor ID: "))
    doctor = find_doctor(doctor_id)

    if doctor is None:
        print("Doctor not found.")
        return

    date = input("Enter appointment date: ")
    time = input("Enter appointment time: ")

    appointment = {
        "id": appointment_counter,
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "doctor": doctor["name"],
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    print("\nAppointment booked successfully!")
    print("Appointment ID:", appointment_counter)

    appointment_counter += 1


def view_appointments():
    line()
    print("                 APPOINTMENTS")
    line()

    if len(appointments) == 0:
        print("No appointments found.")
        return

    for appointment in appointments:
        print("Appointment ID:", appointment["id"])
        print("Patient ID:", appointment["patient_id"])
        print("Patient Name:", appointment["patient_name"])
        print("Doctor:", appointment["doctor"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("-" * 50)


# ============================================================
#                 ADMISSION MODULE
# ============================================================

def admit_patient():
    line()
    print("                 ADMIT PATIENT")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    if patient["admitted"]:
        print("Patient is already admitted.")
        return

    assign_room()


def discharge_patient():
    line()
    print("                 DISCHARGE PATIENT")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    if patient["room"] is None:
        print("Patient is not currently admitted.")
        return

    room_no = patient["room"]

    room = find_room(room_no)

    room["status"] = "Available"
    room["patient_id"] = None

    patient["room"] = None
    patient["admitted"] = False

    print("Patient discharged successfully.")
    print("Room", room_no, "is now available.")


# ============================================================
#                    MEDICINE MODULE
# ============================================================

def add_medicine():
    line()
    print("                 ADD MEDICINE")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    medicine_name = input("Enter medicine name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    total = quantity * price

    medicine = {
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "medicine": medicine_name,
        "quantity": quantity,
        "price": price,
        "total": total
    }

    medicines.append(medicine)

    print("\nMedicine added successfully.")
    print("Medicine cost:", total)


def view_medicines():
    line()
    print("                 MEDICINE RECORDS")
    line()

    if len(medicines) == 0:
        print("No medicine records found.")
        return

    for medicine in medicines:
        print("Patient ID:", medicine["patient_id"])
        print("Patient Name:", medicine["patient_name"])
        print("Medicine:", medicine["medicine"])
        print("Quantity:", medicine["quantity"])
        print("Price:", medicine["price"])
        print("Total:", medicine["total"])
        print("-" * 50)


# ============================================================
#                  PAYMENT & BILLING
# ============================================================

def generate_bill():
    global payment_counter

    line()
    print("                 GENERATE BILL")
    line()

    patient_id = int(input("Enter patient ID: "))

    patient = find_patient(patient_id)

    if patient is None:
        print("Patient not found.")
        return

    consultation_fee = float(input("Enter consultation fee: "))
    room_charge = float(input("Enter room charge: "))

    medicine_charge = 0

    for medicine in medicines:
        if medicine["patient_id"] == patient_id:
            medicine_charge += medicine["total"]

    other_charge = float(input("Enter other charges: "))

    total = (
        consultation_fee
        + room_charge
        + medicine_charge
        + other_charge
    )

    print("\n")
    line()
    print("                  HOSPITAL BILL")
    line()

    print("Patient ID:", patient["id"])
    print("Patient Name:", patient["name"])
    print("Consultation Fee:", consultation_fee)
    print("Room Charges:", room_charge)
    print("Medicine Charges:", medicine_charge)
    print("Other Charges:", other_charge)

    print("-" * 50)
    print("TOTAL BILL:", total)
    print("-" * 50)

    payment = {
        "id": payment_counter,
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "consultation": consultation_fee,
        "room": room_charge,
        "medicine": medicine_charge,
        "other": other_charge,
        "total": total,
        "status": "Pending"
    }

    payments.append(payment)

    print("Bill generated successfully.")
    print("Bill ID:", payment_counter)

    payment_counter += 1


def make_payment():
    line()
    print("                 MAKE PAYMENT")
    line()

    if len(payments) == 0:
        print("No bills found.")
        return

    patient_id = int(input("Enter patient ID: "))

    found = False

    for payment in payments:

        if payment["patient_id"] == patient_id:

            found = True

            print("\nBill ID:", payment["id"])
            print("Patient:", payment["patient_name"])
            print("Total Amount:", payment["total"])
            print("Status:", payment["status"])

            if payment["status"] == "Paid":
                print("This bill is already paid.")
            else:
                payment["status"] = "Paid"
                print("Payment completed successfully.")

    if not found:
        print("No bill found for this patient.")


def payment_history():
    line()
    print("                 PAYMENT HISTORY")
    line()

    if len(payments) == 0:
        print("No payment records found.")
        return

    for payment in payments:

        print("Bill ID:", payment["id"])
        print("Patient ID:", payment["patient_id"])
        print("Patient Name:", payment["patient_name"])
        print("Total:", payment["total"])
        print("Status:", payment["status"])

        print("-" * 50)


# ============================================================
#                    REPORT MODULE
# ============================================================

def hospital_report():
    line()
    print("                 HOSPITAL REPORT")
    line()

    total_patients = len(patients)

    occupied_rooms = 0
    available_room_count = 0

    for room in rooms:

        if room["status"] == "Occupied":
            occupied_rooms += 1
        else:
            available_room_count += 1

    total_doctors = len(doctors)
    total_appointments = len(appointments)

    total_revenue = 0

    for payment in payments:

        if payment["status"] == "Paid":
            total_revenue += payment["total"]

    print("Total Patients:", total_patients)
    print("Total Doctors:", total_doctors)
    print("Total Rooms:", len(rooms))
    print("Occupied Rooms:", occupied_rooms)
    print("Available Rooms:", available_room_count)
    print("Total Appointments:", total_appointments)
    print("Total Paid Revenue:", total_revenue)


# ============================================================
#                 PATIENT MENU
# ============================================================

def patient_menu():

    while True:

        line()
        print("                 PATIENT MANAGEMENT")
        line()

        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_patient()
            pause()

        elif choice == "2":
            view_patients()
            pause()

        elif choice == "3":
            search_patient()
            pause()

        elif choice == "4":
            update_patient()
            pause()

        elif choice == "5":
            delete_patient()
            pause()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


# ============================================================
#                    ROOM MENU
# ============================================================

def room_menu():

    while True:

        line()
        print("                 ROOM MANAGEMENT")
        line()

        print("1. View All Rooms")
        print("2. View Available Rooms")
        print("3. Assign Room")
        print("4. Release Room")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_rooms()
            pause()

        elif choice == "2":
            available_rooms()
            pause()

        elif choice == "3":
            assign_room()
            pause()

        elif choice == "4":
            release_room()
            pause()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ============================================================
#                  DOCTOR MENU
# ============================================================

def doctor_menu():

    while True:

        line()
        print("                 DOCTOR MANAGEMENT")
        line()

        print("1. View Doctors")
        print("2. Assign Doctor")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_doctors()
            pause()

        elif choice == "2":
            assign_doctor()
            pause()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


# ============================================================
#               APPOINTMENT MENU
# ============================================================

def appointment_menu():

    while True:

        line()
        print("                 APPOINTMENT MANAGEMENT")
        line()

        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            book_appointment()
            pause()

        elif choice == "2":
            view_appointments()
            pause()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


# ============================================================
#                ADMISSION MENU
# ============================================================

def admission_menu():

    while True:

        line()
        print("                 ADMISSION MANAGEMENT")
        line()

        print("1. Admit Patient")
        print("2. Discharge Patient")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            admit_patient()
            pause()

        elif choice == "2":
            discharge_patient()
            pause()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


# ============================================================
#                  MEDICINE MENU
# ============================================================

def medicine_menu():

    while True:

        line()
        print("                 MEDICINE MANAGEMENT")
        line()

        print("1. Add Medicine")
        print("2. View Medicine Records")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_medicine()
            pause()

        elif choice == "2":
            view_medicines()
            pause()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


# ============================================================
#                  PAYMENT MENU
# ============================================================

def payment_menu():

    while True:

        line()
        print("                 PAYMENT MANAGEMENT")
        line()

        print("1. Generate Bill")
        print("2. Make Payment")
        print("3. Payment History")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            generate_bill()
            pause()

        elif choice == "2":
            make_payment()
            pause()

        elif choice == "3":
            payment_history()
            pause()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


# ============================================================
#                    MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        line()
        print("          HOSPITAL PATIENT MANAGEMENT SYSTEM")
        line()

        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Room Management")
        print("4. Appointment Management")
        print("5. Admission & Discharge")
        print("6. Medicine Management")
        print("7. Payment & Billing")
        print("8. Hospital Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            room_menu()

        elif choice == "4":
            appointment_menu()

        elif choice == "5":
            admission_menu()

        elif choice == "6":
            medicine_menu()

        elif choice == "7":
            payment_menu()

        elif choice == "8":
            hospital_report()
            pause()

        elif choice == "9":
            print("\nThank you for using Hospital Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# ============================================================
#                    START PROGRAM
# ============================================================

main()