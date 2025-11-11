# Viper Port Scanner
Fork of [Port Scanner](https://github.com/vienhoang/port-scanner) with more features.
It scans ports, saves the results in text files, and plays background music while you wait.

## Preview
![Alt text](preview.jpg?raw=true "Viper Port Scanner")

![Alt text](preview2.jpg?raw=true "Viper Port Scanner")


-----



## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

* **Python 3.8** or newer.
* **Git** (for cloning the repository).
* **pip** (Python's package installer, usually included with Python).

### Installation

Follow these steps to set up your local environment and install the necessary packages.

1.  **Clone the Repository**

    Open your terminal or command prompt and clone this repository to your local machine:

    ```bash
    git clone https://github.com/vienhoang/viper-port-scanner.git
    cd viper-port-scanner
    ```

    > **Note:** If you downloaded the project as a ZIP file, simply unzip it and navigate to the directory in your terminal.

2.  **Create and Activate a Virtual Environment**

    It is highly recommended to use a virtual environment to keep dependencies isolated from your system's Python setup.

    * **On macOS / Linux:**
        ```bash
        # Create a virtual environment named '.venv'
        python3 -m venv .venv

        # Activate the virtual environment
        source .venv/bin/activate
        ```

    * **On Windows (PowerShell):**
        ```bash
        # Create a virtual environment named '.venv'
        python -m venv .venv

        # Activate the virtual environment
        .\.venv\Scripts\Activate.ps1
        ```

    Your terminal prompt should now change to show `(venv)` at the beginning, indicating the virtual environment is active.

3.  **Install Required Packages**

    This project's dependencies are listed in the `requirements.txt` file. Use `pip` to install all of them at once:

    ```bash
    pip install -r requirements.txt
    ```

    This will automatically install `ascii-magic`, `colorama`, `pillow`, `pygame`, and `tqdm` at the correct versions.

## 🏃‍♀️ How to Run the Viper Port Scanner

With the virtual environment still active and all packages installed, you can now run the main script.<br>
python viper_port_scanner.py
1. Run the script.
2. Enter an IP-adress or URL, or press Enter for default value.
3. Enter the starting port in the range, or press Enter for default value.
4. Enter the last port in the range, or press Enter for default value.
5. Enter timeout in seconds between each scanned port.
6. Enjoy the music while the ports are being scanned.

or run the script with CLI arguments.

python viper_port_scanner.py scanme.nmap.org 1 25 1<br>
Scans scanme.nmap.org port 1 to 25 with a timeout of 1s.

* **On macOS / Linux:**
    ```bash
    python3 viper_port_scanner.py
    or
    python3 viper_port_scanner.py scanme.nmap.org 1 25 1
    ```

* **On Windows:**
    ```bash
    python viper_port_scanner.py
    or
    python viper_port_scanner.py scanme.nmap.org 1 25 1
    ```

## 🛑 Deactivating the Environment

When you are finished using the script, you can exit the virtual environment by simply typing:

```bash
deactivate
````

## Extra Features
- Giant viper banner in ascii
- Background music when ports are being scanned
- Save files based on unix timestamp
- Default inputs when pressing Enter

## Assets
- viper.jpg - Made with Copilot
- nes_bg_track.wav - Made with Sonic Pi and Gemini

## License
You may use, modify, and share this code freely for non-commercial purposes.  
Commercial use, resale, or redistribution is not allowed without written permission.

## Author
Made by Vien Hoang | [Linkedin](https://www.linkedin.com/in/vien-hoang-5077bb96/) | [GitHub](https://github.com/vienhoang)
