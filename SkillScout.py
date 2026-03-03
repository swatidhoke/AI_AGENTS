import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from pypdf import PdfReader
import docx
from dotenv import load_dotenv
load_dotenv()

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="AI Job Agent", layout="wide")
st.title("🤖 AI Job Recommendation Agent")

# -----------------------
# LLM
# -----------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# -----------------------
# DEFINE STRUCTURED OUTPUT MODEL
# -----------------------
class JobRecommendation(BaseModel):
    top_roles: list[str] = Field(description="Top 5 recommended job roles")
    skills_identified: list[str] = Field(description="Key skills found in resume")
    missing_skills: list[str] = Field(description="Important missing skills")
    learning_roadmap: list[str] = Field(description="Step-by-step improvement roadmap")

parser = PydanticOutputParser(pydantic_object=JobRecommendation)

# -----------------------
# FILE UPLOAD
# -----------------------
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

def extract_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_pdf(uploaded_file)
    else:
        resume_text = extract_docx(uploaded_file)

    st.subheader("📄 Resume Preview")
    st.text_area("Extracted Text", resume_text[:2000], height=200)

    if st.button("🚀 Analyze Resume"):

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert AI Career Advisor."),
            ("human", """
            Analyze this resume and return structured output.

            {format_instructions}

            Resume:
            {resume}
            """)
        ])

        chain = prompt | llm | parser

        with st.spinner("Analyzing..."):
            result = chain.invoke({
                "resume": resume_text,
                "format_instructions": parser.get_format_instructions()
            })

        st.subheader("🎯 Recommended Roles")
        st.write(result.top_roles)

        st.subheader("🧠 Skills Identified")
        st.write(result.skills_identified)

        st.subheader("⚠ Missing Skills")
        st.write(result.missing_skills)

        st.subheader("📚 Learning Roadmap")
        st.write(result.learning_roadmap)