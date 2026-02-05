# 🚀 Django Production Deployment Guide

**Docker · PostgreSQL · GitHub Actions (CI/CD) · Linode · Nginx · Gunicorn · Custom Domain · SSL**

This repository demonstrates a **complete production-ready deployment pipeline** for a **Django REST Framework (DRF)** application using modern DevOps practices.

You’ll go step-by-step through the entire journey:

> **Local Development → Docker → GitHub → CI/CD → Linode VPS → Custom Domain → HTTPS (SSL)**

---

## 🧱 Tech Stack

* **Backend:** Django REST Framework (DRF)
* **Containerization:** Docker, Docker Compose
* **Database:** PostgreSQL
* **CI/CD:** GitHub Actions
* **Server:** Linode VPS (Linux)
* **Web Server:** Nginx
* **Application Server:** Gunicorn
* **Domain:** Custom domain (via GoDaddy or similar)
* **SSL:** Let’s Encrypt (Certbot)

---

## 📦 Project Architecture

```text
Client (Browser / React)
        ↓
     Nginx (Reverse Proxy)
        ↓
    Gunicorn (WSGI)
        ↓
    Django REST API
        ↓
    PostgreSQL Database
```

---

## 🧰 Prerequisites

Make sure the following tools are installed on your local system before starting:

* Git
* Python **3.10+**
* pip
* Docker & Docker Compose
* VS Code (recommended)

---

## 🛠️ What This Project Covers

✔ Dockerizing a Django REST API
✔ PostgreSQL setup with Docker Compose
✔ Environment-based settings (local / production)
✔ Gunicorn configuration for production
✔ Nginx reverse proxy setup
✔ CI/CD pipeline using GitHub Actions
✔ Automatic deployment to Linode VPS
✔ Custom domain configuration
✔ HTTPS using Let’s Encrypt (Certbot)

---

## 🚦 Deployment Flow

1. **Local Development**

   * Build and test the Django REST API locally
   * Verify Docker containers using Docker Compose

2. **Docker**

   * Containerize Django, PostgreSQL, and Nginx
   * Use `.env` for secure configuration

3. **GitHub**

   * Push code to GitHub repository
   * Maintain clean commits and branches

4. **CI/CD with GitHub Actions**

   * Automated build & deployment pipeline
   * Secure SSH deployment to Linode VPS

5. **Linode VPS**

   * Ubuntu server setup
   * Docker & Nginx installed
   * Containers running in production

6. **Custom Domain**

   * Domain mapped to Linode public IP
   * Nginx configured with domain name

7. **HTTPS (SSL)**

   * Free SSL certificate via Let’s Encrypt
   * Auto-renewal using Certbot

---

## 🔐 Environment Variables

Sensitive data is managed using environment variables:

```env
DEBUG=False
SECRET_KEY=your_secret_key
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=db
```

⚠️ **Never commit `.env` files to GitHub**

---

## ✅ Final Result

* 🚀 Fully production-ready Django REST API
* 🔒 HTTPS secured with SSL
* 🔁 Automated CI/CD pipeline
* 🌍 Live on custom domain
* 🐳 Dockerized & scalable

---

## 📌 Notes

* Frontend (React) can be connected seamlessly to this backend
* This setup follows **industry-level deployment practices**
* Ideal for **portfolio projects**, **startup MVPs**, and **real-world production apps**

---
