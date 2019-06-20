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
LANDING_LOC = os.path.join(__location__ ,'templates//pages//landingpage.html')

landing_html = open(LANDING_LOC).read()


try:
    title = input("\n\nEnter Your Websites Title: ")

    # replace websites title
    landing_html = landing_html.replace("['Title']", title)


    landing_html_write = open(LANDING_LOC, 'w')
    landing_html_write.write(landing_html)
    landing_html_write.close()


except Exception as e:
    print("Please Enter The Right Format..... \nError:" + str(e) + '\n')





