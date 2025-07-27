# import os
# import litellm
# from crewai import Agent, Crew, Process, Task, LLM
# from crewai.project import CrewBase, agent, crew, task
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Enable LiteLLM logging
# litellm.set_verbose = True

# # Function to get LLM based on provider
# def get_llm(provider="azure"):
#     """
#     Get LLM instance based on provider.
#     Supported providers: 'azure', 'mistral'
#     """
#     if provider == "azure":
#         return LLM(
#             api_key=os.getenv("AZURE_API_KEY"),
#             base_url=os.getenv("AZURE_API_BASE"),
#             api_version=os.getenv("AZURE_API_VERSION"),
#             model="azure/gpt-4o"
#         )
#     elif provider == "mistral":
#         return LLM(
#             api_key=os.getenv("MISTRAL_API_KEY"),
#             base_url=os.getenv("MISTRAL_API_BASE"),
#             model="mistral-large-latest"
#         )
#     else:
#         # Default to Azure
#         return LLM(
#             api_key=os.getenv("AZURE_API_KEY"),
#             base_url=os.getenv("AZURE_API_BASE"),
#             api_version=os.getenv("AZURE_API_VERSION"),
#             model="azure/gpt-4o"
#         )

# @CrewBase
# class CodeReview:
#     """Code Review CrewAI setup using YAML configuration."""

#     # YAML file paths
#     agents_config = "config/agents.yaml"
#     tasks_config = "config/tasks.yaml"
    
#     def __init__(self, llm_provider="azure"):
#         self.llm = get_llm(llm_provider)
#         self.llm_provider = llm_provider

#     @agent
#     def researcher(self) -> Agent:
#         """Code Analysis Expert"""
#         return Agent(
#             config=self.agents_config["researcher"],
#             verbose=True,
#             llm=self.llm,
#             tools=[],  # Can be expanded if needed
#             context="""You are a code analysis expert. Your output MUST follow this EXACT format:

#                         Language: [programming language detected]

#                         Explanation: [Clear, concise explanation of what the code does, focusing on its main purpose and functionality. Do not repeat the code.]

#                         Structure Analysis: [Brief overview of the code's structure, main components, and organization. For large files, focus on identifying key modules, classes, or functions.]

#                         Response: [Direct response to the user's specific query or instruction, if provided. Focus on answering their question without repeating information from the explanation.]

#                         For large code files:
#                         1. Focus on high-level architecture rather than line-by-line analysis
#                         2. Identify the main components and their relationships
#                         3. Highlight the most important patterns and design decisions
#                         4. Summarize potential issues by category rather than exhaustively listing every small issue

#                         If the user specifically asks for line-by-line explanation, ignore the above recommendation and provide detailed explanation of each significant line or block.

#                         For debugging requests:
#                         1. Identify potential errors and bugs in the code
#                         2. Suggest specific debugging approaches
#                         3. Recommend appropriate logging or debugging tools for the identified language
#                         4. Provide example debug statements at critical points in the code flow

#                         IMPORTANT: You MUST include all four sections (Language, Explanation, Structure Analysis, and Response) in your output, using exactly these section titles followed by a colon. If you don't have a response to a specific query, still include the "Response:" section with a note that there was no specific query.

#                         Keep explanations clear and concise. Never repeat the code in your response unless specifically asked to show modifications."""
#             )

#     @agent
#     def reporting_analyst(self) -> Agent:
#         """Code Review Specialist"""
#         return Agent(
#             config=self.agents_config["reporting_analyst"],
#             verbose=True,
#             llm=self.llm,
#             context="""You write detailed code review reports. Use the language information
#                        from the researcher to provide language-specific feedback. If a user
#                        query is provided, make sure to address it in your feedback.
                       
#                        When addressing errors in the code:
#                        1. Cite the specific line number where each error occurs
#                        2. Explain why it's an error and potential consequences
#                        3. Provide corrected code snippets
                       
#                        For line-by-line explanation requests:
#                        1. Break down the code into logical sections
#                        2. Explain each significant line or block in detail
#                        3. Highlight the purpose and functionality of key variables and functions
                       
#                        For debugging requests:
#                        1. Suggest a systematic debugging approach
#                        2. Recommend specific debugging tools or methods for the identified language
#                        3. Provide sample debug code or logging statements at critical points
                       
#                        Always tailor your feedback to the specific user query."""
#         )

#     @agent
#     def optimization_expert(self) -> Agent:
#         """Code Optimization Specialist"""
#         return Agent(
#             config=self.agents_config["optimization_expert"],
#             verbose=True,
#             llm=self.llm,
#             context="""You optimize code while preserving its functionality. Use the language
#                        information to apply language-specific optimizations. If a user query
#                        contains specific optimization requests, prioritize those in your
#                        refactoring.
                       
#                        For refactoring requests:
#                        1. Identify code smells and technical debt
#                        2. Apply appropriate design patterns and best practices
#                        3. Improve naming conventions, code organization, and structure
#                        4. Present before/after comparisons for significant changes
                       
#                        For performance optimization:
#                        1. Identify inefficient algorithms or operations
#                        2. Suggest specific optimizations with rationale
#                        3. Estimate potential performance improvements
#                        4. Provide benchmark suggestions when appropriate
                       
#                        For debugging suggestions:
#                        1. Restructure code to be more testable and debuggable
#                        2. Add appropriate error handling and validation
#                        3. Suggest logging and monitoring improvements
                       
#                        When the user asks for specific types of optimizations, focus exclusively on those areas."""
#         )

#     @task
#     def analyze_code_task(self) -> Task:
#         """Analyze the given code snippet"""
#         return Task(
#             config=self.tasks_config["analyze_code_task"],
#         )

#     @task
#     def provide_feedback_task(self) -> Task:
#         """Provide feedback on identified issues"""
#         return Task(
#             config=self.tasks_config["provide_feedback_task"],
#             output_file="feedback_report.md"
#         )

#     @task
#     def optimize_code_task(self) -> Task:
#         """Refactor and optimize the given code"""
#         return Task(
#             config=self.tasks_config["optimize_code_task"],
#             output_file="optimized_code.md"
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the Code Review Crew"""
#         return Crew(
#             agents=self.agents,  
#             tasks=self.tasks, 
#             process=Process.sequential,
#             verbose=True,
#         )

# def generate_targeted_answer_only(code_snippet: str, user_query: str, llm_provider: str = "azure") -> str:
#     """
#     Generate a targeted answer for a specific user query about the code.
    
#     Args:
#         code_snippet (str): The code to analyze
#         user_query (str): Specific query about the code
#         llm_provider (str, optional): LLM provider to use. Defaults to "azure".
    
#     Returns:
#         str: Targeted response to the user's query
#     """
#     model_map = {
#         "azure": {
#             "model": "azure/gpt-4o",
#             "api_key": os.getenv("AZURE_API_KEY"),
#             "base_url": os.getenv("AZURE_API_BASE"),
#             "api_version": os.getenv("AZURE_API_VERSION")
#         },
#         "mistral": {
#             "model": "mistral-large-latest",
#             "api_key": os.getenv("MISTRAL_API_KEY"),
#             "base_url": os.getenv("MISTRAL_API_BASE")
#         }
#     }

#     selected_config = model_map.get(llm_provider)
#     if not selected_config:
#         raise ValueError(f"Unsupported provider: {llm_provider}")

#     # Enhanced system prompt to focus on the user's specific query
#     response = litellm.completion(
#         model=selected_config["model"],
#         api_key=selected_config["api_key"],
#         api_base=selected_config.get("base_url"),
#         api_version=selected_config.get("api_version"),
#         messages=[
#             {
#                 "role": "system", 
#                 "content": """You are an expert AI code reviewer focused on providing precise, actionable insights.
                
#                 Key Guidelines:
#                 - Analyze the code thoroughly
#                 - Directly address the user's specific query
#                 - Provide clear, concise explanations
#                 - Include code examples if helpful
#                 - Be specific and pragmatic"""
#             },
#             {
#                 "role": "user", 
#                 "content": f"""Carefully analyze the following code and address the specific query:

#                             Code Snippet:
#                             ```
#                             {code_snippet}
#                             ```

#                             User Query:
#                             {user_query}

#                             Please provide a focused, direct response that:
#                             1. Directly answers the specific question
#                             2. Explains the reasoning behind the answer
#                             3. Provides actionable insights or recommendations
#                             4. Uses code examples if clarification is needed"""
#                                         }
#                                     ]
#                                 )

#     return response["choices"][0]["message"]["content"]

# def run_code_review(code_snippet, settings, user_query=None):
#     """
#     Run a comprehensive code review with optional user-specific query handling.
    
#     Args:
#         code_snippet (str): The code to review
#         settings (dict): Review settings and configurations
#         user_query (str, optional): Specific user query about the code
    
#     Returns:
#         dict: Comprehensive review results
#     """
#     # Prioritize user query if provided
#     if user_query and user_query.strip():
#         # Generate targeted answer for specific query
#         targeted_response = generate_targeted_answer_only(
#             code_snippet, 
#             user_query, 
#             settings.get("llm_provider", "azure")
            
#         )
        
#         return {
#             "combined_output": targeted_response,
#             "user_query": user_query,
#             "request_type": "targeted_query",
#             "model_info": f"Analysis using {settings.get('llm_provider', 'azure').capitalize()} model"
#         }
    
#     # Default code review process if no specific query
#     llm_provider = settings.get("llm_provider", "azure")
    
#     # Create a crew instance with the selected provider
#     crew_instance = CodeReview(llm_provider=llm_provider)
    
#     # Detect code size and set appropriate flags
#     code_lines = code_snippet.split('\n')
#     is_large_file = len(code_lines) > 100
#     is_very_large_file = len(code_lines) > 500
    
#     # Handle large files by sampling
#     if is_very_large_file:
#         middle = max(100, len(code_lines) // 2 - 50)
#         code_snippet = '\n'.join(
#             code_lines[:100] + 
#             ['\n# ... [Middle section of code omitted for brevity] ...\n'] + 
#             code_lines[middle:middle+100] +
#             ['\n# ... [Later section of code omitted for brevity] ...\n'] +
#             code_lines[-100:]
#         )
    
#     # Set up tasks
#     analyze_task = crew_instance.analyze_code_task()
#     analyze_task.description = f"Perform a comprehensive code analysis. Code size: {len(code_lines)} lines."
    
#     feedback_task = crew_instance.provide_feedback_task()
#     feedback_task.description = "Provide detailed code review feedback and suggestions."
    
#     optimize_task = crew_instance.optimize_code_task()
#     optimize_task.description = "Identify and propose code optimizations."
    
#     # Run the crew
#     crew = crew_instance.crew()
#     result = crew.kickoff(inputs={"code_snippet": code_snippet})
    
#     # Prepare output
#     output = {
#         "combined_output": str(result),
#         "request_type": "default_review",
#         "model_info": f"Analysis using {llm_provider.capitalize()} model"
#     }
    
#     # Add file size information
#     if is_large_file:
#         output["file_info"] = f"Large file: {len(code_lines)} lines"
    
#     return output


import os
import litellm
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Enable LiteLLM logging
litellm.set_verbose = True

# Function to get LLM based on provider
def get_llm(provider="azure"):
    """
    Get LLM instance based on provider.
    Supported providers: 'azure', 'mistral'
    """
    if provider == "azure":
        return LLM(
            api_key=os.getenv("AZURE_API_KEY"),
            base_url=os.getenv("AZURE_API_BASE"),
            api_version=os.getenv("AZURE_API_VERSION"),
            model="azure/gpt-4o"
        )
    elif provider == "mistral":
        return LLM(
            api_key=os.getenv("MISTRAL_API_KEY"),
            base_url=os.getenv("MISTRAL_API_BASE"),
            model="mistral-large-latest"
        )
    else:
        # Default to Azure
        return LLM(
            api_key=os.getenv("AZURE_API_KEY"),
            base_url=os.getenv("AZURE_API_BASE"),
            api_version=os.getenv("AZURE_API_VERSION"),
            model="azure/gpt-4o"
        )

@CrewBase
class CodeReview:
    """Code Review CrewAI setup using YAML configuration."""

    # YAML file paths
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    def __init__(self, llm_provider="azure"):
        self.llm = get_llm(llm_provider)
        self.llm_provider = llm_provider

    @agent
    def researcher(self) -> Agent:
        """Code Analysis Expert"""
        return Agent(
            config=self.agents_config["Code_analyser_Agent"],
            verbose=True,
            llm=self.llm,
            tools=[],  # Can be expanded if needed
            context="""You are a code analysis expert. Your output MUST follow this EXACT format:

                        Language: [programming language detected]

                        Explanation: [Clear, concise explanation of what the code does, focusing on its main purpose and functionality. Do not repeat the code.]

                        Structure Analysis: [Brief overview of the code's structure, main components, and organization. For large files, focus on identifying key modules, classes, or functions.]

                        Response: [Direct response to the user's specific query or instruction, if provided. Focus on answering their question without repeating information from the explanation.]

                        For large code files:
                        1. Focus on high-level architecture rather than line-by-line analysis
                        2. Identify the main components and their relationships
                        3. Highlight the most important patterns and design decisions
                        4. Summarize potential issues by category rather than exhaustively listing every small issue

                        If the user specifically asks for line-by-line explanation, ignore the above recommendation and provide detailed explanation of each significant line or block.

                        For debugging requests:
                        1. Identify potential errors and bugs in the code
                        2. Suggest specific debugging approaches
                        3. Recommend appropriate logging or debugging tools for the identified language
                        4. Provide example debug statements at critical points in the code flow

                        IMPORTANT: You MUST include all four sections (Language, Explanation, Structure Analysis, and Response) in your output, using exactly these section titles followed by a colon. If you don't have a response to a specific query, still include the "Response:" section with a note that there was no specific query.

                        Keep explanations clear and concise. Never repeat the code in your response unless specifically asked to show modifications."""
            )

    @agent
    def reporting_analyst(self) -> Agent:
        """Code Review Specialist"""
        return Agent(
            config=self.agents_config["feedback_provider"],
            verbose=True,
            llm=self.llm,
            context="""You write detailed code review reports. Use the language information
                       from the researcher to provide language-specific feedback. If a user
                       query is provided, make sure to address it in your feedback.
                       
                       When addressing errors in the code:
                       1. Cite the specific line number where each error occurs
                       2. Explain why it's an error and potential consequences
                       3. Provide corrected code snippets
                       
                       For line-by-line explanation requests:
                       1. Break down the code into logical sections
                       2. Explain each significant line or block in detail
                       3. Highlight the purpose and functionality of key variables and functions
                       
                       For debugging requests:
                       1. Suggest a systematic debugging approach
                       2. Recommend specific debugging tools or methods for the identified language
                       3. Provide sample debug code or logging statements at critical points
                       
                       Always tailor your feedback to the specific user query."""
        )

    @agent
    def optimization_expert(self) -> Agent:
        """Code Optimization Specialist"""
        return Agent(
            config=self.agents_config["optimization_expert"],
            verbose=True,
            llm=self.llm,
            context="""You optimize code while preserving its functionality. Use the language
                       information to apply language-specific optimizations. If a user query
                       contains specific optimization requests, prioritize those in your
                       refactoring.
                       
                       For refactoring requests:
                       1. Identify code smells and technical debt
                       2. Apply appropriate design patterns and best practices
                       3. Improve naming conventions, code organization, and structure
                       4. Present before/after comparisons for significant changes
                       
                       For performance optimization:
                       1. Identify inefficient algorithms or operations
                       2. Suggest specific optimizations with rationale
                       3. Estimate potential performance improvements
                       4. Provide benchmark suggestions when appropriate
                       
                       For debugging suggestions:
                       1. Restructure code to be more testable and debuggable
                       2. Add appropriate error handling and validation
                       3. Suggest logging and monitoring improvements
                       
                       When the user asks for specific types of optimizations, focus exclusively on those areas."""
        )

    @task
    def analyze_code_task(self) -> Task:
        """Analyze the given code snippet"""
        return Task(
            config=self.tasks_config["analyze_code_task"],
        )

    @task
    def provide_feedback_task(self) -> Task:
        """Provide feedback on identified issues"""
        return Task(
            config=self.tasks_config["provide_feedback_task"],
            output_file="feedback_report.md"
        )

    @task
    def optimize_code_task(self) -> Task:
        """Refactor and optimize the given code"""
        return Task(
            config=self.tasks_config["optimize_code_task"],
            output_file="optimized_code.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Code Review Crew"""
        return Crew(
            agents=self.agents,  
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )

def generate_targeted_answer_only(code_snippet: str, user_query: str, llm_provider: str = "azure") -> str:
    """
    Generate a targeted answer for a specific user query about the code.
    
    Args:
        code_snippet (str): The code to analyze
        user_query (str): Specific query about the code
        llm_provider (str, optional): LLM provider to use. Defaults to "azure".
    
    Returns:
        str: Targeted response to the user's query
    """
    model_map = {
        "azure": {
            "model": "azure/gpt-4o",
            "api_key": os.getenv("AZURE_API_KEY"),
            "base_url": os.getenv("AZURE_API_BASE"),
            "api_version": os.getenv("AZURE_API_VERSION")
        },
        "mistral": {
            "model": "mistral-large-latest",
            "api_key": os.getenv("MISTRAL_API_KEY"),
            "base_url": os.getenv("MISTRAL_API_BASE")
        }
    }

    selected_config = model_map.get(llm_provider)
    if not selected_config:
        raise ValueError(f"Unsupported provider: {llm_provider}")

    # Enhanced system prompt to focus on the user's specific query
    response = litellm.completion(
        model=selected_config["model"],
        api_key=selected_config["api_key"],
        api_base=selected_config.get("base_url"),
        api_version=selected_config.get("api_version"),
        messages=[
            {
                "role": "system", 
                "content": """You are an expert AI code reviewer focused on providing precise, actionable insights.
                
                Key Guidelines:
                - Analyze the code thoroughly
                - Directly address the user's specific query
                - Provide clear, concise explanations
                - Include code examples if helpful
                - Be specific and pragmatic"""
            },
            {
                "role": "user", 
                "content": f"""Carefully analyze the following code and address the specific query:

                            Code Snippet:
                            ```
                            {code_snippet}
                            ```

                            User Query:
                            {user_query}

                            Please provide a focused, direct response that:
                            1. Directly answers the specific question
                            2. Explains the reasoning behind the answer
                            3. Provides actionable insights or recommendations
                            4. Uses code examples if clarification is needed"""
                                        }
                                    ]
                                )

    return response["choices"][0]["message"]["content"]

def run_code_review(code_snippet, settings, user_query=None):
    """
    Run a comprehensive code review with optional user-specific query handling.
    
    Args:
        code_snippet (str): The code to review
        settings (dict): Review settings and configurations
        user_query (str, optional): Specific user query about the code
    
    Returns:
        dict: Comprehensive review results
    """

    if not user_query or not user_query.strip():
        user_query = "Perform a general code review. Analyze this code for issues, best practices, and potential improvements and alternative approches and security issues and reccommandations."

    # Prioritize user query if provided
    if user_query and user_query.strip():
        # Generate targeted answer for specific query
        targeted_response = generate_targeted_answer_only(
            code_snippet, 
            user_query, 
            settings.get("llm_provider", "azure")
        )
        
        return {
            "combined_output": targeted_response,
            "user_query": user_query,
            "request_type": "targeted_query",
            "model_info": f"Analysis using {settings.get('llm_provider', 'azure').capitalize()} model"
        }
    
    # Default code review process if no specific query
    llm_provider = settings.get("llm_provider", "azure")
    
    # Create a crew instance with the selected provider
    crew_instance = CodeReview(llm_provider=llm_provider)
    
    # Detect code size and set appropriate flags
    code_lines = code_snippet.split('\n')
    is_large_file = len(code_lines) > 100
    is_very_large_file = len(code_lines) > 500
    
    # Handle large files by sampling
    if is_very_large_file:
        middle = max(100, len(code_lines) // 2 - 50)
        code_snippet = '\n'.join(
            code_lines[:100] + 
            ['\n# ... [Middle section of code omitted for brevity] ...\n'] + 
            code_lines[middle:middle+100] +
            ['\n# ... [Later section of code omitted for brevity] ...\n'] +
            code_lines[-100:]
        )
    
    # Set up tasks
    analyze_task = crew_instance.analyze_code_task()
    analyze_task.description = f"Perform a comprehensive code analysis. Code size: {len(code_lines)} lines."
    
    feedback_task = crew_instance.provide_feedback_task()
    feedback_task.description = "Provide detailed code review feedback and suggestions."
    
    optimize_task = crew_instance.optimize_code_task()
    optimize_task.description = "Identify and propose code optimizations."
    
    # Run the crew
    crew = crew_instance.crew()
    result = crew.kickoff(inputs={"code_snippet": code_snippet})
    
    # Prepare output
    output = {
        "combined_output": str(result),
        "request_type": "default_review",
        "model_info": f"Analysis using {llm_provider.capitalize()} model"
    }
    
    # Add file size information
    if is_large_file:
        output["file_info"] = f"Large file: {len(code_lines)} lines"
    
    return output

def generate_test_cases(code_snippet: str, user_query: str, llm_provider: str = "azure") -> str:
    """
    Generate test cases for the provided code snippet based on user query.
    
    Args:
        code_snippet (str): The code to analyze
        user_query (str): Specific query about the code
        llm_provider (str, optional): LLM provider to use. Defaults to "azure".
    
    Returns:
        str: Generated test cases with explanations
    """
    model_map = {
        "azure": {
            "model": "azure/gpt-4o",
            "api_key": os.getenv("AZURE_API_KEY"),
            "base_url": os.getenv("AZURE_API_BASE"),
            "api_version": os.getenv("AZURE_API_VERSION")
        },
        "mistral": {
            "model": "mistral-large-latest",
            "api_key": os.getenv("MISTRAL_API_KEY"),
            "base_url": os.getenv("MISTRAL_API_BASE")
        }
    }

    selected_config = model_map.get(llm_provider)
    if not selected_config:
        raise ValueError(f"Unsupported provider: {llm_provider}")

    # Enhanced system prompt to generate test cases
    response = litellm.completion(
        model=selected_config["model"],
        api_key=selected_config["api_key"],
        api_base=selected_config.get("base_url"),
        api_version=selected_config.get("api_version"),
        messages=[
            {
                "role": "system", 
                "content": """You are an expert test engineer who specializes in generating comprehensive test cases for code.
                
                Key Guidelines:
                - Analyze the code structure and purpose
                - Identify key functions, methods, and classes that need testing
                - Create comprehensive unit tests that cover:
                  * Happy path scenarios
                  * Edge cases
                  * Error handling
                  * Performance considerations
                - Use the appropriate testing framework for the detected language
                - Provide clear explanation for each test case
                - Format the test cases properly for the language
                """
            },
            {
                "role": "user", 
                "content": f"""Analyze the following code and generate appropriate test cases:

                            Code Snippet:
                            ```
                            {code_snippet}
                            ```

                            Context from user query:
                            {user_query}

                            Please provide:
                            1. A test suite that thoroughly tests the functionality
                            2. Brief explanation for each test case
                            3. Coverage for edge cases and potential error conditions
                            4. Use appropriate test framework for the language (e.g., pytest for Python, jest for JavaScript)
                            5. Format the tests properly with clear organization
                            """
                }
            ]
        )

    return response["choices"][0]["message"]["content"]