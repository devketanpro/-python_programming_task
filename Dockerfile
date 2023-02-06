FROM python:3.6
LABEL  Maintainer="devketanpro@me17"
WORKDIR /app
COPY generate_token.py ./
#COPY . ./
CMD ["python", "./generate_token.py" ]