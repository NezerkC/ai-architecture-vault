---
name: google-pwa-launcher
description: Launch and automate installed Google PWAs (Google AI Studio, Google Stitch, Google Gemini) via chrome_proxy.exe on Profile 1 with remote debugging enabled on port 9222.
---

# Google Apps PWA Launcher Guide

Use this skill whenever launching, inspecting, or automating installed Google Web Applications (PWAs) on this system.

## Executable & Environment Specifications
- **Proxy Executable:** `C:\Program Files\Google\Chrome\Application\chrome_proxy.exe`
- **Authenticated Profile:** `Profile 1` (`--profile-directory="Profile 1"`)
- **Remote Debugging Port:** `9222` (`--remote-debugging-port=9222`)

## Application Identifiers & Launch Commands

### 1. Google Stitch (Design with AI)
- **App ID:** `kpkpmmpeainfoiplppkjdnclpakaldhf`
- **Launch Command (PowerShell):**
  ```powershell
  Start-Process "C:\Program Files\Google\Chrome\Application\chrome_proxy.exe" -ArgumentList '--profile-directory="Profile 1"', '--app-id=kpkpmmpeainfoiplppkjdnclpakaldhf', '--remote-debugging-port=9222'
  ```

### 2. Google AI Studio
- **App ID:** `bcmmjkglicliekcndffbfgcfopnidllp`
- **Launch Command (PowerShell):**
  ```powershell
  Start-Process "C:\Program Files\Google\Chrome\Application\chrome_proxy.exe" -ArgumentList '--profile-directory="Profile 1"', '--app-id=bcmmjkglicliekcndffbfgcfopnidllp', '--remote-debugging-port=9222'
  ```

### 3. Google Gemini
- **App ID:** `eoeljdfpolbhhhgocgjdiempcaondodj`
- **Launch Command (PowerShell):**
  ```powershell
  Start-Process "C:\Program Files\Google\Chrome\Application\chrome_proxy.exe" -ArgumentList '--profile-directory="Profile 1"', '--app-id=eoeljdfpolbhhhgocgjdiempcaondodj', '--remote-debugging-port=9222'
  ```

## DevTools Automation Workflow
1. Start the target PWA using its designated launch command.
2. Connect `chrome-devtools-mcp` or the `/browser` subagent to `localhost:9222`.
3. Interact directly with the authenticated session in `Profile 1`.
