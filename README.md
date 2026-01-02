# Buffer Overflow Learning Project — VulnServer (Educational)

## Overview

This repository documents my **safe, research‑oriented exploration** of a classic stack‑based buffer overflow using the intentionally vulnerable application **VulnServer** in a fully isolated lab.

The goal of this work was to understand how crashes occur, how memory corruption impacts program control flow, and how defenders recognize these patterns. This project does **not** share weaponized exploit code.

---

##  What I Practiced

### ✔ Understanding the Stack

* Visualized ESP / EIP / EBP in the debugger
* Observed how overflowing buffers overwrite nearby data

### ✔ Crash Reproduction & Analysis

* Used controlled inputs to trigger predictable crashes
* Validated behavior with x32dbg

### ✔ Control‑Flow Awareness (High Level)

* Identified where execution flow was redirected
* Located candidate instructions like **`jmp esp`** conceptually
* Learned how attackers *could* abuse this — without implementing it

### ✔ Control‑Flow & Exploitation Concepts (Carefully, in a Lab)

* Practiced calculating **buffer offsets** to understand where overwrite occurs
* Identified candidate instructions such as **`jmp esp`** and learned why they matter
* Built a small, controlled **NOP sled** (for learning only) to visualize execution landing zones
* Studied how “payloads” fit logically into memory — without publishing or distributing any

>  I worked through these concepts hands‑on in an isolated lab.
>  The repository intentionally avoids sharing offsets, addresses, shellcode, PoCs, or automation.

---

## 🧪 Lab Environment

| Component  | Details                               |
| ---------- | ------------------------------------- |
| Target App | VulnServer (intentionally vulnerable) |
| Debugger   | x32dbg                                |
| Scripting  | Python (simple socket testing)        |
| OS         | Windows VM (isolated)                 |
| Network    | NAT‑only / no internet access         |

All analysis was performed in a controlled environment.

---

## 🔎 High‑Level Workflow (Non‑Weaponized)

1. **Mapped available commands** in VulnServer
2. **Sent increasing test input** sizes to observe behavior
3. **Confirmed repeatable crash patterns**
4. **Inspected the stack and registers** after crashes
5. **Identified protections** such as ASLR / DEP and discussed impact

Focus was on learning, not exploitation.

---

## 🛡 What This Project Teaches (Defensive Lens)

* Why bounds‑checking and secure coding matter
* What corrupted stack frames look like in practice
* Why protections like ASLR, DEP, and stack cookies exist
* How analysts interpret crash artifacts

---


This repository is intended **only for learning and responsible research**.

---

## Key Takeaways

* Many vulnerabilities originate from simple input‑handling mistakes
* Debugging builds intuition about memory behavior
* Documentation matters more than showing off working exploits
* Ethical boundaries are critical in security research

---

##  Disclaimer

All testing was performed on intentionally vulnerable software in an isolated lab. Do not apply techniques learned here to systems you do not own or lack explicit permission to test.

Security research must always respect **law, ethics, and user safety**.

---

##  Future Work

* Write YARA rules to identify suspicious binaries
* Build PE header analysis utilities
* Explore memory forensics (Volatility)
* Document detection strategies from a blue‑team perspective

---

If you're reviewing this portfolio project, thanks for reading — feedback is welcome!
