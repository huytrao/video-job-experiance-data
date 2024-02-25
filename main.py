import os
import streamlit as st
from google.cloud import storage
from google.oauth2 import service_account
import json
import pandas as pd

html_code = """
<iframe src="https://googlehackathondemo.h5p.com/content/1292202083548551859/embed" width="1089" height="674" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *" aria-label="Gôd"></iframe><script src="https://googlehackathondemo.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
"""
# Phần nút chọn
st.header("Chọn nghề nghiệp bạn muốn trải nghiệm")
software_engineer_button = st.button("Software Engineer")
doctor_button = st.button("Doctor")

# Xử lý sự kiện khi nút được ấn
if doctor_button:
    st.write("Đang cập nhật")
elif software_engineer_button:
    st.write("Bạn đã chọn Software Engineer")
    st.markdown(html_code, unsafe_allow_html=True)
    import plotly.express as px

    # # Kết nối tới google storage


    # from google.cloud import storage

    # # Tạo client của Google Storage
    # client = storage.Client()

    # # Định danh bucket và đường dẫn tới file trên Google Storage
    # bucket_name = 'your-bucket-name'
    # file_name = 'output.csv'

    # # Lấy đối tượng bucket
    # bucket = client.get_bucket(bucket_name)

    # # Lấy đối tượng blob (file) từ bucket
    # blob = bucket.blob(file_name)

    # # Tạo một temporary file để lưu nội dung của file từ Google Storage
    # temp_file = '/path/to/temp/file.csv'

    # # Tải nội dung của file từ Google Storage vào temporary file
    # blob.download_to_filename(temp_file)

    # # Đọc file CSV bằng pandas
    # data = pd.read_csv(temp_file)

    # dữ liệu mẫu 

    data = {
        'Job Title': ['Software Engineer', 'Software Engineer', 'Senior Software Engineer', 'Software Developer', 'Junior Software Engineer', 'Software Engineer', 'Senior Software Engineer', 'Software Developer', 'Software Engineer', 'Junior Software Engineer'],
        'Company': ['ABC Tech', 'XYZ Corp', 'DEF Solutions', '123 Software', 'ABC Tech', 'DEF Solutions', 'ABC Tech', 'XYZ Corp', '123 Software', 'XYZ Corp'],
        'Experience (Years)': [2, 3, 5, 1, 1, 4, 7, 2, 3, 2],
        'Salary ($)': [60000, 65000, 80000, 55000, 50000, 70000, 95000, 60000, 65000, 55000]
    }

    df = pd.DataFrame(data)

    # Tiêu đề
    st.title('Dữ liệu ủa ')

    # Hiển thị bảng dữ liệu
    st.subheader('Dữ liệu Job')
    st.dataframe(df)

    # Đồ thị phân phối kinh nghiệm
    st.subheader('Phân phối Kinh Nghiệm')
    fig_experience = px.histogram(df, x='Experience (Years)', nbins=10, title='Phân phối Kinh Nghiệm')
    st.plotly_chart(fig_experience)

    # Đồ thị biểu đồ tròn theo công ty
    st.subheader('Tỉ lệ Làm Việc ở Các Công Ty')
    fig_company = px.pie(df, names='Company', title='Tỉ lệ Làm Việc ở Các Công Ty')
    st.plotly_chart(fig_company)

    # Đồ thị biểu đồ scatter theo kinh nghiệm và lương
    st.subheader('Mối quan hệ giữa Kinh Nghiệm và Lương')
    fig_salary_experience = px.scatter(df, x='Experience (Years)', y='Salary ($)', color='Job Title', size='Salary ($)', title='Mối quan hệ giữa Kinh Nghiệm và Lương')
    st.plotly_chart(fig_salary_experience)

    ## ở đây sẽ có một hàm xữ lí dữ liệu AI của google 

    
    
    

# Chức năng xử lý tệp tin được kéo và thả
uploaded_file = st.file_uploader("Bạn muốn đóng góp video nghề nghiệp. Kéo và thả file mp4 vào đây")

if uploaded_file is not None:
        # Phần up video
    st.header("Up video")
    with open('credentials.json') as json_file:
        credentials_info = json.load(json_file)

    credentials = service_account.Credentials.from_service_account_info(credentials_info)
    client = storage.Client(credentials=credentials)

    # Đọc file JSON
    # Khởi tạo client của Google Cloud Storage
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"]
    )
    client = storage.Client(credentials=credentials)

    # Tạo bucket trong Google Cloud Storage (nếu chưa tồn tại)
    bucket_name = "your_bucket_name"
    bucket = client.create_bucket(bucket_name)

    # Tạo tên tệp tin trong bucket
    file_name = f"video_{uploaded_file.name}"

    # Tải lên tệp tin lên Google Cloud Storage
    blob = bucket.blob(file_name, chunk_size=1024 * 1024)
    blob.upload_from_file(uploaded_file, rewind=True)

    # In thông báo khi tệp tin đã được tải lên thành công
    st.write("Tệp tin đã được tải lên thành công.")
    st.write(f"Tên tệp tin: {file_name}")
    st.write(f"Dung lượng tệp tin: {os.path.getsize(uploaded_file.name)} bytes")
    st.write("Đường dẫn tới tệp tin trên Google Cloud Storage:")
    st.write(blob.public_url)

