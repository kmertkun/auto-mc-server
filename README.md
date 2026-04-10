# auto-mc-server Installer 🚀
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

A modern, fast, and fully automated cross-platform Minecraft Server Installer. Featuring a beautiful Neo-Cyberpunk styled Dashboard for Windows, and a sleek lightweight Terminal Wizard for Linux servers.

## Features ✨

* **Cross-Platform**: Run the rich GUI on Windows, or use the interactive command-line interface on Linux.
* **Auto-Language**: Automatically detects your OS language (English & Turkish) and provides an in-app language switcher for the UI without freezing.
* **Smart RAM Allocation**: Automatically calculates your system's hardware RAM and allocates the perfect amount for optimal server performance.
* **Integrated Plugin Store (Modrinth)**: Search, find, and queue plugins dynamically through the in-app Modrinth database without needing to switch tabs or download manually.
* **Firewall Automation**: Opens the default Minecraft port (`25565`) automatically via Windows Defender configuration or `UFW` in Linux.
* **Widescreen Neo Dashboard**: Features an ultra-modern wide dashboard to monitor your targets efficiently without feeling cramped.

2. **Install Requirements:**
   Make sure you have Python installed. Then, install the mandatory UI library for the Windows Dashboard:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python main.py
   ```
   *(If you are running this on a Linux server/VPS, the terminal setup wizard will start automatically instead of the GUI).*

## Supported Server Softwares 🧱
- **Vanilla** (Pure, no plugins)
- **Paper** (Highly Optimized, Plugin support)
- **Purpur** (Max optimization, highly customizable)
*(Versions are dynamically fetched from the official APIs).*

## License 📄
This project is open-sourced software licensed under the [MIT license](LICENSE).
