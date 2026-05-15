# Login System Setup Guide

## ✅ What's Connected

Your Flask app is now fully connected to your HTML templates and is ready to use!

### 📂 Project Structure
```
PROJECT 2(LOGIN SYSTEM)/
├── app.py                      # Main Flask application
├── templates/
│   ├── base.html              # Base template (shared styling)
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── dashboard.html         # Dashboard (after login)
│   └── profile.html           # User profile page
├── static/
│   └── css/
│       └── style.css          # Professional styling
├── accounts/                   # User management module
├── .env                        # Configuration (create this)
├── .env.example               # Template for .env
└── requirements.txt           # Python dependencies
```

## 🚀 Getting Started

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env` File
Copy `.env.example` to `.env` and fill in your Supabase credentials:

```bash
# Get these from your Supabase project settings
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-public-key

# Generate a secure secret key
SECRET_KEY=your-secret-key-here
```

### 3. Run the Application
```bash
python app.py
```

The app will start at: **http://127.0.0.1:5000**

---

## 📍 Available Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home (redirects to login/dashboard) |
| `/login/` | GET | Login page |
| `/register/` | GET | Registration page |
| `/dashboard/` | GET | User dashboard (login required) |
| `/profile/` | GET, POST | User profile management (login required) |
| `/logout/` | GET | Log out user |

---

## 🔐 How Authentication Works

### Frontend (JavaScript in HTML)
- **Supabase.js** handles login/registration
- Located in `base.html` - initialized once for all pages
- Uses Email/Password or Google OAuth

### Backend (Flask)
- Receives authentication data from frontend
- Manages user sessions
- Protects routes with `@login_required` decorator
- Provides API endpoints for session management

### Flow
1. User submits login/register form in browser
2. JavaScript calls Supabase authentication
3. If successful, data is sent to backend via API
4. Backend stores user in session
5. User is redirected to dashboard

---

## 🎨 Styling

All pages use the modern CSS design in `static/css/style.css`:
- Professional gradient buttons
- Smooth animations and transitions
- Mobile-responsive design
- Professional color scheme
- Proper form validation styling

---

## 📝 Key Features

✅ **Professional UI** - Modern, clean design  
✅ **Responsive** - Works on mobile and desktop  
✅ **Form Validation** - Client and server-side  
✅ **Error Handling** - User-friendly error messages  
✅ **Loading States** - Visual feedback during actions  
✅ **Session Management** - Secure user sessions  
✅ **Protected Routes** - Dashboard/Profile require login  

---

## 🔧 Customization

### Change Button Colors
Edit `static/css/style.css` - Look for `btn-primary` and `btn-secondary` classes

### Modify Page Content
Edit template files in `templates/` - HTML structure is clean and easy to modify

### Add New Routes
Add new routes to `app.py` following the existing pattern

---

## 🐛 Troubleshooting

### "Supabase credentials not found"
- Create a `.env` file with SUPABASE_URL and SUPABASE_KEY
- App will still work in development mode without it

### Templates not found
- Make sure `templates/` folder exists
- File names are case-sensitive

### Static files (CSS) not loading
- Ensure `static/` folder exists with correct structure
- Check browser console for 404 errors

---

## 📚 Next Steps

1. **Add Supabase Configuration**
   - Sign up at supabase.com
   - Get your project URL and API key
   - Add to `.env` file

2. **Test Authentication**
   - Try registering a new account
   - Try logging in
   - Check dashboard and profile pages

3. **Deploy**
   - Use Gunicorn/Waitress for production
   - Deploy to Heroku, Railway, Vercel, or similar

---

## 📞 Support

All authentication is handled via Supabase. For issues:
- Check Supabase documentation: https://supabase.com/docs
- Verify your API keys are correct
- Check browser console for JavaScript errors

Happy coding! 🎉
