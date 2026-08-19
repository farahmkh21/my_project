*This activity has been created as part of the 42 curriculum by fkhaldi.*

# NetPractice

## Description

NetPractice is a networking training project from the 42 curriculum.

The objective of this project is to understand the fundamentals of computer networking by solving a series of practical networking exercises. Throughout the project, you configure IP addresses, subnet masks, default gateways, and routers to establish successful communication between network devices.

The project contains 10 levels, each presenting a broken network that must be fixed by modifying the available network configuration.

---

## Instructions

### Running the training interface

1. Download and extract the NetPractice project files.
2. Run:

```bash
./run.sh
```

If `run.sh` does not work, start a local HTTP server manually:

```bash
python3 -m http.server 49242
```

Then open:

```
http://localhost:49242
```

in your web browser.

### Completing the exercises

- Enter your 42 login to generate your personal configuration.
- Solve each networking level.
- Click **Check again** to validate your solution.
- Once the level is completed, click **Get my config** to export your configuration.
- Repeat this process for all 10 levels.

### Submission

- Export one configuration file for each level.
- Place all **10 exported configuration files** in the root of your Git repository.
- Include this `README.md` file in the repository root.

---

## Networking Concepts

This project covers the following networking concepts:

- IPv4 addressing
- Subnet masks
- Default gateways
- Routers
- Switches
- TCP/IP
- Network routing
- Network communication
- Basic troubleshooting
- OSI Model fundamentals

---

## Resources

### Documentation

- https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL
- https://www.cloudflare.com/learning/network-layer/what-is-an-ip-address/
- https://www.cloudflare.com/learning/network-layer/what-is-a-subnet/
- https://www.geeksforgeeks.org/computer-network-tutorials/
- https://en.wikipedia.org/wiki/TCP/IP

### AI Usage

AI was used to:

- Improve networking concept explanations.
- Review routing and subnetting solutions.
- Generate and polish the project documentation (README).
- Clarify networking terminology and troubleshooting steps.

All configurations and solutions were reviewed and understood before submission.

---

## Repository Structure

```
.
├── README.md
├── level1
├── level2
├── level3
├── level4
├── level5
├── level6
├── level7
├── level8
├── level9
└── level10
```

---
