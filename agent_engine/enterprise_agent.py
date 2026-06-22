import os
import sys
from google import genai
from google.genai import types
from duckduckgo_search import DDGS
from dotenv import load_dotenv

# ==========================================
# 1. INITIALIZATION & SECURITY CONFIGURATION
# ==========================================
# Securely load environment variables from the isolated .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("[ERROR] GEMINI_API_KEY environment variable not found.")
    print("Ensure you have created a .env file in your root directory containing your key.")
    sys.exit(1)

# The modern genai client automatically detects the key from the environment
client = genai.Client()

# ==========================================
# 2. ENTERPRISE TOOL DEFINITIONS (ZERO-COST)
# ==========================================
def execute_realtime_web_search(query: str) -> str:
    """
    Executes a live web search to fetch real-time global information.
    """
    print(f"\n[AGENT ACTION] Triggering Real-Time Search Tool for: '{query}'...")
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if not results:
                return "No real-time data found for this query."
            
            formatted_results = []
            for idx, res in enumerate(results, 1):
                formatted_results.append(f"[{idx}] Source: {res['href']}\nSnippet: {res['body']}\n")
            return "\n".join(formatted_results)
    except Exception as e:
        return f"Error executing real-time search: {str(e)}"

# ==========================================
# 3. CORE AGENT CLASS ARCHITECTURE
# ==========================================
class EnterpriseGenAgent:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        """
        Initializes the agent utilizing the modern google-genai SDK.
        """
        self.system_instruction = (
            "You are an advanced Enterprise Knowledge Assistant. You have access to a tool "
            "called 'execute_realtime_web_search' which you MUST use if the user asks for "
            "real-time information, current pricing, live metrics, or current dates/events. "
            "Always maintain a precise, analytical, and professional corporate tone."
        )
        
        # Configure model parameters and native function calling via the new types system
        self.config = types.GenerateContentConfig(
            temperature=0.2,
            top_p=0.95,
            system_instruction=self.system_instruction,
            tools=[execute_realtime_web_search],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
        )
        
        # Establish an isolated, stateful memory session using the new chats API
        self.chat_session = client.chats.create(
            model=model_name,
            config=self.config
        )
        print(f"[SYSTEM] Agent initialized using {model_name}. Stateful memory active.")

    def interact(self, user_message: str) -> str:
        """
        Sends user input through the stateful chat engine.
        """
        try:
            response = self.chat_session.send_message(user_message)
            return response.text
        except Exception as e:
            return f"Architectural Execution Error: {str(e)}"

# ==========================================
# 4. RUNTIME VERIFICATION (MOCK SIMULATION)
# ==========================================
if __name__ == "__main__":
    agent = EnterpriseGenAgent()
    
    print("\n--- ENTERPRISE AGENT LIVE TEST RUN ---")
    
    print("\n[User]: Hi, I am Arpita. I specialize in SAP-certified digital transformations.")
    res1 = agent.interact("Hi, I am Arpita. I specialize in SAP-certified digital transformations.")
    print(f"[Agent]: {res1}")
    
    print("\n[User]: What is the current price of Bitcoin today?")
    res2 = agent.interact("What is the current price of Bitcoin today?")
    print(f"[Agent]: {res2}")
    
    print("\n[User]: Do you remember my name and what my business specialization is?")
    res3 = agent.interact("Do you remember my name and what my business specialization is?")
    print(f"[Agent]: {res3}")