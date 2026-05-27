import streamlit as st
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter
import re
import io

st.set_page_config(page_title="PDF Voucher 去重工具")

st.title("📄 PDF Voucher 去重工具")

uploaded_file = st.file_uploader("上传 PDF", type=["pdf"])

pattern = re.compile(r"Voucher_No\s*:\s*(\d+)")

if uploaded_file:

    reader = PdfReader(uploaded_file)
    writer = PdfWriter()

    seen = set()

    progress = st.progress(0)
    total_pages = len(reader.pages)

    with pdfplumber.open(uploaded_file) as pdf:

        for i in range(total_pages):

            page = pdf.pages[i]
            text = page.extract_text()

            if text:
                match = pattern.search(text)

                if match:
                    voucher = match.group(1)

                    if voucher not in seen:
                        writer.add_page(reader.pages[i])
                        seen.add(voucher)

            progress.progress((i + 1) / total_pages)

    output = io.BytesIO()
    writer.write(output)
    output.seek(0)

    st.success("处理完成")

    st.download_button(
        "⬇️ 下载去重 PDF",
        data=output,
        file_name="deduped.pdf",
        mime="application/pdf"
    )
