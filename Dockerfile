FROM python:3.7
WORKDIR /app
ADD animal_bot.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ["python3", "animal_bot.py"]
