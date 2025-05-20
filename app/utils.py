def build_prompt(prompt_content: str) -> str:
   return (
        "You're a professional blog marketer. Based on the following blog content, "
        "generate 3 catchy, SEO-friendly blog titles. "
        "Each title should be 10 words or fewer and include power words.\n\n"
        f"Blog content:\n{prompt_content}"
    )