# راهنمای استقرار پروژه Django در Vercel

## فایل‌های ایجاد شده برای استقرار:

### 1. `vercel.json`
فایل پیکربندی اصلی Vercel که شامل:
- تنظیمات build
- مسیریابی درخواست‌ها
- متغیرهای محیطی

### 2. `api/index.py`
نقطه ورود اصلی برای Vercel که WSGI application را فراخوانی می‌کند.

### 3. `blog_mehran/settings_production.py`
تنظیمات Django برای محیط production شامل:
- DEBUG = False
- ALLOWED_HOSTS = ['*']
- تنظیمات امنیتی
- غیرفعال کردن Celery (چون Vercel serverless است)

### 4. `build.sh`
اسکریپت build که شامل:
- نصب dependencies
- جمع‌آوری فایل‌های static
- اجرای migrations

### 5. `.vercelignore`
فایل‌هایی که نباید در Vercel آپلود شوند.

## مراحل استقرار:

### 1. نصب Vercel CLI
```bash
npm i -g vercel
```

### 2. ورود به Vercel
```bash
vercel login
```

### 3. استقرار پروژه
```bash
vercel
```

### 4. تنظیم متغیرهای محیطی (اختیاری)
```bash
vercel env add SECRET_KEY
```

## نکات مهم:

1. **دیتابیس**: در حال حاضر از SQLite استفاده می‌شود. برای production بهتر است از PostgreSQL استفاده کنید.

2. **فایل‌های Media**: فایل‌های آپلود شده باید در سرویس‌های خارجی مثل AWS S3 یا Cloudinary ذخیره شوند.

3. **Celery**: برای background tasks در Vercel باید از سرویس‌های خارجی استفاده کنید.

4. **Static Files**: فایل‌های static باید در CDN ذخیره شوند.

## مشکلات احتمالی و راه‌حل:

### مشکل: فایل‌های static لود نمی‌شوند
**راه‌حل**: از سرویس‌های CDN مثل Cloudflare یا AWS CloudFront استفاده کنید.

### مشکل: دیتابیس SQLite کار نمی‌کند
**راه‌حل**: از PostgreSQL با سرویس‌هایی مثل Supabase یا PlanetScale استفاده کنید.

### مشکل: فایل‌های media آپلود نمی‌شوند
**راه‌حل**: از AWS S3 یا Cloudinary برای ذخیره فایل‌ها استفاده کنید.

## دستورات مفید:

```bash
# مشاهده لاگ‌ها
vercel logs

# مشاهده اطلاعات پروژه
vercel inspect

# حذف پروژه
vercel remove
```
