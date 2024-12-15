from tkinter import *
from tkinter import filedialog, messagebox
import string

# Function to load file
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return
    try:
        with open(file_path, "r") as file:
            text_content.delete(1.0, "end")  # Clear any existing text
            text_content.insert("end", file.read())  # Insert file content into the Text widget
        status_label.config(text=f"File Loaded: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load the file. {e}")
        status_label.config(text="File loading failed.")

# Function to process the text
def process_text():
    text = text_content.get("1.0", "end-1c")  # Get text from the Text widget
    if not text.strip():
        messagebox.showwarning("Warning", "No text to process!")
        return
    
    lines = text.splitlines()
    num_lines = len(lines)
    words = [word.strip(string.punctuation).lower() for line in lines for word in line.split()]
    
    unique_words = set(words)
    num_unique_words = len(unique_words)

    word_frequencies = {}
    for word in unique_words:
        word_frequencies[word] = words.count(word)

    # Modify lines (capitalize first and last character)
    modified_lines = []
    for line in lines:
        line = line.strip()
        if line:
            modified_line = line[0].upper() + line[1:-1] + line[-1].upper() if len(line) > 1 else line.upper()
            modified_lines.append(modified_line)

    # Display results
    result_text = f"Lines: {num_lines}\nUnique Words: {num_unique_words}\nWord Frequencies: {word_frequencies}\nModified Lines:\n"
    result_text += "\n".join(modified_lines)
    result_display.delete(1.0, "end")
    result_display.insert("end", result_text)

# Function to save modified content
def save_file():
    modified_content = result_display.get("1.0", "end-1c")  # Get text from result display widget
    if not modified_content.strip():
        messagebox.showwarning("Warning", "No content to save!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        try:
            with open(save_path, "w") as file:
                file.write(modified_content)
            status_label.config(text=f"File saved: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save the file. {e}")

# GUI setup
root = Tk()
root.title("String Manipulation and Analysis")

# Layout
frame = Frame(root)
frame.pack(pady=10)

load_button = Button(frame, text="Load File", command=load_file)
load_button.grid(row=0, column=0, padx=10)

process_button = Button(frame, text="Process Text", command=process_text)
process_button.grid(row=0, column=1, padx=10)

save_button = Button(frame, text="Save File", command=save_file)
save_button.grid(row=0, column=2, padx=10)

# Text widget to hold content
text_content = Text(root, height=10, width=60)
text_content.pack(pady=10)

# Text display for results
result_display = Text(root, height=15, width=60)
result_display.pack(pady=10)

status_label = Label(root, text="No file loaded", anchor="w")
status_label.pack(fill="x", padx=10)

root.mainloop()

