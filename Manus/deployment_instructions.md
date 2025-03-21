# Deployment Instructions

This document provides detailed instructions for deploying the AI Lead Magnet Platform in various environments, from development to production.

## Local Development Deployment

### Prerequisites

- Python 3.8+
- pip
- Git
- MongoDB (optional, for local data storage)
- Redis (optional, for local caching)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/karatechopping/ai-lead-magnet-platform.git
   cd ai-lead-magnet-platform
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root with the following variables:
   ```
   # OpenAI API
   OPENAI_API_KEY=your_openai_api_key

   # Database Configuration (optional for local development)
   MONGODB_URI=mongodb://localhost:27017/
   REDIS_URL=redis://localhost:6379

   # Application Settings
   DEBUG=True
   PORT=5000
   HOST=0.0.0.0
   ```

5. **Run the application**:
   ```bash
   python prototype/main.py
   ```

6. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

## Basic Production Deployment (Hetzner VPS)

This section covers deploying to a basic Hetzner VPS as mentioned in your requirements.

### Prerequisites

- Hetzner account
- SSH access to your server
- Domain name (optional but recommended)

### Server Setup

1. **Create a Hetzner VPS**:
   - Log in to your Hetzner account
   - Create a new server (CX11 plan is sufficient for starting, ~$7/month)
   - Choose Ubuntu 22.04 as the operating system
   - Set up SSH keys for secure access

2. **Connect to your server**:
   ```bash
   ssh root@your_server_ip
   ```

3. **Update the system**:
   ```bash
   apt update && apt upgrade -y
   ```

4. **Install required packages**:
   ```bash
   apt install -y python3-pip python3-venv nginx git supervisor
   ```

5. **Create a non-root user** (optional but recommended):
   ```bash
   adduser leadmagnet
   usermod -aG sudo leadmagnet
   su - leadmagnet
   ```

### Application Deployment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/karatechopping/ai-lead-magnet-platform.git
   cd ai-lead-magnet-platform
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install gunicorn  # For production serving
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root with production settings:
   ```
   # OpenAI API
   OPENAI_API_KEY=your_openai_api_key

   # Database Configuration
   # For simplicity, you can use SQLite initially
   # For scaling, consider MongoDB Atlas or a managed Redis service

   # Application Settings
   DEBUG=False
   PORT=8000
   HOST=0.0.0.0
   ```

5. **Configure Supervisor**:
   Create a file at `/etc/supervisor/conf.d/leadmagnet.conf`:
   ```
   [program:leadmagnet]
   command=/home/leadmagnet/ai-lead-magnet-platform/venv/bin/gunicorn -w 4 -b 0.0.0.0:8000 prototype.main:app
   directory=/home/leadmagnet/ai-lead-magnet-platform
   user=leadmagnet
   autostart=true
   autorestart=true
   stopasgroup=true
   killasgroup=true
   stderr_logfile=/var/log/leadmagnet/leadmagnet.err.log
   stdout_logfile=/var/log/leadmagnet/leadmagnet.out.log
   ```

   Create log directory:
   ```bash
   sudo mkdir -p /var/log/leadmagnet
   sudo chown -R leadmagnet:leadmagnet /var/log/leadmagnet
   ```

   Update Supervisor:
   ```bash
   sudo supervisorctl reread
   sudo supervisorctl update
   ```

6. **Configure Nginx**:
   Create a file at `/etc/nginx/sites-available/leadmagnet`:
   ```
   server {
       listen 80;
       server_name your_domain.com;  # Or your server IP if no domain

       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

   Enable the site:
   ```bash
   sudo ln -s /etc/nginx/sites-available/leadmagnet /etc/nginx/sites-enabled/
   sudo nginx -t  # Test configuration
   sudo systemctl restart nginx
   ```

7. **Set up SSL with Let's Encrypt** (optional but recommended):
   ```bash
   sudo apt install -y certbot python3-certbot-nginx
   sudo certbot --nginx -d your_domain.com
   ```

8. **Access your application**:
   Open your browser and navigate to `https://your_domain.com` or `http://your_server_ip`

## Docker Deployment

For more scalable deployments, you can use Docker.

### Prerequisites

- Docker
- Docker Compose

### Setup Steps

1. **Create a Dockerfile** in the project root:
   ```dockerfile
   FROM python:3.8-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   CMD ["python", "prototype/main.py"]
   ```

2. **Create a docker-compose.yml** file:
   ```yaml
   version: '3'

   services:
     app:
       build: .
       ports:
         - "5000:5000"
       environment:
         - OPENAI_API_KEY=${OPENAI_API_KEY}
         - DEBUG=False
         - PORT=5000
         - HOST=0.0.0.0
       restart: always
   ```

3. **Build and run the Docker container**:
   ```bash
   docker-compose up -d
   ```

4. **Access the application**:
   Open your browser and navigate to `http://localhost:5000`

## Scaling Considerations

As your user base grows, consider these scaling strategies:

1. **Database Scaling**:
   - Move from local databases to managed services (MongoDB Atlas, AWS RDS)
   - Implement proper indexing and query optimization

2. **Caching**:
   - Use Redis for caching frequent operations
   - Implement CDN for static assets

3. **Horizontal Scaling**:
   - Deploy multiple application instances behind a load balancer
   - Use Kubernetes for container orchestration

4. **AI Cost Optimization**:
   - Implement caching for AI responses
   - Use tiered approach with templates where possible
   - Consider local LLM deployment for certain operations

## Monitoring and Maintenance

1. **Set up monitoring**:
   - Use Prometheus and Grafana for system monitoring
   - Implement application logging with ELK stack or similar

2. **Regular backups**:
   - Set up automated database backups
   - Store backups in a secure, off-site location

3. **Update procedures**:
   - Establish a CI/CD pipeline for smooth updates
   - Implement blue-green deployments to minimize downtime

## Troubleshooting

### Common Issues

1. **Application won't start**:
   - Check logs: `sudo tail -f /var/log/leadmagnet/leadmagnet.err.log`
   - Verify environment variables are set correctly
   - Ensure all dependencies are installed

2. **Database connection issues**:
   - Verify database credentials
   - Check if database service is running
   - Test connection manually

3. **API rate limiting**:
   - Implement proper caching
   - Add retry logic with exponential backoff
   - Consider upgrading API tier

For more detailed troubleshooting, refer to the logs and error messages.
