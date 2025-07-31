# Business Validation Chatbot

A FastAPI-powered AI chatbot that provides business idea validation, consultation services, and PDF document processing. The chatbot leverages OpenAI's GPT models to deliver expert business advice and comprehensive market analysis.

## 🚀 Features

- **AI-Powered Business Consultation**: Get expert business advice and answers to general business questions
- **Business Idea Validation**: Comprehensive analysis using quantitative data from global sources (World Bank, IMF, OECD, etc.)
- **PDF Text Extraction**: Upload and extract text from PDF documents for analysis
- **E-Learning Course Recommendations**: Intelligent suggestions from a curated catalog of business courses
- **RESTful API**: Clean, documented endpoints for easy integration
- **Docker Support**: Containerized deployment for consistent environments

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional)
- OpenAI API Key

## 🛠️ Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd business-validation-chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8091 --reload
   ```

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - API: http://localhost:8091
   - Documentation: http://localhost:8091/docs

## 📚 API Endpoints

### Chatbot Endpoints

#### POST /chatbot/chat
Chat with the AI business consultant.

**Request Body:**
```json
{
  "history": [],
  "uploadedfile": "optional_file_info",
  "user_message": "How do I validate my business idea?"
}
```

**Response:**
```json
{
  "response": "Detailed AI response with business advice..."
}
```

### PDF Processing Endpoints

#### POST /pdf/extract
Extract text from uploaded PDF files.

**Request:**
- Multipart form data with PDF file

**Response:**
```json
{
  "filename": "document.pdf",
  "text": "Extracted text content...",
  "page_count": 5,
  "success": true,
  "message": "PDF text extracted successfully"
}
```

#### GET /pdf/health
Health check for PDF service.

## 🤖 Chatbot Capabilities

### Business Consultation
- General business questions and advice
- Strategic planning guidance
- Market analysis insights
- Entrepreneurship support

### Business Idea Validation
When you request business idea validation, the chatbot performs:

1. **📈 Statistical Market Validation**
   - Market size, growth rate, and CAGR analysis
   - GDP per capita trends and consumer purchasing power
   - Regional/global demand indicators

2. **🛠️ Feasibility & Operational Reality Check**
   - Infrastructure and logistics assessment
   - Workforce availability analysis
   - Regulatory and economic risk evaluation

3. **🧠 Competitive & Industry Analysis**
   - SWOT analysis with quantitative benchmarks
   - Market share and pricing trend analysis
   - Industry entry/exit rate assessment

4. **⚠️ Risk Exposure Assessment**
   - Top 3 existential risks identification
   - Quantified risk analysis using historical data

5. **✅ Action-Oriented Recommendations**
   - Strategic recommendations based on data
   - Course suggestions from e-learning catalog

### E-Learning Course Catalog (Change based on your requirement)

The chatbot can recommend from these available courses:
- The Non-Tech Entrepreneur
- The Rise of the AI-Driven Professional
- Fuel Your Dream
- Think Like a Founder
- Startup Blueprint (for various regions: India, Australia, US, UK, Africa)
- Digital Marketing Mastery for Entrepreneurs
- The Complete Guide to MVP Development and Validation
- And more...

## 🏗️ Project Structure

```
├── app/
│   ├── core/
│   │   └── config.py              # Configuration settings
│   └── services/
│       └── chatbot/
│           ├── chatbot.py         # Main chatbot logic
│           ├── chatbot_route.py   # API routes
│           ├── chatbot_schema.py  # Pydantic schemas
│           └── pdf_extractor.py   # PDF processing service
├── main.py                        # FastAPI application entry point
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker configuration
├── docker-compose.yml             # Docker Compose setup
├── .dockerignore                  # Docker ignore rules
├── .gitignore                     # Git ignore rules
└── .env                          # Environment variables (create this)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Docker Configuration

The application runs on port 8091 by default. You can modify this in:
- `docker-compose.yml` (port mapping)
- `Dockerfile` (EXPOSE directive)
- `main.py` (local development)

