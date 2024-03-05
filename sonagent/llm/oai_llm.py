import os
from openai import OpenAI
from langchain.prompts import PromptTemplate
from sonagent.llm.prompt import summary_doc, create_git_pull_request_param, GITHUB_PULL_REQUEST_PROMPT

def text_summary(docs):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    sum_prompt = summary_doc(docs)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "play as interactive role, tell user if there is anything else you should take into consideration with the piece of text user trying to learn about. ",
            },
            {"role": "user", "content": sum_prompt},
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message.content


def create_pull_request_info(docs):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    # prompt = create_git_pull_request_param(docs)
    
    prompt_temp = PromptTemplate(
        template=GITHUB_PULL_REQUEST_PROMPT,
        input_variables=["sumary_text"],
    )
    prompt = prompt_temp.format(sumary_text=docs)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "you are a sennior software engineer and you are creating a pull request for the following changes. Your results will be used in another software.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    return response.choices[0].message.content
