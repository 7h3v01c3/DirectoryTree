import os
import fnmatch

def read_gitignore(root_dir):
    ignore_patterns = ['.git', '.gitignore', '.idea']  # Add .git, .gitignore, .idea to default ignore patterns
    gitignore_path = os.path.join(root_dir, '.gitignore')
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    return ignore_patterns

def is_ignored(path, ignore_patterns, root_dir):
    relative_path = os.path.relpath(path, root_dir).replace('\\', '/')
    for pattern in ignore_patterns:
        # Check for direct matches with directories
        if pattern.endswith('/') and fnmatch.fnmatch(relative_path + '/', pattern):
            return True
        # Check for direct matches with files and directories
        if fnmatch.fnmatch(relative_path, pattern):
            return True
        # Check for matches with leading slashes
        if pattern.startswith('/') and fnmatch.fnmatch('/' + relative_path, pattern):
            return True
        # Match base name patterns
        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False

def generate_tree(root_dir, prefix="", ignore_patterns=None):
    if prefix == "":
        print(os.path.basename(root_dir))
        ignore_patterns = read_gitignore(root_dir)
        #print(f"Ignore patterns: {ignore_patterns}")

    items = sorted(os.listdir(root_dir))
    pointers = ['├───'] * (len(items) - 1) + ['└───']

    for pointer, item in zip(pointers, items):
        path = os.path.join(root_dir, item)
        if is_ignored(path, ignore_patterns, root_dir):
            #print(f"Ignoring {path}")
            continue
        print(prefix + pointer + item)
        if os.path.isdir(path):
            extend = '│   ' if pointer == '├───' else '    '
            generate_tree(path, prefix + extend, ignore_patterns)

def main():
    root_dir = input("Enter the directory path: ").strip()
    if os.path.isdir(root_dir):
        generate_tree(root_dir)
    else:
        print("The provided path is not a directory.")

if __name__ == "__main__":
    main()
