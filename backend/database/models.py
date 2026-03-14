from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# ---------------------------
# STUDENTS TABLE
# ---------------------------
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)
    branch = Column(String)

    cgpa = Column(Float)

    projects = Column(Integer)
    experience = Column(Integer)

    github_url = Column(String)
    linkedin_url = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    applications = relationship("Application", back_populates="student")
    skills = relationship("StudentSkill", back_populates="student")


# ---------------------------
# COMPANIES TABLE
# ---------------------------
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String)
    email = Column(String)
    location = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    jobs = relationship("Job", back_populates="company")


# ---------------------------
# JOBS TABLE
# ---------------------------
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    role = Column(String)
    description = Column(String)

    min_cgpa = Column(Float)

    required_skills = Column(String)
    experience_required = Column(Integer)

    salary = Column(Integer)
    location = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="jobs")
    applications = relationship("Application", back_populates="job")


# ---------------------------
# APPLICATIONS TABLE
# ---------------------------
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    status = Column(String)

    applied_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="applications")
    job = relationship("Job", back_populates="applications")


# ---------------------------
# SKILLS TABLE
# ---------------------------
class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    skill_name = Column(String)


# ---------------------------
# STUDENT SKILLS TABLE
# ---------------------------
class StudentSkill(Base):
    __tablename__ = "student_skills"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))

    student = relationship("Student", back_populates="skills")


# ---------------------------
# ML PREDICTIONS TABLE
# ---------------------------
class MLPrediction(Base):
    __tablename__ = "ml_predictions"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    probability = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)


# ---------------------------
# ADMINS TABLE
# ---------------------------
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)
    password = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
