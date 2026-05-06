# ansible-project
Configuration management project using Ansible for Haaga-Helia's Server Management course 

# BaseLine

A simple tool built from a real problem: creating secure, ready-to-use OS baselines. Inspired by the hassle of using other tools where you have to hunt down config files and tweak things manually. The goal here is to make it easy for you: clone the repo, configure one file, and let the project handle the rest. Designed to remove repetitive work and make best practices the default across Debian, Ubuntu, Arch, and Windows, so you can spend more time on your actual projects.

---

## Supported Systems

At the moment, the project supports:

- Debian
- Ubuntu
- Arch Linux
- Windows

### Disclosure

Each operating system now does different things. These are still evolving, and the long-term goal is to refine and standardize them further. I intend to use this, so I want to make this good.  
Different implementations are currently in progress.

---
## Using the tool
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
git clone <repo>
cd baseline
# configure your settings file
# run the setup
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
---

## Setup Walkthroughs

### Windows

#### 1. Download Windows ISO

Download the Windows 11 ISO from Microsoft:

https://www.microsoft.com/fi-fi/software-download/windows11

---

#### 2. Virtual Machine Requirements

Minimum recommended specs:

- 2 CPUs  
- 4 GB RAM  
- 60 GB storage  

---

#### 3. Network Configuration

Ensure the VM is reachable from the host machine.

---

#### 4. Install Windows

- If you are using a VM, use a guide that is specific to your machine since the installation process is slightly different between virtualization platforms  
- Attach the ISO as the VM disk image  
- Start the installation process  

---

#### 5. Create a Local User (Optional)

If you want to avoid using a Microsoft account:

1. At the login screen, press:  
   Shift + F10

2. Run:
```
oobe\bypassnro
```

3. Disconnect from the network  

4. Continue setup with a local user  

Note: The user must have a password.

---

#### 6. Enable Network

Reconnect the VM to the network after setup is complete.

---

#### 7. Enable OpenSSH Server

Open PowerShell as Administrator and run:

```
Add-WindowsCapability -Online -Name OpenSSH.Server*

Start-Service -Name sshd

New-NetFirewallRule -Name "ssh-in-TCP" -DisplayName "Inbound rule for SSH Server (sshd) on TCP port 22" -Action Allow -Direction Inbound -Enabled True -Profile Any -Protocol TCP -LocalPort 22
```

---

## Linux (Debian / Ubuntu)

Minimum recommended specs:

- **Debian:** 1 CPU, 4 GB RAM, 20 GB disk space  
- **Ubuntu:** Dual-core CPU, 6 GB RAM, 25 GB disk space  

---

Setup steps are simpler and more uniform across Linux systems:

### 1. Download the OS

You can basically use any guide for installing Debian / Ubuntu Linux.  
For VMs, use a virtualization-platform-specific guide.  
For hardware installations, you can follow pretty much any YouTube guide (e.g., "how to install Debian/Ubuntu Linux").

---

### 2. Ensure Network Access

Make sure the machine has network connectivity and is accessible by the host.

---

### 3. Install and Enable SSH

Run the following:

```
sudo apt update
sudo apt install -y openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

---

## Arch Linux

You can follow this guide:  
https://www.youtube.com/watch?v=FxeriGuJKTM

Then run:

```
sudo pacman -S openssh
sudo systemctl enable sshd
sudo systemctl start sshd
```
