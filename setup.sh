#!/bin/zsh

# Define the URL and the target directory
URL="https://github.com/krzys-h/UndertaleModTool/releases/download/bleeding-edge/CLI-ubuntu-latest-Release-isBundled-true.zip"
TARGET_DIR="./tools"
ZIP_FILE="${TARGET_DIR}/CLI-ubuntu-latest-Release-isBundled-true.zip"

# Create the target directory if it doesn't exist
if [[ ! -d $TARGET_DIR ]]; then
    echo "Creating directory: $TARGET_DIR"
    mkdir -p $TARGET_DIR
fi

# Download the file to the target directory
echo "Downloading file to $TARGET_DIR..."
curl -L $URL -o "$ZIP_FILE"

# Function to extract the zip file using available tool
extract_zip() {
    if command -v unzip &> /dev/null; then
        echo "Extracting with unzip..."
        unzip -o "$ZIP_FILE" -d "$TARGET_DIR/umt_cli"
    elif command -v 7z &> /dev/null; then
        echo "Extracting with 7z..."
        7z x "$ZIP_FILE" -o"$TARGET_DIR/umt_cli"
    else
        echo "Error: 'unzip' or '7z' is required to extract the ZIP file."
        echo "Please install one of them:"
        echo "  - Debian/Ubuntu: sudo apt-get install unzip"
        echo "  - Fedora: sudo dnf install unzip"
        echo "  - Arch Linux: sudo pacman -S unzip"
        echo "  - MacOS: brew install unzip"
        echo "  - For 7z, replace 'unzip' with 'p7zip' in the above commands."
        exit 1
    fi
}

# Extract the zip file
extract_zip

echo "Download and extraction complete."
