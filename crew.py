from crewai import Crew,Process
from agents import summarizer,translator
from tasks import summary_task,translation_task


# Create crew to manage agents and task workflow
crew = Crew(
    agents=[summarizer, translator], # Agents to include in your crew
    tasks=[summary_task, translation_task], # Tasks in execution order
    verbose=True
)

result = crew.kickoff()
print(result)