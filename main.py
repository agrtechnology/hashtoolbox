import hashlib
import tkinter as tk

class HashResult(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text="MD5").grid(row=0, column=0)
        tk.Label(self, text="SHA1").grid(row=1, column=0)
        tk.Label(self, text="SHA256").grid(row=2, column=0)

        self.hash_results = (tk.Entry(self), tk.Entry(self), tk.Entry(self))
        for i in range(len(self.hash_results)):
            self.hash_results[i].grid(row=i, column=1)

class FileSelector(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.select_file_btn = tk.Button(self, text="Select File", command=parent._create_hashes)
        self.select_file_lbl = tk.Label(self, text="No File Selected")
        self.select_file_btn.grid(row=0, column=0)
        self.select_file_lbl.grid(row=0, column=1)

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("HashToolBox v1.0")
        
        self.filename = None

        self.file_selector = FileSelector(self)
        self.file_selector.grid(row=0, column=0, sticky=tk.W)
        
        self.hashes = HashResult(self)
        self.hashes.grid(row=1, column=0, rowspan=2)

        self.bind("<Configure>", self._triggered)

    def _triggered(self, event):
        print(event)

    def _create_hashes(self):
        self._get_file()
        self._generate_hashes()

    def _get_file(self):
        self.filename = tk.filedialog.askopenfile().name
        self.file_selector.select_file_lbl.config(text=self.filename)

    def _generate_hashes(self):
        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        with open(self.filename, "rb") as f:
            buf = f.read()
            md5.update(buf)
            sha1.update(buf)
            sha256.update(buf)

        hashes = (md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest())
        for i in range(len(hashes)):
            self.hashes.hash_results[i].delete(0, tk.END)
            self.hashes.hash_results[i].insert(0, hashes[i])

if __name__ == "__main__":
    root = tk.Tk()
    App(root).pack()
    root.mainloop()
