# ZORRO Installation Guide on WSL (Windows Subsystem for Linux)

## 📌 Prerequisites
- Windows 10/11 with **WSL 2** installed
- Ubuntu installed via WSL
- Internet connection

## 🚀 Step-by-Step Installation

### 1️⃣ Install WSL & Ubuntu
```powershell
wsl --install -d Ubuntu
```
- This installs **WSL 2** and **Ubuntu**.
- Restart if required.
- Launch Ubuntu from the Start Menu.

### 2️⃣ Verify WSL Version
```powershell
wsl -l -v
```
Ensure Ubuntu is running **WSL version 2**.

### 3️⃣ Download & Move ZORRO to WSL
```bash
mv /mnt/c/Users/YOUR_WINDOWS_USERNAME/Downloads/zorro_linux_x86_64 ~/
```
*(Replace `YOUR_WINDOWS_USERNAME` with your actual Windows username.)*

### 4️⃣ Give Execute Permission
```bash
chmod +x ~/zorro_linux_x86_64
```

### 5️⃣ Move to `/usr/local/bin`
```bash
sudo mv ~/zorro_linux_x86_64 /usr/local/bin/zorro
```

### 6️⃣ Add ZORRO to PATH
```bash
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc && source ~/.bashrc
```

### 7️⃣ Verify Installation
```bash
zorro -h
```
If ZORRO options appear, installation is successful! ✅

## 📜 Summary
| Step | Command |
|------|---------|
| **Install WSL** | `wsl --install -d Ubuntu` |
| **Check WSL Version** | `wsl -l -v` |
| **Move ZORRO to WSL** | `mv /mnt/c/Users/YOUR_WINDOWS_USERNAME/Downloads/zorro_linux_x86_64 ~/` |
| **Give Execute Permission** | `chmod +x ~/zorro_linux_x86_64` |
| **Move to /usr/local/bin** | `sudo mv ~/zorro_linux_x86_64 /usr/local/bin/zorro` |
| **Add ZORRO to PATH** | `echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc && source ~/.bashrc` |
| **Verify ZORRO Installation** | `zorro -h` |

---
### 🎯 Notes
- Make sure you have **WSL 2** enabled.
- You must replace `YOUR_WINDOWS_USERNAME` with your actual Windows username.
- If you face issues, restart WSL with:
  ```powershell
  wsl --shutdown
  ```
- If WSL doesn't start, try:
  ```powershell
  wsl -d Ubuntu --exec bash --noprofile --norc
  ```

📢 **Need help?** Feel free to open an issue!

---
### 🔗 References
- [ZORRO on SourceForge](http://sourceforge.net/projects/probmask/files/)
- [WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
