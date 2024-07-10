from flask import Flask, request, render_template, redirect, url_for, session
import secrets

app = Flask(__name__)

# Generate a secure random secret key
app.secret_key = secrets.token_hex(16)

# Define the logout route
@app.route('/logout')
def logout():
    # Clear the user's session data or authentication status (if you are using session)
    session.pop('user_id', None)  # Replace 'user_id' with your actual session key

    # Redirect the user to the login page
    return redirect(url_for('index'))  # Assuming 'index' is the route for your login page

# ... (the rest of your code)

if __name__ == '__main__':
    app.run(debug=True)
