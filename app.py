# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Updated project data based on provided information
projects = [
    {
        'id': 1,
        'title': 'EventEase',
        'description': 'An event planning platform for seamless vendor coordination.',
        'image': 'static/eventease.jpg',
        'technologies': ['Python', 'Flask', 'SQLAlchemy', 'JavaScript'],
        'github': 'https://github.com/GaneshGupta3/EventEase',
        'live_demo': 'https://eventease.example.com'
    },
    {
        'id': 2,
        'title': 'EduValt',
        'description': 'Document storage and admission management system.',
        'image': 'static/eduvault.png',
        'technologies': ['Python', 'Flask', 'MongoDB', 'Bootstrap'],
        'github': 'https://github.com/GaneshGupta3/eduvault',
        'live_demo': 'https://eduvault.example.com'
    },
    {
        'id': 3,
        'title': 'Solve Together',
        'description': 'Collaborative problem-solving, developing web applications for Industry level practice.',
        'image': 'static/synergysolver.jpg',
        'technologies': ['Python', 'Flask', 'React', 'PostgreSQL'],
        'github': 'https://github.com/GaneshGupta3/synergysolver',
        'live_demo': 'https://synergysolver.example.com'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # You might want to add validation here or store the form data
        
        # Redirect to success page with form data
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))

@app.route('/success')
def success():
    # Get form data from query parameters
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    
    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)