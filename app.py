import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from dotenv import load_dotenv
from functools import wraps
import json

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.environ.get("SECRET_KEY", "your-secret-key-change-this")

# Supabase configuration (optional for development)
supabase = None
try:
    from supabase import create_client, Client
    
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    if supabase_url and supabase_key:
        supabase: Client = create_client(supabase_url, supabase_key)
        print("✓ Supabase connected successfully")
    else:
        print("⚠ Supabase credentials not found. Using development mode.")
except Exception as e:
    print(f"⚠ Supabase initialization failed: {e}")
    print("⚠ App will run in development mode without Supabase")


# ========================================
# Home & Auth Routes
# ========================================

@app.route('/')
def index():
    """Home page - redirect to dashboard if logged in, otherwise to login"""
    return render_template('login.html')


@app.route('/login/', methods=['GET'])
def login():
    """Render login page"""
    return render_template('login.html')


@app.route('/register/', methods=['GET'])
def register():
    """Render registration page"""
    return render_template('register.html')


# ========================================
# Dashboard Routes (Protected)
# ========================================

@app.route('/dashboard/', methods=['GET'])
def dashboard():
    """Render dashboard page - Supabase session check happens on frontend"""
    return render_template('dashboard.html')


@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    """Render and handle profile updates - Supabase session check happens on frontend"""
    user = session.get('user', {})
    
    if request.method == 'POST':
        # Handle profile update
        username = request.form.get('username')
        
        try:
            # Update user metadata
            user['username'] = username
            session['user'] = user
            
            return render_template('profile.html', user=user, message='Profile updated successfully!')
        except Exception as e:
            return render_template('profile.html', user=user, error=str(e))
    
    return render_template('profile.html', user=user)


@app.route('/logout/', methods=['GET'])
def logout():
    """Log out user and clear session"""
    session.clear()
    return redirect(url_for('login'))


# ========================================
# API Routes for Frontend Authentication
# ========================================

@app.route('/api/auth/session', methods=['GET'])
def get_session():
    """Get current user session from Flask (backend session)"""
    if 'user' in session:
        return jsonify({'authenticated': True, 'user': session['user']})
    return jsonify({'authenticated': False})


@app.route('/api/auth/set-session', methods=['POST'])
def set_session():
    """Set user session after frontend Supabase authentication"""
    try:
        data = request.get_json()
        user = data.get('user')
        
        if user:
            session['user'] = user
            return jsonify({'success': True}), 200
        
        return jsonify({'error': 'No user data provided'}), 400
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ========================================
# Health Check
# ========================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Server is running'})


# ========================================
# Error Handlers
# ========================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Page not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


# ========================================
# Template Context
# ========================================

@app.context_processor
def inject_user():
    """Make user available in all templates"""
    return {'current_user': session.get('user')}


if __name__ == '__main__':
    app.run(debug=True)