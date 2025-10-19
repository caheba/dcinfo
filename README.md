# dcinfo
DCInfo - a DataCenter Info tool - manage projects and changes based on your assets

for an initial setup, pleaste find file "setup_dci_env.sh"  
### actual status
downloading the main branch does NOT mean, that this application is running. Tha ctual state is: in deployment.
once, I have a stabile version, I will do further deployment in a different branch and keep up with versioning.  
But for now: It is only testing!  
Dont use this app in production!

## Python version
Actually, we use python 3.13 (check with python -V). But all 3.x versions should work fine.
Older 2.x Versions will not work propperly.

## Django version
dcinfo is based on Django 5

## Production environment
Starting the application will cause a warning:  
WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.  
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/   

