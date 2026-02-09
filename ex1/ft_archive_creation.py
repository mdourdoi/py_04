def create_archive() -> None:
    """Creates the archive"""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("Initializing new storage unit: new_discovery.txt")
    try:
        file = open("new_discovery.txt", mode='w')
    except Exception:
        raise Exception("Cannot create or modify 'new_discovery.txt'")
    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")
    str1 = "[ENTRY 001] New quantum algorithm discovered"
    str2 = "[ENTRY 002] Efficiency increased by 347%"
    str3 = "[ENTRY 003] Archived by Data Archivist trainee"
    print(str1)
    file.write(str1)
    file.write("\n")
    print(str2)
    file.write(str2)
    file.write("\n")
    print(str3)
    file.write(str3)
    file.write("\n")
    print()
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    try:
        create_archive()
    except Exception as cur_error:
        print(cur_error)
