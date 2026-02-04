def test_vault() -> None:
    """Securely opens a file and read/write"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    try:
        file = open('classified_data.txt')
        print("Vault connection established with failsafe protocols")
        file.close()
        print()
        with open("classified_data.txt", 'r') as safe_read:
            print("SECURE EXTRACTION:")
            for line in safe_read:
                print(line, end="")
        print()
        print()
        with open("classified_data.txt", 'a') as safe_append:
            print("SECURE PRESERVATION:")
            str_to_add = "[CLASSIFIED] New security protocols archived"
            print(str_to_add)
            safe_append.write(str_to_add)
        if safe_append.closed and safe_read.closed:
            print("Vault automatically sealed upon completion")
            print()
            print("All vault operations completed with maximum security.")
        else:
            print("Critical alert : Vaulty is not closed !!!")
    except FileNotFoundError:
        print("File 'classified_data.txt' not found, aborting...")


if __name__ == "__main__":
    test_vault()
