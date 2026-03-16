# AI SEO Article Generation Agent

# Overview

This project implements a **backend service for generating SEO-optimized articles using an agentic AI architecture**.

The system is designed to simulate the workflow used by professional SEO content teams. Instead of generating content directly from a single prompt, the service performs **search result analysis (SERP analysis)** to understand what topics and keywords are commonly covered by high-ranking content. These insights are then used to construct a structured outline and generate a complete article aligned with search intent.

The system accepts the following inputs:

- **Topic / primary keyword**
- **Target word count**
- **Language preference**

Using these inputs, the service performs a multi-stage pipeline that includes:

1. Retrieving top search results for the topic  
2. Extracting keywords and related subtopics from SERP data  
3. Generating a structured SEO outline  
4. Producing a full article in Markdown format  
5. Converting the article to HTML for publishing  
6. Suggesting internal linking opportunities  
7. Adding authoritative external references  
8. Generating a FAQ section from common queries  
9. Validating SEO constraints such as heading structure and keyword placement  
10. Scoring the generated article for quality and completeness  

The system is implemented as a **modular agent pipeline**, where each stage of the process is handled by a specialized agent responsible for a specific task (e.g., keyword extraction, outline generation, article writing).

To improve reliability and observability, article generation is executed through a **background job system with stage tracking**, allowing the system to monitor progress and identify failures during the generation pipeline.

The result is a **structured, publish-ready article output** that includes both Markdown and HTML formats along with supporting SEO metadata and analysis.

------------------------------------------------------------------------

## Project Structure
The project follows a modular architecture that separates responsibilities across agents, services, models, utilities, and job orchestration components.

    seo-article-agent
    │
    ├── app
    │
    │   ├── agents
    │   │   ├── serp_agent.py
    │   │   ├── keyword_agent.py
    │   │   ├── topic_agent.py
    │   │   ├── outline_agent.py
    │   │   ├── article_agent.py
    │   │   ├── linking_agent.py
    │   │   ├── faq_agent.py
    │   │   ├── seo_validator_agent.py
    │   │   └── content_scorer_agent.py
    │
    │   ├── jobs
    │   │   ├── job_runner.py
    │   │   └── article_generator_job.py
    │
    │   ├── models
    │   │   ├── article_models.py
    │   │   └── job_models.py
    │
    │   ├── services
    │   │   ├── serp_service.py
    │   │   ├── job_service.py
    │   │   └── llm_service.py
    │
    │   ├── utils
    │   │   ├── json_utils.py
    │   │   └── markdown_utils.py
    │
    │   ├── config
    │   │   └── config.py
    │
    │   └── main.py
    │
    ├── tests
    │   ├── test_seo_validator.py
    │   └── other tests
    │
    ├── examples
    │   ├── input.json
    │   └── output.json
    │
    ├── pytest.ini
    ├── requirements.txt
    ├── .env.example
    └── README.md


## Directory Overview

### `app/agents`
Contains the AI agents responsible for each stage of the content generation pipeline.

- **serp_agent.py** – Retrieves search engine results
- **keyword_agent.py** – Extracts primary and secondary keywords
- **topic_agent.py** – Identifies subtopics from SERP data
- **outline_agent.py** – Generates the article outline
- **article_agent.py** – Produces the article content
- **linking_agent.py** – Suggests internal and external links
- **faq_agent.py** – Generates FAQ sections
- **seo_validator_agent.py** – Validates SEO constraints
- **content_scorer_agent.py** – Evaluates article quality

### `app/jobs`
Handles asynchronous job execution and generation pipeline orchestration.

- **job_runner.py** – Executes background jobs
- **article_generator_job.py** – Implements the full article generation workflow

### `app/models`
Defines Pydantic models used for structured data validation.

- **article_models.py** – Article output schema
- **job_models.py** – Job lifecycle and stage models

### `app/services`
Reusable service components used across the application.

- **serp_service.py** – Fetches SERP results (API or mock)
- **job_service.py** – Job state management
- **llm_service.py** – Wrapper around OpenAI API calls

### `app/utils`
Utility helpers used across the project.

- **json_utils.py** – Cleans and parses LLM JSON responses
- **markdown_utils.py** – Converts Markdown to HTML

### `app/config`
Centralized configuration and environment variable loading.

### `tests`
Contains tests validating SEO constraints and core functionality.

### `examples`
Sample input and output payloads demonstrating how the system works.
## Key Features

### SERP‑Driven Content Generation

The system analyzes top search results to determine: - commonly covered
topics - relevant keywords - search intent

### SEO‑Optimized Structure

Generated articles include: - H1 / H2 / H3 hierarchy - keyword
placement - structured sections - human‑readable writing

### Structured Output

The API returns: - Markdown article - HTML article - SEO metadata -
keyword analysis - internal links - external references - FAQ section -
SEO validation results - content quality score

------------------------------------------------------------------------

## Architecture

[![](https://mermaid.ink/img/pako:eNptU9tuGjEQ_RXLD30pSRZYQkBVJMItJJALS1up3jw4u5PFYrGRsZPQiH_v7CwBKuXJ45lzzngu_uCJSYG3-Utu3pK5tI7NerGOdUf8XINlI73y7sezPbucmZVK2Hf229iUdY3XDi9jqTMvM3giCjs5uWRXomtBOmBD0GClU0azG_NMiCtCdAXe2dRrjJO7S-6eiPrTB9bJQJcZB-CSOYtAWjymsPa5WxO-R_i-uIXNW_GaA6X_7qxMHHuwainthn1DemJ0Wtg7dCnRJ4mBKKs6CIxStNTLhkX-2RWxEj4g-FDce5crDUeEXZXAov4924WJMiTKtehYp5L8S8pnSGk2kXaRmjdN1GuijsSnkznDrmeTMbZdv4J1u7aNCHYjxkovlM6OMkQ-y2DtcHqI1TLHPmBnSrNAl0XdEP9WDDqPX72ucGP3igES_JbgY1EU-kvmKpXO2CPizoedcNYnzlvAtP81fUwKE4FlOGSxKDEWjiX6rzL3x5159CjqNsSeEPtORPIVGG0QrQTF7ih2L6aAefXhBeleCUeDm_zEKzyzKuXtF5mvocKXYJeyuPOPWDMWczeHJcS8jSZuzSLmsd4iaSX1H2OWvI3KSLPGZ_O9iF8VdfeUzKxc7r0WdAqWfgpv18JWlVR4-4O_4716flptNIOw3ghb50GtXuEb9DbC00Y9CKq1MGy2gmpjW-F_KW3ttBEErWYYVs-b9Vrz4qLCIVU4gEn5fekXb_8Bjf9Dbg?type=png)](https://mermaid.live/edit#pako:eNptU9tuGjEQ_RXLD30pSRZYQkBVJMItJJALS1up3jw4u5PFYrGRsZPQiH_v7CwBKuXJ45lzzngu_uCJSYG3-Utu3pK5tI7NerGOdUf8XINlI73y7sezPbucmZVK2Hf229iUdY3XDi9jqTMvM3giCjs5uWRXomtBOmBD0GClU0azG_NMiCtCdAXe2dRrjJO7S-6eiPrTB9bJQJcZB-CSOYtAWjymsPa5WxO-R_i-uIXNW_GaA6X_7qxMHHuwainthn1DemJ0Wtg7dCnRJ4mBKKs6CIxStNTLhkX-2RWxEj4g-FDce5crDUeEXZXAov4924WJMiTKtehYp5L8S8pnSGk2kXaRmjdN1GuijsSnkznDrmeTMbZdv4J1u7aNCHYjxkovlM6OMkQ-y2DtcHqI1TLHPmBnSrNAl0XdEP9WDDqPX72ucGP3igES_JbgY1EU-kvmKpXO2CPizoedcNYnzlvAtP81fUwKE4FlOGSxKDEWjiX6rzL3x5159CjqNsSeEPtORPIVGG0QrQTF7ih2L6aAefXhBeleCUeDm_zEKzyzKuXtF5mvocKXYJeyuPOPWDMWczeHJcS8jSZuzSLmsd4iaSX1H2OWvI3KSLPGZ_O9iF8VdfeUzKxc7r0WdAqWfgpv18JWlVR4-4O_4716flptNIOw3ghb50GtXuEb9DbC00Y9CKq1MGy2gmpjW-F_KW3ttBEErWYYVs-b9Vrz4qLCIVU4gEn5fekXb_8Bjf9Dbg)

------------------------------------------------------------------------

## Job Lifecycle

[![](https://mermaid.ink/img/pako:eNpVkMFuwyAQRH_F2mNlWxgDNhx6aa_9gZYeUCCOFQMWwVVby_9eQlJXvc281c5qdoWD1wYEXKKK5nlUQ1C2-sDSSff28F5U1WMxG6dHN0h3FxmGxbkM7yLDg7fzZKLR__FRjdOV7eNMU7x0t9GvhxKGMGoQRzVdTAnWBKuuHlbpikJCPBlrJIgktQpnCdJtaWlW7tV7CyKGJa0FvwynPWSZ9V-1nYbUxYQnv7gIAnNGcgqIFT6TJ6SmbYMopZwy3OO2hC8QDUM1IZR0LW84ZqjZSvjOd1FNO8ZR33HaE9wjxEoweow-vNzem7-8_QAa9HMl?type=png)](https://mermaid.live/edit#pako:eNpVkMFuwyAQRH_F2mNlWxgDNhx6aa_9gZYeUCCOFQMWwVVby_9eQlJXvc281c5qdoWD1wYEXKKK5nlUQ1C2-sDSSff28F5U1WMxG6dHN0h3FxmGxbkM7yLDg7fzZKLR__FRjdOV7eNMU7x0t9GvhxKGMGoQRzVdTAnWBKuuHlbpikJCPBlrJIgktQpnCdJtaWlW7tV7CyKGJa0FvwynPWSZ9V-1nYbUxYQnv7gIAnNGcgqIFT6TJ6SmbYMopZwy3OO2hC8QDUM1IZR0LW84ZqjZSvjOd1FNO8ZR33HaE9wjxEoweow-vNzem7-8_QAa9HMl)


## Pipeline Stages

[![](https://mermaid.ink/img/pako:eNpVUV1rwjAU_SvlPlexMbU2D4OiPpR1OqwbbM2Q0MZaTBOJ7TYn_vfF1Dl8udxzD-cD7glyVXAgsBHqK98y3TjJkkoq09nyOTtwvV_nSgieN7z4oDKaR8lbGqcdwyQTxx9LLF5WSTyfZaptRCX5uuSSa3YVLVfxJJllxrzKxT1nRI9pZiS7w939NUriabSKF_Psk4mquJ67Xk6v9-D8VbHgGt8RXZzdrb3d_g3BhVJXBZANEwfuQs11zS4YTlQ6DoVmy2tOgZi1YHpHgcqzEe2ZfFeqBtLo1si0asvtzaTdXypOK1ZqVt-umsuC64lqZQMEhSGyLkBO8G0wxn0PITTyh0GAfTTALhyBeB7u4yAM_DAYIh-Ng9HZhR8bPOgH3gCPsOeFoWfGcOwCL6pG6afuifaX518u8pT3?type=png)](https://mermaid.live/edit#pako:eNpVUV1rwjAU_SvlPlexMbU2D4OiPpR1OqwbbM2Q0MZaTBOJ7TYn_vfF1Dl8udxzD-cD7glyVXAgsBHqK98y3TjJkkoq09nyOTtwvV_nSgieN7z4oDKaR8lbGqcdwyQTxx9LLF5WSTyfZaptRCX5uuSSa3YVLVfxJJllxrzKxT1nRI9pZiS7w939NUriabSKF_Psk4mquJ67Xk6v9-D8VbHgGt8RXZzdrb3d_g3BhVJXBZANEwfuQs11zS4YTlQ6DoVmy2tOgZi1YHpHgcqzEe2ZfFeqBtLo1si0asvtzaTdXypOK1ZqVt-umsuC64lqZQMEhSGyLkBO8G0wxn0PITTyh0GAfTTALhyBeB7u4yAM_DAYIh-Ng9HZhR8bPOgH3gCPsOeFoWfGcOwCL6pG6afuifaX518u8pT3)

## Project Installation

Clone the repository:

    git clone <repository-url>
    cd seo-article-agent

Initialize Virtual Environment:

```python -m venv venv```

If using Mac / Linux:

``` source venv/bin/activate```   

If using Windows:

```venv\Scripts\activate```

Install dependencies:

    pip install -r requirements.txt



### Environment Variables

Create `.env`:

    OPENAI_API_KEY=your_openai_key
    SERP_API_KEY=your_serpapi_key
    USE_MOCK_SERP=1

Mock SERP mode allows development without external APIs.



### Running the Server

    uvicorn app.main:app --reload

API documentation:

    http://localhost:8000/docs



### Example Input and Outputs
    Input: examples/input.json
    Output: examples/output.json

#### Input Structure

```json
{
  "topic": "string",
  "word_count": "integer",
  "language": "string"
}
```

#### Output Structure
```json
{
  "topic": "string",
  "outline_markdown": "string",
  "article_markdown": "string",
  "article_html": "string",
  "keyword_analysis": {
    "primary_keyword": "string",
    "secondary_keywords": ["string"]
  },
  "internal_links": [
    {
      "anchor_text": "string",
      "target_topic": "string",
      "placement_hint": "string"
    }
  ],
  "external_links": [
    {
      "source_name": "string",
      "url": "string",
      "citation_reason": "string",
      "suggested_article_section": "string"
    }
  ],
  "faq": [
    {
      "question": "string",
      "answer": "string"
    }
  ],
  "validation": {
    "keyword_in_title": "boolean",
    "keyword_in_intro": "boolean",
    "word_count": "integer",
    "word_count_ok": "boolean"
  },
  "content_quality_score": {
    "score": "number",
    "strengths": ["string"],
    "improvements": ["string"]
  }
}
```
------------------------------------------------------------------------

## Testing

Run tests:

    pytest

Tests validate: - heading hierarchy - keyword placement - word count
rules - markdown → HTML conversion

------------------------------------------------------------------------

## Design Decisions


This section outlines the key architectural and implementation decisions made while designing the SEO article generation system.

---

### Agent-Based Architecture

The system is designed as a **modular agent pipeline**, where each stage of the article generation process is handled by a dedicated agent.

Examples of agents include:

- SERP retrieval
- keyword extraction
- topic identification
- outline generation
- article generation
- linking strategy
- FAQ generation
- SEO validation
- content quality scoring

**Benefits of this approach:**

- Clear separation of responsibilities
- Easier debugging and testing
- Modular extensibility
- Ability to replace or improve individual agents without affecting the entire system

---

### SERP-Driven Content Generation

Instead of generating articles directly from a prompt, the system first analyzes **search engine results**.

SERP results provide:

- ranking titles
- snippets
- URLs

These are used to extract:

- common topics
- search intent
- relevant keywords

This ensures the generated content better aligns with **existing high-ranking content**, which is a core principle of SEO.

---

### Markdown-First Content Generation

Articles are generated in **Markdown format** and then converted to HTML.

Reasons for this approach:

- Markdown is easier for LLMs to structure correctly
- It preserves heading hierarchy cleanly
- Markdown is easier to edit or store in CMS systems
- HTML output is still available for direct publishing

---

### Structured Output Using Pydantic Models

All major outputs are defined using **Pydantic models**.

This ensures:

- predictable API responses
- strong schema validation
- easier integration with downstream systems

Examples include models for:

- article content
- keyword analysis
- linking suggestions
- FAQ entries
- validation results

---

### Background Job Execution

Article generation can take several seconds due to multiple LLM calls and SERP analysis. To prevent blocking API requests, the system executes generation tasks using a **background job runner**.

Each job tracks:

- status (`pending`, `running`, `completed`, `failed`)
- stage progress in the pipeline

This improves reliability and observability of long-running tasks.

---

### In-Memory Job Store

For simplicity, job state is stored in an **in-memory job store**.

This approach was chosen because:

- it reduces infrastructure complexity
- it is sufficient for a take-home assignment
- it allows focus on pipeline design rather than deployment infrastructure

In a production system, this would likely be replaced with:

- Redis
- PostgreSQL
- a distributed job queue (Celery / Temporal / BullMQ)

---

### Mockable SERP Integration

The system supports both:

- real SERP API requests
- mocked SERP responses

This is controlled through the `USE_MOCK_SERP` environment variable.

Benefits:

- easier local testing
- reduced dependency on external APIs
- deterministic development behavior

---

### SEO Validation Layer

A validation step is included to ensure generated content satisfies basic SEO constraints such as:

- keyword placement in title
- keyword placement in introduction
- minimum word count
- heading structure

This step provides programmatic feedback on whether the generated article satisfies expected SEO requirements.

---

### Content Quality Scoring

After article generation, a content scoring agent evaluates the article's quality based on factors such as:

- readability
- structure
- keyword usage
- completeness

This scoring step helps identify areas for potential improvement in generated content.

------------------------------------------------------------------------

## Future Improvements

-   persistent job storage
-   caching SERP results
-   section‑level article generation
-   RAG for authoritative references
-   automatic linking to existing site content

------------------------------------------------------------------------

## Conclusion

This project demonstrates how AI agents can orchestrate SEO research,
structured planning, and content generation to produce high‑quality,
SEO‑optimized long‑form articles.
