# Hospital API

Aim - Build a secure Hospital Managment REST API using Flask that supports RBAC.

- The system should manage hospital information and user accounts with distinct roles(admin, user). [DONE]
- Admins can create, read, update and delete Hospital records. [DONE]

- Regular user can only see and filter hospital store inforamtion. [DONE]
- The system must use JWT for authentication and SQL Alchemy for ORM. [DONE]
- Filtering and pagination should be also included. [DONE]

- Added DB Migration. [DONE]
- Added URl for adding stores, fetch specific stores. Dont allow duplicate entries. [DONE]
- Hospital search functionality [DONE]
- Add token blacklisting (logout/revoke support) [DONE]
- Add “Forgot Password” endpoint [DONE]
- Send reset link/token to email (mock the email part for now) [DONE]
- Prevent brute-force attacks using Flask-Limiter [DONE Learnt Not Implemented now]
- Add relationships: e.g., one Hospital has many Doctors, add another role as doctor [DONE]
- Cache common queries (e.g., hospital list)
- Use joinedload() from SQLAlchemy to avoid redundant DB hits
- Use Flask-Uploads or Flask-S3 to support file uploads
- Use pytest to test models, views, and JWT flow
- Use coverage.py to check what % of code is tested
- Create Dockerfile and docker-compose.yml, Include MySQL in docker-compose.
- Create GraphQL API.
- API Versioing.
- Deploy it on Render.
- Containerize the application.
