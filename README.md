# PosterBazzar – E-Commerce Dummy Store (Django)

A **fully functional dummy e-commerce website** built with **Django 4.1.6** for learning and demonstration purposes.

---

## Features

- **Product Catalog** with categories and search
- **Product Detail Page** with images, price, discount
- **Shopping Cart** (session + user-based)
- **User Authentication** (Login, Signup, Logout)
- **Responsive Static Pages** (About, Contact, Privacy, etc.)
- **Admin Panel** to manage products, categories, sliders
- **Static & Media File Handling** (Whitenoise)

---

## Tech Stack

| Technology       | Version     |
|------------------|-------------|
| Django           | 4.1.6       |
| Python           | 3.9+        |
| SQLite (dev)     | Built-in    |

---

## Local Development

### 1. Clone the Repository
```bash
git clone https://github.com/anujkaran027/PosterBazzar.git
```

### 2. Create Virtual Environment
**Linux/Mac**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root:
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations & Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

---

## Admin Panel
* URL: /admin/
* Login with the superuser created above
* Add:
    - Home Page Sliders (homepage)
    - Categories (shop)
    - Products (shop)
    - Category Images (homepage)

---

## **IMPORTANT**

>The project has many bugs and security issues. (Not recommended for production)

---

## Screenshots

### 1. Home
![Home](https://github.com/anujkaran027/PosterBazzar/blob/7a27c39d9e23e0078bb0ab818d9ca91da142e932/screenshots/Home.png)

### 2. Cart
![cart](https://github.com/anujkaran027/PosterBazzar/blob/7a27c39d9e23e0078bb0ab818d9ca91da142e932/screenshots/cart.png)

### 3. Footer
![Footer](https://github.com/anujkaran027/PosterBazzar/blob/7a27c39d9e23e0078bb0ab818d9ca91da142e932/screenshots/Footer.png)