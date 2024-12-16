import tkinter as tk
import requests

def send_post_request():
    url = url_entry.get()
    data = {
        'param1': param1_entry.get(),
        'param2': param2_entry.get()
    }
    response = requests.post(url, data=data)
    result_text.set(response.text)

# Crear ventana principal
root = tk.Tk()
root.title("Cliente HTTP - Tkinter")

# Etiquetas y campos de entrada
tk.Label(root, text="URL:").grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Param1:").grid(row=1, column=0, padx=5, pady=5)
param1_entry = tk.Entry(root, width=50)
param1_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Param2:").grid(row=2, column=0, padx=5, pady=5)
param2_entry = tk.Entry(root, width=50)
param2_entry.grid(row=2, column=1, padx=5, pady=5)

# Botón de envío
tk.Button(root, text="Enviar POST", command=send_post_request).grid(row=3, column=0, columnspan=2, pady=10)

# Área para mostrar resultados
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, wraplength=400, justify="left").grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Iniciar el bucle principal
root.mainloop()
