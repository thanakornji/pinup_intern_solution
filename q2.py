import sys

class Node:
    def __init__(self, name, is_dir=False, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        self.children = {}

class FileSystem:
    def __init__(self):
        self.root = Node("/", is_dir=True)
        self.current = self.root

    def cwd(self):
        if self.current == self.root:
            print("/")
            return
        
        path_parts = []
        curr = self.current
        while curr != self.root:
            path_parts.append(curr.name)
            curr = curr.parent
        print("/" + "/".join(reversed(path_parts)))

    def cd(self, path):
        if path == "/":
            self.current = self.root
            return
            
        parts = path.split('/')
        target = self.current
        
        if path.startswith('/'):
            target = self.root
            parts = parts[1:]
            
        for part in parts:
            if part == '' or part == '.':
                continue
            if part == '..':
                if target == self.root:
                    print("currently at root")
                    return
                target = target.parent
            else:
                if part not in target.children:
                    print(f"{part} not found.")
                    return
                if not target.children[part].is_dir:
                    print(f"{path} is not a directory.")
                    return
                target = target.children[part]
        self.current = target

    def ls(self):
        if self.current.children:
            names = sorted(self.current.children.keys())
            print(" ".join(names))

    def mkdir(self, dir_name):
        if dir_name in self.current.children:
            print(f"{dir_name} already exists")
        else:
            self.current.children[dir_name] = Node(dir_name, is_dir=True, parent=self.current)

    def touch(self, file_name):
        if file_name in self.current.children:
            print(f"{file_name} already exists")
        else:
            self.current.children[file_name] = Node(file_name, is_dir=False, parent=self.current)

def main():
    fs = FileSystem()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(' ', 1)
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else None
        
        if cmd == "cwd":
            fs.cwd()
        elif cmd == "cd" and arg:
            fs.cd(arg)
        elif cmd == "ls":
            fs.ls()
        elif cmd == "mkdir" and arg:
            fs.mkdir(arg)
        elif cmd == "touch" and arg:
            fs.touch(arg)
        elif cmd == "exit":
            break

if __name__ == "__main__":
    main()