FROM python:3.10-slim

WORKDIR /app

# Копіюємо ліби та встановлюємо
COPY libs /app/libs
RUN pip install --no-index --find-links=/app/libs /app/libs/*.whl

# Копіюємо весь проєкт
COPY . .

# Робимо копію data.json як шаблону, щоб він завжди був всередині образу
RUN cp data.json data_template.json

# Робимо entrypoint виконуваним
RUN chmod +x entrypoint.sh

EXPOSE 8000

# Замість CMD використовуємо ENTRYPOINT
ENTRYPOINT ["./entrypoint.sh"]