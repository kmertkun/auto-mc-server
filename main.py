import os
import threading
import json
import urllib.request
import urllib.error
import urllib.parse
import subprocess
import platform
import sys
import locale

SYSTEM_OS = platform.system()

if SYSTEM_OS == "Windows":
    import ctypes
    import webbrowser
    import tkinter as tk
    from tkinter import messagebox, filedialog
    try:
        import customtkinter as ctk
    except ImportError:
        pass

# ==========================================
# ÇOKLU DİL (LOCALIZATION) SÖZLÜĞÜ
# ==========================================
LANG_DICT = {
    "tr": {
        "cli_title": "auto-mc-server - LINUX TERMINAL MODE",
        "cli_fetching": "Sunucu veritabanı ile bağlantı kuruluyor (Sürümler Çekiliyor)...",
        "sw_choice": "Yazılım Seçimi",
        "vanilla_desc": "Vanilla (Sade/Eklentisiz)",
        "paper_desc": "Paper (Hızlı/Plugin Destekli)",
        "purpur_desc": "Purpur (Detaylı Optimizasyon/Plugin Destekli)",
        "choice_prompt": "Seçiminiz (1/2/3): ",
        "cur_versions": "Mevcut Sürümler",
        "ver_prompt": "Lütfen kurmak istediğiniz sürümün Numarasını girin: ",
        "invalid_sel": "[!] Geçersiz seçim. Varsayılan olarak en günceli seçildi.",
        "ask_crack": "Crack/Korsan oyuncu girişine izin verilsin mi? (E/H) (E Önerilir): ",
        "ask_port": "Güvenlik Duvarı Portu (25565) Linux ufw üzerinden otomatik açılsın mı? (E/H): ",
        "ask_plugin": "Kuruluma internetten eklenti/plugin bulup dahil etmek ister misiniz? (E/H): ",
        "plugin_name": "Eklenti İsmi (Örn: authme, worldedit): ",
        "searching": "Modrinth'te aranıyor...",
        "no_match": "eşleşme bulunamadı.",
        "found_res": "Bulunan Sonuçlar:",
        "add_num": "Eklemek istediğiniz eklentinin numarasını girin (İptal için 0): ",
        "added": "listeye eklendi!",
        "ask_another": "Başka bir eklenti daha aramak ister misiniz? (E/H): ",
        "start_install": "--- Kurulum Başlıyor ---",
        "downloading": "İndiriliyor",
        "jar_downloaded": "Ana jar indirildi.",
        "err_not_found": "HATA: Dosya resmi sunucularda bulunamadı.",
        "downloading_plugins": "Eklentiler indiriliyor...",
        "searching_p": "aranıyor...",
        "p_downloaded": "indirildi.",
        "p_not_found": "Uygun sürümü bulunamadı.",
        "p_err": "Hata",
        "config_files": "Ayar dosyaları (server.properties, vb.) yapılandırılıyor...",
        "install_complete": "Kurulum TAMAMLANDI!\nDizin: {0}\nÇalıştırmak için: cd Server && ./start.sh",
        "gui_title": "auto-mc-server Panel",
        "title": "AUTO-MC-SERVER",
        "subtitle": "Hızlı, Güvenli ve Tam Otomatik Kurulum",
        "step1": "1. Sunucu Yazılım Türü",
        "step2": "2. Hedef Sürüm",
        "step3": "3. Sunucu Ayarları",
        "step4": "4. Otomatik Eklenti Mağazası (Arama)",
        "step5": "5. Kurulum Dizini",
        "loading": "Yükleniyor...",
        "crack_allow": "Crack/Korsan Girişi",
        "port_allow": "Güvenlik Duvarında Port (25565) Aç",
        "search_ph": "Eklenti arat (Örn: authme)...",
        "find": "Bul",
        "to_install": "Kurulacaklar Listesi:",
        "no_plugin_sel": "Henüz eklenti seçilmedi.",
        "browse": "Gözat",
        "sys_info": "Sistem analiz edildi. Sunucuya {0} GB RAM atanacak.",
        "btn_install": "İNDİR VE KUR",
        "status_startup": "Sistem başlatılıyor...",
        "status_conn": "Bağlantı kuruluyor...",
        "status_ready": "Sistem Hazır. Bir versiyon seçin ve başlayın.",
        "warn_vanilla": "Vanilla sunucular eklenti (plugin) desteklemez!",
        "search_fail": "Bağlantı hatası veya bulunamadı.",
        "btn_add": "Ekle",
        "btn_added": "Eklendi",
        "btn_downloading": "İNDİRİLİYOR...",
        "status_main_dl": "Ana Dosya İndiriliyor ({0})...",
        "status_p_dl": "Eklenti indiriliyor: {0}",
        "status_cfg": "Ayar dosyaları yazılıyor...",
        "status_success": "İşlem Başarılı! Sunucunuz oynanmaya hazır.",
        "msg_done": "kurulumu tamamlandı.\nDizin: {0}",
        "msg_err": "Kurulum başarısız oldu:\n{0}",
        "btn_y": "E",
        "warning": "Uyarı",
        "err_title": "Hata",
        "done_title": "Tamamlandı"
    },
    "en": {
        "cli_title": "auto-mc-server - LINUX TERMINAL MODE",
        "cli_fetching": "Connecting to server databases (Fetching Versions)...",
        "sw_choice": "Software Selection",
        "vanilla_desc": "Vanilla (Pure/No Plugins)",
        "paper_desc": "Paper (Fast/Plugin Support)",
        "purpur_desc": "Purpur (Optimized/Plugin Support)",
        "choice_prompt": "Your choice (1/2/3): ",
        "cur_versions": "Available Versions",
        "ver_prompt": "Please enter the number of the version you want to install: ",
        "invalid_sel": "[!] Invalid selection. Defaulted to the latest version.",
        "ask_crack": "Allow Cracked/Offline players to join? (Y/N) (Y Recommended): ",
        "ask_port": "Automatically open Firewall Port 25565 via Linux ufw? (Y/N): ",
        "ask_plugin": "Do you want to search and include plugins in the installation? (Y/N): ",
        "plugin_name": "Plugin Name (Ex: authme, worldedit): ",
        "searching": "Searching on Modrinth...",
        "no_match": "no matches found.",
        "found_res": "Found Results:",
        "add_num": "Enter the number of the plugin to add (0 to cancel): ",
        "added": "added to the list!",
        "ask_another": "Do you want to search for another plugin? (Y/N): ",
        "start_install": "--- Installation Starting ---",
        "downloading": "Downloading",
        "jar_downloaded": "Main jar downloaded.",
        "err_not_found": "ERROR: File not found on official servers.",
        "downloading_plugins": "Downloading plugins...",
        "searching_p": "searching...",
        "p_downloaded": "downloaded.",
        "p_not_found": "Compatible version not found.",
        "p_err": "Error",
        "config_files": "Configuring settings files...",
        "install_complete": "Installation COMPLETE!\nDirectory: {0}\nTo run: cd Server && ./start.sh",
        "gui_title": "auto-mc-server Panel",
        "title": "AUTO-MC-SERVER",
        "subtitle": "Fast, Secure, and Fully Automated Setup",
        "step1": "1. Server Software Type",
        "step2": "2. Target Version",
        "step3": "3. Server Settings",
        "step4": "4. Auto Plugin Store (Search)",
        "step5": "5. Installation Directory",
        "loading": "Loading...",
        "crack_allow": "Allow Offline Login",
        "port_allow": "Open Port (25565) in Firewall",
        "search_ph": "Search plugin (Ex: authme)...",
        "find": "Find",
        "to_install": "To Install List:",
        "no_plugin_sel": "No plugin selected yet.",
        "browse": "Browse",
        "sys_info": "System analyzed. {0} GB RAM will be allocated.",
        "btn_install": "DOWNLOAD AND INSTALL",
        "status_startup": "System starting...",
        "status_conn": "Connecting...",
        "status_ready": "System Ready. Select a version and start.",
        "warn_vanilla": "Vanilla servers do not support plugins!",
        "search_fail": "Connection error or not found.",
        "btn_add": "Add",
        "btn_added": "Added",
        "btn_downloading": "DOWNLOADING...",
        "status_main_dl": "Downloading Main File ({0})...",
        "status_p_dl": "Downloading plugin: {0}",
        "status_cfg": "Writing config files...",
        "status_success": "Operation Successful! Server is ready.",
        "msg_done": "installation complete.\nDirectory: {0}",
        "msg_err": "Installation failed:\n{0}",
        "btn_y": "Y",
        "warning": "Warning",
        "err_title": "Error",
        "done_title": "Done"
    }
}

# ==========================================
# ÇAPRAZ PLATFORM DESTEKLEYİCİ FONKSİYONLAR
# ==========================================

def get_default_os_language():
    try:
        loc, _ = locale.getdefaultlocale()
        if loc and "tr" in loc.lower():
            return "tr"
        else:
            return "en"
    except Exception:
        return "en"

def get_system_ram_gb():
    if SYSTEM_OS == "Windows":
        try:
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [("dwLength", ctypes.c_uint), ("dwMemoryLoad", ctypes.c_uint), ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong), ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong), ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong), ("sullAvailExtendedVirtual", ctypes.c_ulonglong)]
            stat = MEMORYSTATUSEX()
            stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
            total_ram_gb = int(stat.ullTotalPhys / (1024**3))
        except: total_ram_gb = 4
    else:
        try:
            total_ram_gb = 4
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if 'MemTotal' in line:
                        total_ram_gb = int(int(line.split()[1]) / 1024 / 1024)
                        break
        except: total_ram_gb = 4

    if total_ram_gb <= 2: return 1
    elif total_ram_gb <= 4: return 2
    elif total_ram_gb <= 8: return 4
    elif total_ram_gb <= 16: return 8
    elif total_ram_gb <= 32: return 16
    else: return int(total_ram_gb / 2)

def create_server_properties(directory, is_crack):
    file_path = os.path.join(directory, "server.properties")
    val = "false" if is_crack else "true"
    if os.path.exists(file_path):
        with open(file_path, "r") as f: lines = f.readlines()
        with open(file_path, "w") as f:
            found = False
            for line in lines:
                if line.startswith("online-mode="):
                    f.write(f"online-mode={val}\n")
                    found = True
                else: f.write(line)
            if not found: f.write(f"online-mode={val}\n")
    else:
        with open(file_path, "w") as f: f.write(f"online-mode={val}\n")

def create_eula(directory):
    with open(os.path.join(directory, "eula.txt"), "w") as f: f.write("eula=true\n")

def create_start_script(directory, ram_gb, jar_name):
    if SYSTEM_OS == "Windows":
        with open(os.path.join(directory, "baslat.bat"), "w") as f:
            f.write(f"@echo off\ntitle Minecraft ({jar_name})\necho Sunucu Baslatiliyor...\njava -Xms{ram_gb}G -Xmx{ram_gb}G -XX:+UseG1GC -jar {jar_name} nogui\npause\n")
    else:
        sh_path = os.path.join(directory, "start.sh")
        with open(sh_path, "w") as f:
            f.write(f"#!/bin/bash\necho \"Sunucu Baslatiliyor...\"\njava -Xms{ram_gb}G -Xmx{ram_gb}G -XX:+UseG1GC -jar {jar_name} nogui\n")
        try: os.chmod(sh_path, 0o755)
        except: pass

def open_firewall_ports(is_tr):
    if SYSTEM_OS == "Windows":
        try:
            cmds = 'netsh advfirewall firewall add rule name="Minecraft TCP" dir=in action=allow protocol=TCP localport=25565 & netsh advfirewall firewall add rule name="Minecraft UDP" dir=in action=allow protocol=UDP localport=25565'
            if ctypes.windll.shell32.IsUserAnAdmin(): os.system(cmds)
            else: ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/c {cmds}", None, 0)
        except: pass
    else:
        try:
            os.system("sudo ufw allow 25565/tcp >/dev/null 2>&1")
            os.system("sudo ufw allow 25565/udp >/dev/null 2>&1")
        except: pass

def fetch_api_versions():
    cache = {"Vanilla": [], "Paper": [], "Purpur": []}
    try:
        cache["Paper"] = list(reversed(json.loads(urllib.request.urlopen(urllib.request.Request("https://api.papermc.io/v2/projects/paper", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode()).get("versions", [])))
        cache["Purpur"] = list(reversed(json.loads(urllib.request.urlopen(urllib.request.Request("https://api.purpurmc.org/v2/purpur", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode()).get("versions", [])))
        cache["Vanilla"] = [v.get("id") for v in json.loads(urllib.request.urlopen(urllib.request.Request("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode()).get("versions", []) if v.get("type") == "release"]
    except:
        fb = ["1.21.1", "1.20.4", "1.19.4", "1.18.4", "1.17.1", "1.16.5", "1.12.2", "1.8.8"]
        cache = {"Vanilla": fb, "Paper": fb, "Purpur": fb}
    return cache

def check_and_install_java(is_tr, ui_logger=None):
    try:
        subprocess.run(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    msg = "Java bulunamadı. Otomatik yükleniyor (Yönetici izni isteyebilir)..." if is_tr else "Java not found. Installing automatically (Requires Admin)..."
    if ui_logger: ui_logger(msg)
    else: print(f"\n[!] {msg}")

    if SYSTEM_OS == "Windows":
        try:
            dl_url = "https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.2%2B13/OpenJDK21U-jre_x64_windows_hotspot_21.0.2_13.msi"
            installer = os.path.join(os.environ.get("TEMP", os.getcwd()), "java_installer.msi")
            urllib.request.urlretrieve(dl_url, installer)
            
            import ctypes
            import time
            # 'runas' forces the Windows Admin / UAC prompt
            res = ctypes.windll.shell32.ShellExecuteW(None, "runas", "msiexec.exe", f'/i "{installer}" /passive', None, 1)
            if res <= 32: return False
            time.sleep(15) # Give it time to install
            return True
        except:
            return False
    else:
        try:
            if not ui_logger: print("Sudo yetkisi gerekiyor (Şifre isteyebilir)..." if is_tr else "Sudo required (May ask for password)...")
            subprocess.run("sudo apt-get update && sudo apt-get install -y openjdk-21-jre-headless", shell=True, check=True)
            return True
        except:
            return False

# ==========================================
# LINUX İÇİN TERMINAL TABANLI YAPI
# ==========================================
def run_linux_cli():
    print("Select Language / Dil Seçin:\n[1] English\n[2] Türkçe")
    l_inp = input("> ").strip()
    T = LANG_DICT["en" if l_inp == "1" else "tr"]
    print(f"\n{T['cli_fetching']}")
    versions = fetch_api_versions()
    # Eklentilere boğulmamak adına CLI tarafı aynı kompakt yapıda tutuldu...
    print(f"\n[1] {T['sw_choice']}\n1) {T['vanilla_desc']}\n2) {T['paper_desc']}\n3) {T['purpur_desc']}")
    c = input(T['choice_prompt']).strip()
    s = {"1": "Vanilla", "2": "Paper", "3": "Purpur"}.get(c, "Paper")
    print(f"\n[{s}] {T['cur_versions']}")
    sw_v = versions[s][:20] 
    for i, v in enumerate(sw_v): print(f"{i+1}) {v}")
    try:
        v_idx = int(input(f"\n{T['ver_prompt']}").strip()) - 1
        ver = sw_v[v_idx]
    except:
        ver = sw_v[0]
        print(T['invalid_sel'])

    btn_y = T['btn_y']
    is_c = input(f"\n{T['ask_crack']}").strip().upper() == btn_y
    op = input(f"\n{T['ask_port']}").strip().upper() == btn_y
    p_lst = []
    if s != "Vanilla":
        add_p = input(T['ask_plugin']).strip().upper()
        while add_p == btn_y:
            q = input(f"\n{T['plugin_name']}").strip()
            if q:
                print(T['searching'])
                try:
                    data = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.modrinth.com/v2/search?{urllib.parse.urlencode({'query': q, 'facets': '[[\"project_type:plugin\"]]'})}", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode())
                    hits = data.get("hits", [])
                    if not hits: print(f"'{q}' - {T['no_match']}")
                    else:
                        print(T['found_res'])
                        for idx, h in enumerate(hits[:5]): print(f"{idx+1}) {h['title']}")
                        p_choice = input(T['add_num']).strip()
                        if p_choice.isdigit() and 0 < int(p_choice) <= len(hits):
                            sel = hits[int(p_choice)-1]
                            p_lst.append((sel['project_id'], sel['title']))
                            print(f"[{sel['title']}] {T['added']}")
                except Exception as e: print(f"{T['p_err']}: {e}")
            add_p = input(f"\n{T['ask_another']}").strip().upper()

    print(f"\n{T['start_install']}")
    if not check_and_install_java(T == LANG_DICT["tr"]):
        print(f"\n{T['p_err']}: Java kurulumu başarisiz. Lutfen manuel kurun." if T == LANG_DICT["tr"] else f"\n{T['p_err']}: Java installation failed.")
        sys.exit()

    t_dir = os.path.join(os.getcwd(), "Server")
    if not os.path.exists(t_dir): os.makedirs(t_dir)
    j_name = f"{s.lower()}-{ver}.jar"
    j_path = os.path.join(t_dir, j_name)
    dl = None
    if s == "Paper":
        builds = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.papermc.io/v2/projects/paper/versions/{ver}", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode()).get("builds", [])
        if builds: dl = f"https://api.papermc.io/v2/projects/paper/versions/{ver}/builds/{builds[-1]}/downloads/paper-{ver}-{builds[-1]}.jar"
    elif s == "Purpur": dl = f"https://api.purpurmc.org/v2/purpur/{ver}/latest/download"
    elif s == "Vanilla":
        d1 = json.loads(urllib.request.urlopen(urllib.request.Request("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode())
        v_url = next((v.get("url") for v in d1.get("versions", []) if v.get("id") == ver), None)
        if v_url: dl = json.loads(urllib.request.urlopen(urllib.request.Request(v_url, headers={'User-Agent': 'MCInstaller/1.0'})).read().decode()).get("downloads", {}).get("server", {}).get("url")

    if dl:
        urllib.request.urlretrieve(dl, j_path, reporthook=lambda c, bs, ts: sys.stdout.write(f"\r{T['downloading']}: %{int((c*bs*100)/ts) if ts>0 else 0}") or sys.stdout.flush())
        print(f"\n{T['jar_downloaded']}")
    else: print(T['err_not_found']); sys.exit()
        
    if p_lst:
        print(f"\n{T['downloading_plugins']}")
        plug_dir = os.path.join(t_dir, "plugins")
        if not os.path.exists(plug_dir): os.makedirs(plug_dir)
        for i, (pid, ptitle) in enumerate(p_lst):
            try:
                print(f"- {ptitle} {T['searching_p']}")
                l_str = f'[["loaders:{s.lower()}"]]'
                v_str = f'["{ver}"]'
                v_url = f"https://api.modrinth.com/v2/project/{pid}/version?loaders={urllib.parse.quote(l_str, safe='')}&game_versions={urllib.parse.quote(v_str, safe='')}"
                v_data = json.loads(urllib.request.urlopen(urllib.request.Request(v_url, headers={'User-Agent':'MCInst/1.0'})).read().decode())
                if not v_data: v_data = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.modrinth.com/v2/project/{pid}/version", headers={'User-Agent':'MCInst/1.0'})).read().decode())
                if v_data:
                    urllib.request.urlretrieve(v_data[0]["files"][0]["url"], os.path.join(plug_dir, v_data[0]["files"][0]["filename"]))
                    print(f"  ✓ {v_data[0]['files'][0]['filename']} {T['p_downloaded']}")
                else: print(f"  X {T['p_not_found']}")
            except Exception as e: print(f"  X {T['p_err']}: {e}")

    print(f"\n{T['config_files']}")
    create_eula(t_dir); create_server_properties(t_dir, is_c); create_start_script(t_dir, get_system_ram_gb(), j_name)
    if op: open_firewall_ports(T == LANG_DICT["tr"])
    print(f"\n{T['install_complete'].format(t_dir)}")

# ==========================================
# WINDOWS ARAYÜZ (WIDESCREEN DASHBOARD)
# ==========================================
class MCServerInstallerGUI:
    def __init__(self):
        if 'ctk' not in globals(): sys.exit()
            
        self.lang = get_default_os_language()
        self.T = LANG_DICT[self.lang]
            
        self.root = ctk.CTk()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Daha Ferah Widescreen Dashboard
        self.root.geometry("1000x650") 
        self.root.minsize(1000, 650)
        self.root.title(self.T["gui_title"])

        self.downloading = False
        self.versions_cache = {"Vanilla": [], "Paper": [], "Purpur": []}
        self.selected_plugins = [] 
        
        # State Değişkenleri koruma
        self.var_software_val = "Paper"
        self.var_version_val = ""
        self.var_crack_val = True
        self.var_port_val = True
        self.var_path_val = os.path.join(os.getcwd(), "Server")
        
        self.setup_ui()
        threading.Thread(target=self.fetch_all_versions_gui, daemon=True).start()
        self.root.mainloop()

    # Tasarımı temizleyip yeniden çizer (Arayüzde dil değişimi için)
    def render_ui_rebuild(self):
        if self.downloading:
            messagebox.showwarning(self.T["warning"], "İndirme sırasında dil değiştirilemez!" if self.lang=="tr" else "Cannot change language while downloading!")
            # Geri Al
            self.lang_var.set("TR" if self.lang=="tr" else "EN")
            return
            
        # State Kaydetme
        self.var_software_val = self.var_software.get()
        self.var_version_val = self.combo_version.get()
        self.var_crack_val = self.var_crack.get()
        self.var_port_val = self.var_port.get()
        self.var_path_val = self.var_path.get()
        
        for w in self.root.winfo_children(): w.destroy()
        self.root.title(self.T["gui_title"])
        self.setup_ui()
        self.update_version_list()
        
    def switch_language_callback(self, choice):
        self.lang = "tr" if choice == "TR" else "en"
        self.T = LANG_DICT[self.lang]
        self.render_ui_rebuild()

    def fetch_all_versions_gui(self):
        self.root.after(0, lambda: self.lbl_status.configure(text=self.T["status_conn"]))
        data = fetch_api_versions()
        self.versions_cache = data
        self.root.after(0, self.update_version_list)
        self.root.after(0, lambda: self.lbl_status.configure(text=self.T["status_ready"]))
        
    def setup_ui(self):
        T = self.T
        
        # Değişkenler
        self.var_software = ctk.StringVar(value=self.var_software_val)
        self.var_crack = ctk.BooleanVar(value=self.var_crack_val)
        self.var_port = ctk.BooleanVar(value=self.var_port_val)
        self.var_path = ctk.StringVar(value=self.var_path_val)
        
        # --- HEADER ---
        header_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=(15, 5))
        
        # Grid sistemi ile Header'ı ortalamak ve sağa dil butonunu koymak
        header_frame.columnconfigure(0, weight=1)
        header_frame.columnconfigure(1, weight=5)
        header_frame.columnconfigure(2, weight=1)
        
        t_box = ctk.CTkFrame(header_frame, fg_color="transparent")
        t_box.grid(row=0, column=1)
        ctk.CTkLabel(t_box, text=T["title"], font=("Segoe UI Black", 26), text_color="#ff00ff").pack()
        ctk.CTkLabel(t_box, text=T["subtitle"], font=("Segoe UI", 13, "bold"), text_color="#00d2ff").pack()
        
        self.lang_var = ctk.StringVar(value="TR" if self.lang == "tr" else "EN")
        l_switch = ctk.CTkSegmentedButton(header_frame, values=["TR", "EN"], variable=self.lang_var, command=self.switch_language_callback, width=80)
        l_switch.grid(row=0, column=2, sticky="e")

        # --- YATAY ÇERÇEVELER (SOL VE SAĞ PANELS) ---
        main_content = ctk.CTkFrame(self.root, fg_color="transparent")
        main_content.pack(fill="both", expand=True, padx=20, pady=5)
        
        main_content.columnconfigure(0, weight=1, uniform="group1")
        main_content.columnconfigure(1, weight=1, uniform="group1")

        # // SOL PANEL // Setting Dashboard
        left_panel = ctk.CTkFrame(main_content, corner_radius=15, fg_color="#2b2b2b", border_width=2, border_color="#00d2ff")
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        ctk.CTkLabel(left_panel, text=T["step1"], font=("Segoe UI", 14, "bold")).pack(anchor="w", padx=20, pady=(20, 5))
        s_box = ctk.CTkFrame(left_panel, fg_color="transparent")
        s_box.pack(anchor="w", padx=20, pady=5)
        ctk.CTkRadioButton(s_box, text="Vanilla", variable=self.var_software, value="Vanilla", command=self.update_version_list).pack(side="left", padx=(0,15))
        ctk.CTkRadioButton(s_box, text="Paper", variable=self.var_software, value="Paper", command=self.update_version_list).pack(side="left", padx=15)
        ctk.CTkRadioButton(s_box, text="Purpur", variable=self.var_software, value="Purpur", command=self.update_version_list).pack(side="left", padx=15)

        ctk.CTkLabel(left_panel, text=T["step2"], font=("Segoe UI", 14, "bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(15, 5))
        self.combo_version = ctk.CTkOptionMenu(left_panel, values=[T["loading"]], width=350, fg_color="#3d3d3d", button_color="#00d2ff", button_hover_color="#0099cc")
        self.combo_version.pack(anchor="w", padx=20, pady=5)
        if self.var_version_val: self.combo_version.set(self.var_version_val)

        ctk.CTkLabel(left_panel, text=T["step3"], font=("Segoe UI", 14, "bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(15, 5))
        ctk.CTkSwitch(left_panel, text=T["crack_allow"], variable=self.var_crack, progress_color="#00d2ff").pack(anchor="w", padx=20, pady=10)
        ctk.CTkSwitch(left_panel, text=T["port_allow"], variable=self.var_port, progress_color="#00e676").pack(anchor="w", padx=20, pady=10)


        # // SAĞ PANEL // Plugin Store
        right_panel = ctk.CTkFrame(main_content, corner_radius=15, fg_color="#2b2b2b", border_width=2, border_color="#ff00ff")
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        self.plugin_label = ctk.CTkLabel(right_panel, text=T["step4"], font=("Segoe UI", 14, "bold"), text_color="#ffffff")
        self.plugin_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        search_box = ctk.CTkFrame(right_panel, fg_color="transparent")
        search_box.pack(anchor="w", fill="x", padx=20, pady=5)
        self.entry_search = ctk.CTkEntry(search_box, placeholder_text=T["search_ph"], width=300, fg_color="#3d3d3d")
        self.entry_search.pack(side="left", padx=(0, 10), fill="x", expand=True)
        self.entry_search.bind("<Return>", lambda e: self.search_plugins(None))
        self.btn_search = ctk.CTkButton(search_box, text=T["find"], width=60, command=self.search_plugins, fg_color="#555555", hover_color="#666666", text_color="#00d2ff", font=("Segoe UI", 12, "bold"))
        self.btn_search.pack(side="left")

        # Plugin Store results split
        p_split = ctk.CTkFrame(right_panel, fg_color="transparent")
        p_split.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        self.results_frame = ctk.CTkScrollableFrame(p_split, width=200, fg_color="#3d3d3d")
        self.results_frame.pack(side="left", fill="both", expand=True, padx=(0,10))
        
        sel_frame = ctk.CTkFrame(p_split, width=150, fg_color="#333333", corner_radius=10)
        sel_frame.pack(side="right", fill="both")
        sel_frame.pack_propagate(False)
        ctk.CTkLabel(sel_frame, text=T["to_install"], font=("Segoe UI", 12, "bold"), text_color="white").pack(pady=5)
        self.lbl_selected_plugins = ctk.CTkLabel(sel_frame, text=T["no_plugin_sel"], justify="left", wraplength=130, font=("Segoe UI", 11), text_color="gray")
        self.lbl_selected_plugins.pack(anchor="nw", padx=10, pady=5)


        # --- ALT PANEL (Bottom) ---
        bottom_panel = ctk.CTkFrame(self.root, corner_radius=15, fg_color="#2b2b2b", border_width=2, border_color="#39ff14")
        bottom_panel.pack(fill="x", padx=20, pady=(5, 15))

        # Install Box (left) & Button (right)
        bottom_panel.columnconfigure(0, weight=3)
        bottom_panel.columnconfigure(1, weight=1)

        b_left = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        b_left.grid(row=0, column=0, sticky="ew", padx=20, pady=15)
        
        ctk.CTkLabel(b_left, text=T["step5"], font=("Segoe UI", 14, "bold"), text_color="#ffffff").pack(anchor="w", pady=(0, 5))
        p_box = ctk.CTkFrame(b_left, fg_color="transparent")
        p_box.pack(fill="x")
        ctk.CTkEntry(p_box, textvariable=self.var_path, fg_color="#3d3d3d").pack(side="left", fill="x", expand=True, padx=(0, 10))
        ctk.CTkButton(p_box, text=T["browse"], width=80, command=self.browse_path, fg_color="#555555", hover_color="#666666").pack(side="left")

        ctk.CTkLabel(b_left, text=T["sys_info"].format(get_system_ram_gb()), text_color="#00d2ff", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(5,0))

        b_right = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        b_right.grid(row=0, column=1, sticky="e", padx=30, pady=15)

        self.btn_install = ctk.CTkButton(b_right, text=T["btn_install"], command=self.start_install_thread, font=("Segoe UI Black", 16), text_color="#39ff14", width=220, height=50, fg_color="transparent", border_width=2, border_color="#39ff14", hover_color="#0f330f")
        self.btn_install.pack(anchor="e")

        # Global Progress (very bottom)
        prog_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        prog_frame.pack(fill="x", padx=20, pady=(0, 10))
        self.progress_var = ctk.DoubleVar(value=0.0)
        self.progress = ctk.CTkProgressBar(prog_frame, variable=self.progress_var, height=12, progress_color="#00e676")
        self.progress.pack(fill="x", padx=10, pady=(0, 5))
        self.progress.set(0)
        self.lbl_status = ctk.CTkLabel(prog_frame, text=T["status_conn"], font=("Segoe UI", 12, "bold"), text_color="#00d2ff")
        self.lbl_status.pack()

        # Update initial states
        self.update_version_list()
        self._update_selected_list_render()

    def update_version_list(self):
        sw = self.var_software.get()
        v = self.versions_cache.get(sw, [])
        if v:
            self.combo_version.configure(values=v)
            if self.var_version_val in v: self.combo_version.set(self.var_version_val)
            else: self.combo_version.set(v[0])
        else:
            self.combo_version.configure(values=[self.T["loading"]])
            self.combo_version.set(self.T["loading"])

        if sw == "Vanilla":
            self.entry_search.configure(state="disabled")
            self.btn_search.configure(state="disabled")
            self.plugin_label.configure(text_color="gray")
            self.results_frame.configure(fg_color="#1a1a1a") # dim
        else:
            self.entry_search.configure(state="normal")
            self.btn_search.configure(state="normal")
            self.plugin_label.configure(text_color="white")
            self.results_frame.configure(fg_color="#2b2b2b")

    def search_plugins(self, event=None):
        if self.var_software.get() == "Vanilla":
            messagebox.showwarning(self.T["warning"], self.T["warn_vanilla"])
            return
        q = self.entry_search.get().strip()
        if not q: return
        for widget in self.results_frame.winfo_children(): widget.destroy()
        
        loading_lbl = ctk.CTkLabel(self.results_frame, text=self.T["loading"], text_color="gray")
        loading_lbl.pack(pady=10)
        self.btn_search.configure(state="disabled")
        threading.Thread(target=self._search_thread, args=(q, loading_lbl), daemon=True).start()

    def _search_thread(self, query, loading_lbl):
        try:
            params = urllib.parse.urlencode({'query': query, 'facets': '[["project_type:plugin"]]'})
            data = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.modrinth.com/v2/search?{params}", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode())
            self.root.after(0, lambda: self._show_search_results(data.get("hits", []), loading_lbl))
        except:
            self.root.after(0, lambda: loading_lbl.configure(text=self.T["search_fail"], text_color="red"))
        finally:
            self.root.after(0, lambda: self.btn_search.configure(state="normal"))

    def _show_search_results(self, hits, loading_lbl):
        loading_lbl.destroy()
        if not hits: ctk.CTkLabel(self.results_frame, text=self.T["no_match"], text_color="gray").pack(); return
            
        for hit in hits:
            added = any(x[0] == hit["project_id"] for x in self.selected_plugins)
            item_frame = ctk.CTkFrame(self.results_frame, fg_color="#333333")
            item_frame.pack(fill="x", pady=2, padx=5)
            ctk.CTkLabel(item_frame, text=hit["title"][:22], font=("Segoe UI", 12)).pack(side="left", padx=10, pady=5)
            
            w_text = self.T["btn_add"] if not added else self.T["btn_added"]
            btn_add = ctk.CTkButton(item_frame, text=w_text, width=50, height=24, font=("Segoe UI", 11), fg_color="#0080c0" if not added else "#555", hover_color="#00a8ff", state="normal" if not added else "disabled")
            btn_add.configure(command=lambda i=hit["project_id"], t=hit["title"], b=btn_add: self.add_plugin(i, t, b))
            btn_add.pack(side="right", padx=10)

    def add_plugin(self, p_id, title, button_widget):
        if not any(x[0] == p_id for x in self.selected_plugins):
            self.selected_plugins.append((p_id, title))
            button_widget.configure(text=self.T["btn_added"], state="disabled", fg_color="#555555")
            self._update_selected_list_render()

    def _update_selected_list_render(self):
        if not self.selected_plugins:
            self.lbl_selected_plugins.configure(text=self.T["no_plugin_sel"])
        else:
            lines = [f"• {t[:16]}" for i, t in self.selected_plugins]
            self.lbl_selected_plugins.configure(text="\n".join(lines), text_color="#AFFF33") # Hafif neon yeşil vurgu

    def browse_path(self):
        folder = filedialog.askdirectory(initialdir=os.getcwd())
        if folder: self.var_path.set(folder)

    def start_install_thread(self):
        if self.downloading: return
        version = self.combo_version.get()
        target_dir = self.var_path.get()
        if not version or version == self.T["loading"]: return
        self.downloading = True
        self.btn_install.configure(state="disabled", text=self.T["btn_downloading"])
        self.progress_var.set(0)
        
        sw = self.var_software.get()
        is_crk = self.var_crack.get()
        op_port = self.var_port.get()
        p_copy = list(self.selected_plugins)
        
        threading.Thread(target=self.install_server, args=(sw, version, target_dir, is_crk, op_port, p_copy), daemon=True).start()

    def install_server(self, software, version, target_dir, is_crack, open_port, plugins_to_install):
        jar_name = f"{software.lower()}-{version}.jar"
        jar_path = os.path.join(target_dir, jar_name)
        T = self.T
        try:
            def update_lbl(m): self.root.after(0, lambda: self.lbl_status.configure(text=m))
            update_lbl("Java kontrol ediliyor..." if self.lang=="tr" else "Checking Java...")
            if not check_and_install_java(self.lang == "tr", update_lbl):
                raise Exception("Java kurulamadı! Lütfen yönetici izni verin veya manuel kurun." if self.lang=="tr" else "Failed to install Java! Run as admin or install manually.")
            
            if not os.path.exists(target_dir): os.makedirs(target_dir)
            download_url = None
            if software == "Paper":
                builds = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.papermc.io/v2/projects/paper/versions/{version}", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode()).get("builds", [])
                if builds: download_url = f"https://api.papermc.io/v2/projects/paper/versions/{version}/builds/{builds[-1]}/downloads/paper-{version}-{builds[-1]}.jar"
            elif software == "Purpur": download_url = f"https://api.purpurmc.org/v2/purpur/{version}/latest/download"
            elif software == "Vanilla":
                data = json.loads(urllib.request.urlopen(urllib.request.Request("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json", headers={'User-Agent': 'MCInstaller/1.0'})).read().decode())
                version_url = next((v.get("url") for v in data.get("versions", []) if v.get("id") == version), None)
                if version_url: download_url = json.loads(urllib.request.urlopen(urllib.request.Request(version_url, headers={'User-Agent': 'MCInstaller/1.0'})).read().decode()).get("downloads", {}).get("server", {}).get("url")

            def report_hook(c, bs, ts):
                if ts > 0: self.root.after(0, lambda p=(c*bs)/ts: self.progress_var.set(min(1.0, p)))

            if download_url:
                self.root.after(0, lambda: self.lbl_status.configure(text=T["status_main_dl"].format(version)))
                urllib.request.urlretrieve(download_url, jar_path, reporthook=report_hook)

            if software != "Vanilla" and plugins_to_install:
                self.root.after(0, lambda: self.progress_var.set(0))
                plugins_dir = os.path.join(target_dir, "plugins")
                if not os.path.exists(plugins_dir): os.makedirs(plugins_dir)
                for i, (p_id, p_title) in enumerate(plugins_to_install):
                    try:
                        self.root.after(0, lambda t=p_title: self.lbl_status.configure(text=T["status_p_dl"].format(t)))
                        l_str = f'[["loaders:{software.lower()}"]]'
                        v_str = f'["{version}"]'
                        v_url = f"https://api.modrinth.com/v2/project/{p_id}/version?loaders={urllib.parse.quote(l_str, safe='')}&game_versions={urllib.parse.quote(v_str, safe='')}"
                        v_data = json.loads(urllib.request.urlopen(urllib.request.Request(v_url, headers={'User-Agent':'MCInst/1.0'})).read().decode())
                        if not v_data: v_data = json.loads(urllib.request.urlopen(urllib.request.Request(f"https://api.modrinth.com/v2/project/{p_id}/version", headers={'User-Agent':'MCInst/1.0'})).read().decode())
                        if v_data: urllib.request.urlretrieve(v_data[0]["files"][0]["url"], os.path.join(plugins_dir, v_data[0]["files"][0]["filename"]))
                    except: pass

            self.root.after(0, lambda: self.lbl_status.configure(text=T["status_cfg"]))
            create_eula(target_dir)
            create_server_properties(target_dir, is_crack)
            create_start_script(target_dir, get_system_ram_gb(), jar_name)
            if open_port: open_firewall_ports(self.lang == "tr")
            
            self.root.after(0, lambda: self.lbl_status.configure(text=T["status_success"]))
            self.root.after(0, lambda: messagebox.showinfo(T["done_title"], f"{software} {T['msg_done'].format(target_dir)}"))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(T["err_title"], T["msg_err"].format(e)))
        finally:
            self.downloading = False
            self.root.after(0, lambda: self.btn_install.configure(state="normal", text=T["btn_install"]))
            self.root.after(0, lambda: self.progress_var.set(0))

if __name__ == "__main__":
    if SYSTEM_OS == "Windows":
        import ctypes
        import sys
        
        # Arka plandaki sinir bozucu CMD (Terminal) penceresini tamamen gizle
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 0)
            
        if not ctypes.windll.shell32.IsUserAnAdmin():
            # Admin olarak yeniden başlatırken de CMD'yi gizli (0) aç
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join([f'"{sys.argv[0]}"'] + sys.argv[1:]), None, 0)
            sys.exit()
        MCServerInstallerGUI()
    else:
        import os
        import sys
        if os.geteuid() != 0:
            print("INFO: Root privileges are requested for full automation (Java & Firewall).")
            try:
                os.execvp("sudo", ["sudo", sys.executable] + sys.argv)
            except:
                pass
        run_linux_cli()
