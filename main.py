import streamlit as st
import math


# تنظیمات پیشرفته CSS برای پشتیبانی کامل از فارسی
st.markdown("""
<style>
    @font-face {
        font-family: 'Vazir';
        src: url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css') format('woff2');
        font-weight: normal;
        font-style: normal;
    }
    
    /* اعمال استایل برای کل صفحه */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Vazir', 'Tanha', 'Segoe UI', Tahoma, sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* تنظیمات برای محتوای اصلی */
    .main .block-container {
        direction: rtl !important;
        text-align: right !important;
        max-width: 95% !important;
        padding: 1rem 0.5rem !important;
    }
    
    /* استایل برای عنوان‌ها */
    h1, h2, h3, h4, h5, h6 {
        text-align: center !important;
        font-family: 'Vazir', 'Tanha', 'Segoe UI', Tahoma, sans-serif !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* استایل برای فیلدهای ورودی */
    div[data-testid="stTextInput"] {
        margin-bottom: 0.5rem !important;
    }
    
    div[data-testid="stTextInput"] > div > div > input {
        direction: rtl !important;
        text-align: right !important;
        padding: 8px 12px !important;
    }
    
    /* استایل برای لیبل فیلدهای ورودی */
    div[data-testid="stTextInput"] > label {
        direction: rtl !important;
        text-align: right !important;
        display: block !important;
        margin-bottom: 0.2rem !important;
        font-weight: bold !important;
        font-size: 14px !important;
    }
    
    /* استایل برای پیام‌های سیستم */
    .stAlert {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Vazir', 'Tanha', 'Segoe UI', Tahoma, sans-serif !important;
        margin-top: 0.5rem !important;
    }
    
    /* کاهش فاصله بین المان‌ها */
    .stMarkdown {
        margin-bottom: 0.2rem !important;
    }
    
    /* استایل برای دکمه‌ها */
    .stButton > button {
        font-family: 'Vazir', 'Tanha', 'Segoe UI', Tahoma, sans-serif !important;
        direction: rtl !important;
        width: 100% !important;
        margin-top: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

# محتوای برنامه
st.markdown("<h1 style='text-align: center; color: #1f77b4; margin-bottom: 0.5rem;'>ماشین حساب ب.م.م</h1>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: right; direction: rtl; margin-bottom: 1rem;'>
<p style='margin-bottom: 0.5rem;'>این برنامه بزرگترین مقسوم‌علیه مشترک (GCD) چند عدد را محاسبه می‌کند.</p>
</div>
""", unsafe_allow_html=True)

# فیلد ورودی
numbers_input = st.text_input(
    "لطفاً اعداد را وارد کنید (با کاما جدا شوند):",
    placeholder="مثال: ۲۴, ۳۶, ۶۰",
    help="اعداد را با کاما از هم جدا کنید"
)

if numbers_input:
    try:
        numbers = [int(n.strip()) for n in numbers_input.split(",")]
        
        gcd_v = numbers[0]
        for num in numbers[1:]:
            gcd_v = math.gcd(gcd_v, num)
            
        # استفاده از markdown به جای success
        st.markdown(f"""
        <div class='stAlert' style='
            background-color: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 0.5rem;
            border: 1px solid #c3e6cb;
            text-align: right;
            direction: rtl;
            margin-bottom: 0;
        '>
            <b>نتیجه:</b><br>
            بزرگترین مقسوم‌علیه مشترک اعداد {numbers} برابر است با {gcd_v}
        </div>
        """, unsafe_allow_html=True)
        
    except ValueError:
        # همین روش برای پیام خطا
        st.markdown("""
        <div class='stAlert' style='
            background-color: #f8d7da;
            color: #721c24;
            padding: 1rem;
            border-radius: 0.5rem;
            border: 1px solid #f5c6cb;
            text-align: right;
            direction: rtl;
            margin-bottom: 0;
        '>
            لطفاً فقط عدد صحیح وارد کنید و اعداد را با کاما از هم جدا کنید.
        </div>
        """, unsafe_allow_html=True)