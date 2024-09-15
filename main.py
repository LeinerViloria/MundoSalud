import TKinter_Manager as Tk_Manager
import path_manager as pm
import tkinter as tk

def on_listbox_select(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        file = event.widget.get(index)
        file_path = f"{pm.current_directory}/source/{file}"
        Tk_Manager.display_excel_data(ventana_principal, file_path)

ventana_principal = Tk_Manager.getMainWindow()
ventana_principal.configure(background="light blue")
ventana_principal.attributes("-alpha", 1)
ventana_principal.title("MUNDO-SALUD")
ventana_principal.iconbitmap('img/medical.ico')
ventana_principal.minsize(900, 600)

xlsx_files = pm.getFiles()
main_listbox = Tk_Manager.getListBox(ventana_principal, frame_row=8, frame_column=1)
for file in xlsx_files:
    main_listbox.insert(tk.END, file)

main_listbox.bind("<<ListboxSelect>>", on_listbox_select)

ventana_principal.mainloop()
