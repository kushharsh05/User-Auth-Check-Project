# 🔐 Authenticator Web App

A modern authentication system built using **Supabase** for backend services and **HTML, CSS, and JavaScript** for the frontend. This project enables users to securely register, log in, and authenticate using email/password or Google OAuth.

---

## 🚀 Features

- ✅ User Registration (Email & Password)
- ✅ Secure Login System
- ✅ Google OAuth Login
- ✅ Session Handling
- ✅ Responsive UI
- ✅ Supabase Integration
- ✅ Real-time Database

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend (BaaS):** Supabase  
- **Authentication:** Supabase Auth + Google OAuth  
- **Database:** PostgreSQL (via Supabase)

---

## 📂 Project Structure

```
project-root/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── base.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── videos/
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download

```bash
git clone <your-repo-link>
cd project-folder
```

---

### 2️⃣ Setup Supabase

1. Go to https://supabase.com  
2. Create a new project  
3. Copy:
   - Project URL  
   - Publishable (anon) key  

---

### 3️⃣ Configure Supabase

In your HTML files:

```javascript
const supabaseClient = supabase.createClient(
  "YOUR_PROJECT_URL",
  "YOUR_ANON_KEY"
);
```

---

### 4️⃣ Google OAuth Setup (Optional)

- Go to Google Cloud Console  
- Create OAuth Client ID  
- Add redirect URI:

```
https://YOUR_PROJECT_ID.supabase.co/auth/v1/callback
```

- Paste Client ID & Secret in Supabase → Authentication → Providers  

---

### 5️⃣ Run the Project

No backend required.

Use VS Code Live Server:

- Right click `login.html`
- Click **Open with Live Server**

OR open directly in browser.

---

## 🧪 Usage

1. Register a new user  
2. Login using credentials  
3. Access dashboard  
4. Logout  

---

## 🔒 Security Notes

- Do NOT expose Supabase Secret Key  
- Use only Publishable Key in frontend  
- Keep OAuth credentials secure  

---

## 🎯 Future Improvements

- 🔹 Password reset  
- 🔹 Profile page  
- 🔹 Email verification  
- 🔹 Role-based access  
- 🔹 UI enhancements  

---

## 👨‍💻 Authors

- Dhruthi Pai – Backend & Auth  
- Harsh Vardhan Kushwaha – Frontend & Integration  

---

## 📌 Status

✅ Completed  
🚀 Ready for submission  

---
