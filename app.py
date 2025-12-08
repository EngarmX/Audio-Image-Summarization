from flask import Flask, render_template, request, redirect, session, url_for, flash
from werkzeug.utils import secure_filename
from auth.auth import auth
from auth.summarization import process_file_and_summarize
import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'NaWMXYKQNzeNAKyJ5RPcYDbMSxZ2KWbCgw2Ml8wmupU'
app.register_blueprint(auth, url_prefix='/api')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' not in session:
        flash('Please login first.', 'warning')
        return redirect(url_for('index'))

    extracted_text, summary, uploaded_file_name, uploaded_file_type, selected_length = None, None, None, None, 'medium'

    if request.method == 'POST':
        file = request.files['file']
        if not file:
            flash('No file uploaded.', 'danger')
            return redirect(url_for('dashboard'))

        filename = secure_filename(file.filename)
        temp_path = os.path.join("temp", filename)
        os.makedirs("temp", exist_ok=True)

        # Debug: Check if file is being saved
        print(f"Saving file to: {temp_path}")
        file.save(temp_path)
        print(f"File exists after saving: {os.path.exists(temp_path)}")

        # Get the summary_length from the form
        summary_length = request.form.get('summary_length', 'medium')  # Default to 'medium' if not provided

        try:
            # Pass both file_path and summary_length to the function
            extracted_text, summary = process_file_and_summarize(temp_path, summary_length)
            uploaded_file_name = file.filename
            uploaded_file_type = file.content_type
            selected_length = summary_length
            flash('File processed successfully.', 'success')

        except Exception as e:
            flash(str(e), 'danger')

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
                print(f"File removed: {temp_path}")
            else:
                print(f"File not found for removal: {temp_path}")

    return render_template('dashboard.html', 
                        username=session['user'], 
                        extracted_text=extracted_text, 
                        summary=summary,
                        uploaded_file_name=uploaded_file_name,
                        uploaded_file_type=uploaded_file_type,
                        selected_length=selected_length)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
