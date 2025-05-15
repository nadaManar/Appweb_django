1-email et nom prenom des participantes. 
---------------------------------------------
okba,               salma    ,    salma.okba@etu.univ-orleans.fr;
Manar,              Nada      ,   nada.manar@etu.univ-orleans.fr;
EL Madani,          Amina    ,   amina.el-madani@etu.univ-orleans.fr
Bounadi,            fatima     ,  fatima.bounadi@etu.univ-orleans.fr;



2- les commandes utilisées.
Questions1:
django-admin startproject ct
python3  manage.py startapp uo

Question3:
python3 manage.py createsuperuser (username:group21 , password:group21)
python3 manage.py runserver

quiestion4:
python3  manage.py dumpdata auth.user --indent 2 > uo/fixtures/enseignant.json
python3  manage.py migrate

Question 6:
python3 manage.py dumpdata uo.Formation --indent 2 > uo/fixtures/formations.json
python3 manage.py loaddata formation
Question7:
python3 manage.py makemigrations
python3 manage.py migrate
Question 8:
 python3  manage.py dumpdata uo.UE --indent 2 > uo/fixtures/ue.json
 utilisation de la commande dumpdata pour faire remplir le ue.json 
 python3 manage.py loaddata ue
 utilisation de la commande loaddata pour remplir la table uo_ue dans la base