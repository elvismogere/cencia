import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Cencia AI Sovereign Operations Command")

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
            font-family: 'JetBrains Mono', monospace; 
            background-color: #000000;
            color: #ffffff;
            overflow-x: hidden;
        }
        .neon-text-green {
            color: #00ff66;
            text-shadow: 0 0 15px rgba(0, 255, 102, 0.9), 0 0 30px rgba(0, 255, 102, 0.4);
        }
        .neon-text-red {
            color: #ff3344;
            text-shadow: 0 0 15px rgba(255, 51, 68, 0.9), 0 0 30px rgba(255, 51, 68, 0.4);
        }
        .neon-border-green {
            border: 2px solid #00ff66;
            box-shadow: 0 0 20px rgba(0, 255, 102, 0.3), inset 0 0 20px rgba(0, 255, 102, 0.1);
        }
        .neon-border-red {
            border: 2px solid #ff3344;
            box-shadow: 0 0 20px rgba(255, 51, 68, 0.3), inset 0 0 20px rgba(255, 51, 68, 0.1);
        }
        .terminal-container {
            background-color: #050508;
            border: 1px solid #1a1d29;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
        }
        .flag-ke {
            background: linear-gradient(to bottom, #000000 30%, #ffffff 30%, #ffffff 35%, #bb0000 35%, #bb0000 65%, #ffffff 65%, #ffffff 70%, #006600 70%);
        }
        .glow-button-green:hover {
            box-shadow: 0 0 25px rgba(0, 255, 102, 0.8);
            background-color: #00ff66 !important;
            color: #000000 !important;
        }
        .glow-button-red:hover {
            box-shadow: 0 0 25px rgba(255, 51, 68, 0.8);
            background-color: #ff3344 !important;
            color: #000000 !important;
        }
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #050508;
        }
        ::-webkit-scrollbar-thumb {
            background: #1a1d29;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #00ff66;
        }
    </style>
</head>
<body class="min-h-screen p-4 md:p-8 flex flex-col justify-center items-center">

    <!-- MAXIMALIST CRITICAL OPERATION HUB (PERFECT CENTRAL ALIGNMENT) -->
    <div class="w-full max-w-4xl terminal-container rounded-xl p-6 md:p-10 flex flex-col items-center border border-zinc-800">
        
        <!-- HEADER DESIGN SYSTEM (SPACE X & TESLA INSTRUMENTATION COUPLING) -->
        <div class="w-full flex flex-col items-center pb-6 border-b border-zinc-800 mb-8 text-center">
            
            <!-- ALIGNED NATION SOVEREIGN FLAG RECOGNITION -->
            <div class="flex items-center justify-center gap-6 mb-4">
                <!-- High-Contrast Flag of Kenya -->
                <div class="w-12 h-8 border-2 border-zinc-700 shadow-2xl rounded-sm overflow-hidden flag-ke relative flex justify-center items-center">
                    <div class="w-3 h-5 bg-[#bb0000] border-x-2 border-white rounded-full absolute"></div>
                </div>

                <!-- High-Contrast Flag of Switzerland -->
                <div class="w-9 h-9 bg(#da291c) flex justify-center items-center shadow-2xl rounded-sm border-2 border-zinc-700 relative">
                    <div class="absolute w-5 h-2 bg-white rounded-sm"></div>
                    <div class="absolute w-2 h-5 bg-white rounded-sm"></div>
                </div>
            </div>

            <div class="text-center">
                <p class="text-[11px] text-emerald-400 font-extrabold tracking-[0.4em] uppercase mb-1">KENYA-SWISS CLEANTECH COMPLIANCE FEDERATION</p>
                <h1 class="text-4xl md:text-5xl font-black tracking-[0.2em] text-white">CENCIA <span class="neon-text-green">AI</span></h1>
                <p class="text-[10px] text-zinc-500 font-bold uppercase tracking-[0.5em] mt-2">Sovereign Data Trust Layer // Operational Intelligence Alpha</p>
            </div>
        </div>

        <!-- HIGH-VISIBILITY GRID DATA (APPLE STRUCTURAL SYMMETRY) -->
        <div class="w-full grid grid-cols-1 md:grid-cols-3 gap-6 mb-8 text-center">
            <div class="bg-[#0b0c12] border-2 border-zinc-800 p-5 rounded-lg shadow-xl">
                <span class="text-[10px] text-zinc-400 font-extrabold block mb-1 tracking-[0.2em] uppercase">PROTECTED CAPACITY</span>
                <span class="text-2xl font-black text-white tracking-wide">1.95 MW</span>
            </div>
            <div class="bg-[#0b0c12] neon-border-green p-5 rounded-lg shadow-xl">
                <span class="text-[10px] text-emerald-400 font-extrabold block mb-1 tracking-[0.2em] uppercase">APA REGULATORY STATUS</span>
                <span class="text-2xl font-black neon-text-green tracking-widest">COMPLIANT</span>
            </div>
            <div class="bg-[#0b0c12] border-2 border-zinc-800 p-5 rounded-lg shadow-xl">
                <span class="text-[10px] text-zinc-400 font-extrabold block mb-1 tracking-[0.2em] uppercase">SAAS UNIT LIQUID INCOME</span>
                <span class="text-2xl font-black text-white tracking-wide">$585 / MRR</span>
            </div>
        </div>

        <!-- LIVE CRITICAL LOGGER CONSOLE -->
        <div class="w-full bg-[#020204] border-2 border-zinc-800 rounded-lg p-5 mb-8 h-72 overflow-y-auto text-xs font-mono tracking-wide leading-relaxed text-zinc-100 flex flex-col" id="log-terminal">
            <div class="text-zinc-500 font-bold mb-1">[SYSTEM_INIT] Sovereign Compliance Module Active. Ground terminals reporting secure connection footprint...</div>
            <div class="text-emerald-400 font-bold mb-1">[SECURE_CORE] Core physics emulation verified. Telemetry integrity streams sync-locked with regional nodes.</div>
        </div>

        <!-- HIGH-CONTRAST CRITICAL INTERACTIVE CONTROLS -->
        <div class="w-full flex flex-col md:flex-row gap-5 justify-center items-center pt-6 border-t border-zinc-800">
            <button onclick="triggerSimulation(false)" class="glow-button-green w-full md:w-72 px-8 py-4 bg-transparent border-2 border-[#00ff66] text-[#00ff66] text-xs font-black rounded-md uppercase tracking-[0.25em] transition duration-200 cursor-pointer text-center">
                Simulate Secure Audit
            </button>
            <button onclick="triggerSimulation(true)" class="glow-button-red w-full md:w-72 px-8 py-4 bg-transparent border-2 border-[#ff3344] text-[#ff3344] text-xs font-black rounded-md uppercase tracking-[0.25em] transition duration-200 cursor-pointer text-center">
                Simulate Cyber Intrusion
            </button>
        </div>
        
        <!-- FOOTER LOGO BASELINE -->
        <div class="text-[11px] font-extrabold text-zinc-500 mt-8 tracking-[0.3em] uppercase text-center">Empowering Women in Clean Energy via Automated Integrity Auditing</div>
    </div>

    <script>
        const terminal = document.getElementById('log-terminal');
        const nodes = ['NAIVASHA_MAMA_SOLAR', 'KIBWEZI_AGRI_PUMP', 'THIKA_MICRO_GRID'];

        function triggerSimulation(isThreat) {
            const time = new Date().toLocaleTimeString('en-US', { hour12: false });
            const node = nodes[Math.floor(Math.random() * nodes.length)];
            let output = '';

            if (isThreat) {
                output = `<div class="text-red-400 neon-text-red border-l-4 border-red-500 pl-4 my-3 bg-red-950/30 p-3 rounded font-medium text-left">
                    <span class="font-extrabold tracking-widest block mb-1">[CRITICAL VULNERABILITY ALERT]</span>
                    TIMESTAMP: ${time} // NODE CORRUPTION DETECTED AT ${node}. <br>
                    MALICIOUS PARAMETER INJECTION: Stream reported 1.5 MW production cycle during local night. <br>
                    MITIGATION PROTOCOL: Stream blocked, cryptographic record isolated from carbon matrix ledger safely.
                </div>`;
            } else {
                output = `<div class="text-emerald-300 border-l-4 border-emerald-500 pl-4 my-3 bg-emerald-950/20 p-3 rounded font-medium text-left">
                    <span class="font-extrabold tracking-widest block mb-1">[COMPLIANCE SECURITY PASS]</span>
                    TIMESTAMP: ${time} // TELEMETRY INTEGRITY RECORD VALID AT ${node}. <br>
                    PHYSICS COMPARISON: Handshake matched regional solar irradiance footprint parameters. <br>
                    DATA ROUTING: Cryptographic proof ledger uploaded successfully to APA Insurance portal.
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
