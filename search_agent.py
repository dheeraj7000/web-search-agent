import ollama
import requests
import os
from typing import Dict, List
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class SimpleSearchAgent:
    def __init__(self, model_name="llama2"):
        self.model_name = model_name
        self.serpapi_key = os.getenv("SERPAPI_KEY")
        if not self.serpapi_key:
            raise ValueError("❌ Missing SERPAPI_KEY in .env file")

    def search_web(self, query, num_results=3):
        """Perform real web search using SerpAPI"""
        url = "https://serpapi.com/search"
        params = {
            "q": query,
            "num": num_results,
            "api_key": self.serpapi_key,
            "engine": "google"
        }

        response = requests.get(url, params=params)
        data = response.json()

        results = []
        if "organic_results" in data:
            for r in data["organic_results"][:num_results]:
                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("link", ""),
                    "snippet": r.get("snippet", "")
                })

        return results
    
    def generate_response(self, query, context):
        """Generate response using Ollama"""
        prompt = f"""
        Based on the user query and context, provide a helpful answer.

        Query: {query}
        Context: {context}

        Please provide a comprehensive answer that addresses the query using the context provided.

        Answer:
        """
        
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response['message']['content']
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def run(self, query):
        """Run the search agent"""
        print(f"🔍 Searching for: {query}")
        
        # Step 1: Search web
        results = self.search_web(query)
        context = "\n".join([f"{r['title']}: {r['snippet']}" for r in results])
        
        # Step 2: Generate response
        print("🤖 Generating response...")
        answer = self.generate_response(query, context)
        
        # Format response
        response = {
            "query": query,
            "sources": results,
            "answer": answer
        }
        
        # Print results
        print(f"\n📋 Response:")
        print(f"Query: {response['query']}")
        print(f"\nAnswer: {response['answer']}")
        print(f"\nSources:")
        for source in response['sources']:
            print(f"  - {source['title']}: {source['url']}")
        
        return response


# Usage example
if __name__ == "__main__":
    agent = SimpleSearchAgent("tinyllama:latest")
    
    queries = [
        "What is quantum computing?",
        "How does quantum computing work?",
        "What are the applications of quantum computing?"
    ]
    
    for query in queries:
        print(f"\n{'='*60}")
        print(f"QUERY: {query}")
        print(f"{'='*60}")
        
        result = agent.run(query)
        print(f"\n✅ Search completed!")
