# Nikhil Yarra

I build AI systems and leave the experiments public.

**Verification for WhyHireWrong? — October 2, 2026**

Currently working as an **AI Engineer**, mostly somewhere between models, retrieval, tools, evaluation, and the software required to make them useful.

[Portfolio](https://nymav.github.io/ny-portfolio/) · [LinkedIn](https://www.linkedin.com/in/nikhil-yarra/) · [Email](mailto:nikhilyarra01@gmail.com)

---

## Now

I'm interested in what happens **around** a model.

How context gets selected.  
How tools get called.  
How an answer stays connected to evidence.  
How you know when the system failed.  
And where probabilistic behavior should stop and deterministic software should take over.

Most of my current work touches some combination of:

`LLMs` `retrieval` `agents` `evaluation` `multimodal systems` `Python`

---

## Experiments

### 01 — Mailayer

**What if an inbox behaved more like memory than a list of messages?**

A Gmail intelligence system built around retrieval and grounded generation.

```text
mailbox
   ↓
sync ──→ lexical + semantic retrieval
                    ↓
              query rewriting
                    ↓
                 rerank
                    ↓
            thread context
                    ↓
                  model
                    ↓
             answer + source
```

The interesting part isn't getting an LLM to answer a question about email.

It's deciding **which evidence it should see**, whether that evidence is strong enough, and what the system should do when it isn't.

Built with FastAPI, Gmail API, SQLite/FTS, embeddings, local models and a React/Vite interface.

---

### 02 — DRAX TBS

**How much infrastructure does useful document RAG actually need?**

```text
PDF → parse → chunk → embed → retrieve → context → local model
```

DRAX started as an experiment around turning documents into something a model could actually reason over without pretending the model already knew their contents.

The system handles PDF ingestion, embeddings, vector retrieval, context construction and configurable local inference.

The experiment is less about "chat with PDF" and more about the boundary between **retrieval quality and model quality**.

---

### 03 — Facial Emotion Detection

**Before I started spending most of my time around LLMs, I was breaking vision models.**

Transfer-learning experiments for multi-class facial emotion recognition using:

`VGG16` · `ResNet50` · `DenseNet121`

The work covered image preprocessing, augmentation, class imbalance, model training and comparative evaluation.

No magic accuracy number here. The useful part was seeing how much model behavior changes before the image ever reaches the network.

---

### 04 — ny-portfolio

**A portfolio that I didn't want to feel like a portfolio.**

Instead of another grid of project cards, I treated the interface itself as part of the experiment.

→ **[enter](https://nymav.github.io/ny-portfolio/)**

---

## Things I've changed my mind about

**"Just give the model more context."**  
More context is not necessarily better context.

**"Semantic search solves retrieval."**  
Sometimes lexical evidence is exactly what you need. Hybrid retrieval exists for a reason.

**"If the model produced valid JSON, the agent worked."**  
Schema correctness and decision correctness are very different things.

**"The model can decide everything."**  
Some decisions should remain boring, deterministic software.

**"A confident answer is a good answer."**  
Evidence first.

---

## Graveyard

Not every experiment deserves to become a product.

```text
× retrieval without evaluation
  → you can build a very convincing wrong-answer machine

× unlimited agent autonomy
  → interesting demo, uncomfortable engineering

× giant prompts as architecture
  → eventually the prompt becomes the bug

× treating fallback as an edge case
  → in model-backed software, failure is part of the normal path

× adding AI because AI can be added
  → still looking for the user problem
```

I keep these because failed assumptions are often more reusable than successful demos.

---

## Under the hood

I mostly work in Python.

Around that, whatever the system needs:

```text
models       GPT · Claude · Gemini · Llama · Mistral · Qwen
retrieval    embeddings · semantic search · hybrid search · reranking
agents       tools · routing · structured outputs · validation · fallbacks
backend      FastAPI · Flask · REST · async workflows
ml           scikit-learn · TensorFlow/Keras · transfer learning
data         Pandas · NumPy · SQL
shipping     Docker · AWS/cloud · Git · Pytest · Postman
```

The stack isn't the interesting part.

**What the pieces are doing together is.**

---

## Currently

```text
working on      AI systems @ Warren and Carter
thinking about  multimodal models + reliable model behavior
building        retrieval / agent / evaluation systems
learning        by implementing things I don't completely understand yet
```

M.S. Data Science — New Jersey Institute of Technology  
B.Tech Computer Science & Engineering — GITAM

---

If something here is interesting:

[**GitHub**](https://github.com/nymav) · [**Portfolio**](https://nymav.github.io/ny-portfolio/) · [**LinkedIn**](https://www.linkedin.com/in/nikhil-yarra/) · [**Email**](mailto:nikhilyarra01@gmail.com)

<sub>Some things here work. Some are experiments. That's the point.</sub>
