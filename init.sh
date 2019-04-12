  git clone https://github.com/Dmitry-Raskovalov/stepic-web-project.git
  sudo apt remove python-django -y
  sudo apt remove gunicorn -y
  sudo apt update
  sudo apt install python3-pip
  pip3 install Django==2.0.0
  pip3 install gunicorn
  sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
  sudo rm -rf /etc/nginx/sites-enabled/default
  sudo /etc/init.d/nginx restart
  sudo gunicorn -c /home/box/web/etc/gunicorn-hello.conf hello:application
  sudo gunicorn -c /home/box/web/etc/gunicorn-django.conf ask.wsgi:application
