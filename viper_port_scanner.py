#!/usr/bin/env python3
"""
Network Scanner Project With Extra Features
Student: Vien
Date: 251104
"""
# Importing modules
import socket
import sys
from tqdm import tqdm
from colorama import init, Fore
from ascii_magic import AsciiArt

# Init colors
init()
GREEN = Fore.GREEN

# Global list to save ports
open_ports = []

# Setup ascii banner image
def ascii_banner():
    print(GREEN + "*" * 120)
    my_art = AsciiArt.from_image('viper.jpg')
    my_output = my_art.to_ascii()
    print(my_output)
    print("Viper Port Scanner - Scan Hard, Scan Fast, No Mercy!!!")
        
# Set range ports, including the max port
def start_multiscan(target, start_port, max_port, timeout=1.0):

    # Calculation for progress bar
    total_ports = max_port - start_port + 1
    with tqdm(total=total_ports, desc=f"{GREEN}Scanning {target} from [{start_port}] to [{max_port}]", unit="port") as progress_bar:

        # Set range ports, including the max port
        for port in range(start_port, max_port + 1):
            #AF_INET = IPv4, SOCK_STREAM = constant, create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Try to connect port with time out
            try:
                s.settimeout(timeout)
                # Returns to 0 if a port is open
                result = s.connect_ex((target, port))
                # If a port is open, add the open port to the open_ports list
                if result == 0:
                    # Try to identify the port service
                    try:
                        # For HTTP-ports
                        if port in (80, 8080):
                            # Sends an HTTP HEAD request to the connected server, asking for only HTTP headers without a body
                            s.sendall(b"HEAD / HTTP/1.0\r\nHost: %b\r\n\r\n" % target.encode())
                        # Read max 1024 bytes from the opened socket
                        data = s.recv(1024)
                        # Convert the data and do split and strip empy spaces, and get the first part
                        banner = data.decode(errors="ignore").splitlines()[0].strip()
                        
                        # If the banner exists
                        if banner:
                            # Add open port to the open_ports list
                            open_ports.append(f"Port {port} : Banner {banner}")
                            progress_bar.write(f"\n{GREEN}Banner for {target}:{port} -> {banner}")
                        else:
                            open_ports.append(f"Port {port} : No banner received")
                            progress_bar.write(f"\n{GREEN}No banner received for {target}:{port}")

                    # Socket timed out error
                    except socket.timeout:
                        open_ports.append(f"Port {port} : No banner (timeout)")
                        progress_bar.write(f"\n{GREEN}No banner (timeout) for {target}:{port}")
                    # Catch other errors
                    except Exception as e:
                        open_ports.append(f"Port {port} : Error reading banner {e}")
                        progress_bar.write(f"\n{GREEN}Error reading banner for {target}:{port}: {e}")
            # DNS lookup failed error
            except socket.gaierror as e:
                progress_bar.write(f"\n{GREEN}Hostname could not be resolved. {e}")
                return open_ports
            # Socket error
            except socket.error as e:
                progress_bar.write(f"\n{GREEN}Could not connect to server. {e}")
                return open_ports
            # Close socket
            finally:
                s.close()
                progress_bar.update(1)
                
        # Save port to file
        save_ports_to_file(target, open_ports)

# Save the ports to file, default file name port_results.txt
def save_ports_to_file(target, port_list, file_name="port_results.txt"):

    # Saves only open ports
    if port_list:
        print(f"{GREEN}\nSave ports to file: ") 
        # Print open port(s)
        for port in port_list:
            print(port)    
        
        # Try to save to file
        try:
            with open(file_name, "w") as f:
                f.write(f"Open ports for target IP {target}\n")
                # Separate each line with \n at the end
                for port in port_list:
                    f.write(f"{port}\n")
                # Print out the result of the saved file 
                print(f"{GREEN}The results have been saved to the file: {file_name}")

        # File not found error
        except FileNotFoundError:
            print("File not found.")
        # Writing to file errors
        except IOError:
            print("An I/O error occurred.")
        # Other errors
        except:
            print("Something went wrong...")
        # Close file
        f.close()
    else:
        print("\nNo ports are open.")

# Run the program
if __name__ == "__main__":
    
    ascii_banner()
        
    # Set default timeout to 1s
    timeout = 1

    # Optional CLI arguments, i.e multi_port_scanner.py scanme.nmap.org 1 30 2
    # len(sys.argv) checks are optional CLI arguments.
    # Assume an argument format of <domain name or IP>, <start_port>, <end_port>, <timeout>
    if len(sys.argv) == 5:
        target = socket.gethostbyname(sys.argv[1])
        start_port = int(sys.argv[2])
        max_port = int(sys.argv[3])
        timeout = float(sys.argv[4])

    # Optional CLI arguments, i.e multi_port_scanner.py scanme.nmap.org 1 30
    # len(sys.argv) checks are optional CLI arguments.
    # Assume an argument format of <domain name or IP>, <start_port>, <end_port>.
    elif len(sys.argv) == 4:
        target = socket.gethostbyname(sys.argv[1])
        start_port = int(sys.argv[2])
        max_port = int(sys.argv[3])   
        
    # I.e multi_port_scanner.py scanme.nmap.org
    # With only 2 arguments, it will ask the user to input <start_port> and <end_port>.
    elif len(sys.argv) == 2:
    # Translate hostname to IPv4. It will also accept just the IP.
        target = socket.gethostbyname(sys.argv[1])
        start_port = int(input('starting port: '))
        max_port = int(input('ending port: '))

    # Else inputs from console
    # As last resort, it will ask the user to input IP or domain.
    else: # It will convert <domain name> to IPv4, before asking for <start_port> and <end_port>.
        domain_name = str(input(GREEN + 'Enter target IP or domain: '))
        # Spit url and get the domain name
        if "http" in domain_name:
            target = domain_name.split("://")
            domain_name = target[1]

        target = socket.gethostbyname(domain_name)
        start_port = int(input(GREEN + 'Starting port: '))
        max_port = int(input(GREEN + 'Ending port: '))
        timeout = float(input(GREEN + "Set timout for each port: "))
        
    # Scan the give url with start and end ports
    start_multiscan(target, start_port, max_port, timeout)