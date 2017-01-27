---
# FSND-Linux-Server-Configuration
You will take a baseline installation of a Linux distribution on a virtual machine and prepare it to host your web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.

## Server Details
IP Address: 52.36.42.167

SSH Port: 2200

Application URL: [http://ec2-52-36-42-167.us-west-2.compute.amazonaws.com/](http://ec2-52-36-42-167.us-west-2.compute.amazonaws.com/)

##
---
## Configurations Made
### User Management
1. Create new user **grader**.
2. Give **grader** permission to *sudo*.
3. Give **grader** secure passwords.
3. Disable **root** user for remote login.

### Security
1. Configure **UFW** to only allow application ports.
2. Enforce Key-based **SSH** authentication.
3. Host **SSH** on non-default port: *2200*.

### Application Functionality
1. Update all installed packages.
2. Configure the local timezone to **UTC**.
3. Install and configure **Apache** to serve a Python **mod_wsgi** application.
4. Install and configure **PostgreSQL**.

---
## Softwares Installed
* apache2
* libapache2-mod-wsgi
* postgresql
* libpq-dev
* python-dev
