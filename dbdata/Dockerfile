FROM postgres:latest

# Set environment variables
ENV POSTGRES_DB=social
ENV POSTGRES_USER=parthasamanta
ENV POSTGRES_PASSWORD=12098

# Add initialization script to create the database and user
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432
