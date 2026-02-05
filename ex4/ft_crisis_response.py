def safe_access(file: str) -> None:
    """Handles the safe acces to a file"""
    try:
        with open(file, 'r') as safe_access:
            print(f"ROUTINE ACCESS: Attempting access to \'{file}\''...")
            content = safe_access.read()
            print(f"RESPONSE: Archive recovered - ``{content}\'\'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to \'{file}\'...")
        message = "Archive not found in storage matrix"
        status = "Crisis handled, system stable"
        raise FileNotFoundError(message, status)
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to {file}...")
        message = "Security protocols deny access"
        status = "Crisis handled, security maintained"
        raise PermissionError(message, status)


def safe_access_handler(file: str) -> None:
    """Handles errors raised by the safe access"""
    try:
        safe_access(file)
    except (FileNotFoundError, PermissionError) as cur_error:
        print(f"RESPONSE: {cur_error.args[0]}")
        print(f"STATUS: {cur_error.args[1]}")


def crisis_response() -> None:
    """Tests several files and handles errors"""
    print("===CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    safe_access_handler("lost_archive.txt")
    print()
    safe_access_handler("classified_data.txt")
    print()
    safe_access_handler("standard_archive.txt")


if __name__ == "__main__":
    crisis_response()
