from blog_mehran.wsgi import application

# This is the entry point for Vercel
def handler(request):
    return application(request)
