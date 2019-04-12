sudo apt-get update
sudo apt-get install -f python3.5
sudo curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python3.5 get-pip.py
sudo pip install django
sudo pip install gunicorn
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
# sudo gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application &
gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application