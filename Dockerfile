FROM python:3.10

RUN mkdir -p /user/src/app/
WORKDIR /user/src/app/

COPY . /user/src/app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

EXPOSE 80