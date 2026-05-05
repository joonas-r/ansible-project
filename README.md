# ansible-project
Configuration management project using Ansible for Haaga-Helia's Server Management course 

## Mikä tämä on?

Tämän pelikirjan tarkoitus on asettaa hallittaville koneille perustason konfiguraatio riippumatta siitä, millä käyttöjärjestelmällä ne toimivat. 
Tämä pelikirja toimii Debianilla, Ubuntulla, Arch Linuxilla ja Windowsilla. 

### Windows
- Luo kaksi uutta käyttäjää ja käyttäjäprofiilia, joista toinen on admin
- Asettaa sijainnin ja aikavyöhykkeen Suomeen
- Hakee päivitykset Windows updatesta, ja asentaa kriittiset ja tietoturvapäivitykset heti
- Asentaa Firefoxin
- Poistaa Bing-haun
- Varmistaa sshd-palvelun olevan päällä ja käynnistyvän automaattisesti
- Lisää sshd-palveluun avaimen ja poistaa mahdollisuuden kirjautua salasanalla

## Miten tämä toimii (Windows)

ansible-playbook --user käyttäjä --become-user käyttäjä --ask-become-pass site.yml

### Hallittava kone: 

- Windows 11 asennus (Pro/Enterprise), jossa käyttäjällä on admin-oikeudet.
- OpenSSH
  - Ominaisuuden asennus
  - Palvelun käynnistys
  - Palomuurin portin avaus
- Jos teet virtuaalikoneella
  - Yhteinen NAT tai Bridged verkko

### Ansiblen konfiguraatio

- Ansible käyttää oletuksena WinRM
  - Vaatii ylimääräistä konfigurointia Ansiblen puolelta
    - pywinrm moduuli
    - SSL/TLS sertifikaatit
    ```
    ansible_connection=winrm
    ansible_winrm_transport=ntlm
    ```
- Konfiguroitu tässä tehtävässä käyttämään SSH-yhteyttä
  - hosts: ip osoite:22
  ```
  ansible_connection=ssh
  ansible_shell_type=powershell
  ```

### Muut Ansible configit

	become_method: runas
	ansible_user: <Windows admin käyttäjä>
	become_user: <Windows admin käyttäjä>

## Windows - Hallittavan koneen asennus,  karkea walkthrough

- Lataa ISO tiedosto: https://www.microsoft.com/fi-fi/software-download/windows11
- Virtuaalikoneen minimi: 2 prosessoria, 4gb ramm, 60gb tallennustilaa
- Varmista että ulkoiselta koneelta on yhteys virtuaalikoneeseen:
  - NAT Network / Bridged adapter
- Käytä Windows ISO kuvaa virtuaalikoneen levykuvana
- Windows-asennus
    - Jos haluat paikallisen käyttäjän: Kirjautumisen kohdalla, Shift+F10, `oobe\bypassnro` ja irroita verkkoyhteys
    - Käyttäjällä pitää olla salasana
- Yhdistä kone verkkoon
- Powershell: Run as admin

``` 
# Ota palvelu käyttöön
Add-WindowsCapability -Online -Name OpenSSH.Server*

# Käynnistä palvelu ja aseta käynnistymään automaattisesti
Start-Service -Name sshd
Set-Service -Name sshd -StartupType Automatic

# Uusi sääntö palomuuriin 
New-NetFirewallRule -Name 'ssh-in-TCP' -DisplayName 'Inbound rule for SSH Server (sshd) on TCP port 22' -Action Allow -Direction Inbound -Enabled True -Profile Any -Protocol 'TCP' -LocalPort 22
```
