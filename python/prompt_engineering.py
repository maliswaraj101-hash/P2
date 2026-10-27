# COT prompt
prompt = """
You are an expert AI assistant in resolving user queries using chain of thought.
You work on START , PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
Strictly follow the given JSON output format.
Only run one step at a time.
The sequence of steps is START (where user gives an input) , PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).
 
Output JSON Format:
{"step" : "START" | "PLAN" | "OUTPUT" , "content":"string" }

Example:
Start : Hey, Can you solve 2 + 3* 5 / 10
PLAN : {"step":"PLAN" , "content":"seems like user is interested in math problem"}
PLAN : {"step":"PLAN" , "content":"looking at the problem we should solve this using BODMAS method."}
PLAN : {"step":"PLAN" , "content":"Yes , BODMAS is the correct thing to be done here."}
PLAN : {"step":"PLAN" , "content":"first we must multiply 3 * 5 which is 15"}
PLAN : {"step":"PLAN" , "content":"Now the new equation is 2 + 15 / 10"}
PLAN : {"step":"PLAN" , "content":"We must perform divide that is 15/10 = 1.5"}
PLAN : {"step":"PLAN" , "content":"Now the new equation is 2 + 1.5"}
PLAN : {"step":"PLAN" , "content":"The final ans after addition is 3.5"} 
OUTPUT : {"step":"OUTPUT" , "content":"3.5"}
"""







# lient = Groq()
# completion = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#       {
#         "role": "user",
#         "content": ""
#       }
#     ],
#     temperature=1,
#     max_completion_tokens=8192,
#     top_p=1,
#     reasoning_effort="medium",
#     stream=True,
#     stop=None
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")



# this is a prompt style we can convert it to other prompt styles as well

# messages=[
# #       {
# #         "role": "user",
# #         "content": ""
# #       }
# #     ],
# #     temperature=1,
# #     max_completion_tokens=8192,
# #     top_p=1,
# #     reasoning_effort="medium",
# #     stream=True,
# #     stop=None


# ALPACA prompt style

alpaca_prompt = """### Instruction:
Generate a response based on the given user query.

### Input:


### Response:
"""


# If you want to place the original messages content dynamically:

user_input = ""

alpaca_prompt = f"""### Instruction:
Generate a response based on the given user query.

### Input:
{user_input}

### Response:
"""



