import streamlit as st
import math

st.title("پیدا کردن ب.م.م")
st.write("این برنامه بزرگترین مقسوم‌علیه مشترک چند عدد را محاسبه می‌کند.")

numbers_input = st.text_input("اعداد مورد نظر خود را وارد کرده و با کاما جدا کنید:")

if numbers_input:
    try:
        numbers = [int(n.strip()) for n in numbers_input.split(",")]

        gcd_v = numbers[0]
        for num in numbers[1:]:
            gcd_v = math.gcd(gcd_v,num)

        st.success(f"بزرگ‌ترین مقسوم‌علیه مشترک اعداد {numbers} برابر {gcd_v} است.")
        

    except ValueError:
            st.error("لطفا فقط عدد صحیح وارد کنید و اعداد را با کاما جدا کنید.")