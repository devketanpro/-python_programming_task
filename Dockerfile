FROM python:3.6
# install python requirements
RUN pip install --upgrade pip
RUN pip install pip-tools  # for building new requirements.txt files

# copy just requirements and install before rest of code to avoid having to
# reinstall packages during build every time code changes
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip install -r requirements.txt
LABEL  Maintainer="devketanpro@me17"
WORKDIR /app
COPY generate_token.py ./
#COPY . ./
CMD ["python", "./generate_token.py" ]