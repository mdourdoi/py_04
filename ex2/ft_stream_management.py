import sys


def ft_test_streams() -> None:
    """Tests stdin, stdout and stderr"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    id = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")
    print()
    print(f"[STANDARD] Archive status from {id}: {report}")
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_test_streams()
