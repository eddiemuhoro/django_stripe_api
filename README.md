# 💳 Django Stripe Checkout API

A lightweight Django REST API that integrates Stripe Checkout for secure online payments.  
This project allows you to initiate Stripe payment sessions and handle webhook callbacks to confirm successful transactions.

---

## ✨ Features

- 🔐 Secure integration with Stripe API using secret keys
- 💸 Initiate Stripe Checkout sessions via POST requests
- 🔁 Handle Stripe webhooks for transaction verification
- 🧾 Clean class-based views (CBVs) using Django REST Framework
- 🧪 Sandbox & production-ready architecture

---

## 🧰 Tech Stack

| Layer       | Tools                          |
|-------------|---------------------------------|
| Backend     | Django, Django REST Framework   |
| Payments    | Stripe Checkout API             |
| Utilities   | `stripe` Python SDK, `python-dotenv` |
| Testing     | Stripe CLI, Postman, Ngrok      |

---

## 📁 Project Structure

django_stripe_project/
├── stripe_project/ # Django project settings
├── api/ # Stripe logic lives here
│ ├── views.py # Checkout session & webhook views
│ ├── serializers.py # Request validation for payment
│ ├── urls.py # Routes for Stripe integration
│ └── utils.py # (Optional) Stripe helpers
├── .env # Environment variables
├── requirements.txt # Dependencies
└── manage.py

yaml
Copy
Edit

---






