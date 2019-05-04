from setuptools import setup, find_packages

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),       # find package directories automatically
    include_package_data=True,      # include other files listed in MANIFEST.in
    zip_safe=False,
    install_requires=[
        'flask', 'flask-sqlalchemy', 'flask-migrate', 'flask-login'
    ]
)
