FROM python:3.9-slim

RUN set -x &&\
    apt-get update &&\
    apt-get install -y alien wget libaio1 libtiff5-dev \
	zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev  \
	python-tk python-dev openssl libssl-dev libldap2-dev libsasl2-dev \
	libkrb5-dev sshpass

RUN pip install cx_Oracle

# ORACLE LIB INSTALLATION
RUN wget -P /tmp/ https://download.oracle.com/otn_software/linux/instantclient/19600/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm --no-check-certificate
RUN alien -iv /tmp/oracle-instantclient19.6-basic-19.6.0.0.0-1.x86_64.rpm

ENV ORACLE_HOME=/usr/lib/oracle/19.6/client64
ENV LD_LIBRARY_PATH=$ORACLE_HOME/lib
ENV PATH=$ORACLE_HOME/bin:$PATH

WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt