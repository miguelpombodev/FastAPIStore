FROM mcr.microsoft.com/mssql/server:2017-latest
EXPOSE 1433


COPY ./scripts /usr/src/app
WORKDIR /usr/src/app

ENV ACCEPT_EULA Y
ENV SA_PASSWORD P@ssw0rd

RUN chmod +x ./entrypoint.sh

CMD [ "./entrypoint.sh" ]