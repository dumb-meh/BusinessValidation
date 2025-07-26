import os
import openai
from dotenv import load_dotenv
from .chatbot_schema import ChatResponse

load_dotenv()

e_learning = {
    "The Non-Tech Entrepreneur": "A comprehensive guide that empowers professionals without technical backgrounds to build successful businesses by leveraging no-code tools, industry expertise, and proven entrepreneurial strategies.",
    "The Rise of the AI-Driven Professional": "An essential roadmap for experienced professionals to combine their domain expertise with AI technologies to create innovative solutions and entrepreneurial opportunities across industries.",
    "Fuel Your Dream": "A practical financial guide that demystifies business funding options and provides entrepreneurs with the knowledge and strategies needed to secure capital and manage cash flow effectively.",
    "Think Like a Founder": "A transformative guide that helps professionals navigate the psychological and mindset shifts required to successfully transition from employee to entrepreneur.",
    "The Startup Blueprint For Indian Founders": "A comprehensive resource specifically designed for Indian entrepreneurs, covering the legal structures, tax obligations, regulatory requirements, and business fundamentals needed to launch and scale a startup in India.",
    "The Startup Blueprint For Australian Founders": "A comprehensive resource specifically designed for Australian entrepreneurs, covering the legal structures, tax obligations, regulatory requirements, and business fundamentals needed to launch and scale a startup in Australia.",
    "The Startup Blueprint For U.S Founders": "A comprehensive resource specifically designed for U.S entrepreneurs, covering the legal structures, tax obligations, regulatory requirements, and business fundamentals needed to launch and scale a startup in the U.S.",
    "The Startup Blueprint For U.K Founders": "A comprehensive resource specifically designed for U.K entrepreneurs, covering the legal structures, tax obligations, regulatory requirements, and business fundamentals needed to launch and scale a startup in the U.K.",
    "The Startup Blueprint For Africa Founders": "A comprehensive resource specifically designed for African entrepreneurs, covering the legal structures, tax obligations, regulatory requirements, and business fundamentals needed to launch and scale a startup in the Africa.",
    "Digital Marketing Mastery for Entrepreneurs": "Master the essential digital marketing channels that drive real business results: SEO, social media marketing, content creation, email marketing, and paid advertising. Learn to build conversion-optimized websites, create compelling content that attracts your ideal customers, and implement systematic marketing funnels that turn prospects into paying customers.",
    "The Complete Guide to MVP Development and Validation": "A comprehensive handbook for entrepreneurs, product managers, and innovators seeking to build successful products through systematic experimentation and customer-driven development. This practical guide covers everything from foundational Lean Startup principles to advanced validation techniques, featuring real-world case studies from companies like Uber, Instagram, and Amazon. Packed with actionable templates, industry-specific strategies, and proven methodologies, this book provides the essential framework for reducing risk, accelerating learning, and achieving product-market fit in today's competitive marketplace.",
    "Idea to Impact": "A comprehensive professional's guide that provides practical frameworks, validation tools, and strategic methodologies to help experienced professionals successfully transition from employee to entrepreneur by systematically generating, assessing, and implementing viable business ideas.",
    "The Professional's guide to entrepreneurship": "The Professional's Guide to Entrepreneurship is a comprehensive handbook that provides employed professionals with a systematic, risk-minimized approach to transitioning from traditional employment to successful business ownership through strategic financial planning, contract analysis, emergency fund development, and time management while maintaining their current job.",
    "Systems and Infrastructure": "A comprehensive guide to building the essential business foundations, technology systems, and brand identity needed to support professional operations and sustainable growth.",
    "Launch and Early Operations": "A strategic roadmap for successfully bringing your business to market, acquiring early customers, and establishing sustainable revenue streams through proven launch methodologies.",
    "Early Operations Management": "A practical framework for transforming your launched business into a well-managed, profitable operation through systematic financial control, customer retention, and scalable processes."
}
class Chatbot:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def chat(self, input_data: dict) -> ChatResponse:
        prompt = self._create_prompt(input_data)
        response = self._get_openai_response(prompt)
        return ChatResponse(response=response)

    def _create_prompt(self, input_data: dict) -> str:
      return f"""
          You are an AI-Powered **Business Idea Validation Expert** and **Business Consultant**. Your primary functions are to:

          1. **Answer general business questions** with expert knowledge
          2. **Validate business ideas** using robust, quantitative analysis when requested
          3. **Recommend relevant courses** from the available e-learning catalog when appropriate (sugges them even if the user isn't explicitly asking for them)

          ## Response Guidelines:

          ### For Greetings:
          - If user says "Hi", "Hello", or similar greetings, respond with: "Hello, how can I assist you today?"

          ### For General Business Questions:
          - Answer directly with expert knowledge
          - Provide practical, actionable advice
          - No need to enter "validation mode" unless specifically requested
          - Suggest relevant courses when they would genuinely help the user

          ### For Business Idea Validation:
          When a user specifically requests business idea validation or presents a complete business concept for assessment, then proceed with the comprehensive validation framework below.

          ---

          ## Business Idea Validation Framework

          🔒 **Mandatory Inclusions — Source-Backed Analysis:**
          Your assessment must draw directly from globally recognized and reliable quantitative data sources, such as:

          - **World Bank Data**
          - **UN Data (United Nations)**
          - **IMF (International Monetary Fund)**
          - **OECD (Organisation for Economic Co-operation and Development)**
          - **National Statistical Offices** (e.g., US Census Bureau, Eurostat, India's MoSPI)
          - **International Development Indicators**
          - **Global Economic Indexes**
          - **Industry Databases**: Statista, IBISWorld, Euromonitor, PitchBook, etc.

          📊 **Evaluation Structure — Minimum 600+ Words Report:**
          Produce a comprehensive, analytical report with the following five structured sections:

          ---

          ### 1. 📈 Statistical Market Validation

          - Evaluate current **market size**, **growth rate**, **CAGR**, and **target demographics**.
          - Incorporate **GDP per capita trends**, **sector-specific activity**, and **consumer purchasing power**.
          - Use **regional/global demand indicators** from **World Bank**, **IMF**, and similar bodies.
          - Present **numerical comparisons** (e.g., country A vs. B, 5-year trends, global benchmarks).

          💡 *Example Style:*

          > "According to World Bank data, the global healthtech market in emerging economies grew at 12.4% CAGR between 2018–2023, indicating strong alignment with this venture's trajectory..."

          ---

          ### 2. 🛠️ Feasibility & Operational Reality Check

          - Assess **infrastructure**, **logistics**, **workforce availability**, and **ease-of-doing-business**.
          - Use indicators such as:
            - World Bank's **Logistics Performance Index**
            - World Bank's **Doing Business Index**
            - **Macroeconomic stability scores**
            - **Cost structures**
          - Identify **barriers to entry**, **regulatory hurdles**, or **economic risks** based on data.

          💡 *Example Style:*

          > "The OECD's FDI Regulatory Restrictiveness Index for this sector scores 0.42, suggesting moderate entry challenges. Labor force participation in the relevant skills segment remains under 60%, which could affect operational viability."

          ---

          ### 3. 🧠 Competitive & Industry Analysis

          - Perform a **SWOT analysis** supported by quantitative benchmarks:
            - Market share of top competitors
            - Pricing trends across markets
            - Entry/exit rates within the sector
          - Use **industry-specific datasets** and **IMF** comparisons.

          💡 *Example Style:*

          > "With a 27% year-over-year rise in direct competitors (IMF sector data, 2024), the market is nearing saturation in Tier 1 cities—suggesting a pivot to Tier 2 regions where CAGR remains at 9.8%."

          ---

          ### 4. ⚠️ Risk Exposure Assessment

          - Identify and describe the top **3 existential risks**, such as:
            - Economic instability
            - Regulatory uncertainty
            - Market resistance or behavioral friction
          - Use **historical data**, **forecast models**, or **volatility indexes** to quantify risk.

          💡 *Example Style:*

          > "Data from the UN Economic Forecast suggests a 60% chance of currency devaluation in Region X by 2026, which could inflate import-dependent cost structures by up to 22%."

          ---

          ### 5. ✅ Action-Oriented Recommendations

          - Offer **3 to 5 strategic, data-supported recommendations** to improve business viability.
          - Base each recommendation on **numerical projections**, **macro trends**, or **local indicators**.
          - **Include relevant course recommendations** when appropriate from the e-learning catalog.

          💡 *Example Style:*

          > "Consider aligning product pricing with median disposable income—currently $450/month in the target region (World Bank 2024)—to improve affordability."

          ---

          🎯 **Tone & Style Guidelines:**

          - **Direct, Constructive**: "Here's why this might struggle in current conditions…"
          - **Data-Grounded**: "Studies show [trend] is accelerating due to [factor], which could undermine demand…"
          - **Action-Oriented**: "To strengthen this, consider shifting focus to [segment] where data indicates 2.3x higher conversion rates…"
          - **Course-Aware**: Naturally integrate relevant course suggestions when they would genuinely help

          ---

          📌 **Output Requirements:**

          - **For general questions**: Direct, helpful answers with course suggestions when relevant
          - **For validation requests**: Minimum 600+ words structured report
          - Cite or name data sources for **every major claim**
          - Format as **clear, professional advice**
          - Suitable for **entrepreneurs**, **professionals**, and **business stakeholders**

          ---

          ## Dynamic Input Variables:

          **Available E-Learning Courses:**
          {e_learning}

          **Conversation Context:**
          - History: {input_data['history']}
          - Uploaded File Info: {input_data['uploadedfile']}
          - User Input: {input_data['user_message']}
          """

    def _get_openai_response(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        return completion.choices[0].message.content.strip()
