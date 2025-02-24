FROM python:3.6
MAINTAINER Ashok Bollepalli "pavan"
COPY . /flasktest.py
WORKDIR /flasktest.py
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "flasktest.py"]
