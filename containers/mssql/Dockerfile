FROM mcr.microsoft.com/mssql/server
EXPOSE 1433

USER root

COPY ./scripts /usr/src/app
WORKDIR /usr/src/app

ENV ACCEPT_EULA Y
ENV SA_PASSWORD Passw0rd

RUN chmod +x ./initialize.sh
RUN chmod +x ./entrypoint.sh

USER mssql
# ENTRYPOINT /bin/bash ./entrypoint.sh
CMD [ "./entrypoint.sh" ]