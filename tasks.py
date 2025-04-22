from crewai import Task

def create_summary_task(url):
    return Task(
        description=f'Summarize this documentation from {url}:\n\nuseFetch(url) is a Robotic arm website.',
        expected_output="A clear, concise summary of the myarm_m750",
        agent=summarizer # Agent assigned to task
    )

url = 'https://www.elephantrobotics.com/en/myarm-m750/'
summary_task = create_summary_task(url)

translation_task = Task(
    description='Translate the summary to Telugu',
    expected_output="Telugu translation of the Robotic documentation",
    agent=translator,
    dependencies=[summary_task] # Must run after the summary task
)
