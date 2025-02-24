# Step 1 - Build React frontend
FROM node:18 AS builder

WORKDIR /app/src/frontend
COPY ./src/frontend .

RUN npm install && npm run build


# Step 2 - Serve with Flask
FROM python:3.10-alpine
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./src/backend /app/src/backend
COPY --from=builder /app/src/frontend /app/src/frontend

EXPOSE 5000

WORKDIR /app/src/backend
CMD ["gunicorn", "-b", ":5000", "wsgi"] 
