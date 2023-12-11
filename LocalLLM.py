from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplat
eimport streamlit as st
import random
import os
from langchain.llms import GooglePalm
from langchain.chains import LLMChain

APIKEY = '<Your API KEY>'
os.environ['TRANSFORMERS_CACHE'] = r'<Location where you want to store the LLM Models>'

st.title("Home LLM")
# You can add your questions here!
QuestRand = ["How many meters does one Minecraft block equal?",
"When you first spawn in the game what dimension do you start in?",
"What is the most famous evil mob in Minecraft?",
"What is the material you need if you want to make automatic machines and farms?",
"What is the best material you can get in Minecraft to make tools and armor with?",
"What type of food do cows and sheep eat?",
"Where can you find the Drowned Mob?",
"What is the most common crafting material used?",
"How many alternative dimensions can you visit as well as the overworld?",
"When you first visit The End what terrifying creature is waiting for you?",
"How much did that cost?",
"Are you flying a drone?",
"You work for the government?",
"How high can you fly that thing?",
"You ever crash that thing?"]

randinteger = random.randint(0,len(QuestRand)-1)
st.write(str(QuestRand[randinteger]))
userQuest = st.text_input('Ask me anything...', "")
option = st.selectbox(
    'Select a task',
    ('Text-to-text', 'Text Generation', 'Summarization'))
    
st.divider()

st.subheader("Choose wisely :sunglasses:")
st.markdown(":blue[Text-to-text], generation is frequently employed for tasks such as translating English sentences into French or summarizing lengthy paragraphs.")
st.markdown(":blue[Text Generation], also known as Causal Language Modeling, is the process of generating text that closely resembles human writing.")

if st.button("Start"):
    st.write('You selected:', option)
    model_idInput="google/flan-t5-large"
    taskInput="text2text-generation"
    maxNewTok = 600
    if option == "Text-to-text":
        model_idInput="google/flan-t5-large"
        taskInput="text2text-generation"
        maxNewTok = 600
    elif option == "Summarization":
        model_idInput = "sshleifer/distilbart-cnn-12-6"
        taskInput="summarization"
        maxNewTok = 100
    elif option == "Text Generation":
        model_idInput = "gpt2"
        taskInput="text-generation"
        maxNewTok = 600
    
    with st.spinner('Running Prompt '+userQuest):
        print("Running with")
        print("Model :", model_idInput)
        print("Task :", taskInput)
        print("Max Tokens :",maxNewTok)
        hf = HuggingFacePipeline.from_model_id(
            device_map="auto",
            model_id=model_idInput,
            task=taskInput,
            pipeline_kwargs={"max_new_tokens": maxNewTok},
        )
        template = """Question: {question}

        Answer: """
        prompt = PromptTemplate.from_template(template)

        chain = prompt | hf

        question = userQuest

        Ans = chain.invoke({"question": question})
        print(Ans)
        st.divider()
        st.write(Ans)
        st.divider()
        st.balloons()
        
if st.button("Ask Palm2"):
    st.markdown(":blue[MakerSuite], is currently one of the best APIs' that is free and decently powerful")
    os.environ["GOOGLE_API_KEY"] = APIKEY
    Palm = GooglePalm(temperature=0.1,max_itter=3)
    prompt = PromptTemplate(template="""Answer the question:{question} most appropriately""",
                                    input_variables=['question'])
    llmchain = LLMChain(llm=Palm, prompt=prompt)
    with st.spinner('Running Prompt '+ userQuest):
        print("Running with")
        print("Model :", Palm)
        Ans = llmchain.invoke({"question": userQuest})
        print(Ans)
        st.divider()
        st.write(Ans.get("text"))
        st.divider()
        st.balloons()
    
