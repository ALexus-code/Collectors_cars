FROM python:3.12.0-bookworm
WORKDIR /Collectors_cars
COPY ./ /Collectors_cars
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8000
CMD ["python3",  "manage.py" , "runserver", "0.0.0.0:8000"]