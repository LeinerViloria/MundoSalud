import TKinterManager as Tk_Manager
import path_manager as pm
import tkinter as tk

ventana_principal = Tk_Manager.getMainWindow()
ventana_principal.configure(background="light blue")
ventana_principal.attributes("-alpha", 1)
ventana_principal.title("MUNDO-SALUD")
ventana_principal.iconbitmap('img/medical.ico')

Tk_Manager.setFullScreen(ventana_principal)

xlsx_files = pm.getFiles()
main_listbox = Tk_Manager.getListBox(ventana_principal, 20, 0)
for file in xlsx_files:
    main_listbox.insert(tk.END, file)

ventana_principal.mainloop()