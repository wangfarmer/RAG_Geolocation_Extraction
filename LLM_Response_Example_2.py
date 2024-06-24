# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Prompt content
instruction="""You are acting as a reviewer for a Q1 transplant journal. Please evaluate the following abstract and determine if it should be accepted for publication."""
content = """Infections are a major cause of morbidity and mortality in kidney transplant recipients. To some extent, these may be preventable. Careful pretransplant screening, immunization, and post-transplant prophylactic antimicrobials may all reduce the risk for post-transplant infection. However, because transplant recipients may not manifest typical signs and symptoms of infection, diagnoses may be confounded. Furthermore, treatment regimens may be complicated by drug interactions and the need to maintain immunosuppression to avoid allograft rejection. This article reviews common post-transplant infections, including prophylactic, diagnostic, and treatment strategies, providing guidance regarding care of kidney transplant patients with infection."""
prompt = instruction+" "+content
message = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": prompt},
]

# Call API to generate responses
completion = client.chat.completions.create(
        model="model-identifier",
        messages=message,
        temperature=0.7,
        stream=True,
    )
for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

'''
def get_completion(prompt):
    history = [
        {"role": "system", "content": "You are acting as a reviewer for a Q1 transplant journal. Please evaluate the following abstract and determine if it should be accepted for publication."},
        {"role": "user", "content": prompt},
    ]
    completion = client.chat.completions.create(
        model="model-identifier",
        messages=history,
        temperature=1.0,
        stream=True,
        max_tokens=100
    )
    output =''
    for chunk in completion:
        if chunk.choices[0].delta.content:
            output += str(chunk.choices[0].delta.content)

    return output
'''