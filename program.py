import streamlit as st
import pandas as pd
from datetime import datetime

# Function to read a CSV or Excel file
def read_file(file_path):
    if file_path.endswith('.csv'):
        # Custom function to remove commas from the 'NIK' column
        def remove_commas(x):
            return x.replace(',', '').rstrip('.0') # Remove trailing .0

        # Specify columns to be read from the CSV file, excluding the 'NO' column
        converters = {'NOMOR KARTU KELUARGA': remove_commas, 'NIK': remove_commas}
        df = pd.read_csv(file_path, usecols=lambda column: column != 'NO', converters=converters)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return None

    # Set the index starting from 1
    df.index = range(1, len(df) + 1)

    return df

# Function to delete data from a file by index
def delete_data_by_index(file_path, index):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return

    df = df.drop(index=index).reset_index(drop=True)

    if file_path.endswith('.csv'):
        df.to_csv(file_path, index=False)
    elif file_path.endswith(('.xls', '.xlsx')):
        df.to_excel(file_path, index=False)

# Function to add data to the file
def add_data(file_path, data):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return

    new_data = pd.DataFrame(data, index=[len(df) + 1])
    df = pd.concat([df, new_data])

    if file_path.endswith('.csv'):
        df.to_csv(file_path, index=False)
    elif file_path.endswith(('.xls', '.xlsx')):
        df.to_excel(file_path, index=False)

# Function to update data in the file by index and column
def update_data_by_index(file_path, index, column_name, new_value):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file_path)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        return

    df.at[index, column_name] = new_value

    if file_path.endswith('.csv'):
        df.to_csv(file_path, index=False)
    elif file_path.endswith(('.xls', '.xlsx')):
        df.to_excel(file_path, index=False)

# Function to calculate age from birthdate
def calculate_age(birthdate, current_year):
    try:
        birth_year = int(birthdate[-4:])
        age = current_year - birth_year
        return age
    except:
        return ""

# Main function
def main():
    st.title("Sistem Informasi Desa Tontayuo")

    # List of dataset files
    dataset_files = {
        "Data Penduduk Dunggala": "dunggala.csv",
        "Data Penduduk Tontayuo Daa": "tontayuo_daa.csv",
        "Data Penduduk Tontayuo Kiki": "tontayuo_kiki.csv"
    }

    # Sidebar - Choose dataset
    selected_dataset = st.sidebar.selectbox("PILIH DATASET:", list(dataset_files.keys()))

    # Fixed file path based on the selected dataset
    file_path = dataset_files[selected_dataset]
    df = read_file(file_path)
    if df is not None:
        
        # Get current year
        current_year = datetime.now().year
        # Calculate age and add new 'UMUR' column
        df['UMUR'] = df['TANGGAL LAHIR'].apply(lambda x: calculate_age(x, current_year))
        # Convert 'UMUR' column to integer
        df['UMUR'] = pd.to_numeric(df['UMUR'], errors='coerce')
        # Rearrange columns to place 'UMUR' after 'TANGGAL LAHIR'
        df = df[['NOMOR KARTU KELUARGA', 'NIK', 'NAMA', 'TANGGAL LAHIR', 'UMUR', 'PEKERJAAN', 'L/P']]

        st.dataframe(df)

        # Sidebar - Menu selection
        selected_menu = st.sidebar.selectbox("PILIH MENU:", ["Tambah Data", "Hapus Data", "Perbarui Data", "Pengelompokan Data"])

        if selected_menu == "Tambah Data":
            data_to_add = {
                'NOMOR KARTU KELUARGA': st.sidebar.text_input("NOMOR KARTU KELUARGA:"),
                'NIK': st.sidebar.text_input("NIK:"),
                'NAMA': st.sidebar.text_input("NAMA:"),
                'TANGGAL LAHIR': st.sidebar.text_input("TANGGAL LAHIR:"),
                'PEKERJAAN': st.sidebar.text_input("PEKERJAAN:"),
                'L/P': st.sidebar.text_input("L/P:")
            }

            if st.sidebar.button("Tambah Data"):
                add_data(file_path, data_to_add)
                df = read_file(file_path)
                st.success("Data berhasil ditambahkan!")
                st.dataframe(df)

        elif selected_menu == "Hapus Data":
            delete_index = st.sidebar.number_input("INDEKS BARIS YANG DIHAPUS:", min_value=1, max_value=len(df), step=1, key="delete_index")
            if st.sidebar.button("Hapus Data"):
                delete_data_by_index(file_path, int(delete_index-1))
                df = read_file(file_path)
                st.success("Data berhasil dihapus!")
                st.dataframe(df)

        elif selected_menu == "Perbarui Data":
            update_index = st.sidebar.number_input("INDEKS BARIS YANG DIPERBARUI:", min_value=1, max_value=len(df), step=1, key="update_index")
            selected_column = st.sidebar.selectbox("KOLOM YANG DIPERBARUI:", df.columns)
            new_value = st.sidebar.text_input(f"NILAI BARU UNTUK {selected_column}:")
            if st.sidebar.button("Perbarui Data"):
                update_data_by_index(file_path, int(update_index-1), selected_column, new_value)
                df = read_file(file_path)
                st.success("Data berhasil diperbarui!")
                st.dataframe(df)

        elif selected_menu == "Pengelompokan Data":
            submenu = st.sidebar.selectbox("PILIH PENGELOMPOKAN:", ["NOMOR KARTU KELUARGA", "UMUR", "PEKERJAAN", "L/P"])

            if submenu == "NOMOR KARTU KELUARGA":
                nomor_kk = st.sidebar.text_input("NOMOR KARTU KELUARGA:")
                grouped_df = df[df['NOMOR KARTU KELUARGA'] == nomor_kk]

            elif submenu == "UMUR":
                umur_awal = st.sidebar.number_input("UMUR AWAL:", min_value=0, max_value=current_year, step=1, value=0)
                umur_akhir = st.sidebar.number_input("UMUR AKHIR:", min_value=0, max_value=current_year, step=1, value=current_year)
                grouped_df = df[(df['UMUR'] >= umur_awal) & (df['UMUR'] <= umur_akhir)]

            elif submenu == "PEKERJAAN":
                pekerjaan = st.sidebar.text_input("PEKERJAAN:")
                grouped_df = df[df['PEKERJAAN'] == pekerjaan]

            elif submenu == "L/P":
                jenis_kelamin = st.sidebar.text_input("L/P:")
                grouped_df = df[df['L/P'] == jenis_kelamin]

            if st.sidebar.button("Hasil Pengelompokan"):
                st.dataframe(grouped_df)
                st.write(f"Jumlah penduduk dalam pengelompokan: {len(grouped_df)} orang")

         # Menghitung jumlah NO KK yang berbeda
        distinct_kk = len(df['NOMOR KARTU KELUARGA'].unique())
        total_penduduk = len(df)

        # Menampilkan total NO KK yang berbeda dan total penduduk
        st.write(f"Total Kepala Keluarga: {distinct_kk}")
        st.write(f"Total Penduduk: {total_penduduk} orang")
        
        st.download_button(
            label="Download",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name='updated_file.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
