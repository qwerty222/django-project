sudo /etc/init.d/mysql start

mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "GRANT ALL ON qa.* TO 'www-data'@'localhost';"


sudo python /home/box/web/ask/manage.py makemigrations
sudo python /home/box/web/ask/manage.py migrate
