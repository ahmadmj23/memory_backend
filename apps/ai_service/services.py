class BackstoryGenerator:
    """
    Interface for AI Backstory generation.
    This can be replaced by a clearer implementation using OpenAI/Gemini APIs.
    """
    
    def generate(self, descriptions: list[str]) -> str:
        # Mock implementation for MVP
        if not descriptions:
            return "No artifacts provided to weave a story."
            
        return (
            "In the depths of memory, " 
            + " and ".join(descriptions[:3]) 
            + f" came together to form a rich tapestry of history. (Mock generated story for {len(descriptions)} items)"
        )

# Singleton/Factory accessible to views
ai_generator = BackstoryGenerator()
