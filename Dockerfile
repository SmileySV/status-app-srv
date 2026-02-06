# Вихідний образ — легкий Nginx
FROM nginx:alpine

# Видаляємо дефолтну сторінку nginx
RUN rm -rf /usr/share/nginx/html/*

# Копіюємо ВСІ файли з поточної папки (index, setStatus, data.json, images)
# Це набагато зручніше, ніж прописувати кожен файл окремо
COPY . /usr/share/nginx/html/

# Виставляємо порт
EXPOSE 80

# Запускаємо nginx
CMD ["nginx", "-g", "daemon off;"]