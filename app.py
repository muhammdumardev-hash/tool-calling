import json
import streamlit as st
from groq import Groq

from tools import get_student_result


st.set_page_config(
    page_title="Student Result AI",
    page_icon="🎓"
)

st.title("🎓 Student Result AI Assistant")
st.write("Ask about a student's result and the AI will use a tool when needed.")


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

MODEL = st.secrets["GROQ_MODEL"]


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_student_result",
            "description": "Get a student's result using their student ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "student_id": {
                        "type": "string",
                        "description": "Student ID such as STU-101"
                    }
                },
                "required": ["student_id"]
            }
        }
    }
]


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful student result assistant. "
                "Use the get_student_result tool when the user asks "
                "for a student's result. Never invent student results."
            )
        }
    ]


for message in st.session_state.messages:

    if message["role"] != "system":

        with st.chat_message(message["role"]):
            st.write(message["content"])


user_input = st.chat_input(
    "Ask about a student result..."
)


if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)


    response = client.chat.completions.create(
        model=MODEL,
        messages=st.session_state.messages,
        tools=tools,
        tool_choice="auto"
    )


    assistant_message = response.choices[0].message


    if assistant_message.tool_calls:

        st.info("🔧 AI is calling the student result tool...")


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_message.content or "",
                "tool_calls": [
                    {
                        "id": tool_call.id,
                        "type": "function",
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments
                        }
                    }
                    for tool_call in assistant_message.tool_calls
                ]
            }
        )


        for tool_call in assistant_message.tool_calls:

            if tool_call.function.name == "get_student_result":

                arguments = json.loads(
                    tool_call.function.arguments
                )

                student_id = arguments["student_id"]

                result = get_student_result(student_id)


                st.write(
                    f"**Tool:** `{tool_call.function.name}`"
                )

                st.write(
                    f"**Argument:** `{student_id}`"
                )

                st.write(
                    f"**Result:** {result}"
                )


                st.session_state.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    }
                )


        final_response = client.chat.completions.create(
            model=MODEL,
            messages=st.session_state.messages
        )


        final_answer = (
            final_response.choices[0].message.content
        )


    else:

        final_answer = assistant_message.content

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": final_answer
            }
        )


    with st.chat_message("assistant"):
        st.write(final_answer)