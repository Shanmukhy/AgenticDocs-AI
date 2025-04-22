from crewai import Agent, LLM

from dotenv import load_dotenv

load_dotenv()

import os

os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

llm = LLM(model="groq/llama-3.3-70b-versatile")

llm = LLM(
    model="llama-3.1-70b-versatile",
    temperature=0.5,
    max_completion_tokens=1024,
    top_p=0.9,
    stop=None,
    stream=False,
)

# Create your CrewAI agents with role, main goal/objective, and backstory/personality
summarizer = Agent(
    role='Documentation Summarizer', # Agent's job title/function
    goal='Create concise summaries of technical documentation', # Agent's main objective
    backstory='Technical writer who excels at simplifying complex concepts', # Agent's background/expertise
    llm=llm, # LLM that powers your agent
    verbose=True # Show agent's thought process as it completes its task
)

translator = Agent(
    role='Technical Translator',
    goal='Translate technical documentation to other languages',
    backstory='Technical translator specializing in software documentation',
    llm=llm,
    verbose=True
)
