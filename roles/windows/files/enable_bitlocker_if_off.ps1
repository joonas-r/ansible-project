If ((Get-BitLockerVolume ($env:SystemDrive)).ProtectionStatus -eq "Off") {
    Enable-BitLocker $env:SystemDrive -TpmProtector -RecoveryKeyPath "C:\Recovery\" -RecoveryKeyProtector
    $Ansible.Changed = $true
}
else {
    $Ansible.Changed = $false
}

