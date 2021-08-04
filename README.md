# Att&ckCommands

This is a tool that I have developed to help learn penetration testing and red teaming.

### Installation and Use
To install:
```
sudo git clone /opt/Att&ckCommands
```

To use:
```
python3 Att&ckCommands.py <section> <OS>
```

The `section` is what part of the [MITRE ATT&CK framework](https://attack.mitre.org/) you want to list commands from. Sections include:
- `recon` (Reconnaissance)
- `init` (Initial Access)

The `OS` is optional, defaults to all operating systems. List of operating systems below:
- `Windows`
- `Linux`
- `Mac`