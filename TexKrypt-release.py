import random
import re
import string
import tkinter as tk
from tkinter import messagebox, scrolledtext

print("**********_TexKrypt_**********")


def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def key_creation(key):
    key_characters = string.ascii_letters + string.punctuation
    random_chars = [random.choice(key_characters) for _ in range(len(key) - 1)]
    key_with_chars = ''.join(str(key[i]) + random_chars[i] for i in range(len(key) - 1)) + str(key[-1])
    return key_with_chars


def encrypt(plain_text):
    replace_num_list = []
    key = []

    plain_text_length = int(len(plain_text) * random.uniform(10, 50))
    generated_string = [*generate_random_string(plain_text_length)]
    plain_text_split = [*plain_text]

    for z in range(plain_text_length):
        replace_num_list.append(z)

    for y in plain_text_split:
        replace_index = random.choice(replace_num_list)
        generated_string[replace_index] = y
        replace_num_list.remove(replace_index)
        key.append(replace_index)

    cipher_text = ''.join(generated_string)
    return cipher_text, key_creation(key)


def decrypt(encrypted_text, encryption_key):
    numbers = re.findall(r'\d+', encryption_key)
    split_key = [int(num) for num in numbers]

    decrypted_text = ''
    for i in split_key:
        try:
            decrypted_text += encrypted_text[i]
        except IndexError:
            return "Incorrect Key or Text!"

    return decrypted_text


def on_encrypt():
    plain_text = plain_text_entry.get("1.0", tk.END).strip()
    if plain_text:
        cipher_text, key = encrypt(plain_text)
        encrypted_text_entry.delete("1.0", tk.END)
        encrypted_text_entry.insert(tk.END, cipher_text)
        encryption_key_entry.delete(0, tk.END)
        encryption_key_entry.insert(tk.END, key)
    else:
        messagebox.showwarning("Invalid Input", "Please enter text to encrypt.")


def on_decrypt():
    encrypted_text = encrypted_text_entry.get("1.0", tk.END).strip()
    encryption_key = encryption_key_entry.get().strip()
    if encrypted_text and encryption_key:
        decrypted_text = decrypt(encrypted_text, encryption_key)
        plain_text_entry.delete("1.0", tk.END)
        plain_text_entry.insert(tk.END, decrypted_text)
    else:
        messagebox.showwarning("Invalid Input", "Please enter encrypted text and encryption key to decrypt.")


root = tk.Tk()
root.title("TexKrypt")
root['bg'] = 'black'

frame = tk.Frame(root, padx=10, pady=10, bg='black')
frame.pack(padx=10, pady=10)

plain_text_label = tk.Label(frame, text="Enter Text: ", bg='black', fg='white')
plain_text_label.grid(row=0, column=0, sticky="w")

plain_text_entry = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=10, bg='black', fg='white')
plain_text_entry.grid(row=1, column=0, columnspan=2, pady=5)

encrypt_button = tk.Button(frame, text="Encrypt", command=on_encrypt, bg='black', fg='white')
encrypt_button.grid(row=2, column=0, pady=5)

decrypt_button = tk.Button(frame, text="Decrypt", command=on_decrypt, bg='black', fg='white')
decrypt_button.grid(row=2, column=1, pady=5)

encrypted_text_label = tk.Label(frame, text="Encrypted Text: ", bg='black', fg='white')
encrypted_text_label.grid(row=3, column=0, sticky="w")

encrypted_text_entry = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=10, bg='black', fg='white')
encrypted_text_entry.grid(row=4, column=0, columnspan=2, pady=5)

encryption_key_label = tk.Label(frame, text="Encryption Key: ", bg='black', fg='white')
encryption_key_label.grid(row=5, column=0, sticky="w")

encryption_key_entry = tk.Entry(frame, width=52, bg='black', fg='white')
encryption_key_entry.grid(row=6, column=0, columnspan=2, pady=5)

exit_button = tk.Button(frame, text="Exit", command=root.quit, bg='black', fg='white')
exit_button.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
