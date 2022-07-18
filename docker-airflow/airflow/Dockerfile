FROM python:3.7.7

RUN mkdir /app
WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
ADD requirements-app.txt .
RUN pip install -r requirements-app.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
ENV AIRFLOW_HOME /app
