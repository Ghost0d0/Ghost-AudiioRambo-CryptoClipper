# 🎧 Ghost/AudiioRambo Crypto Clipper 🚀💰  
Call me audiiorambo when I'm researching malware

_This is a cybersecurity research tool for educational purposes — demonstrating clipboard hijacking techniques used in crypto-based malware._

> **📢 Disclaimer:** This project is strictly intended for **educational** and **authorized cybersecurity research** only. It is meant to help security professionals understand and defend against clipboard-based crypto malware.  
> **Do NOT deploy on systems you do not own or have written permission to test. Unauthorized usage is illegal and unethical.**

---

![AudiioRambo Logo](https://www.veve.me/collectibles/_next/image?url=https%3A%2F%2Fd11unjture0ske.cloudfront.net%2Fbrand_image.93526e78-d51f-4866-944e-72ba053bf228.e1c39b4f-b9f0-49d8-b566-b662bbdd376b.webpFull.webp&w=1060&q=75)

---

## 📌 Project Purpose

AudiioRambo is a research-focused demonstration tool that simulates how clipboard hijacking malware works, helping ethical hackers and blue teams to:

- Understand how clipboard-based threats operate
- Develop better detection and defense mechanisms
- Raise awareness of crypto malware tactics

---

## 🔥 Key Features

- **🪙 Multi-Crypto Support** – Detects and replaces wallet addresses for: BTC, ETH, LTC, XMR, SOL, DOGE, XRP, TRX  
- **📎 Clipboard Hijacking Engine** – Uses 4 methods for reliable clipboard takeover  
- **🛡️ Evasion Logic** – Skips execution on predefined machine names (e.g., lab/testing environments)  
- **🔁 Persistence** – Adds itself to Windows startup for repeated execution  
- **📡 Discord Webhook Alerts** – Sends a message on successful clipboard hijack events  
- **🖼️ Builder GUI** – Easy configuration interface with icon support and one-click executable creation  

---

## 🧠 How It Works

### 🧰 `builder.py` – GUI-Based Configurator
- Select which cryptocurrencies to target  
- Input attacker-controlled wallet addresses  
- Set a custom icon (optional)  
- Build an executable payload using PyInstaller  

### 💀 `malware.pyw` – The Simulated Payload
- Monitors clipboard in the background  
- Detects and replaces wallet strings  
- Sends alert to Discord webhook  
- Adds itself to system startup  
- Ignores execution on specific machine names  

---

## ⚙️ Setup & Build

### 📦 Requirements

Ensure Python 3.8+ and Windows OS are installed.

Install required libraries:
```bash
pip install -r requirements.txt
```

### 🏗️ Build Steps

1. Run:
   ```bash
   python builder.py
   ```
2. Configure:
   - Cryptocurrencies
   - Wallet addresses
   - Icon (optional)
   - Discord URL hook 
3. Click **Build Executable**
4. The payload is saved to the `/dist` folder

---

## 📂 requirements.txt

```
pyinstaller
pyperclip
pynput
requests
tk
```

---

## 🕹️ Simulated Usage Flow

> ✅ **For authorized testing in lab environments only**

1. Execute the compiled file on a test system  
2. It will:
   - Start silently in the background
   - Watch the clipboard for crypto wallet patterns
   - Replace with test wallet addresses
   - Notify via Discord webhook (if configured)

---

## ⚠️ Educational Purpose Only

This tool should **never** be used outside ethical testing scenarios. Its purpose is to help researchers, red teams, and blue teams understand:

- How crypto clippers function  
- What patterns defenders can monitor  
- How to create detection rules & countermeasures  

---

## 📜 Legal Notice

This software is provided **as-is**, without any guarantees. It is meant strictly for:

- ✅ Authorized penetration testing  
- ✅ Cybersecurity training labs  
- ✅ Malware research in safe, controlled environments  

**Unauthorized use, deployment, or distribution is strictly forbidden.**  
By using this tool, you agree to assume full responsibility and comply with all applicable laws.

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---
> Buy me a coffee - _0xf89c84554c78B3194A56042bd803CcA62EA423E9_
> 
> 👻 **AudiioRambo / Ghost** – _Because even ghosts leave traces._
