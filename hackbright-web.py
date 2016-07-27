from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)

    projects = hackbright.get_grades_by_github(github)
    
    return render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            projects=projects)

@app.route("/student-search")
def get_student_form():
    """Show a form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add-form")
def display_student_add_form():
    """Add a student."""
    #first, last, github = request.form.get()

    return render_template("student_add.html")

@app.route("/student-add", methods=['POST'])
def handle_student_add():
    """Add a student."""
    first = request.form.get("firstname")
    last = request.form.get("lastname")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    return render_template("confirm_add.html", github=github)

@app.route("/projects")
def get_project():
    title = request.args.get('title')
    print "OMG THE TITLE --------", title
    projects_info = hackbright.get_project_by_title(title)
    print "HEY LOOK PROJECTS -----------", projects_info

    return render_template("project_info.html", projects_info=projects_info)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
