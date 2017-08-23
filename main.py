import tkinter.filedialog
import tkinter as tk
import hashlib

class FileSelector(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.select_file_btn = tk.Button(self, text="Select File", command=parent._generate_hashes)
        self.select_file_lbl = tk.Label(self, text="No File Selected")
        self.select_file_btn.grid(row=0, column=0)
        self.select_file_lbl.grid(row=0, column=1)

class HashResult(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.hash_results = []

        for i in range(len(parent.hash_functions)):
            tk.Label(self, text=parent.hash_functions[i]).grid(row=i, column=0)
            self.hash_results.append(tk.Entry(self))
            self.hash_results[i].grid(row=i, column=1)

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("HashToolBox v1.1")

        self.hash_functions = (
            "MD5",
            "SHA1",
            "SHA256"
            )

        self.file_selector = FileSelector(self)
        self.file_selector.grid(row=0, column=0, sticky=tk.W)
        
        self.hashes = HashResult(self)
        self.hashes.grid(row=1, column=0, rowspan=2)

    def _generate_hashes(self):
        file = tk.filedialog.askopenfile()
        if file:
            filename = file.name
            self.file_selector.select_file_lbl.config(text=filename)
            
            with open(filename, "rb") as f:
                buf = f.read()

            for i in range(len(self.hash_functions)):
                hasher = hashlib.new(self.hash_functions[i])
                hasher.update(buf)
                hash_result = hasher.hexdigest()
                
                self.hashes.hash_results[i].delete(0, tk.END)
                self.hashes.hash_results[i].insert(0, hash_result)

if __name__ == "__main__":
    root = tk.Tk()
    App(root).grid()
    root.mainloop()
