services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: airflow
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
    volumes:
      - postgres-db-volume: /var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U" "airflow"]
      interval: 5s
      timeout: 5
    restart: always

docker run -it \
  -e POSTGRES_DB: "root" \
  -e POSTGRES_USER: "root" \
  -e POSTGRES_PASSWORD: "ny_taxi" \
  -v ny_taxi_postgres_data:/var/lib/postgresql/data

postgres:13