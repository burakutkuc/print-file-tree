import os

def print_directory_tree(path: str, indent: str = ""):
    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        print(indent + "└── [Permission Denied]")
        return

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        print(indent + connector + entry)
        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            print_directory_tree(full_path, indent + extension)

def main():
    folder_path = input("Enter the folder path: ").strip()
    
    if not os.path.exists(folder_path):
        print("The specified path does not exist.")
        return
    if not os.path.isdir(folder_path):
        print("The specified path is not a directory.")
        return

    print(folder_path)
    print_directory_tree(folder_path)

if __name__ == "__main__":
    main()
