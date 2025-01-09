import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write("## ☝️⬇️")
    with open('template.xlsx', 'rb') as f:
        st.download_button(
            label='下載範本',
            data=f,
            file_name='長文本工作表+關鍵字對照表（範本）.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

with col2:
    st.write("## ✌️⬆️")
    uploaded_file = st.file_uploader(
        label='編輯後上傳',
        type=['xlsx', 'xls'],
        # help='Upload your Excel file here'
    )

with col3:
    st.write("## ⏳")
#     if uploaded_file is not None:
#         st.write("→")
#         st.write("## Step 3: Download Result")
#         # Read the uploaded file
#         uploaded_df = pd.read_excel(uploaded_file)

#         # Process the uploaded file (e.g., add a new column)
#         uploaded_df['New Column'] = 'Result'

#         # Create a download button for the result
#         with st.container():
#             @st.cache
#             def convert_df(df):
#                 return df.to_excel(index=False)

#             csv = convert_df(uploaded_df)
#             st.download_button(
#                 label='Download Result',
#                 data=csv,
#                 file_name='result.xlsx',
#                 mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#             )
#     else:
#         st.write("")