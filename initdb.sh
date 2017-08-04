sudo /etc/init.d/mysql start

mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'pass123';
				 GRANT ALL ON qa.* TO 'django'@'localhost';"

sudo python /home/box/web/ask/manage.py makemigrations
sudo python /home/box/web/ask/manage.py makemigrations
