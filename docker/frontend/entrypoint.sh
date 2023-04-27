#!/bin/sh

if [ -f .env ]; then
  ENV_FILE=.env
else
  ENV_FILE=.env.example
fi

touch .env.tmp
VARIABLES=$(awk -F'=' '{print $1}' $ENV_FILE)

for VARIABLE in $VARIABLES; do
  ENV=$(env | grep $VARIABLE)
  if [ -n "$ENV" ]; then
    echo $ENV >> .env.tmp
  else
    echo $(grep $VARIABLE $ENV_FILE) >> .env.tmp
  fi
done

if [ ! -f .env ]; then
  mv .env.tmp .env
else
  echo 'The file .env is existed no changes are made'
  rm .env.tmp
fi

echo -e $RESULT > .env

npm run prod