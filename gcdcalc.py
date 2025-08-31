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
    
    .stTextInput > div > div > input {
        direction: rtl;
        text-align: right;
    }
    
    .stAlert {
        direction: rtl;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# استفاده از markdown برای تمام متون فارسی
st.markdown("<h1 style='text-align: right; direction: rtl;'>پیدا کردن ب.م.م</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right; direction: rtl;'>این برنامه بزرگترین مقسوم‌علیه مشترک چند عدد را محاسبه می‌کند.</p>", unsafe_allow_html=True)

numbers_input = st.text_input(":اعداد مورد نظر خود را وارد کرده و با کاما جدا کنید")

if numbers_input:
    try:
        numbers = [int(n.strip()) for n in numbers_input.split(",")]
        
        gcd_v = numbers[0]
        for num in numbers[1:]:
            gcd_v = math.gcd(gcd_v, num)
            
        st.success(f"بزرگ‌ترین مقسوم‌علیه مشترک اعداد {numbers} برابر {gcd_v} است.")
    
    except ValueError:
        st.error("لطفا فقط عدد صحیح وارد کنید و اعداد را با کاما جدا کنید.")
