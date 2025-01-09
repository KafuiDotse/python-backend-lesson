from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///users.db"
    db.init_app(app)

    from model import User
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        return render_template("./index.html")
    
    @app.route("/sign-up",methods=["POST","GET"])
    def Sign_Up():
        if request.method=="POST":
            name=request.form.get("name")
            password=request.form.get("password")
            confirm_password=request.form.get("confirm-password")
            valid_password=""
            if password==confirm_password:
                valid_password=password

            user1=User(username=name, password=valid_password)
            db.session.add(user1)
            db.session.commit()
            return redirect("/home")
        return render_template("sign_up.html")
    
    @app.route("/login",methods=["GET","POST"])
    def Login():
        if request.method=="POST":
            username=request.form.get("username")
            password=request.form.get("password")

            user_list=User.query.filter_by(username=username).all()
           
            for user in user_list:
                if user.password==password:
                    print("Succesfull")
                    return redirect("/home")
            print("Not successfull")

        return render_template("login.html")

    
    @app.route("/delete-all")
    def Delete():
        user_list=User.query.all()
        for user in user_list:
            db.session.delete(user)
            db.session.commit()
        return redirect("/")
    
    @app.route("/home")
    def Home():
        return render_template("./home.html")
    
    return app