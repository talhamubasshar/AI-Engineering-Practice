# 12-Week Applied AI Engineer Roadmap: Month 2

---

### Executive Alignment & Progression Context

```
Current Status : Month 1 complete (Async Python, FastAPI, Structured Outputs, Tool Calling, Project 1)
Month 2 Focus  : Embeddings, Vector Databases, Advanced RAG, Evaluation (Ragas), ML Essentials & Project 2
Milestone      : Job applications kick off in Week 8 (Dual-Track: Islamabad/Rawalpindi & Remote)
Hardware       : AMD Ryzen 7 PRO 8840U (Local CPU embeddings via Ollama/FastEmbed, hosted APIs for LLM)
Budget         : $0 (Supabase pgvector / Qdrant Cloud free tier, Gemini text-embedding-004 / Groq free)
Time Budget    : 27 hours/week (3h/day Mon–Fri = 15h, 6h/day Sat–Sun = 12h)
Start Date     : Week 5 (November 30, 2026)
```

---

## What is Realistic vs. What is Fantasy in Month 2

> [!IMPORTANT]
> **What is Realistic:**
> - Building a production-grade **Advanced RAG** pipeline that outperforms 90% of naive tutorial implementations.
> - Implementing **Hybrid Search** (BM25 sparse keyword + dense vector search) combined with **Reciprocal Rank Fusion (RRF)** and **Cross-Encoder Reranking**.
> - Implementing page-level, grounded **Citations** that link directly to source text and render in Next.js.
> - Writing automated evaluation pipelines using **Ragas** / **DeepEval** measuring Faithfulness, Answer Relevance, and Context Precision.
> - Connecting production observability using **Langfuse** (tracing latency, cost, and retrieval quality).
> - Mastering entry-level ML concepts (vectors, cosine similarity math, bias/variance, precision/recall/F1, confusion matrices, scikit-learn).
> - Launching your professional job search outreach at the end of Week 8.

> [!WARNING]
> **What is NOT Realistic (and what you must NOT waste time on):**
> - Training or fine-tuning embedding models from scratch (contrastive learning / triplet loss math).
> - Building custom vector index algorithms (e.g., implementing HNSW graph traversal in C++ from scratch).
> - Complex Knowledge Graph construction (GraphRAG at scale is computationally expensive and overkill for entry-level roles; keep it at conceptual awareness).
> - Advanced deep learning math (calculating multi-variable calculus backpropagation gradients by hand).

---

# Month 2: Embeddings, Vector Databases, Advanced RAG, Evaluation & ML Essentials

## Month 2 Goal
> Master document ingestion, semantic chunking, vector indexing with **pgvector** and **Qdrant**, implement **Advanced RAG** (Hybrid Search, Reranking, Query Rewriting, Citations), establish quantitative **Evaluation & Tracing** (Ragas + Langfuse), grasp practical ML foundations, ship **Portfolio Project 2** (an Enterprise Document Intelligence Platform), and initiate your job search in Week 8.

### Month 2 Outcomes
By the end of Month 2, you can:
1. Explain the geometry of embeddings, calculate dot products and cosine similarity in pure Python/NumPy, and select optimal embedding models.
2. Ingest, parse, and chunk messy real-world PDFs and Markdown documents using structural and semantic chunking strategies without losing table data or section context.
3. Deploy and query vector databases (**pgvector** in PostgreSQL and **Qdrant**), utilizing metadata filtering and HNSW index tuning.
4. Eliminate retrieval failure modes by implementing **Hybrid Search** (BM25 + Dense Vectors) fused with **Reciprocal Rank Fusion (RRF)** and **Cross-Encoder Reranking** (Cohere free tier / local FlashRank).
5. Prevent hallucinations and context poisoning using **Query Rewriting**, **HyDE** (Hypothetical Document Embeddings), and grounded citation extraction.
6. Quantify RAG performance using industry-standard metrics (**Faithfulness**, **Answer Relevance**, **Context Precision**, **Context Recall**) via **Ragas** and **DeepEval**.
7. Instrument full-stack LLM applications with **Langfuse** to monitor traces, user feedback, token consumption, and retrieval latencies in real time.
8. Understand practical ML foundations: precision/recall/F1 tradeoffs, supervised vs. unsupervised learning, train/test splits, and baseline classification with scikit-learn.
9. Ship, publicly deploy, and record a video walkthrough for **Portfolio Project 2: DocuMind**, and launch tailored applications to Islamabad tech companies and remote B2B startups.

---

## Concept Classification for Month 2

| Concept | Tier | Why |
| :--- | :---: | :--- |
| **Embeddings & Vector Dimensions** | `CORE` | Foundational representation of unstructured semantic data. |
| **Similarity Metrics (Cosine, Dot Product, Euclidean/L2)** | `CORE` | Mathematical basis for all vector search and retrieval operations. |
| **Chunking Strategies (Fixed, Recursive, Structure-aware, Semantic)** | `CORE` | Chunking quality dictates 80% of RAG retrieval success or failure. |
| **Vector DBs & Metadata Filtering (pgvector, Qdrant)** | `CORE` | Real-world enterprise RAG requires filtering by tenant, date, or user ID. |
| **Hybrid Search (BM25 Sparse + Dense Vectors) & RRF** | `CORE` | Pure vector search fails on acronyms, part numbers, and exact keywords. |
| **Cross-Encoder Reranking (Cohere / FlashRank)** | `CORE` | The single highest ROI optimization for retrieval precision. |
| **Grounded Citations & Source Attribution** | `CORE` | Mandatory requirement for enterprise trust and legal compliance. |
| **RAG Triad & Metrics (Faithfulness, Answer Relevance, Context Precision)** | `CORE` | How real AI engineers prove a pipeline works instead of relying on "vibes". |
| **Observability & Tracing (Langfuse)** | `CORE` | Crucial for debugging multi-step retrieval failures and tracking production costs. |
| **NumPy & Pandas Essentials** | `CORE` | Standard data manipulation tools for parsing evals and tabular data. |
| **ML Evaluation Metrics (Precision, Recall, F1, Confusion Matrix)** | `CORE` | Standard technical interview topics; directly maps to RAG precision and recall. |
| **Supervised vs Unsupervised, Overfitting/Underfitting, Bias-Variance** | `CORE` | Core conceptual knowledge tested in every applied AI engineering interview. |
| **HNSW & IVF Indexing Intuition** | `GOOD-TO-KNOW` | Needed to configure vector database performance at scale ($>100\text{k}$ vectors). |
| **Query Rewriting, Multi-Query & HyDE** | `GOOD-TO-KNOW` | Techniques to bridge the gap between user intent and vector search queries. |
| **Contextual Compression & Prompt Packing** | `GOOD-TO-KNOW` | Reduces prompt token bloat and keeps context clean. |
| **Scikit-Learn Basics (Logistic Regression, Decision Trees, K-Means)** | `GOOD-TO-KNOW` | Practical baseline ML modeling; proves you understand fundamental algorithms. |
| **RAG vs. Long-Context Models Decision Framework** | `GOOD-TO-KNOW` | Architectural tradeoff (cost vs. latency vs. recall degradation). |
| **Document Parsing Engines (pypdf, pdfplumber, Docling)** | `GOOD-TO-KNOW` | Real-world data ingestion is messy; parsing determines data cleanliness. |
| **Neural Network Basics & PyTorch Tensors** | `AWARENESS` | Conceptual understanding of neurons, activations, loss, and gradient descent. |
| **GraphRAG & Knowledge Graphs** | `AWARENESS` | Know when entities/relations outperform chunk-based RAG; do not build yet. |

---

## Week 5: Vectors, Embeddings, Chunking & Vector Databases (pgvector & Qdrant)

### Week Theme
> The mechanics of vector representations, chunking strategies, and storing/filtering high-dimensional embeddings in PostgreSQL (`pgvector`) and Qdrant.

### Concepts to Master
- `CORE`: Vector embeddings: what they represent, embedding models (Google `text-embedding-004`, Ollama `nomic-embed-text`, `all-MiniLM-L6-v2`).
- `CORE`: Vector mathematics: Dot Product, Cosine Similarity, and Euclidean Distance ($L_2$) implemented in pure NumPy.
- `CORE`: Chunking strategies: Fixed character, Recursive Character (`RecursiveCharacterTextSplitter`), Markdown structure-aware chunking, and semantic chunking tradeoffs (chunk size vs. chunk overlap).
- `CORE`: Vector Databases: **pgvector** (Postgres extension for Supabase/Neon) and **Qdrant** (specialized Rust-based vector database).
- `CORE`: Metadata filtering: Combining vector similarity search with structured SQL `WHERE` clauses (e.g., `user_id == '123' AND department == 'finance'`).
- `GOOD-TO-KNOW`: Indexing algorithms intuition: Flat search (exact kNN) vs. Approximate Nearest Neighbors (**HNSW** - Hierarchical Navigable Small World, **IVF** - Inverted File Index).
- `GOOD-TO-KNOW`: Document parsing basics: Extracting clean text from PDFs and Markdown using `pypdf` and `pdfplumber`.

---

### Daily Schedule: Week 5 (27 Hours)

#### Monday (3 hrs) — Vector Math & Embedding Intuition
- **Hour 1–2**: The geometry of embeddings. Write a script from scratch in Python using `numpy` that implements Dot Product, Cosine Similarity, and Euclidean Distance without external ML libraries.
- **Hour 3**: Generate embeddings for 10 sentences using Google AI Studio (`text-embedding-004` free tier) and local Ollama (`ollama pull nomic-embed-text`). Calculate pairwise cosine similarity matrices and verify semantic clustering.

#### Tuesday (3 hrs) — Chunking Strategies & Ingestion Engineering
- **Hour 1–2**: Chunking deep dive. Compare Fixed-size chunking vs. Recursive chunking vs. Document structure-aware chunking. Understand why chunk overlap (e.g., 10–20%) prevents cutting off thoughts mid-sentence.
- **Hour 3**: Write `chunking_lab.py`: parse a 10-page public financial report PDF using `pypdf`. Chunk it using three different strategies and inspect chunk quality, sentence boundary preservation, and token distribution.

#### Wednesday (3 hrs) — pgvector & PostgreSQL Vector Store
- **Hour 1–2**: Spin up a free Supabase PostgreSQL database or local Postgres container with the `vector` extension enabled (`CREATE EXTENSION vector;`). Create a table with an `id`, `content`, `metadata (jsonb)`, and `embedding vector(768)`.
- **Hour 3**: Write an async Python script with `asyncpg` to insert 100 embedded chunks. Query the table using pgvector's cosine distance operator `<=>` (`ORDER BY embedding <=> query_vector LIMIT 5`).

#### Thursday (3 hrs) — Specialized Vector DB: Qdrant Setup & Metadata Filtering
- **Hour 1–2**: Set up a free cluster on [Qdrant Cloud](https://cloud.qdrant.io) (or run Qdrant via local Docker). Connect using `qdrant-client`. Understand collections, payloads, and vector points.
- **Hour 3**: Implement strict payload/metadata filtering: perform a vector search restricted to a specific `tenant_id` and `created_year >= 2024`. Understand why pre-filtering is critical for multi-tenant enterprise data.

#### Friday (3 hrs) — HNSW Indexing & Search Optimization
- **Hour 1–2**: Learn how Approximate Nearest Neighbor (ANN) search works. Understand HNSW graph construction (`m`, `ef_construction`, `ef_search`) vs. Flat exhaustive search.
- **Hour 3**: Benchmark search latency on pgvector with and without an HNSW index (`CREATE INDEX ON items USING hnsw (embedding vector_cosine_ops);`).

#### Saturday (6 hrs) — Full Ingestion Pipeline Engine
- **Hour 1–3**: Design and build an automated ingestion pipeline in Python: accepts uploaded PDF/Markdown files, extracts text, removes boilerplate, chunks text recursively, enriches chunks with metadata (source, page number, chunk index), and generates embeddings in batches.
- **Hour 4–6**: Connect the pipeline to store vectors in both pgvector and Qdrant. Implement duplicate document detection (hashing file contents via SHA-256) to prevent redundant ingestion.

#### Sunday (6 hrs) — Mini-Project 5 & Review
- **Hour 1–4**: Build, test, and polish **Mini-Project 5: Multi-Tenant Semantic Document Ingestion Engine**.
- **Hour 5**: Verify metadata isolation: ensure Tenant A cannot retrieve documents belonging to Tenant B under any semantic query.
- **Hour 6**: Complete Week 5 Self-Test and log key engineering lessons.

---

### Hands-on Tasks: Week 5
1. [ ] Implement vector cosine similarity from scratch in pure NumPy and verify it matches `scipy.spatial.distance.cosine`.
2. [ ] Embed text using both Google `text-embedding-004` (cloud) and `nomic-embed-text` (via Ollama CPU local) and compare latency and dimensionality.
3. [ ] Set up a PostgreSQL database with `pgvector` and write raw SQL vector similarity queries using the `<=>` operator.
4. [ ] Ingest a multi-page PDF, extract page numbers and section headers into JSON metadata, and store vectors with metadata in Qdrant.

---

### Mini-Project 5: Multi-Tenant Semantic Document Ingestion Engine
- **Description**: A modular FastAPI backend service that allows multiple corporate tenants to upload policy PDFs and documentation, processes them through an intelligent chunking pipeline with metadata tagging (department, confidentiality level, upload date), and exposes a fast semantic search endpoint with strict tenant filtering.
- **Stack**: FastAPI, Pydantic v2, `pgvector` / Supabase, Google `text-embedding-004` or Ollama embeddings, `pypdf`, `numpy`.
- **Requirements**:
  - `POST /api/v1/documents/upload`: Multipart form-data PDF upload with `tenant_id` and `department` tags.
  - Automatic document parsing, SHA-256 deduplication, and recursive chunking (500 tokens, 10% overlap).
  - Batch embedding generation with error handling and rate-limit backoff.
  - `POST /api/v1/search`: Accepts query string, `tenant_id`, and top-k; returns relevant chunks with similarity scores and page numbers.
  - Multi-tenant security guarantee: Tenant query cannot return chunks from any other tenant under any circumstances.

---

### Self-Test: Week 5
1. **Q**: What is the mathematical definition of Cosine Similarity between two vectors $\mathbf{A}$ and $\mathbf{B}$?  
   *Answer*: $\text{Cosine Similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|} = \frac{\sum A_i B_i}{\sqrt{\sum A_i^2} \sqrt{\sum B_i^2}}$.
2. **Q**: When is the Dot Product of two vectors mathematically identical to their Cosine Similarity?  
   *Answer*: When both vectors are normalized to unit length (magnitude $\|\mathbf{A}\| = 1$ and $\|\mathbf{B}\| = 1$).
3. **Q**: What is the primary drawback of naive fixed-character chunking (e.g., splitting every 500 characters)?  
   *Answer*: It cuts sentences, words, and semantic thoughts mid-stream, separating related context and corrupting embedding representations.
4. **Q**: What does the `<=>` operator represent in `pgvector`?  
   *Answer*: Cosine distance ($1 - \text{cosine similarity}$). Note: `<->` is Euclidean ($L_2$) distance, and `<#>` is negative inner product.
5. **Q**: Why is metadata filtering critical in production enterprise RAG systems?  
   *Answer*: To enforce data privacy, multi-tenant isolation, role-based access control (RBAC), and to restrict search spaces to relevant timeframes or document types.
6. **Q**: What is the tradeoff between an exact kNN search (Flat) and an Approximate Nearest Neighbor (ANN) index like HNSW?  
   *Answer*: Flat search guarantees 100% recall but scales linearly $O(N)$ with slow query times at scale; HNSW provides logarithmic $O(\log N)$ sub-millisecond retrieval with a negligible sacrifice in recall ($~95\text{--}99\%$) and higher memory/build overhead.
7. **Q**: What are the key parameters of an HNSW index, and what do they control?  
   *Answer*: `m` (maximum number of bi-directional links per node in the graph) and `ef_construction` / `ef_search` (size of the dynamic candidate list evaluated during index construction and query time; higher values increase recall at the cost of speed/RAM).
8. **Q**: Why is chunk overlap necessary during text splitting?  
   *Answer*: To maintain continuity of semantic context across chunk boundaries, ensuring that concepts spanning the split point are not lost to either chunk.
9. **Q**: If two documents have a cosine distance of $0.05$, how semantically similar are their embeddings?  
   *Answer*: Extremely similar (cosine similarity is $1 - 0.05 = 0.95$).
10. **Q**: What happens if you try to insert an embedding vector with 1536 dimensions into a pgvector column configured as `vector(768)`?  
    *Answer*: PostgreSQL will reject the insert with a dimension mismatch error; the vector column dimension must strictly match the embedding model's output dimension.

---

## Week 6: Advanced Retrieval, Hybrid Search, Reranking & Citations

### Week Theme
> Overcoming naive RAG failure modes by combining sparse keyword search with dense vector search (Hybrid Search), Cross-Encoder Reranking, query transformation, and grounded citation generation.

### Concepts to Master
- `CORE`: Naive RAG failure modes: vocabulary mismatch, keyword blindness, lost-in-the-middle, context stuffing, and hallucinated answers.
- `CORE`: **Hybrid Search**: Combining Sparse search (BM25 / full-text search) + Dense vector search to capture both exact keywords (product codes, error logs, legal names) and semantic concepts.
- `CORE`: **Reciprocal Rank Fusion (RRF)**: Merging ranked lists from sparse and dense retrieval into a unified score without score normalization issues.
- `CORE`: **Cross-Encoder Reranking**: Re-scoring top candidate chunks ($k=25 \to k=5$) using a Cross-Encoder model (Cohere Rerank API free tier or local `flashrank` / `bge-reranker`).
- `CORE`: **Grounded Citations**: Structuring system prompts and output schemas to force the LLM to cite exact chunk IDs, file names, and page numbers for every factual claim.
- `GOOD-TO-KNOW`: Query transformation: **Query Rewriting** (resolving pronouns and conversational context), **Multi-Query** generation, and **HyDE** (Hypothetical Document Embeddings).
- `GOOD-TO-KNOW`: Contextual Compression: Removing irrelevant sentences from retrieved chunks before feeding them to the LLM prompt.
- `AWARENESS`: GraphRAG intuition (extracting knowledge entities and relationships to answer global dataset questions).

---

### Daily Schedule: Week 6 (27 Hours)

#### Monday (3 hrs) — Naive RAG Failure Modes & BM25 Sparse Search
- **Hour 1–2**: Analyze why dense embeddings fail on exact keywords (e.g., searching for error code `ERR_7092_TIMEOUT` or part number `AB-402`). Learn BM25 algorithm fundamentals (term frequency + inverse document frequency with document length normalization).
- **Hour 3**: Implement BM25 in Python using `rank_bm25` (or PostgreSQL `tsvector` full-text search). Benchmark retrieval results on technical documents vs. dense vector search.

#### Tuesday (3 hrs) — Hybrid Search & Reciprocal Rank Fusion (RRF)
- **Hour 1–2**: Understand Reciprocal Rank Fusion:
  $$\text{RRF\_Score}(d) = \sum_{m \in M} \frac{1}{60 + r_m(d)}$$
  Why RRF works: it relies on ranking positions rather than raw uncalibrated similarity scores.
- **Hour 3**: Build `hybrid_retriever.py`: run BM25 and pgvector dense search concurrently, combine their results using RRF, and output the top 20 candidate chunks.

#### Wednesday (3 hrs) — Cross-Encoder Reranking Lab
- **Hour 1–2**: Understand Bi-Encoders vs. Cross-Encoders. Why Bi-Encoders are fast for retrieval (independent vectors) but miss subtle nuances, and why Cross-Encoders (joint attention over query + chunk) are accurate but computationally heavier.
- **Hour 3**: Integrate a reranker: use the free tier of [Cohere Rerank](https://cohere.com) (`rerank-v3.5`) or local Python `flashrank` (runs on CPU in $<20\text{ms}$). Take the top 20 chunks from Hybrid Search and rerank them down to the 5 most relevant.

#### Thursday (3 hrs) — Query Transformation: Rewriting & HyDE
- **Hour 1–2**: Implement conversational Query Rewriting: take a multi-turn chat history (User: "What is ACME Corp's refund policy?", Follow-up: "Does it apply to digital software?") and rewrite the follow-up into a standalone search query.
- **Hour 3**: Implement **HyDE** (Hypothetical Document Embeddings): prompt an LLM to generate a hypothetical answer to a query, embed that hypothetical answer, and search vector space with it. Compare recall on conceptual questions.

#### Friday (3 hrs) — Grounded Citations & Hallucination Suppression
- **Hour 1–2**: Prompt engineering for citations. Enforce strict grounding: instruct the model to answer *only* based on the provided context, and format every factual sentence with a bracketed citation anchor (e.g., `[Doc1:Page4]`).
- **Hour 3**: Implement Pydantic structured output for citations: model `AnswerWithCitations` containing `answer_markdown: str` and `citations: list[Citation]` (chunk ID, document name, page number, quoted excerpt).

#### Saturday (6 hrs) — Full-Stack Citation UI: Next.js + FastAPI
- **Hour 1–3**: Build a FastAPI endpoint `/api/v1/rag/query` that runs: Query Rewrite $\to$ Hybrid Search (BM25 + pgvector) $\to$ Cross-Encoder Rerank $\to$ Grounded LLM Generation with Citations.
- **Hour 4–6**: Connect to Next.js frontend: build an interactive citation popover. When a user clicks `[1]` in the answer, highlight the referenced text and open a side-drawer showing the exact document page and snippet.

#### Sunday (6 hrs) — Mini-Project 6 & Review
- **Hour 1–4**: Build, test, and polish **Mini-Project 6: Enterprise Hybrid Search & Citation Engine**.
- **Hour 5**: Test edge cases: adversarial queries with no relevant context (ensure the model explicitly says "I cannot find this in the documents" rather than hallucinating).
- **Hour 6**: Complete Week 6 Self-Test and log learnings.

---

### Hands-on Tasks: Week 6
1. [ ] Implement Reciprocal Rank Fusion (RRF) algorithm from scratch in Python.
2. [ ] Connect Cohere Rerank or local `flashrank` to rerank 25 candidate chunks down to 5.
3. [ ] Implement a conversational query rewriter that resolves pronouns from previous turns.
4. [ ] Build a Next.js citation pill component that opens a modal displaying source chunk text and metadata.

---

### Mini-Project 6: Enterprise Hybrid Search & Citation Engine
- **Description**: An advanced RAG query microservice capable of answering complex enterprise questions over multi-page PDF policies. It combines full-text search with vector search, applies cross-encoder reranking, and produces answers with verifiable, clickable citations.
- **Stack**: FastAPI, PostgreSQL (`tsvector` + `pgvector`), Groq Llama 3.3 / Gemini Flash, Cohere Rerank or FlashRank, Pydantic v2.
- **Requirements**:
  - Ingestion of at least 3 complex multi-page policy PDFs (e.g., corporate HR handbook, IT security policy, financial terms).
  - Hybrid retrieval pipeline: PostgreSQL full-text search (BM25) + pgvector cosine similarity.
  - RRF fusion layer combining both retrieval streams.
  - Cross-encoder reranker filtering candidates to top 4 chunks.
  - Strict Pydantic output schema containing the synthesized response and a list of verified citations with source snippet quotes.
  - Verification test: Passing a question whose answer is not in the text must yield: `"I don't have enough information in the provided documentation to answer this question."`

---

### Self-Test: Week 6
1. **Q**: What is the core limitation of dense vector search when dealing with specific part numbers, legal identifiers, or error codes?  
   *Answer*: Embedding models compress text into a dense semantic space where individual rare tokens, acronyms, or random strings may have similar or noisy representations to other numbers/tokens, resulting in poor retrieval for exact string matches.
2. **Q**: How does the BM25 algorithm score the relevance of a document to a query?  
   *Answer*: It evaluates term frequency (how often query terms appear in the document, saturated so extreme repetition has diminishing returns) penalized by inverse document frequency (how rare the term is across all documents) and normalized by document length.
3. **Q**: What is the mathematical formulation of Reciprocal Rank Fusion (RRF), and why does it use a constant $k \approx 60$?  
   *Answer*: $\text{RRF}(d) = \sum \frac{1}{k + r(d)}$. The smoothing constant $k$ (conventionally 60) prevents high-ranking outliers from dominating the score when one list ranks an item very high and another ranks it lower.
4. **Q**: What is the architectural difference between a Bi-Encoder (embedding model) and a Cross-Encoder (reranker)?  
   *Answer*: A Bi-Encoder processes the query and document independently into two separate vectors and compares them via cosine similarity (fast, scalable for millions of items); a Cross-Encoder feeds the query and document together into the transformer with full cross-attention between every query token and document token (slower, but significantly more accurate).
5. **Q**: Why shouldn't you run a Cross-Encoder across your entire database of 100,000 document chunks?  
   *Answer*: Cross-Encoders require a full forward pass through the transformer for each query-document pair; running it 100,000 times would take tens of seconds or minutes of compute, making it suitable only as a second-stage reranker over the top $20\text{--}50$ candidates.
6. **Q**: What is the "Lost in the Middle" phenomenon in LLM context windows?  
   *Answer*: Empirical research shows LLMs are most effective at retrieving and reasoning over information placed at the very beginning or very end of their context window, while information placed in the middle is frequently overlooked or ignored.
7. **Q**: What is Hypothetical Document Embeddings (HyDE)?  
   *Answer*: A retrieval technique where an LLM first generates a hypothetical (hallucinated) answer to the user's query; that hypothetical answer is then embedded to perform vector search, moving the search vector closer to the document answer space rather than the query space.
8. **Q**: How do you prevent an LLM from hallucinating answers when the retrieved context does not contain the answer?  
   *Answer*: Through strict system prompt constraints ("Answer only based on the provided context. If the context does not contain the facts, state that you do not know"), low temperature ($0.0$), and requiring explicit quote citations.
9. **Q**: In PostgreSQL, what data type and function are used to implement BM25-style full-text search?  
   *Answer*: The `tsvector` type (for storing parsed lexemes), `to_tsquery()` (for parsing queries), and `ts_rank()` (for scoring document relevance).
10. **Q**: What is Contextual Compression in RAG pipelines?  
    *Answer*: An intermediate step that passes retrieved chunks through a small model or filter to strip out irrelevant sentences or boilerplate before injecting them into the final LLM prompt, reducing context window clutter and cost.

---

## Week 7: RAG Evaluation, Observability & Practical ML Essentials

### Week Theme
> Measuring what matters: quantitative RAG evaluation with Ragas, production tracing with Langfuse, and mastering foundational data/ML concepts for engineering interviews.

### Concepts to Master
- `CORE`: Quantitative RAG Evaluation: Golden evaluation sets, ground truth datasets, and the **RAG Triad**.
- `CORE`: **RAG Metrics**: **Faithfulness** (groundedness / no hallucination), **Answer Relevance** (does it answer the prompt?), **Context Precision** (is signal ranked above noise?), and **Context Recall** (did retrieval catch all necessary facts?).
- `CORE`: Evaluation frameworks: **Ragas** (`ragas`) and **DeepEval** (`deepeval`) utilizing LLM-as-a-Judge.
- `CORE`: Production Observability: Instrumenting LLM calls, latency, cost, and retrieval traces with **Langfuse** (open-source, generous cloud free tier).
- `CORE`: Practical ML Foundations:
  - Vectors, dot product, and cosine similarity.
  - Supervised vs. Unsupervised learning.
  - Train/Test splits, cross-validation, overfitting vs. underfitting, bias-variance tradeoff.
  - Classification metrics: Accuracy, Precision, Recall, $F_1$-score, Confusion Matrix, ROC-AUC intuition.
- `GOOD-TO-KNOW`: Scikit-learn basics: Training a baseline logistic regression and decision tree classifier, evaluating with a confusion matrix.
- `AWARENESS`: Neural network basics: Neuron, weights, bias, activation functions (ReLU, Softmax), loss functions, and gradient descent intuition.

---

### Daily Schedule: Week 7 (27 Hours)

#### Monday (3 hrs) — RAG Evaluation Theory & Golden Datasets
- **Hour 1–2**: The limits of "vibe checks". Learn how to construct a Golden Test Dataset: 20 synthetic or human-verified question-context-ground_truth triplets.
- **Hour 3**: Write a script that parses a test dataset and structures it into the format expected by modern evaluation frameworks (Question, Contexts, Generated Answer, Ground Truth).

#### Tuesday (3 hrs) — Ragas & LLM-as-a-Judge Metrics
- **Hour 1–2**: Deep dive into Ragas metrics: Understand how LLM-as-a-Judge prompts measure Faithfulness (claims in answer supported by context) and Context Precision (position of relevant chunks in context).
- **Hour 3**: Run an automated evaluation script using `ragas` over your Week 6 pipeline. Generate a quantitative scorecard (Faithfulness: 0.92, Answer Relevance: 0.88, Context Precision: 0.85).

#### Wednesday (3 hrs) — Observability & Tracing with Langfuse
- **Hour 1–2**: Sign up for [Langfuse Cloud](https://cloud.langfuse.com) (free tier). Integrate the Langfuse Python SDK (`from langfuse.decorators import observe, langfuse_context`).
- **Hour 3**: Instrument your FastAPI RAG endpoint: wrap embedding generation, database retrieval, reranking, and final LLM completion into nested trace spans. Inspect traces, latencies, and token costs in the Langfuse web dashboard.

#### Thursday (3 hrs) — ML Essentials: Vectors, Stats & Pandas
- **Hour 1–2**: Data handling essentials. Install `pandas` and `scikit-learn`. Learn DataFrame manipulation: loading CSV/JSON data, filtering rows, handling null values, calculating mean, median, standard deviation, and value counts.
- **Hour 3**: Implement vector operations and normalization using NumPy. Verify calculations on real embeddings.

#### Friday (3 hrs) — ML Essentials: Classification Metrics & Scikit-Learn
- **Hour 1–2**: The core ML metrics every AI engineer must know:
  - $\text{Precision} = \frac{TP}{TP + FP}$ (when we predict positive, how often are we right?)
  - $\text{Recall} = \frac{TP}{TP + FN}$ (what fraction of actual positives did we catch?)
  - $F_1\text{-score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$
  - Confusion Matrix interpretation (TP, FP, TN, FN).
- **Hour 3**: Train a simple baseline classifier in `scikit-learn` (e.g., spam detection or text classification) using `TfidfVectorizer` and `LogisticRegression`. Split data using `train_test_split` and print a `classification_report`.

#### Saturday (6 hrs) — ML Modeling: Overfitting, Bias-Variance & Regression Testing
- **Hour 1–3**: Deep dive into Overfitting vs. Underfitting and the Bias-Variance tradeoff. Understand how regularization (L1/L2) and cross-validation prevent overfitting. Connect this intuition to LLMs (overfitting on system prompts, catastrophic forgetting).
- **Hour 4–6**: Build an automated regression test script for your RAG system: if a code change or new prompt lowers Ragas Faithfulness below 0.85, fail the CI test.

#### Sunday (6 hrs) — Mini-Project 7 & Review
- **Hour 1–4**: Build, test, and polish **Mini-Project 7: Automated RAG Eval CI/CD Pipeline with Langfuse Tracing**.
- **Hour 5**: Run evaluation benchmarks comparing Naive RAG vs. Advanced Hybrid Reranked RAG to mathematically prove the performance lift.
- **Hour 6**: Complete Week 7 Self-Test and log results.

---

### Hands-on Tasks: Week 7
1. [ ] Create a 20-question Golden Dataset with verified ground-truth answers for a technical document.
2. [ ] Run an automated evaluation script with `ragas` calculating Faithfulness, Answer Relevance, and Context Recall.
3. [ ] Instrument a FastAPI application with Langfuse and inspect full execution traces, latency bottlenecks, and token costs in the web dashboard.
4. [ ] Train a baseline text classifier in scikit-learn using TF-IDF and Logistic Regression and generate a precision/recall/F1 confusion matrix.

---

### Mini-Project 7: Automated RAG Eval Pipeline & Langfuse Tracing Dashboard
- **Description**: An evaluation and observability test harness that runs automated benchmark suites against your RAG backend, logs complete multi-step traces to Langfuse, computes quantitative metrics via Ragas, and outputs an automated Markdown evaluation report.
- **Stack**: Python 3.12, `ragas`, `langfuse`, `pandas`, `scikit-learn`, `pytest`.
- **Requirements**:
  - Evaluation suite executing 20 diverse test cases across 3 categories: Fact Retrieval, Multi-Hop Synthesis, and Out-of-Scope / Adversarial questions.
  - Automated calculation of Ragas scores (Faithfulness, Answer Relevance, Context Precision).
  - Comparative benchmark: Runs test suite against both Naive RAG (vector only) and Advanced RAG (Hybrid + Reranking) and outputs a markdown comparison table.
  - Full Langfuse trace recording for every evaluation run.
  - Threshold assertions: Automated exit code 1 if Faithfulness falls below 0.80.

---

### Self-Test: Week 7
1. **Q**: What are the four core metrics of the RAG Triad, and what does each measure?  
   *Answer*: 
   1. *Context Precision*: Are retrieved chunks relevant and ranked high?
   2. *Context Recall*: Did retrieval capture all information needed to answer the question?
   3. *Faithfulness*: Is the generated answer grounded strictly in the retrieved context?
   4. *Answer Relevance*: Does the answer directly address the user's original query?
2. **Q**: In an LLM-as-a-Judge setup, how does a model evaluate the "Faithfulness" of an answer?  
   *Answer*: The judge LLM extracts all individual factual claims from the generated answer, checks each claim against the provided context chunks, and computes the ratio of supported claims to total claims.
3. **Q**: In medical or legal AI applications, would you optimize for Precision or Recall, and why?  
   *Answer*: Recall; missing a critical positive case (false negative, like an undetected tumor or mandatory compliance clause) has catastrophic consequences compared to reviewing a false alarm (false positive).
4. **Q**: What is the mathematical definition of the $F_1$-score, and why is it preferred over simple Accuracy on imbalanced datasets?  
   *Answer*: $F_1 = 2 \cdot \frac{P \cdot R}{P + R}$ (harmonic mean of Precision and Recall). On imbalanced datasets (e.g., 99% non-fraud, 1% fraud), a trivial model predicting "non-fraud" achieves 99% accuracy but has zero predictive utility; $F_1$ accounts for both false positives and false negatives.
5. **Q**: What is the difference between Overfitting and Underfitting?  
   *Answer*: Overfitting occurs when a model learns noise and idiosyncrasies of training data, failing to generalize to unseen data (high variance, low training error, high test error); Underfitting occurs when a model is too simple to capture underlying patterns (high bias, high training error, high test error).
6. **Q**: What is the purpose of OpenTelemetry-style tracing in LLM applications via tools like Langfuse?  
   *Answer*: LLM applications involve non-deterministic, multi-step asynchronous processes (query rewriting, multiple database retrievals, reranking, model generation); tracing breaks down the call tree into discrete spans, pinpointing exact latency bottlenecks, token costs, and where hallucinations originated.
7. **Q**: What is a "Golden Evaluation Dataset" in RAG engineering?  
   *Answer*: A curated, verified benchmark dataset containing realistic user queries paired with the exact context chunks required to answer them and the human-validated ground truth answers.
8. **Q**: If your RAG system has high Context Precision but low Faithfulness, what is the root cause?  
   *Answer*: The retrieval system is fetching the correct context, but the generative LLM is ignoring the context, hallucinating ungrounded facts, or being distracted by its pre-trained parametric knowledge.
9. **Q**: What does a Confusion Matrix display?  
   *Answer*: A $2 \times 2$ (or $N \times N$) table mapping actual class labels against predicted class labels, showing True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN).
10. **Q**: In scikit-learn, what is the purpose of `train_test_split(X, y, test_size=0.2, random_state=42)`?  
    *Answer*: It partitions data into 80% training data (to fit model weights) and 20% unseen test data (to evaluate true generalization performance), using a fixed random seed to ensure reproducible splits.

---

## Week 8: Portfolio Project 2 — Production Document Intelligence Engine & Job Search Kickoff

### Week Theme
> Full-stack architecture, deployment, and evaluation benchmarking of Flagship Project 2 (DocuMind), accompanied by the initiation of your proactive job search routine.

### Concepts to Master
- `CORE`: End-to-end Enterprise RAG Architecture: Next.js 15 App Router + FastAPI async backend + pgvector / Qdrant + Cohere/FlashRank Reranking.
- `CORE`: Grounded citations UX: Interactive UI linking citations directly to document view and page highlights.
- `CORE`: Production evaluation reporting: Embedding quantitative Ragas scorecards directly into the GitHub repository and README.
- `CORE`: Modern AI CV & LinkedIn positioning: Framing frontend experience + backend/LLM skills as an "AI Full-Stack Engineer".
- `CORE`: The proactive job search system: Targeting Islamabad/Rawalpindi software houses (Arbisoft, Systems Ltd, 10Pearls, Emumba, Devsinc, local GenAI startups) and global remote platforms (Wellfound, LinkedIn, Remotive).
- `GOOD-TO-KNOW`: Cloud deployment of vector search backends with Docker on Render/Railway and database hosting on Supabase/Neon.

---

### Daily Schedule: Week 8 (27 Hours)

#### Monday (3 hrs) — Project 2 Architecture & Domain Setup
- **Hour 1–2**: Architect **Portfolio Project 2: "DocuMind"** — an Enterprise Document Intelligence & Policy Auditor that allows companies to upload complex PDF documentation, performs hybrid retrieval with cross-encoder reranking, and streams answers with interactive citations.
- **Hour 3**: Set up database schemas on Supabase (PostgreSQL with `pgvector` and `tsvector` full-text search) and configure backend project structure.

#### Tuesday (3 hrs) — Ingestion Pipeline & Hybrid Retrieval Backend
- **Hour 1–2**: Build backend ingestion service: Handles PDF parsing, page numbering, metadata tagging, and vector storage in pgvector.
- **Hour 3**: Implement Hybrid Retrieval with Reciprocal Rank Fusion (RRF) and Cross-Encoder reranking (Cohere API / FlashRank).

#### Wednesday (3 hrs) — Streaming RAG Backend & Citations Engine
- **Hour 1–2**: Build `/api/v1/query/stream`: Server-Sent Events endpoint streaming answer tokens while generating grounded citations.
- **Hour 3**: Add fallback logic: if retrieval similarity scores fall below threshold $\tau$, stream a graceful refusal message rather than attempting to guess.

#### Thursday (3 hrs) — Frontend: Next.js Interactive Document Viewer
- **Hour 1–2**: Build the Next.js UI: Split-screen interface with a chat panel on the left and an interactive document viewer on the right.
- **Hour 3**: Implement interactive citations: Clicking any citation badge in the chat automatically navigates the PDF/document viewer to the exact page and highlights the source snippet.

#### Friday (3 hrs) — Quantitative Evaluation & Benchmark Suite
- **Hour 1–2**: Run the automated Ragas test suite against DocuMind over a 25-question evaluation set. Generate the final metrics scorecard (Faithfulness, Answer Relevance, Context Precision).
- **Hour 3**: Instrument Langfuse tracing to capture live user sessions, latency percentiles ($p50, p95$), and token costs.

#### Saturday (6 hrs) — Production Deployment, Docker & Video Walkthrough
- **Hour 1–3**: Dockerize backend, deploy to Render/Railway, and deploy Next.js frontend to Vercel. Test end-to-end functionality on live URLs.
- **Hour 4–5**: Author a comprehensive README: Include architecture diagram, benchmark scorecard table, technical challenges overcome, and setup guide.
- **Hour 6**: Record a crisp 2-minute Loom walkthrough: Demonstrate PDF upload, ask a complex question, showcase hybrid retrieval and reranking, click a citation to highlight source text, and show the Langfuse trace.

#### Sunday (6 hrs) — Career Transition: CV, LinkedIn & First Applications
- **Hour 1–2**: Rewrite CV: Frame background as an **AI Full-Stack Engineer** (highlighting Next.js frontend mastery combined with Python, FastAPI, pgvector, and Advanced RAG pipelines). Link both Project 1 and Project 2 live URLs and video demos prominently.
- **Hour 3–4**: Optimize LinkedIn profile: Add featured section with Project 2 Loom video and GitHub repository. Connect with 15 engineering leads and recruiters in Islamabad/Rawalpindi and remote AI startups.
- **Hour 5–6**: Submit your first 5 high-intent job applications with tailored cover notes highlighting your build-first portfolio. Complete Week 8 Self-Test.

---

### Hands-on Tasks: Week 8
1. [ ] Deploy a full-stack RAG application (DocuMind) with live frontend on Vercel and backend on Render.
2. [ ] Embed an interactive citation viewer in Next.js that navigates to source document pages on click.
3. [ ] Run an automated Ragas evaluation run and publish the benchmark metrics scorecard directly in the GitHub README.
4. [ ] Send 5 targeted job applications and connect with 15 AI engineering leads in Islamabad/Rawalpindi and remote companies.

---

### Portfolio Project 2: Flagship Specification
```
Project Name : DocuMind — Enterprise Document Intelligence & Policy Auditor
Repository   : github.com/<your-username>/documind
Live Demo    : documind.vercel.app (Frontend) | documind-api.onrender.com (Backend)
Stack        : Next.js 15, TypeScript, Tailwind CSS, FastAPI, Python 3.12, Pydantic v2,
               Supabase (PostgreSQL + pgvector), Cohere Rerank / FlashRank,
               Groq Llama 3.3 / Gemini Flash, Langfuse, Ragas, Docker.
```

#### Core Features
1. **Hybrid Retrieval Pipeline**: Combines PostgreSQL full-text search (BM25) and dense pgvector embeddings via Reciprocal Rank Fusion (RRF).
2. **Cross-Encoder Reranking**: Re-ranks top 25 retrieved candidates down to 5 using Cohere Rerank / FlashRank for high context precision.
3. **Interactive Grounded Citations**: Real-time token streaming with clickable citation badges that highlight exact source snippets and page numbers in an embedded document viewer.
4. **Verifiable Quality Scorecard**: Automated evaluation suite published with quantitative Ragas benchmarks (Faithfulness $>90\%$, Answer Relevance $>88\%$).
5. **Full Observability**: Live Langfuse integration capturing execution traces, latency bottlenecks, and token expenses.

---

### Self-Test: Week 8
1. **Q**: Why does a hybrid search system (BM25 + pgvector) consistently outperform a pure vector search system on enterprise documents?  
   *Answer*: Pure vector search excels at broad semantic concepts but struggles with exact keyword queries (acronyms, part numbers, error codes, legal references); BM25 handles exact keyword matching, and their fusion via RRF captures both semantic intent and lexical accuracy.
2. **Q**: What is the primary purpose of a second-stage Cross-Encoder reranker in a RAG pipeline?  
   *Answer*: To re-evaluate the top candidates retrieved by the first stage using full cross-attention between query and chunk, re-ordering them so the most contextually relevant chunks appear at the very top of the context window, combating the "lost in the middle" problem.
3. **Q**: How does providing page-level citations reduce legal and operational risk in enterprise LLM deployment?  
   *Answer*: It enables human-in-the-loop verification, allowing end-users and compliance officers to instantly verify that the model's answer is directly supported by official documentation rather than a plausible-sounding hallucination.
4. **Q**: If your RAG evaluation shows high Faithfulness (0.95) but low Answer Relevance (0.60), what is occurring?  
   *Answer*: The model is strictly faithful to the provided context and is not hallucinating, but it is failing to actually answer the question asked by the user (e.g., providing off-topic factual summaries or being excessively cautious).
5. **Q**: What three links must appear at the top of your GitHub README for an applied AI portfolio project?  
   *Answer*: 
   1. Live public application demo link.
   2. 2-minute Loom video walkthrough link.
   3. Live backend API interactive docs link (`/docs`).
6. **Q**: What is the most effective way to position 6 months of professional frontend experience on an AI engineering CV?  
   *Answer*: Position yourself as an **AI Full-Stack Engineer** who builds end-to-end applications: combining frontend mastery (streaming chat UIs, generative interfaces, complex state) with backend Python engineering (FastAPI, vector databases, RAG pipelines, evaluations).
7. **Q**: Why are automated evaluation scorecards (Ragas/DeepEval) more persuasive to hiring managers than demo screenshots?  
   *Answer*: Screenshots only show that the happy path works for one curated example; an evaluation scorecard proves you understand production engineering, regression testing, and have rigorously benchmarked performance across edge cases.
8. **Q**: How should you follow up with an engineering manager or tech lead after applying for an AI engineering role on LinkedIn?  
   *Answer*: Send a concise, personalized message highlighting a specific technical insight from your project (e.g., "Built a hybrid RAG pipeline with pgvector + Cohere reranking that hit 92% faithfulness on Ragas; here's a 2-min Loom demo: [link]").
9. **Q**: What is the typical cold-start delay on free-tier Render/Railway deployments, and how should your frontend handle it?  
   *Answer*: Free instances spin down after inactivity, causing a 30–50 second cold start on the first request; the frontend should display a user-friendly status badge ("Waking up demo backend service, please allow ~30s...") rather than failing silently with a timeout error.
10. **Q**: What are the top 3 technology companies in the Islamabad/Rawalpindi area known for hiring AI/GenAI engineers?  
    *Answer*: Arbisoft, Systems Limited, and 10Pearls (along with specialized firms like Emumba, Afiniti, and local venture-backed AI startups).

---

## Month 2 Checklist

### Learn
- [ ] Master vector mathematics (Dot Product, Cosine Similarity, Euclidean Distance).  
  *Done when*: You implement all three from scratch in NumPy and calculate pairwise similarity matrices.
- [ ] Understand chunking tradeoffs (Fixed, Recursive, Structure-Aware, Semantic).  
  *Done when*: You can explain when to use recursive splitting vs. markdown header splitting and why chunk overlap matters.
- [ ] Master pgvector syntax and vector indexing (HNSW vs. Flat).  
  *Done when*: You write raw SQL queries creating tables with `vector(768)`, building HNSW indices, and querying with `<=>`.
- [ ] Master Hybrid Search architecture and Reciprocal Rank Fusion (RRF).  
  *Done when*: You can explain the RRF formula and implement it in pure Python.
- [ ] Master Cross-Encoder Reranking principles.  
  *Done when*: You can explain why Cross-Encoders are more accurate than Bi-Encoders and integrate a reranker.
- [ ] Understand the RAG Triad and Ragas evaluation metrics.  
  *Done when*: You can define Faithfulness, Answer Relevance, Context Precision, and Context Recall from memory.
- [ ] Master core ML interview concepts.  
  *Done when*: You can calculate Precision, Recall, and $F_1$ from a confusion matrix and explain the Bias-Variance tradeoff.
- [ ] Understand Langfuse observability and OpenTelemetry-style tracing.  
  *Done when*: You can explain what a trace, span, and generation represent in an LLM pipeline.

### Build
- [ ] Built a multi-tenant document ingestion pipeline with deduplication and metadata tagging.  
  *Done when*: Ingestion handles multi-page PDFs, chunks text, and stores vectors with strict tenant metadata isolation.
- [ ] Built a Hybrid Search engine combining BM25 and pgvector with RRF.  
  *Done when*: Service returns relevant results for both exact code/keyword queries and broad semantic concepts.
- [ ] Built a Cross-Encoder reranking pipeline with Cohere / FlashRank.  
  *Done when*: Top 25 retrieved chunks are re-ordered and pruned down to the top 5 with relevance scores.
- [ ] Built a grounded citation engine with Pydantic structured output.  
  *Done when*: Model output contains verified bracketed citations mapping directly to chunk metadata and quotes.
- [ ] Built a Next.js split-screen document viewer with interactive citation highlighting.  
  *Done when*: Clicking a citation pill in the chat jumps to the referenced page and highlights the snippet.
- [ ] Built an automated evaluation script with Ragas.  
  *Done when*: Script executes over a 20-item dataset and outputs a quantitative scorecard.
- [ ] Built and shipped **Portfolio Project 2: DocuMind**.  
  *Done when*: Application is deployed live on Vercel + Render with public GitHub repository.

### Practice
- [ ] Solved 5 algorithmic problems related to string manipulation, hash maps, and two pointers in Python.  
  *Done when*: You can implement these patterns cleanly without syntax hesitation.
- [ ] Trained a baseline classifier in scikit-learn on a public text dataset.  
  *Done when*: You train a logistic regression model and print a `classification_report` with precision, recall, and $F_1$.
- [ ] Conducted latency and cost benchmarking between pure vector search and hybrid reranked search.  
  *Done when*: You have documented concrete latency numbers for both pipelines in your project README.

### Ship / Publish
- [ ] Containerized the DocuMind backend with Docker and deployed to Render / Railway.  
  *Done when*: Backend responds to public health checks and Swagger UI loads at `/docs`.
- [ ] Deployed the DocuMind Next.js frontend to Vercel.  
  *Done when*: Frontend is accessible on a public URL and connects to the production backend.
- [ ] Published the GitHub repository with an architecture diagram (Mermaid) and Ragas evaluation scorecard.  
  *Done when*: Repo includes full setup instructions, architecture diagram, and benchmark results table.
- [ ] Recorded and published a 2-minute Loom walkthrough video.  
  *Done when*: Video link is featured at the top of the repository README.

### Job Search & Career Kickoff (Week 8)
- [ ] Updated CV to position as an **AI Full-Stack Engineer** featuring Project 1 and Project 2.  
  *Done when*: CV contains links to both live apps, both Loom videos, both GitHub repos, and specific metric claims.
- [ ] Updated LinkedIn profile with Featured Section showcasing DocuMind and OpsCopilot.  
  *Done when*: Profile displays video demos and repository links prominently.
- [ ] Created a target list of 25 companies (15 in Islamabad/Rawalpindi + 10 remote B2B startups).  
  *Done when*: Spreadsheet contains company name, tech lead / recruiter contact, job opening URL, and custom pitch note.
- [ ] Submitted first 5 personalized job applications with custom Loom links.  
  *Done when*: 5 applications have been delivered directly to hiring managers or company portals.

---

## Common Mistakes in Month 2 & How to Avoid Them

### 1. Relying Purely on Naive Vector Search for Everything
- **The Mistake**: Building a RAG system using only cosine similarity on dense embeddings, and wondering why it fails whenever a user searches for an invoice number, exact error code, or specific person's name.
- **Why it kills you**: Hiring managers test RAG projects on edge cases and exact keywords; naive vector search fails immediately.
- **How to avoid it**: Always implement **Hybrid Search** (BM25 + Dense Vectors) fused with **Reciprocal Rank Fusion (RRF)**.

### 2. Skipping the Reranker
- **The Mistake**: Feeding the top 10 raw vector search results directly into the LLM prompt.
- **Why it kills you**: Vector search produces false positives that clutter the context window, driving up token costs, triggering the "lost in the middle" effect, and causing hallucinations.
- **How to avoid it**: Add a second-stage Cross-Encoder reranker (Cohere Rerank or local FlashRank) to prune candidates to the top 3–5 high-precision chunks.

### 3. Vibe-Based Prompt Tuning (No Quantitative Evaluation)
- **The Mistake**: Changing prompt wording or chunk sizes based on 1 or 2 manual queries, having no idea if the change broke 10 other queries.
- **Why it kills you**: Inability to demonstrate regression testing or quantitative metrics during technical interviews.
- **How to avoid it**: Establish a 20-question Golden Dataset on Day 1 of testing and run **Ragas** to track Faithfulness and Context Recall before and after changes.

### 4. Over-Complicating Chunking Before Checking Data Quality
- **The Mistake**: Spending days writing complex semantic chunking algorithms while feeding in messy, uncleaned PDF text with broken tables and header garbage.
- **Why it kills you**: "Garbage in, garbage out". No chunking or embedding algorithm can save corrupt, unparsed text.
- **How to avoid it**: Inspect raw parser outputs (`pdfplumber`) and clean the text (removing running headers, page numbers, and formatting artifacts) before chunking.

### 5. Not Starting the Job Search in Week 8
- **The Mistake**: Telling yourself: "I'll wait until I master Agents, MCP, and PyTorch in Month 3 before applying anywhere."
- **Why it kills you**: Hiring cycles take 3 to 6 weeks from initial outreach to offer; waiting until Week 12 means you won't get hired until Month 5.
- **How to avoid it**: Launch outreach at Week 8 with your two flagship projects (OpsCopilot and DocuMind). You are already more qualified than applicants who only have generic notebook tutorials.

---

## Month-End Review & Self-Rating (0 to 3)

Score yourself honestly on each capability:
- **0**: Cannot do it without step-by-step guidance.
- **1**: Can do it with documentation and debugging.
- **2**: Can build it independently and explain tradeoffs.
- **3**: Can build it from scratch, handle edge cases, and mentor someone else.

| Skill / Capability | Required Bar | Self-Rating (0–3) |
| :--- | :---: | :---: |
| **Vector Math Intuition (Dot Product, Cosine, $L_2$ Distance)** | **2** | [ ] |
| **Chunking Engineering & PDF Ingestion Pipelines** | **2** | [ ] |
| **pgvector & Qdrant Metadata Filtering Implementation** | **2** | [ ] |
| **Hybrid Search (BM25 + Dense) & RRF Implementation** | **2** | [ ] |
| **Cross-Encoder Reranking Integration (Cohere / FlashRank)** | **2** | [ ] |
| **Grounded Citations Generation & Frontend UI Linking** | **2** | [ ] |
| **Automated Evaluation Pipelines (Ragas / DeepEval)** | **2** | [ ] |
| **Production Observability & Tracing with Langfuse** | **2** | [ ] |
| **Foundational ML Concepts (Precision, Recall, $F_1$, Bias-Variance)** | **2** | [ ] |
| **CV / Portfolio Positioning & Proactive Outreach** | **2** | [ ] |

### What to Repeat If You Miss the Bar
- **If you score $<2$ on Hybrid Search & Reranking**: Do not proceed to Month 3 until you have built a standalone Python script demonstrating BM25 + dense search + reranking on a sample dataset with logged before-and-after scores.
- **If you score $<2$ on Ragas Evaluation**: Spend 2 days building a golden dataset of 15 question-answer pairs and automate a pytest script that asserts Faithfulness $>0.85$.
- **If you score $<2$ on Job Search Outreach**: Do not write a line of code for Month 3 until your CV is updated and you have sent 5 targeted applications with your DocuMind Loom demo.
