def open_ancient_text() -> None:
    """Open the selected file and read its content"""
    try:
        file_name = 'ancient_fragment.txt'
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()
        print(f"Accessing Storage Vault: {file_name}")
        file = open('ancient_fragment.txt', 'r')
        print("Connection established...")
        print()
        for line in file:
            print(line, end="")
        file.close()
        print()
        print()
        print("Data recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("The file 'ancient_fragment.txt' does not exists, aborting...")


if __name__ == "__main__":
    open_ancient_text()
