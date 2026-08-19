*This activity has been created as part of the 42 curriculum by fkhaldi.*

# Born2beroot

## Description

Born2beroot is a system administration project from the 42 curriculum. The goal of this project is to create and configure a secure virtual server while following a strict set of requirements.

The project introduces fundamental concepts such as:

- Virtualization
- Linux system administration
- User and group management
- SSH configuration
- Firewall management
- Password policies
- Disk partitioning with LVM
- System monitoring
- Security hardening

A virtual machine was created using VirtualBox and a Debian Linux operating system was installed and configured according to the project specifications.


## Instructions

Requirements

- VirtualBox
- Debian Stable
- SSH
- UFW
- AppArmor
- LVM

## Installation

1. Create a new virtual machine using VirtualBox.
2. Install Debian Stable.
3. Configure encrypted LVM partitions.
4. Install and configure SSH on port 4242.
5. Disable root login through SSH.
6. Configure UFW to allow only port 4242.
7. Create the required users and groups.
8. Configure password aging and complexity policies.
9. Configure sudo according to project requirements.
10. Create the monitoring.sh script.
11. Configure cron to execute monitoring.sh every 10 minutes.

Running

Start the virtual machine and log in using the created user account.

Check system status:

systemctl status ssh
sudo ufw status

Run monitoring manually:

bash monitoring.sh


## Project Description

Operating System Choice

Why Debian?

Debian was selected because it is stable, beginner-friendly, well documented, and widely used in server environments.

## Advantages

- Excellent stability
- Large community support
- Extensive documentation
- Reliable package management through apt

## Disadvantages

- More conservative software updates
- Slightly older package versions compared to some distributions


## Main Design Choices

Partitioning

The system uses encrypted Logical Volume Management (LVM).

## Benefits:

- Flexible storage management
- Easier partition resizing
- Improved security through encryption

## Security Policies

The server was hardened through:

- Strong password policies
- Restricted sudo configuration
- SSH protection
- Firewall rules
- AppArmor profiles

## User Management

Two main accounts are configured:

- root
- fkhaldi

The user account belongs to:

- sudo
- user42

Installed Services

- OpenSSH Server
- UFW Firewall
- AppArmor
- Cron


## Comparisons

Debian vs Rocky Linux

Debian

Advantages:

- Easier for beginners
- Huge documentation ecosystem
- Simpler package management

Disadvantages:

- Slower update cycle

Rocky Linux

Advantages:

- Enterprise-oriented
- Binary compatible with RHEL
- Popular in professional server environments

Disadvantages:

- More complex administration for beginners


## AppArmor vs SELinux

AppArmor

Advantages:

- Easier configuration
- More beginner-friendly
- Simpler profile management

Disadvantages:

- Less granular control

SELinux

Advantages:

- Extremely powerful security controls
- Fine-grained access policies

Disadvantages:

- More difficult to learn and maintain


## UFW vs firewalld

UFW

Advantages:

- Simple syntax
- Easy setup
- Ideal for small servers

Disadvantages:

- Fewer advanced features

firewalld

Advantages:

- Dynamic rule management
- Rich networking capabilities

Disadvantages:

- More complex configuration


## VirtualBox vs UTM

VirtualBox

Advantages:

- Cross-platform support
- Large community
- Easy to use

Disadvantages:

- Limited support on Apple Silicon devices

UTM

Advantages:

- Excellent support for Apple Silicon
- Native virtualization on macOS

Disadvantages:

- Smaller user community


## Resources

Documentation

- Debian Documentation
- OpenSSH Documentation
- UFW Documentation
- AppArmor Documentation
- VirtualBox Documentation
- Linux man pages
- debian.org⁠
- debian-handbook.info⁠
- openssh.com⁠
- openssh.com⁠
- help.ubuntu.com⁠
- apparmor.net⁠
- sourceware.org⁠
- man7.org⁠

## AI Usage

AI was used as a learning assistant to:

- Understand Linux concepts
- Learn system administration terminology
- Review configuration choices
- Clarify project requirements

All configuration and implementation steps were completed manually and verified through testing.


Learning Outcomes

Through this project I learned:

- How virtualization works
- Basic Linux administration
- Secure server configuration
- User and permission management
- SSH and firewall configuration
- Storage management using LVM
- System monitoring and automation using cron
