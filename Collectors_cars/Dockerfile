FROM python 3.11 alpine
WORKDIR /collectors_cars
COPY ./ /collectors_cars
RUN apk update && pip install -r ../requirements.txt --no-cache-dir
EXPOSE 8000
CWD ["python3",  "manage.py" , "runserver", "0.0.0.0:8000"]
