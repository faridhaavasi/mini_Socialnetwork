FROM python:latest
WORKDIR src/
COPY requirments.txt src
COPY . src
EXPOSE 8000
RUN pip install -r requirments.txt
CMD ['python', 'manage.py makemigrations', 'manage.py migrate', 'manage.py runserver 0000:8000']


