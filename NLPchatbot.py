import os
import openai
import gradio as gr

openai.api_key = '<API KEY>'

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",

def generate_response(prompt):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=1024,
      n=1,
      stop=None,
      timeout=10,
    )
    message = response.choices[0].text.strip()
    return message


def conversation_history(input,history):
    history=history or []
    s=list(sum(history,()))
    s.append(input)
    inp = ''.join(s)
    output = generate_response(inp)
    history.append((input,output))
    return history,history

blocks=gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("submit")
    submit.click(conversation_history,inputs=[message,state],outputs=[chatbot,state])

blocks.launch(debug=True)
