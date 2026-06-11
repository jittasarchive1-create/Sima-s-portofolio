from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile_data = {
        "name": "Sima Tita",
        "role": "Full-Stack Developer / Cybersecurity Enthusiast",
        "about": "Informatics Engineering student at Universitas Muhammadiyah Surakarta with over 3 years of coding experience.",
    }
    
    experiences_data = [
        {
            "role": "Full-Stack Developer Intern",
            "company": "findYourLOvetech",
            "period": "June 2025 - Present",
            "tasks": [
                "Developed and maintained modern web applications using Laravel and Tailwind CSS.",
                "Implemented secure and scalable database architectures using MySQL.",
                "Collaborated with the team to analyze system requirements and optimize backend performance."
            ]
        }
    ]
    
    projects_data = [
        {
            "title": "Logbook Internship",
            "description": "A web-based internship activity management system designed to support attendance tracking and progress reporting.",
            "features": [
                "Mentor and intern attendance management",
                "Progress report upload and activity documentation",
                "Internship activity monitoring in a centralized system"
            ],
            "technologies": ["HTML", "Tailwind CSS", "JavaScript", "PHP", "Laravel", "MySQL"]
        },
        {
            "title": "Monev App With Laravel",
            "description": "A monitoring and evaluation web application built with Laravel to manage regional data, activities, and centralized monitoring.",
            "features": [
                "Regional data management for monitoring workflows",
                "Activity, package, realization, and planning modules",
                "Centralized monitoring for all recorded data"
            ],
            "technologies": ["HTML", "Tailwind CSS", "JavaScript", "PHP", "Laravel", "MySQL"]
        }
    ]
    
    return render_template('index.html', profile=profile_data, experiences=experiences_data, projects=projects_data)

if __name__ == '__main__':
    app.run(debug=True)
