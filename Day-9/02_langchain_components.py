"""
Day 9 - LangChain Components & Chains
Advanced demo showcasing multiple LangChain components and concepts.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


load_dotenv()


class TopicAnalysis(BaseModel):
    """Structured output for topic analysis."""
    overview: str = Field(description="3-sentence overview of the topic")
    key_concepts: List[str] = Field(description="3-5 key concepts to understand")
    difficulty_level: str = Field(description="Beginner, Intermediate, or Advanced")


def build_basic_chain():
    """Basic chain using modern syntax."""
    llm = ChatOpenAI(
        model=os.getenv("OPEN_ROUTER_MODEL"),
        temperature=0,
        openai_api_base=os.getenv("BASE_URL"),
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/langchain-demo",
            "X-Title": "LangChain Components Demo"
        }
    )
    
    prompt = PromptTemplate(
        template="Write a 3-sentence overview of {topic} for beginners.",
        input_variables=["topic"],
    )
    
    return prompt | llm


def build_chat_chain():
    """Chat-style chain with system and human messages."""
    llm = ChatOpenAI(
        model=os.getenv("OPEN_ROUTER_MODEL"),
        temperature=0.7,
        openai_api_base=os.getenv("BASE_URL"),
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/langchain-demo",
            "X-Title": "LangChain Components Demo"
        }
    )
    
    system_template = "You are an expert educator who explains complex topics in simple terms."
    human_template = "Explain {topic} in a conversational way, as if talking to a friend."
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("human", human_template)
    ])
    
    return chat_prompt | llm


def build_structured_chain():
    """Chain with structured output parsing."""
    llm = ChatOpenAI(
        model=os.getenv("OPEN_ROUTER_MODEL"),
        temperature=0,
        openai_api_base=os.getenv("BASE_URL"),
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/langchain-demo",
            "X-Title": "LangChain Components Demo"
        }
    )
    
    parser = PydanticOutputParser(pydantic_object=TopicAnalysis)
    
    prompt = PromptTemplate(
        template="Analyze the topic '{topic}' and provide:\n{format_instructions}",
        input_variables=["topic"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )
    
    return prompt | llm | parser


def build_multi_step_chain():
    """Multi-step chain combining different components."""
    llm = ChatOpenAI(
        model=os.getenv("OPEN_ROUTER_MODEL"),
        temperature=0.3,
        openai_api_base=os.getenv("BASE_URL"),
        openai_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://github.com/your-repo/langchain-demo",
            "X-Title": "LangChain Components Demo"
        }
    )
    
    # Step 1: Generate overview
    overview_prompt = PromptTemplate(
        template="Write a brief overview of {topic} in 2 sentences.",
        input_variables=["topic"]
    )
    
    # Step 2: Generate questions
    questions_prompt = PromptTemplate(
        template="Based on this overview: {overview}\n\nGenerate 3 questions a beginner might ask about {topic}.",
        input_variables=["overview", "topic"]
    )
    
    # Step 3: Answer the questions
    answer_prompt = PromptTemplate(
        template="Answer this question about {topic}: {question}\n\nProvide a clear, beginner-friendly answer.",
        input_variables=["topic", "question"]
    )
    
    return {
        "overview_chain": overview_prompt | llm,
        "questions_chain": questions_prompt | llm,
        "answer_chain": answer_prompt | llm
    }


def main() -> str:
    """
    Demonstrate various LangChain components and concepts.
    
    Returns:
        str: Demonstration results
    """
    # Validate environment variables
    if not os.getenv("OPEN_ROUTER_API_KEY"):
        raise ValueError("OPEN_ROUTER_API_KEY not set in .env file")
    
    topic = "artificial intelligence"
    results = []
    
    # 1. Basic Chain
    results.append("=== 1. Basic Chain ===")
    basic_chain = build_basic_chain()
    basic_result = basic_chain.invoke({"topic": topic})
    results.append(basic_result.content if hasattr(basic_result, 'content') else str(basic_result))
    results.append("")
    
    # 2. Chat Chain
    results.append("=== 2. Chat-Style Chain ===")
    chat_chain = build_chat_chain()
    chat_result = chat_chain.invoke({"topic": topic})
    results.append(chat_result.content if hasattr(chat_result, 'content') else str(chat_result))
    results.append("")
    
    # 3. Structured Output
    results.append("=== 3. Structured Output ===")
    structured_chain = build_structured_chain()
    structured_result = structured_chain.invoke({"topic": topic})
    results.append(f"Overview: {structured_result.overview}")
    results.append(f"Key Concepts: {', '.join(structured_result.key_concepts)}")
    results.append(f"Difficulty: {structured_result.difficulty_level}")
    results.append("")
    
    # 4. Multi-step Chain
    results.append("=== 4. Multi-step Chain ===")
    multi_chains = build_multi_step_chain()
    
    # Step 1: Generate overview
    overview_result = multi_chains["overview_chain"].invoke({"topic": topic})
    overview_text = overview_result.content if hasattr(overview_result, 'content') else str(overview_result)
    results.append(f"Overview: {overview_text}")
    
    # Step 2: Generate questions
    questions_result = multi_chains["questions_chain"].invoke({"overview": overview_text, "topic": topic})
    questions_text = questions_result.content if hasattr(questions_result, 'content') else str(questions_result)
    results.append(f"Questions: {questions_text}")
    
    # Step 3: Answer one question
    sample_question = "What is artificial intelligence?"
    answer_result = multi_chains["answer_chain"].invoke({"topic": topic, "question": sample_question})
    answer_text = answer_result.content if hasattr(answer_result, 'content') else str(answer_result)
    results.append(f"Answer to '{sample_question}': {answer_text}")
    
    return "\n".join(results)


if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except (ValueError, Exception) as e:
        print(f"Error: {e}")
        exit(1)


