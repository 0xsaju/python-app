from setuptools import setup, find_packages

setup(
    name='user-management-service',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'gunicorn',
    ],
    entry_points={
        'console_scripts': [
            'run-app=app:create_app',
        ],
    },
)