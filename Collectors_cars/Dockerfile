FROM python:3.12.0-bookworm
WORKDIR /opt/app
COPY ./Collectors_cars/ .
COPY ./requirements.txt .
RUN ls -lh
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8000
CMD ["python3",  "./manage.py" , "runserver", "0.0.0.0:8000"]