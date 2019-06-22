### Name: Sourena Khanzadeh
### Online Demo: [iShare](https://ishareflask.herokuapp.com)
### Project Title: iShare
### Instructor: [Ghassem Tofighi](https://ghassem.com)
### License: [MIT License](https://opensource.org/licenses/MIT)
# Welcome to iShare
![Sample Logo](static/images/iShare_logo.png)
## About iShare
---
This is a very simple app that allows you to connect your repository code to a piece of paper. This app is very similar to [paperswithcode.com](https://paperswithcode.com). You can modify this app the way you want to. Follow the instructions sections to use iShare like it's meant to be used. In iShare you can create sections as an admin, have disscussion in each paper, and allow users to upload their git repository with a pdf paper attached to it.  

## Default features
---
> __YOU CAN ~~DISABLE~~/ENABLE EACH OF THESE FEATURES IN SETTING'S PAGE, SOME AS ADMIN AND SOME AS USER__
* ### Discussion Board 
  * allows user's to create discussions in the paper section.
      * _NOTE: admin only can ~~disable~~ or enable this feature_
* ### SMTP Email Service
  * Send's users a welcoming email on signing up and allow you to send weekly or monthly email 
      * _NOTE: admin only can ~~disable~~ or enable this feauture_
* ### Animation's
  * wave animation for the landing page 

## Tasks
- [x]  ~~Page Pagination~~ 
- [x]  ~~tags~~ 
- [ ]  Enhanced Sections 
- [x]  ~~About Page~~ 
## Watch This Video
---
[![video](camera.png)](https://www.youtube.com/watch?v=cEFqgPxfpx8)

## Automatic Heroku Deployment
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
---
Install heroku plugin < mlab > to be able to use iShare.
go to __settings__ in heroku and reveal config, insert MONGODB_URI
in confi vars and add [mongodb URI value], for more information go to [here](https://docs.mlab.com/connecting/#connect-string)

## To Add an Admin
---
sign up as a regular user, then go to mlab, find the user you want to make admin, turn that user __fsr__ from false to true.

## How To Change Email Content Sent To New Users
---
go to myModules>admin>email_services>email_content.html

change email_content.html as you wish.
```html
<h1>Welcome To iShare</h1>
    <section>
        <p>Thank You For Joining The Community, [USER]</p>
        <p> Click here and join our youtube <a href="https://youtube.com">YouTube</a></p>
</section>
```
_NOTE_: ['USER'] will be replaced by the new  user that just signed up and gets the greeting.

## Change About Us
---
go to templates>pages>about.html

change about.html as you please:
```html
{% block body%}
<!-- Write About your website here-->

{% endblock %}
```

## Mannual Installation: _Not__Recommended_ (_NOTE_:You Must deploy to heroku mannually)
---
```bash
    git clone https://github.com/sourenaKhanzadeh/iShare.git
    
    cd iShare
    
    python config.py
```
> 1. run __config.py__ 
> 1. Enter all inputs __config.py__ requires
> 1. _OPTIONAL_: delete __config.py__ 
## Requirements
---
Take a look at ___requirements.txt___
```text
certifi==2019.3.9
chardet==3.0.4
Click==7.0
dnspython==1.16.0
Flask==1.0.3
Flask-SocketIO==4.1.0
gunicorn==19.9.0
idna==2.8
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
pymongo==3.8.0
python-engineio==3.8.1
python-socketio==4.1.0
requests==2.22.0
six==1.12.0
urllib3==1.25.3
Werkzeug==0.15.4

```
The above are the modules you need to install.
install using _pip_
```bash
    pip install -r requirements.txt
```
## manual Heroku Deployement
```bash
  npm install -g heroku
  
  heroku create
  
  heroku git:clone -a [apps_name]
  
  git init
  
  git commit -m "initialize commit"
  
  git push heroku master
  
  heroku open
```
## Tree view
---
* myModules
  * admin
      * email_service
        * admin_email.py
        * email-content.html
      * admin.py
      * delete.py
      * edit.py
      * section.py
   * github
      * github_api.py
      * repos.py
      * users.py
   * model
      * database
        * database.py
        * deleteone.py
        * findone.py
        * insert.py
        * query.py
      * hash.py
      * login.py
      * logout.py
      * signup.py
   * paper_manager
      * detail.py
      * query.py
      * upload.py
   * tools
      * tools.py
   * user
      * delete.py
      * about.py
      * edit.py
      * profile.py
      * settings.py
* static
    * images
      * iShare_logo.png
    * css
      * styleA.css
    * js
      * admin.js
      * discussion.js
      * header.js
      * landing.js
      * query.js
      * settings.js
      * wave.js
    * sass
      * styleA.scss
      * animation.scss
      * constants.scss
      * defaults.scss
      * media.scss
      * mixins.scss
* templates
    * pages
      * admin.html
      * detail.html
      * edit.html
      * landingpage.html
      * login-register.html
      * profile.html
      * query.html
      * settings.html
      * upload.html
      * about.html
    * template
      * footer.html
      * header.html
