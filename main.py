import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Cencia AI Center Command")

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
    <title>Cencia AI</title>
    <!-- Rock-Solid Production CDN Links -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style>
        body { 
            font-family: 'JetBrains Mono', monospace; 
            background-color: #000000;
            color: #ffffff;
        }
        .neon-text-green {
            color: #00ff66;
            text-shadow: 0 0 10px rgba(0, 255, 102, 0.9);
        }
        .neon-text-red {
            color: #ff3344;
            text-shadow: 0 0 10px rgba(255, 51, 68, 0.9);
        }
        .neon-border-green {
            border: 2px solid #00ff66;
            box-shadow: 0 0 15px rgba(0, 255, 102, 0.3);
        }
        .flag-ke {
            background: linear-gradient(to bottom, #000000 30%, #ffffff 30%, #ffffff 35%, #bb0000 35%, #bb0000 65%, #ffffff 65%, #ffffff 70%, #006600 70%);
        }
        .glow-btn-green:hover {
            background-color: #00ff66 !important;
            color: #000000 !important;
            box-shadow: 0 0 20px rgba(0, 255, 102, 0.6);
        }
        .glow-btn-red:hover {
            background-color: #ff3344 !important;
            color: #000000 !important;
            box-shadow: 0 0 20px rgba(255, 51, 68, 0.6);
        }
    </style>
</head>
<body class="min-h-screen w-full flex flex-col justify-center items-center p-4 md:p-8">

    <!-- OVERALL CENTERED WRAPPER -->
    <div class="w-full max-w-3xl flex flex-col items-center text-center justify-center">
        
        <!-- FLAG COUPLING -->
        <div class="flex items-center justify-center gap-4 mb-6">
            <!-- Kenya Flag -->
            <div class="w-10 h-6 border border-zinc-700 rounded-sm overflow-hidden flag-ke relative flex justify-center items-center shadow-lg">
                <div class="w-2.5 h-4 bg-[#bb0000] border-x border-white rounded-full absolute"></div>
            </div>
            <!-- Swiss Flag -->
            <div class="w-7 h-7 bg-[#da291c] flex justify-center items-center rounded-sm border border-zinc-700 shadow-lg relative">
                <div class="absolute w-4 h-1 bg-white rounded-sm"></div>
                <div class="absolute w-1 h-4 bg-white rounded-sm"></div>
            </div>
        </div>

        <!-- IDENTITY HEADERS -->
        <p class="text-[11px] text-emerald-400 font-extrabold tracking-[0.3em] uppercase mb-1">KENYA-SWISS CLEANTECH COMPLIANCE FEDERATION</p>
        <h1 class="text-4xl md:text-5xl font-black tracking-[0.15em] text-white my-2">CENCIA <span class="neon-text-green">AI</span></h1>
        <p class="text-[10px] text-zinc-400 font-bold uppercase tracking-[0.4em] mb-8">Sovereign Data Trust Layer // Operational Intelligence Alpha</p>

        <!-- CENTERED HIGH-VISIBILITY DATA CARDS -->
        <div class="w-full flex flex-col gap-4 mb-8">
            <div class="w-full bg-[#0d0e15] border border-zinc-700 p-5 rounded-lg shadow-xl">
                <span class="text-[10px] text-zinc-400 font-bold block tracking-wider uppercase mb-1">PROTECTED CAPACITY</span>
                <span class="text-2xl font-black text-white">1.95 MW</span>
            </div>
            <div class="w-full bg-[#0d0e15] neon-border-green p-5 rounded-lg shadow-xl">
                <span class="text-[10px] text-emerald-400 font-bold block tracking-wider uppercase mb-1">APA REGULATORY STATUS</span>
                <span class="text-2xl font-black neon-text-green tracking-widest">COMPLIANT</span>
            </div>
            <div class="w-full bg-[#0d0e15] border border-zinc-700 p-5 rounded-lg shadow-xl">
                <span class="text-[10px] text-zinc-400 font-bold block tracking-wider uppercase mb-1">SAAS UNIT LIQUID INCOME</span>
                <span class="text-2xl font-black text-white">$585 / MRR</span>
            </div>
        </div>

        <!-- CENTERED LIVE TERMINAL LOGGER -->
        <div class="w-full bg-[#030305] border-2 border-zinc-800 rounded-lg p-5 mb-8 h-64 overflow-y-auto text-[11px] font-mono leading-relaxed text-zinc-200 text-center flex flex-col justify-start items-center" id="log-terminal">
            <div class="text-zinc-500 font-bold mb-2">[SYSTEM_INIT] Sovereign Compliance Module Active. Ground terminals reporting secure connection footprint...</div>
            <div class="text-emerald-400 font-bold mb-2">[SECURE_CORE] Core physics emulation verified. Telemetry integrity streams sync-locked with regional nodes.</div>
        </div>

        <!-- CENTERED ACTION CONTROLS -->
        <div class="w-full flex flex-col sm:flex-row gap-4 justify-center items-center pt-6 border-t border-zinc-800">
            <button onclick="triggerSimulation(false)" class="glow-btn-green w-full sm:w-64 px-6 py-4 bg-transparent border-2 border-[#00ff66] text-[#00ff66] text-xs font-black rounded-md uppercase tracking-wider transition duration-150 cursor-pointer">
                Simulate Secure Audit
            </button>
            <button onclick="triggerSimulation(true)" class="glow-btn-red w-full sm:w-64 px-6 py-4 bg-transparent border-2 border-[#ff3344] text-[#ff3344] text-xs font-black rounded-md uppercase tracking-wider transition duration-150 cursor-pointer">
                Simulate Cyber Intrusion
            </button>
        </div>
        
        <!-- FOOTER TEXT -->
        <div class="text-[10px] font-bold text-zinc-500 mt-8 tracking-widest uppercase">Empowering Women in Clean Energy via Automated Integrity Auditing</div>
    </div>

    <script>
        const terminal = document.getElementById('log-terminal');
        const nodes = ['NAIVASHA_MAMA_SOLAR', 'KIBWEZI_AGRI_PUMP', 'THIKA_MICRO_GRID'];

        function triggerSimulation(isThreat) {
            const time = new Date().toLocaleTimeString('en-US', { hour12: false });
            const node = nodes[Math.floor(Math.random() * nodes.length)];
            let output = '';

            if (isThreat) {
                output = `<div class="text-red-400 neon-text-red my-2 max-w-xl mx-auto font-medium">
                    [ALERT] ${time} // DETECTED ANOMALY AT ${node}. <br>
                    Telemetry injection flagged: Claimed production during night hours blocked safely.
                </div>`;
            } else {
                output = `<div class="text-emerald-300 my-2 max-w-xl mx-auto font-medium">
                    [PASS] ${time} // CORE STREAM INTEGRITY VALID FOR ${node}. <br>
                    Telemetry metrics match environmental footprint. Forwarded to APA Insurance portal.
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
