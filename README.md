<img src='26_35866.ico'/>

# FangOff

Simple GUI Tool to De-Fang a link and Re-Fang it, included both Windows executable and Python for you.

## Modules

Only modules used are available by default:

- `tkinter`
- `webbrowser`
- `sys`
- `optparse`

## What's included

Python file for you Linux People

Exe For all you Windows lovers

## How to Run

### Windows exclusive

Run the `.exe` you will get a popup box, enter the URL and click De-Fang to defang the URL. Enter the URl and Click Re-Fang to add the fangs bank into the file.

### Python via Windows, Linux & macOS

Run the python script, you will get a popup box, enter the URL and click De-Fang to defang the URL. Enter the URl and Click Re-Fang to add the fangs bank into the file.

You may also use it in pure CLI mode (type `python FangOff.py -h` for options).

## What it will do

Defang URLs, Email addresses, and IP addresses

| Input  | Output  |
|---|---|
| cyberviking@thecyberviking.com  |  cyberviking[AT]thecyberviking[.]com  |
| https://www.thecyberviking.com/ | hxxps://thecyberviking[.]com/  |
| 127.0.0.1  | 127[.]0[.]0[.]1  |

## Because someone will ask

[VirusTotal of `FangOff.exe`](https://www.virustotal.com/gui/file/9a7725b5fcd754da1d5fd0515bc48fd34f7a19a4430d9122720dd6e28ff92d87/detection)

Original Sha256 hash = 9a7725b5fcd754da1d5fd0515bc48fd34f7a19a4430d9122720dd6e28ff92d87

## Changelog

version 1.6 - added CLI functionality
version 1.5 - added functionality to De-Fang Re-Fang a text file

## Thanks

Major thanks to AtomicNicos for helping out with some issues I was having
