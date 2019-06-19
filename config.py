"""
Run This Script to configure
Admin and create super users
run all the initial settings
"""
import os

# get current location
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

print("""
---------------------
| Welcome to iShare |
---------------------
For more informations go to  https://github.com/sourenaKhanzadeh/iShare

-----------------------------------------------------------------------
    /^\   ---------    ==   ==  ----------   ===========     *========
    \//  / =====\ \\\   ||   ||  | ===  == |  | |  _____  |  ||
    |||   \\\     \_\\\  ||   ||  | ^     ^ |  | |  |   | |   ||
    |||  = \\\          =======  | - (.) - |  | |=========   |========    
    |||  || \\\         =======  |\/\/\/\/\|  | |     \ \    ||
    |||  ||  \\\        ||   ||    \\\   //    | |      \ \   ||
    ===  ======        ==   ==   =========   ===      ===    =========
-----------------------------------------------------------------------
""")
#####################
#   LOCATIONS HERE  #
#####################
EMAIL_SERVICES_LOC = os.path.join(__location__ ,'myModules//admin//email_service//admin_email.py')
LANDING_LOC = os.path.join(__location__ ,'templates//pages//landingpage.html')

admin_email_py = open(EMAIL_SERVICES_LOC).read()
landing_html = open(LANDING_LOC).read()


try:
    title = input("\n\nEnter Your Websites Title: ")

    # replace websites title
    landing_html = landing_html.replace("['Title']", title)


    landing_html_write = open(LANDING_LOC, 'w')
    landing_html_write.write(landing_html)
    landing_html_write.close()

    # input website email and password
    email_services = True if input("Do You Want To Submit The New Users An Email (Y/n): ") == 'Y' else False
    if email_services:
        admin_email = input("Enter Your Websites Email Address: ")
        admin_password = input("Enter Your Websites Email's Password: ")

        # replace websites main Email address and password
        admin_email_py = admin_email_py.replace("['ENTER_USERNAME']", admin_email)
        admin_email_py = admin_email_py.replace("['ENTER_PASSWORD']", admin_password)
    else:
        admin_email_py = admin_email_py.replace("['ENTER_USERNAME']", "")
        admin_email_py = admin_email_py.replace("['ENTER_PASSWORD']", "")

    # overwrite admin_email.py
    admin_email_py_write = open(EMAIL_SERVICES_LOC, 'w')
    admin_email_py_write.write(admin_email_py)
    admin_email_py_write.close()

except Exception as e:
    print("Please Enter The Right Format..... \nError:" + str(e) + '\n')





