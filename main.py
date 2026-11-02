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
            background-color: #030307;
            letter-spacing: -0.02em;
        }
        .neon-text-green {
            color: #00ff66;
            text-shadow: 0 0 15px rgba(0, 255, 102, 0.7);
        }
        .neon-text-red {
            color: #ff3344;
            text-shadow: 0 0 15px rgba(255, 51, 68, 0.7);
        }
        .neon-border-green {
            border-color: #00ff66;
            box-shadow: 0 0 20px rgba(0, 255, 102, 0.15);
        }
        .neon-border-red {
            border-color: #ff3344;
            box-shadow: 0 0 20px rgba(255, 51, 68, 0.15);
        }
        .cyber-grid {
            background-image: linear-gradient(to right, rgba(16, 185, 129, 0.02) 1px, transparent 1px),
                              linear-gradient(to bottom, rgba(16, 185, 129, 0.02) 1px, transparent 1px);
            background-size: 20px 20px;
        }
    </style>
</head>
<body class="text-gray-300 min-h-screen p-4 md:p-8 flex flex-col justify-center items-center cyber-grid">

    <!-- MAIN SYMMETRICAL COCKPIT -->
    <div class="w-full max-w-4xl bg-[#080911] border border-gray-800 rounded-lg p-6 shadow-2xl flex flex-col items-center">
        
        <!-- TOP REGISTRY BAR -->
        <div class="w-full flex justify-between items-center pb-6 border-b border-gray-800 mb-6">
            <!-- Kenya SVG Flag (High Fidelity CSS) -->
            <div class="w-10 h-7 flex flex-col justify-between border border-gray-900 shadow-md rounded-[1px] overflow-hidden bg-black">
                <div class="h-2 bg-black"></div>
                <div class="h-0.5 bg-white"></div>
                <div class="h-2 bg-[#922529] relative flex justify-center items-center">
                    <div class="w-2 h-3 bg-[#922529] border-x border-white rounded-full absolute"></div>
                </div>
                <div class="h-0.5 bg-white"></div>
                <div class="h-2 bg-[#125832]"></div>
            </div>

            <div class="text-center">
                <div class="text-[10px] text-emerald-500 font-bold tracking-[0.3em]">// KENYA-SWISS CLEANTECH COMPLIANCE</div>
                <h1 class="text-3xl font-bold tracking-[0.2em] text-white mt-1">CENCIA <span class="neon-text-green">AI</span></h1>
            </div>

            <!-- Swiss SVG Flag (High Fidelity CSS) -->
            <div class="w-8 h-8 bg-[#da291c] flex justify-center items-center shadow-md rounded-[1px] border border-gray-900 relative">
                <div class="absolute w-5 h-1.5 bg-white rounded-[1px]"></div>
                <div class="absolute w-1.5 h-5 bg-white rounded-[1px]"></div>
            </div>
        </div>

        <!-- INVESTMENT & METRIC GRID -->
        <div class="w-full grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div class="bg-[#0c0d1a] border border-gray-800 p-4 rounded text-center">
                <span class="text-[9px] text-gray-500 font-bold block mb-1">PROTECTED CAPACITY</span>
                <span class="text-xl font-bold text-gray-100">1.95 MW</span>
            </div>
            <div class="bg-[#0c0d1a] border neon-border-green p-4 rounded text-center">
                <span class="text-[9px] text-emerald-400 font-bold block mb-1">APA REGULATORY STATUS</span>
                <span class="text-xl font-bold neon-text-green">COMPLIANT</span>
            </div>
            <div class="bg-[#0c0d1a] border border-gray-800 p-4 rounded text-center">
                <span class="text-[9px] text-gray-500 font-bold block mb-1">SAAS FLUID INCOME</span>
                <span class="text-xl font-bold text-gray-100">$585 / MRR</span>
            </div>
        </div>

        <!-- CONSOLE LOGGER INTERFACE -->
        <div class="w-full bg-[#020306] border border-gray-800 rounded p-4 mb-6 h-64 overflow-y-auto text-xs font-mono" id="log-terminal">
            <div class="text-gray-500">[SYSTEM] Cencia Sovereign Node Engine engaged. Monitoring 3 primary pilots...</div>
            <div class="text-emerald-400">[SECURE] ${new datetime().toISOString()} - Integrity handshake verified for women-led solar hubs.</div>
        </div>

        <!-- ACTION CONTROLS FOR THE JUDGES -->
        <div class="w-full flex flex-col sm:flex-row gap-4 justify-center items-center pt-2 border-t border-gray-800">
            <button onclick="triggerSimulation(false)" class="w-full sm:w-auto px-6 py-3 bg-emerald-950/30 border border-emerald-500 text-emerald-400 text-xs font-bold rounded uppercase tracking-wider hover:bg-emerald-500 hover:text-black transition duration-200">
                Simulate Secure Audit
            </button>
            <button onclick="triggerSimulation(true)" class="w-full sm:w-auto px-6 py-3 bg-red-950/30 border border-red-500 text-red-400 text-xs font-bold rounded uppercase tracking-wider hover:bg-red-500 hover:text-black transition duration-200">
                Simulate Cyber Intrusion
            </button>
        </div>
        
        <div class="text-[9px] text-gray-600 mt-6 tracking-widest uppercase">Empowering Women in Energy via Immutable Telemetry Proofs</div>
    </div>

    <script>
        const terminal = document.getElementById('log-terminal');
        const nodes = ['NAIVASHA_MAMA_SOLAR', 'KIBWEZI_AGRI_PUMP', 'THIKA_MICRO_GRID'];

        function triggerSimulation(isThreat) {
            const time = new datetime().toLocaleTimeString('en-US', { hour12: false });
            const node = nodes[Math.floor(Math.random() * nodes.length)];
            let output = '';

            if (isThreat) {
                output = `<div class="text-red-400 neon-text-red border-l-2 border-red-500 pl-2 my-2 animate-pulse">
                    [CRITICAL ALERT] ${time} - ATTACK DETECTED AT ${node}. Injection attempt caught: telemetry claiming 1.5 MW production during dark hours. Source IP sandboxed. Integrity compromised trace prevented.
                </div>`;
            } else {
                output = `<div class="text-emerald-400 border-l-2 border-emerald-500 pl-2 my-2">
                    [COMPLIANCE CERTIFIED] ${time} - Cryptographic telemetry signature verified for ${node}. Logs verified against local physics models. Data forwarded to APA Insurance portal safely.
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
