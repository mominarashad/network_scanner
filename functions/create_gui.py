import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from functions.scan_range import scan_range
from functions.save_results import save_results_csv
from functions.save_results_json import save_results_json
from functions.generate_graph import generate_graph
import threading
import random
# List of network trivia
network_trivia = [
    "Did you know? The first computer virus was created in 1983!",
    "Did you know? The world's first 1GB hard drive, released in 1980, weighed over 200 pounds!",
    "Did you know? The term 'Wi-Fi' doesn't stand for anything. It's just a name!",
    "Did you know? The first email was sent by Ray Tomlinson to himself in 1971!",
    "Did you know? The first-ever web page was published on August 6, 1991, by Tim Berners-Lee!"
]

def create_gui():
    root = tk.Tk()
    root.title("Network Scanner")
    root.geometry("1200x700")  # Increased size for better spacing
    
    # Set initial mode to dark
    mode = "dark"

    # Function to toggle between light and dark modes
    def toggle_mode():
        nonlocal mode
        if mode == "dark":
            root.configure(bg="#ecf0f1")
            ip_label.configure(bg="#ecf0f1", fg="#2C3E50")
            title_label.configure(bg="#ecf0f1", fg="#2C3E50")
            tree.configure(style="Light.Treeview")
            mode = "light"
            toggle_button.config(bg="#3498db", fg="white", text="Switch to Dark Mode")
        else:
            root.configure(bg="#2C3E50")
            ip_label.configure(bg="#2C3E50", fg="white")
            title_label.configure(bg="#2C3E50", fg="white")
            tree.configure(style="Custom.Treeview")
            mode = "dark"
            toggle_button.config(bg="#e67e22", fg="white", text="Switch to Light Mode")

    # Title label
    title_label = tk.Label(root, text="Network Scanner", bg="#2C3E50", fg="white", font=("Arial", 18, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Toggle button for theme
    toggle_button = tk.Button(root, text="Switch to Light Mode", command=toggle_mode, font=("Arial", 12, "bold"),
                              bg="#e67e22", fg="white", width=20)
    toggle_button.grid(row=0, column=2, padx=20, pady=20, sticky="e")

    # Entry label and field with placeholder
    ip_label = tk.Label(root, text="Enter IP Address or Range:", bg="#2C3E50", fg="white", font=("Arial", 12, "bold"))
    ip_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    ip_entry = tk.Entry(root, width=30, font=("Arial", 12))
    ip_entry.insert(0, "e.g., 192.168.1.0/24")  # Placeholder text
    ip_entry.grid(row=1, column=1, padx=20, pady=20, sticky="w")

    # Table for displaying results
    columns = ("IP Address", "MAC Address", "Vendor", "Open Ports", "OS", "Network Speed", "Domain", "Security Status")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=15, style="Custom.Treeview")
    tree.tag_configure('evenrow', background="#ecf0f1")  # Styling even rows
    tree.tag_configure('oddrow', background="#bdc3c7")  # Styling odd rows
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")

    tree.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

    results = []

    # Frame for buttons
    button_frame = tk.Frame(root, bg="#ecf0f1")
    button_frame.grid(row=3, column=0, columnspan=3, pady=20)

    # Scan button
    scan_button = tk.Button(button_frame, text="Scan", bg="#3498db", fg="white", font=("Arial", 12, "bold"))
    scan_button.pack(side="left", padx=10, pady=10)

    # Export buttons
    export_csv_button = tk.Button(button_frame, text="Export to CSV", bg="#2ecc71", fg="white", font=("Arial", 12, "bold"),
                                   command=lambda: save_results_csv(results))
    export_csv_button.pack(side="left", padx=10, pady=10)

    export_json_button = tk.Button(button_frame, text="Export to JSON", bg="#9b59b6", fg="white", font=("Arial", 12, "bold"),
                                   command=lambda: save_results_json(results))
    export_json_button.pack(side="left", padx=10, pady=10)

    generate_graph_button = tk.Button(button_frame, text="Generate Graph", bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
                                      command=lambda: generate_graph(results))
    generate_graph_button.pack(side="left", padx=10, pady=10)

    # Progress bar for visual feedback during scanning
    progress_bar = ttk.Progressbar(root, mode='indeterminate', length=400)
    progress_bar.grid(row=4, column=0, columnspan=3, pady=10)

    def start_scan():
        ip_range = ip_entry.get()
        if not ip_range:
            messagebox.showerror("Input Error", "Please enter a valid IP address or range!")
            return

        progress_bar.start()
        threading.Thread(target=scan_range, args=(ip_range, tree, progress_bar, results), daemon=True).start()

    # Update scan button to use threading
    scan_button.config(command=start_scan)

    # Trivia button
    def show_trivia():
        trivia = random.choice(network_trivia)
        messagebox.showinfo("Network Trivia", trivia)

    trivia_button = tk.Button(button_frame, text="Show Trivia", bg="#f1c40f", fg="black", font=("Arial", 12, "bold"),
                              command=show_trivia)
    trivia_button.pack(side="left", padx=10, pady=10)

    # Start GUI loop
    toggle_mode()  # Initialize to dark mode
    root.mainloop()
