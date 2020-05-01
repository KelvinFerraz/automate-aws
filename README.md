**Allow mail if use Google Gmail**
https://www.google.com/settings/security/lesssecureapps

# Dependencias Linux
sudo apt install wkhtmltopdf python-pip3 xvfb

# Dependencias pip3
sudo pip3 install -r requiriments.txt

# Create folders
mkdir {img,logs,pdfs}


# Run app
python3 automate.py && python3 sendmail

# Understand code

automate.py = You need configure user and password for take the billings screenshot
sendmail.py = You need configure a user mail and port
