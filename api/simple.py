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
    <title>وبلاگ مهران</title>
    <style>
        body {
            font-family: Tahoma, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            direction: rtl;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        .success {
            background: #d4edda;
            color: #155724;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 1px solid #c3e6cb;
            text-align: center;
        }
        .info {
            background: #d1ecf1;
            color: #0c5460;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 1px solid #bee5eb;
        }
        .steps {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        .steps ol {
            padding-right: 20px;
        }
        .steps li {
            margin: 10px 0;
            line-height: 1.6;
        }
        .emoji {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1><span class="emoji">🎉</span> تبریک! وبلاگ شما در Vercel کار می‌کند</h1>
        
        <div class="success">
            <strong><span class="emoji">✅</span> استقرار موفقیت‌آمیز بود!</strong><br>
            پروژه Django شما حالا در Vercel در حال اجرا است.
        </div>
        
        <div class="info">
            <strong><span class="emoji">📝</span> نکات مهم:</strong><br>
            • این یک نسخه ساده است<br>
            • برای استفاده کامل، باید دیتابیس و فایل‌های static را تنظیم کنید<br>
            • فایل‌های media باید در سرویس‌های خارجی ذخیره شوند
        </div>
        
        <div class="steps">
            <h2><span class="emoji">🚀</span> مراحل بعدی:</h2>
            <ol>
                <li><strong>تنظیم دیتابیس PostgreSQL:</strong> از سرویس‌هایی مثل Supabase یا PlanetScale استفاده کنید</li>
                <li><strong>آپلود فایل‌های static به CDN:</strong> از Cloudflare یا AWS CloudFront استفاده کنید</li>
                <li><strong>تنظیم فایل‌های media در AWS S3:</strong> برای ذخیره تصاویر و فایل‌ها</li>
                <li><strong>تنظیم متغیرهای محیطی:</strong> SECRET_KEY، DATABASE_URL و غیره</li>
                <li><strong>تنظیم دامنه سفارشی:</strong> برای دسترسی آسان‌تر</li>
            </ol>
        </div>
        
        <div class="info">
            <strong><span class="emoji">🔗</span> لینک‌های مفید:</strong><br>
            • <a href="https://vercel.com/docs" target="_blank">مستندات Vercel</a><br>
            • <a href="https://docs.djangoproject.com/" target="_blank">مستندات Django</a><br>
            • <a href="https://supabase.com/" target="_blank">Supabase (دیتابیس)</a>
        </div>
        
        <div class="success">
            <strong><span class="emoji">🎯</span> وضعیت فعلی:</strong><br>
            پروژه شما با موفقیت در Vercel استقرار یافت و محافظت غیرفعال شد!
        </div>
    </div>
</body>
</html>
        '''
    }
