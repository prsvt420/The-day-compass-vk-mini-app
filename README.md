# Дневной компас

Это приложение подойдет пользователям, которые ищут вдохновение или советы в повседневной жизни.

## Установка и запуск

**Склонируйте проект:**

```
git clone https://github.com/prsvt420/The-day-compass-vk-mini-app.git
cd The-day-compass-vk-mini-app
```

### Frontend

**1. Установите зависимости**

```
cd frontend/
```

```
npm install
npm install @vkontakte/vk-tunnel --include=dev
```

**2. Запустите мини-приложение локально**

```
cd frontend/
```

```
npm run start -- --host
```

**3. Запустите VK Tunnel**

**Важно!** Откройте ещё одно окно командной строки. Не закрывайте окно, в котором вы запустили сервер мини-приложения локально и не останавливайте работу сервера.

```
cd frontend/
```

```
npm run tunnel
```

После запуска требуется пройти аутентификацию по похожей ссылке:

```
https://user113553650-7743de1d.tunnel.vk-apps.com/
```

После подтверждения доступа требуется нажать Y/y. Если все сделано правильно то вы получите ссылку на мини приложение:

```
https://user113553650-7743de1d.tunnel.vk-apps.com/
```

Ее нужно указать в настройках мини приложения.

### Backend

**Важно!** Перед работой нужно создать файл .env в папке src со следующим содержимым:

```
GIGA_CHAT_AUTHORIZATION_KEY=... [https://developers.sber.ru/dev]
VK_AUTHORIZATION_KEY=... [https://dev.vk.com/ru/]
```

```
cd backend/
```

Создадим Docker образ приложения:

```
docker build -t the-day-compass-vk-mini-app-backend .
```

Запустим контейнер с образом приложения:

```
docker run -p 8000:8000 the-day-compass-vk-mini-app-backend
```


## Makefile

После успешной установки и запуска приложения можно воспользоваться Makefile в корне проекта. Он запустит 3 консольных окна с необходимыми командами для запуска приложения:

```
make run
```