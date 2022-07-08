FROM --platform=linux/amd64 python:3.10.4-slim

RUN mkdir /home/FastAPIStore

WORKDIR /home/FastAPIStore

RUN apt-get -y update && apt-get install -y gnupg
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y gcc g++ unixodbc-dev unixodbc freetds-dev freetds-common freetds-bin tdsodbc

RUN apt-get install -y curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get -y update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17=17.7.1.1-1
RUN apt-get install apt-transport-https -y
RUN apt-get install libssl1.0 libssl-dev -y

COPY requirements.txt /home/FastAPIStore/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /home/FastAPIStore/requirements.txt

EXPOSE 8000

COPY . /home/FastAPIStore

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5700"]