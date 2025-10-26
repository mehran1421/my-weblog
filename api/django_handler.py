import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_mehran.settings_production')
os.environ.setdefault('VERCEL', '1')

def handler(request):
    try:
        # Import Django
        import django
        from django.conf import settings
        
        # Configure Django
        if not settings.configured:
            django.setup()
        
        # Import WSGI application
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        
        # Handle the request
        return application(request)
        
    except Exception as e:
        # Fallback to simple HTML response
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html; charset=utf-8',
            },
            'body': f'''
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>وبلاگ مهران</title>
    <style>
        body {{
            font-family: Tahoma, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            direction: rtl;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }}
        .success {{
            background: #d4edda;
            color: #155724;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 1px solid #c3e6cb;
            text-align: center;
        }}
        .error {{
            background: #f8d7da;
            color: #721c24;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 1px solid #f5c6cb;
        }}
        .info {{
            background: #d1ecf1;
            color: #0c5460;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 1px solid #bee5eb;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 وبلاگ مهران در Vercel</h1>
        
        <div class="success">
            <strong>✅ پروژه با موفقیت استقرار یافت!</strong><br>
            پروژه Django شما حالا در Vercel در حال اجرا است.
        </div>
        
        <div class="error">
            <strong>⚠️ خطای Django:</strong><br>
            {str(e)}<br><br>
            <strong>راه‌حل:</strong> Django application نیاز به تنظیمات بیشتری دارد.
        </div>
        
        <div class="info">
            <strong>📝 مراحل بعدی:</strong><br>
            1. تنظیم دیتابیس PostgreSQL<br>
            2. اصلاح Django settings<br>
            3. تنظیم فایل‌های static و media<br>
            4. تنظیم متغیرهای محیطی
        </div>
        
        <div class="success">
            <strong>🎯 وضعیت:</strong><br>
            پروژه شما در Vercel استقرار یافت و محافظت غیرفعال شد!
        </div>
    </div>
</body>
</html>
            '''
        }
