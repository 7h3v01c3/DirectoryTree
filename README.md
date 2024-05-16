# Directory Tree Generator

This script generates a visual representation of a directory tree, excluding files and directories specified in a `.gitignore` file and some default patterns such as `.git`, `.gitignore`, and `.idea`.

I use PyCharm and some of the directories are specifically excluded for Pycharm users.

## Features

- Reads `.gitignore` file to exclude specified files and directories.
- Excludes common patterns such as `.git`, `.gitignore`, and `.idea` by default.
- Recursively generates a tree structure for the directory.
- Provides a clean and visual output in the console.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/directory-tree-generator.git
   cd directory-tree-generator
   ```

2. **(Optional) Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **(Optional) Install dependencies:**

   If you decide to extend the script or use additional features, you might need to install some dependencies. For now, no additional dependencies are required.

## Usage

1. **Run the script:**

   ```bash
   python main.py
   ```

2. **Enter the directory path when prompted:**

   ```plaintext
   Enter the directory path: /path/to/your/directory
   ```

   The script will print the directory tree structure, excluding files and directories specified in the `.gitignore` file and the default patterns.

## Example Output

```
MyProject
├───file1.py
├───file2.py
├───requirements.txt
├───static
│   ├───background
│   │   ├───image1.jpg
│   │   └───image2.webp
│   ├───images
│   │   ├───logo1.jpg
│   │   └───logo2.webp
│   └───style.css
├───templates
│   ├───accounts
│   │   └───account_settings.html
│   ├───base.html
│   ├───index.html
│   ├───login.html
│   └───signup.html
└───README.md
```

## Note

If you want to see which files and directories are being ignored during the execution of the script, you can uncomment the print statements in the script:

```python
# print(f"Ignoring {path}")
```

## Contributing

1. **Fork the repository.**
2. **Create a new branch.**
3. **Make your changes.**
4. **Commit and push your changes.**
5. **Create a pull request.**

## License

This project is licensed under the MIT License.

## Acknowledgments

- Inspired by the need to visualize directory structures while excluding certain files and directories based on `.gitignore` patterns.
