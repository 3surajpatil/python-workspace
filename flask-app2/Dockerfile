FROM python:3.13.2-alpine
# Or any preferred Python version.
WORKDIR /flask-app2
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "flask_app2_service.py"]  
EXPOSE 6153
# Or enter the name of your unique directory and parameter set.