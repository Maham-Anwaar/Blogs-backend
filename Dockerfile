###########
# BUILDER #
###########

FROM python:3.11-alpine as builder

LABEL maintatiner='Carte Blanche'

WORKDIR /home/app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /home/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.11-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV APP_HOME=/home/app
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/scripts
RUN mkdir $APP_HOME/mediafiles
RUN mkdir $APP_HOME/code

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /home/app/wheels /wheels
COPY --from=builder /home/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./scripts $APP_HOME/scripts
RUN sed -i 's/\r$//g'  $APP_HOME/scripts/entrypoint.sh
RUN chmod +x  $APP_HOME/scripts/entrypoint.sh

# copy project
COPY ./app $APP_HOME/code
WORKDIR $APP_HOME/code

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/scripts/entrypoint.sh"]
