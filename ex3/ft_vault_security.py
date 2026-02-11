def vault_security() -> None:
    """Securely opens a file and read/write"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()
    try:
        with open("classified_data.txt", 'r') as safe_read:
            print("SECURE EXTRACTION:")
            content = safe_read.read()
            print(content)
            print()
    except Exception:
        raise Exception("Cannot open 'classified_data.txt'.")
    try:
        with open("security_protocols.txt", 'w') as safe_write:
            print("SECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archived")
            safe_write.write("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion")
            print()
    except Exception:
        raise Exception("Cannot create or modify 'security_protocols.txt'")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        vault_security()
    except Exception as cur_error:
        print(cur_error)
