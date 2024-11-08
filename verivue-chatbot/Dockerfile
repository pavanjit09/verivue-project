# Laravel Dockerfile
FROM php:8.1-fpm

# Set the working directory inside the container
WORKDIR /var/www/html

# Copy all project files to the container
COPY . .

# Install required extensions
RUN apt-get update && apt-get install -y libonig-dev libzip-dev unzip \
    && docker-php-ext-install pdo mbstring zip

# Expose port 8000 (Laravel default)
EXPOSE 8000

# Run Laravel server
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
