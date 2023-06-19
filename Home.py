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

st.header("Work Experience")
st.write("---")
col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("Data Engineer")
    st.write("Sep 2020 - Present")
    st.markdown("_Nettium Sdn. Bhd._")

    empty_line(6)

    st.subheader("Technical Specialist")
    st.write("March 2020 – Sept 2020")
    st.markdown("_MiHCM Asia Sdn Bhd_")

    empty_line(8)

    st.subheader("Data Coordinator")
    st.write("March 2018 – Feb 2020")
    st.markdown("_QS Enrolment Solutions Sdn.Bhd_")

    empty_line(6)

    st.subheader("SAP Technical Consultant Intern ")
    st.write("Feb 2017 – July 2017")
    st.markdown("_Aspert Innovations Sdn Bhd_")

with col2:
    content = f"""

    •	Write the script for web scraping and automation on the task process of doing data reconciliation by using Microsoft Excel VBA Selenium.

    •	Assisted in creating the report by using SSRS

    •	Provide UAT test when new product launched

    •	Provide support to stakeholder when the issue arises (eg: product issue, report error, data not tally)

    """

    st.write(content)

    empty_line(4)

    content2 = f"""

    •	Main responsible in data migration and support client when issue arise.
        
    •	Assisted in creating SQL query script for data migration and data accuracy check in Remote Test Server.
        
    •	Assisted in creating system report by using SSRS.
        
    •	Assisted in testing application to find the bug and data accuracy.
        
    •	Provide support to client when the issue arises (eg: report error, data isn’t show up in application).
        
    •	Application Used: SSRS, MSSQL 2012 and MSSQL 2017, Remote Test Server

    """

    st.write(content2)

    empty_line(4)

    content3 = f"""

    •	Main responsible is to ensure client’s data is updated and correct before upload into CRM.
        
    •	Assisted in creating Macro to do data cleansing in Microsoft Excel. Example Macro that perform auto V-look up, if else conditions, and data formatting.
        
    •	Provide support during issues arise related to incorrect data in CRM.
        
    •	Knowledge on Robotics Process Automation.
        
    •	Application Used: Microsoft Excel 2016, CRM


    """

    st.write(content3)

    empty_line(4)

    content4 = f"""
    •	Creating stored procedure for Crystal Report with SQL Server 2014. 
    
    •	Assist in develop automation function for report format conversion with VB.NET
    
    •	Assisted in providing technical support to client.
    
    •	Application Used: MS SQL Server 2014, MS Visual Studio 2012, SAP Crystal Report

    """
    st.write(content4)

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

st.header("Computer Skills")
st_star_rating(label="SQL", maxValue=5, defaultValue=4, key="rating", read_only=True)
st_star_rating(label="Microsoft Excel", maxValue=5, defaultValue=5, key="rating1", read_only=True)
st_star_rating(label="Microsoft Excel VBA", maxValue=5, defaultValue=5, key="rating2", read_only=True)
st_star_rating(label="Python", maxValue=5, defaultValue=2, key="rating3", read_only=True)










