FROM ubuntu:16.04
FROM python:3.7

WORKDIR    /opt/oracle
RUN        apt-get update && apt-get install -y libaio1 wget unzip \
            && wget https://download.oracle.com/otn_software/linux/instantclient/instantclient-basiclite-linuxx64.zip \
            && unzip instantclient-basiclite-linuxx64.zip \
            && rm -f instantclient-basiclite-linuxx64.zip \
            && cd /opt/oracle/instantclient* \
            && rm -f *jdbc* *occi* *mysql* *README *jar uidrvci genezi adrci \
            && echo /opt/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
            && ldconfig
           
RUN curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN docker-compose --version
RUN pip install cx_Oracle

ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
