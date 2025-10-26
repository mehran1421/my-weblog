def handler(request):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html; charset=utf-8',
        },
        'body': '''
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>وبلاگ مهران - تست</title>
    <style>
        body {
            font-family: 'Tahoma', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            direction: rtl;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .success {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            border: 1px solid #c3e6cb;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 تبریک! وبلاگ شما در Vercel کار می‌کند</h1>
        
        <div class="success">
            <strong>✅ استقرار موفقیت‌آمیز بود!</strong><br>
            پروژه Django شما حالا در Vercel در حال اجرا است.
        </div>
        
        <p>این یک صفحه تست ساده است. حالا می‌توانید Django application کامل را راه‌اندازی کنید.</p>
        
        <h2>مراحل بعدی:</h2>
        <ol>
            <li>تنظیم دیتابیس PostgreSQL</li>
            <li>آپلود فایل‌های static به CDN</li>
            <li>تنظیم فایل‌های media در AWS S3</li>
            <li>تنظیم متغیرهای محیطی</li>
        </ol>
    </div>
</body>
</html>
        '''
    }
