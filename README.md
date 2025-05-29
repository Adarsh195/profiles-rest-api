# Profiles REST API

## Description
A REST API for managing user profiles. This project allows users to create, update, retrieve, and manage user profiles with authentication. Built using Django REST Framework.

## Features
- User profile creation and management
- User authentication
- Profile status updates
- Permission-based access control
- Browsable API

## Technology Stack
- Python
- Django
- Django REST Framework
- SQLite (development)
- Vagrant (development environment)

## Prerequisites
- Python 3.6+
- pip
- Virtualenv (recommended)
- Vagrant and VirtualBox (for development environment)

## Installation

### Local Development
1. Clone the repository
   ```bash
   git clone https://github.com/adarshsinghai/profiles-rest-api.git
   cd profiles-rest-api
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations
   ```bash
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

### Using Vagrant
1. Clone the repository
   ```bash
   git clone https://github.com/adarshsinghai/profiles-rest-api.git
   cd profiles-rest-api
   ```

2. Start the Vagrant environment
   ```bash
   vagrant up
   ```

3. SSH into the Vagrant machine
   ```bash
   vagrant ssh
   ```

4. Navigate to the project directory
   ```bash
   cd /vagrant
   ```

5. Start the development server
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## API Endpoints

- `/api/profile/` - List all user profiles
- `/api/profile/<profile_id>/` - Retrieve specific profile
- `/api/login/` - User authentication
- `/api/feed/` - Profile status updates

## Usage Examples

### Creating a new profile
```bash
curl -X POST http://localhost:8000/api/profile/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","name":"Test User","password":"testpassword"}'
```

### Authentication
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpassword"}'
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Django REST Framework documentation
- Python Django community
