
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Contact Book App")
root.geometry("700x500")
root.config(bg="#f0f0f0")

contacts = []
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get("1.0", tk.END).strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    messagebox.showinfo("Success", "Contact Added Successfully!")
    clear_fields()
    view_contacts()


def view_contacts():
    listbox.delete(0, tk.END)

    for index, contact in enumerate(contacts):
        display = f"{index+1}. {contact['name']} - {contact['phone']}"
        listbox.insert(tk.END, display)


def search_contact():
    keyword = entry_search.get().lower()

    listbox.delete(0, tk.END)

    found = False

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            display = f"{contact['name']} - {contact['phone']}"
            listbox.insert(tk.END, display)
            found = True

    if not found:
        messagebox.showinfo("Search", "No Contact Found")


def delete_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact to delete")
        return

    index = selected[0]
    del contacts[index]

    messagebox.showinfo("Deleted", "Contact Deleted Successfully")
    view_contacts()


def update_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showerror("Error", "Select a contact to update")
        return

    index = selected[0]

    contacts[index]["name"] = entry_name.get()
    contacts[index]["phone"] = entry_phone.get()
    contacts[index]["email"] = entry_email.get()
    contacts[index]["address"] = entry_address.get("1.0", tk.END).strip()

    messagebox.showinfo("Updated", "Contact Updated Successfully")
    view_contacts()


def load_selected_contact(event):
    selected = listbox.curselection()

    if not selected:
        return

    index = selected[0]
    contact = contacts[index]

    clear_fields()

    entry_name.insert(0, contact["name"])
    entry_phone.insert(0, contact["phone"])
    entry_email.insert(0, contact["email"])
    entry_address.insert(tk.END, contact["address"])


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)


title = tk.Label(
    root,
    text="CONTACT BOOK APPLICATION",
    font=("Arial", 20, "bold"),
    bg="#f0f0f0",
    fg="darkblue"
)
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Name", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, width=40)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Phone", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="w")
entry_phone = tk.Entry(frame, width=40)
entry_phone.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Email", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame, width=40)
entry_email.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Address", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, sticky="nw")
entry_address = tk.Text(frame, width=30, height=4)
entry_address.grid(row=3, column=1, pady=5)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Contact", width=15, bg="green", fg="white", command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Update Contact", width=15, bg="orange", fg="white", command=update_contact).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete Contact", width=15, bg="red", fg="white", command=delete_contact).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="View Contacts", width=15, bg="blue", fg="white", command=view_contacts).grid(row=0, column=3, padx=5)

search_frame = tk.Frame(root, bg="#f0f0f0")
search_frame.pack(pady=10)

tk.Label(search_frame, text="Search", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0)

entry_search = tk.Entry(search_frame, width=30)
entry_search.grid(row=0, column=1, padx=5)

tk.Button(search_frame, text="Search Contact", bg="purple", fg="white", command=search_contact).grid(row=0, column=2)

listbox = tk.Listbox(root, width=70, height=12, font=("Arial", 11))
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", load_selected_contact)

root.mainloop()