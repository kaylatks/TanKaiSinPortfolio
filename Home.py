import streamlit as st
from streamlit_star_rating import st_star_rating

st.set_page_config(layout="wide")


def empty_line(numbers):
    for number in range(1, numbers):
        st.markdown("<br>", unsafe_allow_html=True)


# st.markdown("<h1 style='text-align: center; color: black;'>Tan Kai Sin</h1>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; color: black;'>Data Engineer</h1>", unsafe_allow_html=True)

sidebar_column = st.sidebar.columns([1, 6])
with sidebar_column[0]:

    empty_line(10)
    st.header("Contact")
    empty_line(1)
    st.image("emailicon.png", width=25)
    st.image("phoneicon.png", width=25)
    empty_line(3)

    st.header("Languages")
    empty_line(1)
    st.image("englishicon.png", width=25)
    st.image("chineseicon.png", width=25)

with sidebar_column[1]:
    st.markdown("<h1 style='text-align: left;font-size: 50px; color: black;'>Tan Kai Sin</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left;font-size: 25px; color: black;'>Data Engineer</h1>", unsafe_allow_html=True)
    empty_line(6)
    st.write("kaisin95.kst@gmail.com")
    st.write("0177591309")
    empty_line(5)
    st.write("English")
    st.write("Mandarin")
    empty_line(6)


    with open("TAN_KAI_SIN_RESUME.pdf", "rb") as file:
        file_bytes = file.read()
        st.download_button("Resume Download", data=file_bytes, file_name="TAN_KAI_SIN_RESUME.pdf")

st.header("Work Experience")
st.write("---")
col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("Data Engineer")
    st.write("Oct 2024 - Present")
    st.markdown("_Livein Sdn. Bhd._")

    empty_line(6)

    st.subheader("Data Engineer")
    st.write("Oct 2023 - Sep 2024")
    st.markdown("_RHB Bank Berhad_")

    empty_line(6)

    st.subheader("Data Engineer")
    st.write("Sep 2020 - Sep 2023")
    st.markdown("_Nettium Sdn. Bhd._")

    empty_line(8)

    st.subheader("Technical Specialist")
    st.write("March 2020 – Sept 2020")
    st.markdown("_MiHCM Asia Sdn Bhd_")

    empty_line(6)

    st.subheader("Data Coordinator")
    st.write("March 2018 – Feb 2020")
    st.markdown("_QS Enrolment Solutions Sdn.Bhd_")

    empty_line(5)

    st.subheader("SAP Technical Consultant Intern ")
    st.write("Feb 2017 – July 2017")
    st.markdown("_Aspert Innovations Sdn Bhd_")

with col2:
    content6 = f"""

            •	Design and implement an ETL pipeline to seamlessly integrate data into a data warehouse using AWS Lambda.

            •	Design and develop detailed summary reports using Python and PostgreSQL, and implement an automated solution to replace traditional manual processes, ensuring data integrity, accuracy, and optimized performance.

            •	Develop an advanced web scraping solution using Python, BeautifulSoup, and Selenium for efficient data extraction and analysis.

            •	Technical Skills:  PostgreSQL, Python, Pandas, Beautiful Soup, AWS Lambda, Microsoft Excel

            """

    st.write(content6)

    empty_line(3)

    content5 = f"""

        •	Drove development of the Enterprise Data Lake (EDL) data pipeline.

        •	Supported and prepared SIT and UAT testing of the pipeline, ensuring data integrity and adherence to business requirements.

        •	Facilitated efficient data access for analytics by supporting ad-hoc SAS tasks and data ingestion into Hive.

        •	Technical Skills:  Python, Pyspark, Apache Nifi, Hadoop, SAS, HDFS, Bitbucket Version Control

        """

    st.write(content5)

    empty_line(4)

    content4 = f"""

    •	Automated manual data processing pipeline (login, web scraping, cleansing, tallying) using Microsoft Excel VBA & Selenium, reducing time from 1 hour to 15 minutes (75% reduction).

    •	Developed Excel macros to automate data manipulation tasks (VLOOKUP, filtering, copying, importing).

    •	Implemented Tesseract OCR to automate captcha bypass for login.

    •	Contributed to report creation using SSRS and provided UAT testing & user support.
    
    •	Technical Skills:  SSRS, MSSQL, Microsoft Excel VBA, Web Scraping

    """

    st.write(content4)

    empty_line(4)

    content3 = f"""

    •	Managed data migration processes and provided client assistance for resolving issues.
        
    •	Developed SQL queries for data migration and data integrity checks in test environments.
        
    •	Contributed to SSRS report creation to enhance data visualization and analysis.
        
    •	Provided responsive client support for resolving issues like report errors and data inconsistencies.
    
    •	Technical Skills: MSSQL, SSRS, data migration

    """

    st.write(content3)

    empty_line(4)

    content2 = f"""

    •	Ensured client data accuracy and completeness before CRM upload.
        
    •	Developed Excel macros using VLOOKUP, conditional logic, and formatting to streamline data cleaning.
        
    •	Provided technical assistance for CRM data accuracy issues.
        
    •	Technical Skills: Microsoft Excel VBA, ETL process


    """

    st.write(content2)

    empty_line(4)

    content1 = f"""
    •	Creating stored procedure for Crystal Report with SQL Server 2014. 
    
    •	Assist in develop automation function for report format conversion with VB.NET
    
    •	Assisted in providing technical support to client.
    
    •	Application Used: MS SQL Server 2014, MS Visual Studio 2012, SAP Crystal Report

    """
    st.write(content1)

empty_line(5)
st.header("Education")
st.write("***")
st.write("2015 - 2017")
st.write("Bachelor Degree of Information Systems (Honours) in Enterprise Information Systems")
st.write("Tunku Abdul Rahman University College")

empty_line(2)
st.write("2013 - 2015")
st.write("Diploma In Science (Business Information Systems)")
st.write("Tunku Abdul Rahman University College")

st.markdown("<hr style='border-top: 1px solid lightgray;'>", unsafe_allow_html=True)

st.header("Technical Skills")
st_star_rating(label="SQL", maxValue=5, defaultValue=4, key="rating", read_only=True)
st_star_rating(label="Microsoft Excel", maxValue=5, defaultValue=5, key="rating1", read_only=True)
st_star_rating(label="Microsoft Excel VBA", maxValue=5, defaultValue=5, key="rating2", read_only=True)
st_star_rating(label="Python", maxValue=5, defaultValue=3, key="rating3", read_only=True)
st_star_rating(label="HDFS", maxValue=5, defaultValue=3, key="rating4", read_only=True)
st_star_rating(label="Apache Nifi", maxValue=5, defaultValue=3, key="rating5", read_only=True)










