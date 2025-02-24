FROM python:3.6
COPY . /flasktest.py
WORKDIR /flasktest.py
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "flasktest.py"]
