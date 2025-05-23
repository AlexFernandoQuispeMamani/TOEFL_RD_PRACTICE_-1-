# -*- coding: utf-8 -*-
"""
Created on Wed May 21 13:58:51 2025

@author: ALEX
"""

import streamlit as st

st.set_page_config(
    page_title="TOEFL PRACTICE",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    .stApp {
        background: #e6f0e6;
        color: #004d00;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    .css-1v3fvcr h1, .css-18e3th9 h1 {
        color: #004d00;
        font-weight: 700;
        font-size: 2.5rem;
    }

    .passage-container {
        height: 600px;
        overflow-y: scroll;
        padding: 1.5rem;
        background-color: white;
        border: 2px solid #4caf50;
        border-radius: 12px;
        text-align: justify;
        font-size: 16px;
        line-height: 1.7;
        color: #004d00;
        box-shadow: 0 4px 10px rgba(0, 77, 0, 0.15);
    }

    .timer-text {
        text-align: right;
        font-weight: 600;
        font-size: 1.4rem;
        color: #2e7d32;
        margin-top: 0;
    }

    div.stButton > button {
        background-color: #4caf50;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        border: none;
        transition: background-color 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #388e3c;
        cursor: pointer;
    }

    /* ========== Estilos para radios y checkboxes ========== */
    label, 
    [data-baseweb="radio"] label, 
    [data-baseweb="checkbox"] label, 
    label[data-testid="stRadioLabel"] {
        color: #004d00 !important;
        font-weight: 600;
        font-size: 16px;
        opacity: 1 !important;
    }

    label[data-testid="stRadioLabel"] {
        font-size: 18px !important;
        font-weight: 700 !important;
    }

    [data-baseweb="radio"] div,
    [data-baseweb="radio"] div span,
    [data-baseweb="radio"] > div > div {
        color: #004d00 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }

    [data-baseweb="checkbox"] div,
    [data-baseweb="checkbox"] div span,
    [data-baseweb="checkbox"] > div > div {
        color: #004d00 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }

    .stRadio > div, .stCheckbox > div {
        opacity: 1 !important;
        color: #004d00 !important;
    }

    input[type="radio"]:disabled + div, 
    input[type="checkbox"]:disabled + div {
        opacity: 1 !important;
        color: #004d00 !important;
    }

    /* ==== Corrige colores de mensajes de alerta (warning, success, info) ==== */
    div[role="alert"] {
        font-weight: 700;
        font-size: 16px;
        border-radius: 10px;
        padding: 1rem;
        color: #664d03 !important;           /* color de texto legible */
        background-color: #fff3cd !important; /* fondo crema claro */
        border-left: 6px solid #f5c542;       /* estilo clásico de advertencia */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Ruta absoluta del archivo del pasaje
PASAGE_PATH = "natufian.txt"

# Leer el contenido del pasaje
with open(PASAGE_PATH, 'r', encoding='utf-8') as file:
    passage_text = file.read()

# Preguntas y opciones
questions = [
    {
        "text": "1. All of the following are mentioned in paragraph 1 as evidence that the Natufians may have engaged in the growing and processing of cereals and grains EXCEPT",
        "options": [
            "A. tools with a specific pattern of wear",
            "B. the widespread presence of grinding stones",
            "C. the presence of clay containers",
            "D. results from the analysis of Natufian teeth."
        ],
        "answer": "C",
        "type": "multiple_choice"
    },
    {
        "text": "2. Why does the author say that “many such...intensive use” in connection with Natufian agriculture?",
        "options": [
            "A. To argue that the Natufian people consumed grains long before they included fish in their diet",
            "B. To suggest that Natufian people could not replace their tools frequently because they had to travel very long distances to find grinding stones",
            "C. To illustrate the sophistication of the Natufians in the design of stone tools",
            "D. To support the claim that the archaeological record of the Natufian period shows clear evidence of agricultural origins"
        ],
        "answer": "D",
        "type": "multiple_choice"
    },
    {
        "text": "3. The phrase attest to in the passage is closest in meaning to",
        "options": [
            "A. symbolize",
            "B. provide evidence of",
            "C. are predictive of",
            "D. coincide with"
        ],
        "answer": "B",
        "type": "multiple_choice"
    },
    {
        "text": "4. Which of the sentences below best expresses the essential information in the highlighted sentence in the passage? Incorrect choices change the meaning in important ways or leave out essential information.",
        "options": [
            "A. Studies of the teeth of Natufians suggest the importance of cereals in their culture although they still hunted and foraged.",
            "B. The Natufians specialized in collecting cereals and may have been in the process of domesticating certain animals.",
            "C. Studies of the teeth of Natufians suggest that these people became hunter-foragers after they began domesticating cereals.",
            "D. The Natufians’ diet consisted mostly of cereals and lacked sufficient meat."
        ],
        "answer": "A",
        "type": "multiple_choice"
    },
    {
        "text": "5. Paragraph 2 suggests that compared with their predecessors, the Natufians",
        "options": [
            "A. had smaller camps",
            "B. had more permanent settlements",
            "C. engaged in trade less often",
            "D. had more meat in their diets"
        ],
        "answer": "B",
        "type": "multiple_choice"
    },
    {
        "text": "6. According to paragraph 2, the abundance of wild cereals in the Natufian diet probably meant that the Natufians",
        "options": [
            "A. had to move their settlements more often",
            "B. needed to supplement their diets with salt",
            "C. found it easy to store their food supplies",
            "D. no longer needed meat to provide essential minerals"
        ],
        "answer": "C",
        "type": "multiple_choice"
    },
    {
        "text": "7. All of the following are mentioned in paragraph 3 as part of the cultural change experienced by the Natufians EXCEPT:",
        "options": [
            "A. Technological advances",
            "B. Personal ornamentation",
            "C. Cave painting",
            "D. Community burial sites"
        ],
        "answer": "C",
        "type": "multiple_choice"
    },
    {
        "text": "8. According to paragraph 4, which of the following may have helped push the Natufians toward farming as a way of life?",
        "options": [
            "A. At the same time as the Natufian population was increasing, the climate was becoming less hospitable.",
            "B. The development of sickles and other tools made it possible for Natufians to exploit new kinds of cereals.",
            "C. The climate changed during the Natufian period and produced conditions favorable to growing cereals.",
            "D. Increasing competition from neighboring populations may have forced Natufians to grow cereals more intensively."
        ],
        "answer": "D",
        "type": "multiple_choice"
    },
    {
    "text": (
        "9. Look at the four squares S that indicate where the following sentence could be added to the passage. "
        "Where would the sentence best fit?\n\n"
        "Further evidence of an evolving cultural complexity comes from Natufian burials.\n\n"
        "As always, there is more to a major cultural change than simply a shift in economics. The Natufians made "
        "(and presumably wore) beads and pendants in many materials, including gemstones and marine shells that had "
        "to be imported, and it is possible that this ornamentation actually reflects a growing sense of ethnic identity "
        "and perhaps some differences in personal and group status. Cleverly carved figurines of animals, women, and other "
        "subjects occur in many sites, and Natufian period cave paintings have been found in Anatolia, Syria, and Iran. "
        "**A.** More than 400 Natufian burials have been found, most of them simple graves set in house floors. "
        "**B.** As archaeologist Belfer-Cohen notes, these burials may reflect an ancestor cult and a growing sense of "
        "community emotional ties and attachment to a particular place, and toward the end of the Natufian period, people "
        "in this area were making a strict separation between living quarters and burial grounds. "
        "**C.** In contrast with the Pleistocene cultures of the Levant, Natufian culture appears to have experienced "
        "considerable social change. **D.**"
    ),
    "options": [
        "A. A",
        "B. B",
        "C. C",
        "D. D"
    ],
    "answer": "B",
    "type": "multiple_choice"
},
    {
        "text": "10. An introductory sentence for a brief summary of the passage is provided below. Complete the summary by selecting the THREE answer choices that express the most important ideas in the passage. Some sentences do not belong in the summary because they express ideas that are not presented in the passage or are minor ideas in the passage.\n\nThe Natufians differed from their predecessors in many ways—most significantly, in their move toward agriculture.",
        "options": [
            "A. The Natufians used tools to collect and process food, but their lack of containers suggests that they rarely had excess food to store.",
            "B. Natufian culture developed somewhat differently in different regions, in part because of differences in the types and amount of food available from place to place.",
            "C. The increase in salt in the Natufians’ diet suggests that meat was becoming harder to find, perhaps because of climate change.",
            "D. Although their diet included meat from hunting, extensive evidence suggests that the Natufians consumed a lot of cereals and may even have been cultivating them.",
            "E. The Natufians engaged in trade and lived in large camps in which they sometimes built permanent structures.",
            "F. Natufian art, personal ornamentation, and burial sites suggest cultural changes involving an increasing sense of ethnic identity and perhaps an ancestor cult"
        ],
        "answer": ["D", "E", "F"],
        "type": "multiple_answer"
    }
]


# Estado inicial
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "show_results" not in st.session_state:
    st.session_state.show_results = False

import time

# Estado del temporizador
if "timer_started" not in st.session_state:
    st.session_state.timer_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None

st.title("📝 TOEFL PRACTICE")

st.markdown(
    """
    <style>
    /* Fondo general de la app */
    .stApp {
        background: #e6f0e6;  /* verde muy claro */
        color: #004d00;       /* verde oscuro para texto */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Estilo para el título principal */
    .css-1v3fvcr h1, .css-18e3th9 h1 {
        color: #004d00; /* verde oscuro */
        font-weight: 700;
        font-size: 2.5rem;
    }

    /* Contenedor del texto del pasaje */
    .passage-container {
        height: 600px;
        overflow-y: scroll;
        padding: 1.5rem;
        background-color: white;
        border: 2px solid #4caf50;  /* verde */
        border-radius: 12px;
        text-align: justify;
        font-size: 16px;
        line-height: 1.7;
        color: #004d00;
        box-shadow: 0 4px 10px rgba(0, 77, 0, 0.15);
    }

    /* Temporizador */
    .timer-text {
        text-align: right;
        font-weight: 600;
        font-size: 1.4rem;
        color: #2e7d32;
        margin-top: 0;
    }

    /* Botones con colores verdes */
    div.stButton > button {
        background-color: #4caf50;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        border: none;
        transition: background-color 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #388e3c;
        cursor: pointer;
    }

    /* Cambia el color del texto de las opciones del radio button */
    div[data-baseweb="radio"] label {
        color: #1a7f37 !important;  /* Verde */
        font-weight: 600;
        font-size: 16px;
    }

    /* Cambia el color del texto "Select one:" */
    div[class^='block-container'] > div:nth-child(3) > div {
        color: #1a7f37;
        font-weight: 700;
        font-size: 18px;
        margin-bottom: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Fila con botón START (izquierda) y temporizador (derecha)
col_start, col_timer = st.columns([2, 2])

with col_start:
    if st.button("▶️ START"):
        st.session_state.timer_started = True
        st.session_state.start_time = time.time()

with col_timer:
    if st.session_state.timer_started:
        elapsed = time.time() - st.session_state.start_time
        remaining = max(0, 1080 - int(elapsed))  # 18 minutos = 1080 segundos
        mins, secs = divmod(remaining, 60)
        st.markdown(f"<p class='timer-text'>🕒 {mins:02}:{secs:02}</p>", unsafe_allow_html=True)

        if remaining == 0 and not st.session_state.show_results:
            st.session_state.show_results = True
            st.experimental_rerun()


# Mostrar columnas
col1, col2 = st.columns([9, 9])

with col1:
    if not st.session_state.show_results:
        current_question = questions[st.session_state.question_index]
        st.markdown(f"### Question {st.session_state.question_index + 1}")
        st.markdown(current_question["text"])

        q_key = f"question_{st.session_state.question_index}"

        if current_question.get("type") == "multiple_answer":
            selected = st.session_state.get(q_key, [])

            for i, option in enumerate(current_question["options"]):
                if st.checkbox(option, key=f"{q_key}_{i}", value=option in selected):
                    if option not in selected and len(selected) < 3:
                        selected.append(option)
                else:
                    if option in selected:
                        selected.remove(option)

            st.session_state[q_key] = selected

            if len(selected) != 3:
                st.warning("You must select exactly THREE options.")

        else:
            previous_answer = st.session_state.get(q_key, None)
            answer = st.radio("Select one:", current_question["options"],
                              index=current_question["options"].index(previous_answer) if previous_answer in current_question["options"] else 0,
                              key=f"radio_{st.session_state.question_index}")
            st.session_state[q_key] = answer

        # Navegación
        col_back, col_next = st.columns([1, 1])
        with col_back:
            if st.session_state.question_index > 0:
                if st.button("⬅️ Back"):
                    st.session_state.question_index -= 1
                    st.rerun()
        with col_next:
            if st.session_state.question_index < len(questions) - 1:
                if st.button("Next ➡️"):
                    st.session_state.question_index += 1
                    st.rerun()
            else:
                if st.button("Show Results"):
                    st.session_state.show_results = True
                    st.rerun()

    else:
        st.markdown("## Results")

        correct_answers = 0
        detailed_feedback = []

        for i, q in enumerate(questions):
            q_key = f"question_{i}"
            user_answer_full = st.session_state.get(q_key, None)
            correct = q["answer"]

            if q.get("type") == "multiple_answer":
                # user_answer_full es lista de opciones completas
                user_letters = [opt.split(".")[0] for opt in user_answer_full] if user_answer_full else []
                correct_letters = correct
                is_correct = set(user_letters) == set(correct_letters)
                if is_correct:
                    correct_answers += 2  # Puntaje 2 para multi_answer

                user_display = ", ".join([f"{l}." for l in user_letters]) if user_letters else "Not selected"
                correct_display = ", ".join([f"{l}." for l in correct_letters])

            else:
                # Extraer solo la letra de la respuesta seleccionada
                if user_answer_full:
                    user_letter = user_answer_full.split(".")[0].strip()
                else:
                    user_letter = None
                correct_letter = correct

                is_correct = (user_letter == correct_letter)
                if is_correct:
                    correct_answers += 1  # Puntaje 1 para multiple_choice

                user_display = f"{user_letter}." if user_letter else "Not selected"
                correct_display = f"{correct_letter}."

            detailed_feedback.append(
                f"**Question {i+1}:** Your answer: {user_display} | Correct: {correct_display} {'✅' if is_correct else '❌'}"
            )

        for line in detailed_feedback:
            st.markdown(line)

        final_score = round((correct_answers / 11) * 30, 2)
        st.success(f"✅ Raw score: {correct_answers} / 11")
        st.info(f"🎯 TOEFL Reading estimated score: **{final_score} / 30**")

        if st.button("🔄 Restart Test"):
            for i in range(len(questions)):
                st.session_state.pop(f"question_{i}", None)
                st.session_state.pop(f"question_{i}_0", None)
                st.session_state.pop(f"question_{i}_1", None)
                st.session_state.pop(f"question_{i}_2", None)
                st.session_state.pop(f"question_{i}_3", None)
                st.session_state.pop(f"radio_{i}", None)
            st.session_state.question_index = 0
            st.session_state.show_results = False
            st.rerun()

with col2:
    st.markdown("<h3 style='text-align: center;'>Natufian Culture</h3>", unsafe_allow_html=True)

    # Aquí reemplaza el bloque anterior por este bloque
    st.markdown(f"""
        <div class='passage-container'>
            {passage_text}
        </div>
    """, unsafe_allow_html=True) 
