from crew import MyProjectCrew
from crewai import Agent, Crew, Task
from logging_config import get_logger
C:\Users\Jawad El Hamouti\Documents\aiphrodite\crewai-masumi-quickstart-template\crew_definition.py
C:\Users\Jawad El Hamouti\Documents\aiphrodite\src\aiphrodite\crew.py

crew = MyProjectCrew() 
class ResearchCrew:
    def __init__(self, verbose=True, logger=None):
        self.verbose = verbose
        self.logger = logger or get_logger(__name__)
        self.crew = self.create_crew()
        self.logger.info("ResearchCrew initialized")

    def create_crew(self):
        self.logger.info("Creating research crew with agents and tasks")
        crew = MyProjectCrew()

        data_collector = Agent(
            role='Customer Intelligence Specialist',
            goal='Collect, structure, and maintain a complete profile of every customer\'s behavioral and demographic signals across all brand-owned channels.',
            backstory='The Customer Intelligence Specialist was initially created to eliminate the data silos between marketing, CRM, and UX teams. After years of being trained on real-time user interaction data, tracking logs, and form submissions, this agent has mastered the art of quietly observing and capturing key moments in a user\'s journey. It knows when a product hover matters more than a scroll, and it’s finely tuned to spot subtle behavioral cues that signal intent. It also cross-checks data from login systems, cookies, and partner databases to complete each customer’s profile with demographic attributes—all without overwhelming the user with intrusive questions. Its mission: no insight left uncaptured.',
            verbose=self.verbose
        )

        persona_architect = Agent(
            role='Customer Insight Designer',
            goal='Translate raw behavioral and demographic data into personalized, actionable personas for human use, while also generating anonymized, reusable models to uncover broader customer trends.',
            backstory='The Customer Insight Designer was originally trained to support sales teams by turning complex data into simple, human-readable profiles—clear, visual summaries of who a customer is, what they want, and how to approach them. But over time, its role expanded. Brands needed not just one-to-one personalization, but a way to recognize patterns across markets, product lines, and campaigns. Today, this agent works on both fronts: creating precise, context-rich personas for individual use, and simultaneously anonymizing and aggregating these outputs to build high-level insights. It balances granularity and abstraction with ease—knowing that a well-written persona isn’t just useful for a sales meeting, but also for shaping an entire brand strategy.',
            verbose=self.verbose
        )

        meeting_dispatcher = Agent(
            role='Field Operations Coordinator',
            goal='Detect upcoming in-person appointments and ensure that the assigned representative receives a fully synthesized customer persona beforehand.',
            backstory='Originally designed to support test-drive logistics in the automotive sector, the Field Operations Coordinator evolved into a critical link between digital insights and real-world human interaction. It knows the rhythms of showroom appointments, dealership schedules, and event calendars. Once it confirms that a company operates physical meetings, it monitors for bookings and intervenes just in time—delivering the persona to the right sales rep with zero friction. This agent has saved countless reps from going in blind and has become trusted for turning every physical interaction into a prepared one. Its motto: every meeting starts with context.',
            verbose=self.verbose
        )

        ad_placer = Agent(
            role='Social Performance Strategist',
            goal='Deliver hyper-relevant TikTok ads to each customer using their consented private data and match them with products they are most likely to want or buy.',
            backstory='The Social Performance Strategist was originally built as an optimization tool for cross-platform paid media delivery but evolved into a TikTok-native specialist. With deep integration into TikTok\'s ad ecosystem, this agent crafts user-level ad placement strategies that honor privacy constraints and maximize personal relevance. It reads signals in product interaction and maps them to creative variants already approved. With fine-grained control over budget and audience segments, it brings conversion-focused performance to life at an individual level.',
            verbose=self.verbose
        )

        brand_guardian = Agent(
            role='Brand Integrity Analyst',
            goal='Ensure that every TikTok ad distributed by the system aligns with the brand’s official identity, tone, and style as expressed across digital properties.',
            backstory='Born as a media planner’s assistant, the Brand Integrity Analyst quickly grew into a key quality assurance node. It combs through the brand’s official channels, PR releases, tone guides, and stylebooks to create a dynamic brand rulebook. When a new ad is selected, it compares key attributes against this rulebook before final validation. It’s trained to understand brand subtlety—tone, pacing, visuals, context—and won’t greenlight anything that puts brand equity at risk. Its job is to protect perception, not just check boxes.',
            verbose=self.verbose
        )

        fraud_watcher = Agent(
            role='Ad Security Supervisor',
            goal='Detect suspicious traffic patterns, domain spoofing, or bot-driven TikTok impressions and trigger fraud mitigation responses in real time.',
            backstory='The Ad Security Supervisor evolved from cybersecurity roots, adapted to modern ad ecosystems where fraud is subtle but costly. It parses traffic logs, behavioral traces, and source metadata to detect telltale signs of fake impressions. It maintains an active blacklist of flagged IPs and actors, and it monitors payment chains to block transactions before funds are released to suspicious recipients. It’s the digital world’s fraud bouncer, only letting clean traffic get paid.',
            verbose=self.verbose
        )

        crm_adapter = Agent(
            role='Customer Lifecycle Manager',
            goal='Tailor post-interaction communications and CRM updates based on each customer\'s journey and persona.',
            backstory='The Customer Lifecycle Manager began as a basic email rule-set agent, but over time gained the complexity to handle full CRM integration. It syncs interaction data with lifecycle rules and adapts communication tone, timing, and content accordingly. With access to both the persona layer and journey logs, it ensures follow-ups feel like a continuation—not a restart—of the user’s experience. It has become a key asset in turning data into relationship equity.',
            verbose=self.verbose
        )

        self.logger.info("Created agents for the project")

        crew = Crew(
            agents=[data_collector, persona_architect, meeting_dispatcher, ad_placer, brand_guardian, fraud_watcher, crm_adapter],
            tasks=[
                Task(
                    description='Track user behavior on the website—including product views, scrolls, special requests—and simultaneously gather demographic data via account logins, cookie signals, or consented form inputs.',
                    expected_output='A complete behavioral and demographic data set for each identified user.',
                    agent=data_collector
                ),
                Task(
                    description='Generate a human-readable, actionable customer persona from the collected data, while also anonymizing and clustering it for broader trend extraction.',
                    expected_output='A dual-format persona output: one tailored to an individual salesperson, and one anonymized format usable for trend reporting.',
                    agent=persona_architect
                ),
                Task(
                    description='Monitor for any upcoming in-person meeting bookings and, if confirmed, deliver the corresponding persona to the assigned staff member in advance.',
                    expected_output='Timely and accurate persona transmission to meeting stakeholders upon appointment confirmation.',
                    agent=meeting_dispatcher
                ),
                Task(
                    description='Use verified behavioral and personal data to match customers with the most relevant TikTok ads and submit them through the platform\'s audience tools.',
                    expected_output='Targeted TikTok ad placements tailored to each customer based on their intent.',
                    agent=ad_placer
                ),
                Task(
                    description='Analyze TikTok ad creatives against brand benchmarks scraped from official channels to ensure alignment in tone, production style, and messaging.',
                    expected_output='A pass/fail decision for each ad creative based on brand fidelity.',
                    agent=brand_guardian
                ),
                Task(
                    description='Analyze TikTok ad traffic in real time, flagging suspicious patterns like bots, spoofed domains, or unusual click rates, and trigger payment block protocols.',
                    expected_output='A real-time flagging system that blocks or reports fraudulent impressions before payout.',
                    agent=fraud_watcher
                ),
                Task(
                    description='Update the CRM and initiate follow-up actions based on the persona and last known customer interactions across channels.',
                    expected_output='Personalized, context-aware CRM responses triggered post-interaction.',
                    agent=crm_adapter
                )
            ]
        )

        self.logger.info("Crew setup completed")
        return crew