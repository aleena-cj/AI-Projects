import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

hospital = {
    "Cardiology": {
        "doctor": "Dr. Sharma",
        "timing": "9 AM - 1 PM",
        "room": "101"
    },
    "Neurology": {
        "doctor": "Dr. Gupta",
        "timing": "10 AM - 2 PM",
        "room": "102"
    },
    "Orthopedics": {
        "doctor": "Dr. Rao",
        "timing": "11 AM - 4 PM",
        "room": "103"
    }
}


class HospitalBot:

    def __init__(self, root):
        self.root = root
        self.root.title("CareWell Hospital Assistant")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f4f6f9")

        self.selected_department = None

        # Header
        header = tk.Frame(root, bg="#0078D7", height=70)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="🏥 CareWell Hospital Assistant",
            font=("Segoe UI", 20, "bold"),
            bg="#0078D7",
            fg="white"
        )
        title.pack(pady=15)

        # Main Frame
        main = tk.Frame(root, bg="#f4f6f9")
        main.pack(fill="both", expand=True)

        # Sidebar
        sidebar = tk.Frame(main, bg="#2c3e50", width=250)
        sidebar.pack(side="left", fill="y")

        tk.Label(
            sidebar,
            text="Departments",
            font=("Segoe UI", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack(pady=20)

        for dept in hospital.keys():
            btn = tk.Button(
                sidebar,
                text=dept,
                font=("Segoe UI", 12),
                bg="#3498db",
                fg="white",
                width=20,
                command=lambda d=dept: self.show_department(d)
            )
            btn.pack(pady=10)

        # Chat Section
        right = tk.Frame(main, bg="white")
        right.pack(side="right", fill="both", expand=True)

        self.chat = tk.Text(
            right,
            font=("Segoe UI", 11),
            bg="white",
            bd=0
        )
        self.chat.pack(fill="both", expand=True, padx=10, pady=10)

        self.chat.insert(
            tk.END,
            "\n🤖 Welcome to CareWell Hospital!\n\n"
            "Select a department from the left panel.\n\n"
        )

        bottom = tk.Frame(right, bg="#ecf0f1")
        bottom.pack(fill="x")

        self.entry = ttk.Entry(bottom, font=("Segoe UI", 12))
        self.entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        send_btn = tk.Button(
            bottom,
            text="Send",
            bg="#0078D7",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            command=self.send_message
        )
        send_btn.pack(side="right", padx=10)

    def show_department(self, dept):

        self.selected_department = dept

        info = hospital[dept]

        self.chat.insert(
            tk.END,
            f"\n👤 Selected: {dept}\n\n"
        )

        self.chat.insert(
            tk.END,
            f"🤖 Department: {dept}\n"
            f"Doctor: {info['doctor']}\n"
            f"Timing: {info['timing']}\n"
            f"Room No: {info['room']}\n\n"
        )

        book = messagebox.askyesno(
            "Appointment",
            f"Book appointment in {dept}?"
        )

        if book:
            self.book_appointment()

    def book_appointment(self):

        name = simpledialog.askstring(
            "Appointment",
            "Enter Patient Name"
        )

        if name:

            self.chat.insert(
                tk.END,
                f"✅ Appointment booked successfully\n"
                f"Patient: {name}\n"
                f"Department: {self.selected_department}\n\n"
            )

            messagebox.showinfo(
                "Success",
                "Appointment Confirmed"
            )

    def send_message(self):

        msg = self.entry.get().strip()

        if not msg:
            return

        self.chat.insert(
            tk.END,
            f"\n👤 {msg}\n"
        )

        self.chat.insert(
            tk.END,
            "🤖 Please select a department from the left panel.\n\n"
        )

        self.entry.delete(0, tk.END)


root = tk.Tk()
app = HospitalBot(root)
root.mainloop()