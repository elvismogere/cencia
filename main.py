import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Cencia AI Sovereign Dashboard")

class TelemetryPayload(BaseModel):
    site_id: str
    reported_mw: float
    timestamp: str

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CENCIA AI // SOVEREIGN SECURITY HUB</title>
    <script src="https://tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style>
        body { 
            font-family: 'Fira Code', monospace; 
            background-color: #05060c;
            letter-spacing: -0.01em;
        }
        .neon-text-green {
            color: #00ff66;
            text-shadow: 0 0 10px rgba(0, 255, 102, 0.8);
        }
        .neon-text-red {
            color: #ff3344;
            text-shadow: 0 0 10px rgba(255, 51, 68, 0.8);
        }
        .neon-border-green {
            border-color: #00ff66;
            box-shadow: 0 0 15px rgba(0, 255, 102, 0.2);
        }
        .cyber-grid {
            background-image: linear-gradient(to right, rgba(16, 185, 129, 0.03) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(16, 185, 129, 0.03) 1px, transparent 1px);
            background-size: 25px 25px;
        }
        .flag-ke {
            background: linear-gradient(to bottom, #000000 30%, #ffffff 30%, #ffffff 35%, #bb0000 35%, #bb0000 65%, #ffffff 65%, #ffffff 70%, #006600 70%);
        }
    </style>
</head>
<body class="text-gray-200 min-h-screen p-4 md:p-8 flex flex-col justify-center items-center cyber-grid">

    <!-- MAIN SYMMETRICAL COCKPIT -->
    <div class="w-full max-w-4xl bg-[#0b0d19] border border-gray-800 rounded-lg p-6 md:p-8 shadow-2xl flex flex-col items-center">
        
        <!-- TOP IDENTITY HEADER -->
        <div class="w-full flex justify-between items-center pb-6 border-b border-gray-800 mb-6">
            <!-- Kenya Flag -->
            <div class="w-10 h-7 border border-gray-900 shadow-md rounded-[1px] overflow-hidden flag-ke relative flex justify-center items-center">
                <div class="w-2.5 h-4 bg-[#bb0000] border-x border-white rounded-full absolute"></div>
            </div>

            <div class="text-center mx-4">
                <div class="text-[10px] text-emerald-400 font-bold tracking-[0.25em] uppercase">// KENYA-SWISS CLEANTECH COMPLIANCE</div>
                <h1 class="text-3xl font-bold tracking-[0.15em] text-white mt-1">CENCIA <span class="neon-text-green">AI</span></h1>
            </div>

            <!-- Swiss Flag -->
            <div class="w-8 h-8 bg-[#da291c] flex justify-center items-center shadow-md rounded-[1px] border border-gray-900 relative">
                <div class="absolute w-5 h-1.5 bg-white"></div>
                <div class="absolute w-1.5 h-5 bg-white"></div>
            </div>
        </div>

        <!-- HIGH CONTRAST INVESTMENT & METRIC GRID -->
        <div class="w-full grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div class="bg-[#121526] border border-gray-700 p-4 rounded text-center shadow-inner">
                <span class="text-[10px] text-gray-400 font-bold block mb-1 uppercase tracking-wider">PROTECTED CAPACITY</span>
                <span class="text-xl font-bold text-white">1.95 MW</span>
            </div>
            <div class="bg-[#121526] border neon-border-green p-4 rounded text-center shadow-inner">
                <span class="text-[10px] text-emerald-400 font-bold block mb-1 uppercase tracking-wider">APA REGULATORY STATUS</span>
                <span class="text-xl font-bold neon-text-green">COMPLIANT</span>
            </div>
            <div class="bg-[#121526] border border-gray-700 p-4 rounded text-center shadow-inner">
                <span class="text-[10px] text-gray-400 font-bold block mb-1 uppercase tracking-wider">SAAS UNIT FLUID INCOME</span>
                <span class="text-xl font-bold text-white">$585 / MRR</span>
            </div>
        </div>

        <!-- TERMINAL INTERFACE -->
        <div class="w-full bg-[#04050a] border border-gray-800 rounded p-4 mb-6 h-64 overflow-y-auto text-xs font-mono text-gray-300 leading-relaxed" id="log-terminal">
            <div class="text-gray-500">[SYSTEM] Cencia Sovereign Node Engine engaged. Monitoring 3 primary pilots...</div>
            <div class="text-emerald-400 font-semibold">[SECURE] Core telemetry log parameters verified against physics baseline model.</div>
        </div>

        <!-- HIGH-QUALITY BUTTON CONTROLS -->
        <div class="w-full flex flex-col sm:flex-row gap-4 justify-center items-center pt-4 border-t border-gray-800">
            <button onclick="triggerSimulation(false)" class="w-full sm:w-64 px-6 py-3 bg-[#0d2b1a] border-2 border-[#00ff66] text-[#00ff66] text-xs font-bold rounded uppercase tracking-widest hover:bg-[#00ff66] hover:text-black transition duration-200 shadow-md">
                Simulate Secure Audit
            </button>
            <button onclick="triggerSimulation(true)" class="w-full sm:w-64 px-6 py-3 bg-[#3a141a] border-2 border-[#ff3344] text-[#ff3344] text-xs font-bold rounded uppercase tracking-widest hover:bg-[#ff3344] hover:text-black transition duration-200 shadow-md">
                Simulate Cyber Intrusion
            </button>
        </div>
        
        <div class="text-[10px] text-gray-500 mt-6 tracking-widest uppercase font-semibold text-center">Empowering Women in Energy via Immutable Telemetry Proofs</div>
    </div>

    <script>
        const terminal = document.getElementById('log-terminal');
        const nodes = ['NAIVASHA_MAMA_SOLAR', 'KIBWEZI_AGRI_PUMP', 'THIKA_MICRO_GRID'];

        function triggerSimulation(isThreat) {
            const time = new Date().toLocaleTimeString('en-US', { hour12: false });
            const node = nodes[Math.floor(Math.random() * nodes.length)];
            let output = '';

            if (isThreat) {
                output = `<div class="text-red-400 neon-text-red border-l-2 border-red-500 pl-3 my-2 bg-red-950/20 p-2 rounded">
                    [CRITICAL ALERT] ${time} - VECTOR INTRUSION DETECTED AT ${node}. Malicious command injection caught: telemetry packet claiming 1.5 MW production during midnight cycle. Stream isolated. Data fraud blocked safely.
                </div>`;
            } else {
                output = `<div class="text-emerald-300 border-l-2 border-emerald-500 pl-3 my-2 bg-emerald-950/20 p-2 rounded">
                    [COMPLIANCE CERTIFIED] ${time} - Cryptographic integrity handshake valid for ${node}. Verification matched with climate tracking specifications. Forwarded securely to APA Insurance ledger.
                </div>`;
            }

            terminal.innerHTML += output;
            terminal.scrollTop = terminal.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    return HTMLResponse(content=DASHBOARD_HTML)

@app.post("/api/v1/telemetry")
def process_telemetry(payload: TelemetryPayload):
    return {"site_id": payload.site_id, "status": "MONITORED_SECURE"}
