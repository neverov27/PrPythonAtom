import os.path
import pickle


class FileWriter:

    def __init__(self, path):
        if self._check_path(path):
            self._path = path
            self.file = None

    def _check_path(self, path):
        return os.path.exists(os.path.dirname(path))

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        if self._check_path(path):
            self._path = path

    @path.deleter
    def path(self):
        del self._path
        
    def __enter__(self):
        self.file = open(self._path, 'a')
        return self
            
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.file = None

    def print_file(self):
        with open(self._path) as f:
            return f.read()

    def write(self, text):
        self.file.write(text)

    def save_yourself(self, file_name):
        with open(file_name, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, "rb") as f:
            return pickle.load(f)
