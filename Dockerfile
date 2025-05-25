FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /user_balance
COPY requirements.txt /user_balance

RUN pip install --upgrade pip
RUN pip install -r /user_balance/requirements.txt

COPY . /user_balance

EXPOSE 8000

CMD ["python", "manage.py runserver 0.0.0.0:8000"]