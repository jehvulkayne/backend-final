from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from typing import List

@CrewBase
class MyProjectCrew():
    """Crew configuration for multi-agent marketing system"""

    agents: List[Agent]
    tasks: List[Task]

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def data_collector(self) -> Agent:
        return Agent(config=self.agents_config['data_collector'])

    @agent
    def persona_architect(self) -> Agent:
        return Agent(config=self.agents_config['persona_architect'])

    @agent
    def meeting_dispatcher(self) -> Agent:
        return Agent(config=self.agents_config['meeting_dispatcher'])

    @agent
    def ad_placer(self) -> Agent:
        return Agent(config=self.agents_config['ad_placer'])

    @agent
    def brand_guardian(self) -> Agent:
        return Agent(config=self.agents_config['brand_guardian'])

    @agent
    def fraud_watcher(self) -> Agent:
        return Agent(config=self.agents_config['fraud_watcher'])

    @agent
    def crm_adapter(self) -> Agent:
        return Agent(config=self.agents_config['crm_adapter'])

    @task
    def data_collection_task(self) -> Task:
        return Task(config=self.tasks_config['data_collection_task'])

    @task
    def persona_creation_task(self) -> Task:
        return Task(config=self.tasks_config['persona_creation_task'])

    @task
    def persona_delivery_task(self) -> Task:
        return Task(config=self.tasks_config['persona_delivery_task'])

    @task
    def personalized_ad_task(self) -> Task:
        return Task(config=self.tasks_config['personalized_ad_task'])

    @task
    def brand_alignment_task(self) -> Task:
        return Task(config=self.tasks_config['brand_alignment_task'])

    @task
    def fraud_detection_task(self) -> Task:
        return Task(config=self.tasks_config['fraud_detection_task'])

    @task
    def crm_followup_task(self) -> Task:
        return Task(config=self.tasks_config['crm_followup_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
