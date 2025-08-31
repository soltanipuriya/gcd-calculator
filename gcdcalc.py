import streamlit as st
import math

# تنظیمات کلی صفحه برای پشتیبانی از فارسی
st.markdown("""
<style>
    @font-face {
        font-family: 'Vazir';
        src: url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v30.1.0/dist/Vazir.woff2') format('woff2');
    }
    
    * {
        font-family: 'Vazir', 'Tanha', 'Segoe UI', Tahoma, sans-serif !important;
    }
    
    .main .block-container {
        direction: rtl;
        text-align: right;
    }
    
    /* استایل مخصوص فیلدهای ورودی */
    div[data-testid="stTextInput"] > div > div > input {
        direction: rtl;
        text-align: right;
        padding: 8px 12px;
    }
    
    /* استایل مخصوص لیبل فیلدهای ورودی */
    div[data-testid="stTextInput"] > label {
        direction: rtl;
        text-align: right;
        display: block;
        margin-bottom: 5px !important; /* کاهش فاصله */
        font-weight: bold;
    }
    
    /* کاهش فاصله کلی بین المان‌ها */
    .stTextInput {
        margin-bottom: 10px !important;
    }
    
    .stAlert {
        direction: rtl;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# عنوان برنامه
st.markdown("<h1 style='text-align: right; direction: rtl; margin-bottom: 30px;'>پیدا کردن ب.م.م</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right; direction: rtl; margin-bottom: 20px;'>این برنامه بزرگترین مقسوم‌علیه مشترک چند عدد را محاسبه می‌کند.</p>", unsafe_allow_html=True)

# فیلد ورودی با استایل بهبود یافته
numbers_input = st.text_input(
    "اعداد مورد نظر خود را وارد کرده و با کاما جدا کنید:",
    help="مثال: ۲۴, ۳۶, ۶۰"
)

if numbers_input:
    try:
        numbers = [int(n.strip()) for n in numbers_input.split(",")]
        
        gcd_v = numbers[0]
        for num in numbers[1:]:
            gcd_v = math.gcd(gcd_v, num)
            
        st.success(f"بزرگ‌ترین مقسوم‌علیه مشترک اعداد {numbers} برابر {gcd_v} است.")
    
    except ValueError:
        st.error("لطفا فقط عدد صحیح وارد کنید و اعداد را با کاما جدا کنید.")
