import socket
import sys

def check_service_status(host, port):
    """Simple TCP port connectivity check for Network+ and Security+ practice."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    try:
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Host {host}:{port} is OPEN")
        else:
            print(f"[-] Host {host}:{port} is CLOSED (Code: {result})")
    except Exception as e:
        print(f"[!] Error checking {host}:{port} -> {str(e)}")
    finally:
        s.close()

if __name__ == "__main__":
    print("[*] CompTIA Network Diagnostics Script initialized.")
    # Check DNS (Port 53) and HTTPS (Port 443) on Google Public DNS
    check_service_status("8.8.8.8", 53)
    check_service_status("8.8.8.8", 443)
