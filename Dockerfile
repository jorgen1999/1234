FROM python:3.11-rc-bullseye
# The following configuration tells django to
# writes to the terminal in real time.
# In this situation the output will not be buffered anywhere

ENV PYTHONUNBUFFERED 1

# The following configuration is used to
# creates a new folder in your container.
# The folder will be the project's root folder
# inside the container.
# The folder will be used as the work directory
# subsequent commands.

WORKDIR /mysite.

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations mysite
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
