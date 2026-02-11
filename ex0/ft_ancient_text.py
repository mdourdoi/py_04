def open_ancient_text() -> None:
    """Open the selected file and read its content"""
    file_name = 'ancient_fragment.txt'
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open('ancient_fragment.txt', 'r')
    except Exception:
        raise Exception("Cannot open 'ancient_fragment.txt'")
    print("Connection established...")
    print()
    content = file.read()
    print("RECOVERED DATA:")
    print(content)
    file.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    try:
        open_ancient_text()
    except Exception as cur_error:
        print(cur_error)
