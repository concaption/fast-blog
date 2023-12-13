### FastAPI Blog 🔥

#### Introduction
Welcome to the FastAPI Blog 🔥 - a modern, fast (high-performance) blogging platform built with FastAPI and SQLAlchemy. This application provides a robust backend system for blog management, offering features like user authentication, blog creation, updating, deletion, and real-time blog updates.

#### Features
- **User Authentication**: Secure login system to access token-based authentication.
- **Blog Management**: Create, read, update, and delete (CRUD) functionalities for blog posts.
- **Real-Time Updates**: Leverage FastAPI's capability for real-time communication.
- **Data Validation**: Comprehensive validation for user inputs to maintain data integrity.
- **Scalable Architecture**: Designed to be easily scalable for future enhancements.

#### Endpoints
The application exposes several endpoints:

1. **Token**:
   - `POST /token`: User authentication to receive an access token.

2. **Users**:
   - `POST /users/`: Create a new user account.

3. **Blogs**:
   - `GET /blogs/`: Retrieve all blogs.
   - `POST /blogs/`: Create a new blog post.
   - `GET /blogs/{id}`: Get a specific blog post.
   - `PUT /blogs/{id}`: Update a specific blog post.
   - `DELETE /blogs/{id}`: Delete a specific blog post.

4. **Home**:
   - `GET /`: A simple endpoint to confirm the API is operational.

#### How to Run

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/concaption/fast-blog)


1. **Prerequisites**: Ensure you have Python and pip installed.
2. **Installation**: Clone the repository and install dependencies.
   ```bash
   git clone https://github.com/concaption/fast-blog
   cd fast-blog
   make
   ```
3. **Run the Application**: Start the FastAPI server.
   ```bash
   make run
   ```
4. **Access Swagger UI**: Navigate to `http://localhost:8000/docs` to access the Swagger UI for API interaction.

#### Technology Stack
- **FastAPI**: High-performance web framework for building APIs.
- **SQLAlchemy**: SQL toolkit and ORM for database interactions.
- **SQLite**: Database engine for development.
- **Uvicorn**: ASGI server for running FastAPI.

#### Security
The application uses OAuth2 password flow for secure access. Passwords are hashed and tokens are used for secure API access.

#### Future Enhancements
- Adding more interactive features with WebSockets.
- Implementing advanced user roles and permissions.

#### Contributions
Contributions to the FastAPI Blog 🔥 are welcome! Please read the contribution guidelines before making a pull request.

#### License
[MIT License](LICENSE.txt)

#### Contact
For any queries or feedback, please reach out to concaption@gmail.com.
