# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from foundry_local import FoundryLocalManager

alias = "phi-3-mini-4k"
manager = FoundryLocalManager(alias)
llm = ChatOpenAI(
    model=manager.get_model_info(alias).id,
    base_url=manager.endpoint,
    api_key=manager.api_key,
    temperature=0,
    streaming=False
)

class MyBot(ActivityHandler):
    # See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.

    async def on_message_activity(self, turn_context: TurnContext):

        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are a helpful assistant that translates {input_language} to {output_language}. Do not explain the translation, just translates to {output_language}"
            ),
            ("human", "{input}")
        ])

        chain = prompt | llm

        ai_msg = chain.invoke({
            "input_language": "English",
            "output_language": "French",
            "input": turn_context.activity.text
        })
        
        await turn_context.send_activity(f"{ ai_msg.content }")

        # await turn_context.send_activity(f"You said '{ turn_context.activity.text }'")

    async def on_members_added_activity(
        self,
        members_added: ChannelAccount,
        turn_context: TurnContext
    ):
        for member_added in members_added:
            if member_added.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")
