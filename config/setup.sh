sudo apt-get install uwsgi nginx uwsgi-plugin-python
sudo ln -s /home/zarik/web/django_projects/cms_ve/cms_usadba/config/nginx/cms_usadba.conf /etc/nginx/sites-enabled/
sudo ln -s /home/zarik/web/django_projects/cms_ve/cms_usadba/config/uwsgi/usadbacms.ini /etc/uwsgi/apps-enabled/
sudo service nginx restart
sudo service uwsgi restart
