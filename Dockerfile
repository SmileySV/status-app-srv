# Вихідний образ — легкий Nginx
FROM nginx:alpine

# Видаляємо дефолтну сторінку nginx
RUN rm /usr/share/nginx/html/*

# Копіюємо нашу сторінку у контейнер
COPY index.html /usr/share/nginx/html/

# Виставляємо порт, який використовує Nginx
EXPOSE 80

# Запускаємо nginx у foreground (щоб контейнер не закрився)
CMD ["nginx", "-g", "daemon off;"]
