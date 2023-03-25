import os

class File:
    def __init__(self, path):
        self.path = path
    
    def write(self, data):
        with open(self.path, 'w') as f:
            f.write(data)
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

class Directory:
    def __init__(self, path):
        self.path = path
    
    def create(self):
        os.makedirs(self.path, exist_ok=True)
    
    def list_files(self):
        files = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for filename in filenames:
                files.append(os.path.join(dirpath, filename))
        return files
    
    def search_file(self, filename):
        found_files = []
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                if f == filename:
                    found_files.append(os.path.join(dirpath, f))
        return found_files

class FileSystem:
    def __init__(self, root):
        self.root = Directory(root)
    
    def create_file(self, path):
        file = File(path)
        file.write('')
    
    def create_directory(self, path):
        directory = Directory(path)
        directory.create()
    
    def list_files(self, path):
        directory = Directory(path)
        return directory.list_files()
    
    def insert_file(self, file_path, data):
        directory_path = os.path.dirname(file_path)
        directory = Directory(directory_path)
        directory.create()
        file = File(file_path)
        file.write(data)
    
    def view_dir(self, path):
        print(f"Listing contents of directory: {path}")
        files = self.list_files(path)
        for file_path in files:
            print(file_path)
    
    def search_file(self, filename, target_directory=None):
        if target_directory is not None:
            directory = Directory(target_directory)
            found_files = directory.search_file(filename)
        else:
            found_files = []
            for dirpath, dirnames, filenames in os.walk(self.root.path):
                for f in filenames:
                    if f == filename:
                        found_files.append(os.path.join(dirpath, f))
        return found_files

if __name__ == '__main__':
    root_path = input("Enter root directory path: ")
    fs = FileSystem(root_path)

    file_path = input("Enter file path: ")
    data = input("Enter data to write to file: ")
    fs.insert_file(file_path, data)

    fs.view_dir(root_path)

    file_to_search = input("Enter file name to search: ")
    target_directory = input("Enter directory to search in (optional): ")
    found_files = fs.search_file(file_to_search, target_directory)
    if len(found_files) == 0:
        print("No files found.")
    else:
        print("Found files:")
        for file_path in found_files:
            print(file_path)
