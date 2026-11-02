# Cencia // The Trust Layer for Clean Energy

Cencia provides continuous, AI-driven telemetry monitoring and cryptographic data verification for solar and clean-energy infrastructure in Kenya. By matching reported generation logs against environmental physics and real-world weather patterns, Cencia mitigates cyber vulnerabilities and protects the integrity of carbon credit tracking from digital manipulation.

## 🚀 System Architecture & MVP Stage
- **Backend Core:** FastAPI (Python 3.10+)
- **Front-End Dashboard:** Tailwind CSS & Embedded JavaScript (SpaceX Instrumentation Aesthetic)
- **Deployment Platform:** Hosted Live on Render

## 🛠️ Local Development Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd cencia
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Mission-Control Dashboard Locally:**
   ```bash
   uvicorn main:app --reload
   ```
   Open your browser and navigate to `http://127.0.0.1:8000` to view the live telemetry cockpit stream.

## 🔒 Cybersecurity Scope
- **Anomaly Detection:** Real-time flagging of impossible power claims (e.g., anomalies like >0.01 MW generation during local night cycles).
- **Integrity Logs:** Cryptographic verification structure tracking device behavioral drift and unauthorized payload parameters.
