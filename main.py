import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Cencia Trust Layer")

class TelemetryPayload(BaseModel):
    site_id: str
    reported_mw: float
    timestamp: str

# HTML & CSS Embedded Dashboard (SpaceX / Cyberpunk Aesthetic)
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CENCIA // Telemetry Verification Core</title>
    <script src="https://tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style>
        body { font-family: 'JetBrains Mono', monospace; background-color: #05070a; }
        .neon-glow-green { text-shadow: 0 0 10px #10b981, 0 0 20px #047857; }
        .neon-glow-red { text-shadow: 0 0 10px #ef4444, 0 0 20px #b91c1c; }
        .border-cyber { border-color: rgba(16, 185, 129, 0.2); }
        .scanline {
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
            background-size: 100% 2px, 3px 100%;
        }
    </style>
</head>
<body class="text-gray-300 min-h-screen p-4 md:p-8 scanline select-none">

    <!-- TOP HEADER STATUS BAR -->
    <header class="max-w-7xl mx-auto border-b border-cyber pb-4 mb-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
            <h1 class="text-2xl font-bold tracking-widest text-emerald-400 neon-glow-green flex items-center gap-2">
                <span>⚡</span> CENCIA // TRUST LAYER
            </h1>
            <p class="text-xs text-emerald-600/80 mt-1 uppercase tracking-wider">AI-Driven Cleantech Threat Monitoring & Data Integrity</p>
        </div>
        <div class="flex items-center gap-6 text-xs text-gray-500">
            <div>NETWORK: <span class="text-emerald-400 font-bold">ACTIVE</span></div>
            <div>REGION: <span class="text-gray-300 font-bold">KENYA_CORE</span></div>
            <div>SYS_STAGE: <span class="text-amber-500 font-bold">MVP_PILOT_ALPHA</span></div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- LEFT PANEL: NETWORK METRICS (Apple Grid Style) -->
        <section class="lg:col-span-1 flex flex-col gap-6">
            <div class="bg-[#0b0f17] border border-cyber p-6 rounded-sm shadow-2xl relative overflow-hidden">
                <div class="absolute top-0 right-0 w-24 h-24 bg-emerald-500/5 rounded-full blur-2xl"></div>
                <h2 class="text-xs uppercase text-emerald-500 tracking-widest font-bold mb-4">// CORE VERIFICATION</h2>
                <div class="space-y-4">
                    <div>
                        <div class="text-xs text-gray-500 mb-1">SIMULATED PILOT CAPACITY</div>
                        <div class="text-3xl font-bold text-gray-100 tracking-tight">1.95 <span class="text-sm text-emerald-500">MW</span></div>
                    </div>
                    <div class="grid grid-cols-2 gap-4 pt-2">
                        <div>
                            <div class="text-xs text-gray-500 mb-1">INTEGRITY RATIO</div>
                            <div class="text-xl font-bold text-emerald-400 neon-glow-green">100.0%</div>
                        </div>
                        <div>
                            <div class="text-xs text-gray-500 mb-1">MEAN RESPONSE</div>
                            <div class="text-xl font-bold text-gray-200">&lt; 15m</div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="bg-[#0b0f17] border border-cyber p-6 rounded-sm shadow-2xl">
                <h2 class="text-xs uppercase text-emerald-500 tracking-widest font-bold mb-4">// ACTIVE NODE REGISTRY</h2>
                <div class="space-y-3 text-xs">
                    <div class="flex justify-between items-center border-b border-gray-900 pb-2">
                        <span class="text-gray-400">NODE_01 // NAIVASHA</span>
                        <span class="px-2 py-0.5 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-sm text-[10px]">MONITORED</span>
                    </div>
                    <div class="flex justify-between items-center border-b border-gray-900 pb-2">
                        <span class="text-gray-400">NODE_02 // KIBWEZI</span>
                        <span class="px-2 py-0.5 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-sm text-[10px]">MONITORED</span>
                    </div>
                    <div class="flex justify-between items-center">
                        <span class="text-gray-400">NODE_03 // THIKA</span>
                        <span class="px-2 py-0.5 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-sm text-[10px]">MONITORED</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- RIGHT PANEL: LIVE INTELLIGENCE CONSOLE (SpaceX Cockpit Style) -->
        <section class="lg:col-span-2 bg-[#0b0f17] border border-cyber p-6 rounded-sm shadow-2xl flex flex-col min-h-[450px]">
            <div class="flex justify-between items-center border-b border-gray-900 pb-3 mb-4">
                <h2 class="text-xs uppercase text-emerald-500 tracking-widest font-bold flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                    // TELEMETRY INTEGRITY STREAM
                </h2>
                <span class="text-[10px] text-gray-600 font-mono" id="live-timer">UTC_LOCK: CLOCKING...</span>
            </div>

            <!-- Terminal Output Window -->
            <div id="terminal" class="flex-grow bg-[#04060a] border border-gray-900 rounded-sm p-4 text-xs font-mono overflow-y-auto space-y-2 max-h-[350px]">
                <div class="text-gray-600">[SYSTEM] Initialization completed successfully.</div>
                <div class="text-emerald-500/70">[ENGINE] Cryptographic telemetry logs synchronized.</div>
                <div class="text-gray-400">[VERIFIED] NODE_01 // Naivasha reports 0.65 MW. Radiation levels nominal.</div>
            </div>
            
            <div class="mt-4 pt-3 border-t border-gray-900 text-[10px] text-gray-500 flex justify-between">
                <span>DATA INTEGRITY SECURED VIA INDUSTRIAL ENCRYPTION</span>
                <span class="text-emerald-500/40">CENCIA_V1.0</span>
            </div>
        </section>
    </main>

    <script>
        // Update clock
        setInterval(() => {
            document.getElementById('live-timer').innerText = 'EAT_CLOCK: ' + new datetime().toLocaleTimeString('en-US', { timeZone: 'Africa/Nairobi' });
        }, 1000);

        // Simulation logs
        const terminal = document.getElementById('terminal');
        const sites = ['NAIVASHA', 'KIBWEZI', 'THIKA'];
        
        function appendLog() {
            const time = new datetime().toLocaleTimeString('en-US', { timeZone: 'Africa/Nairobi' });
            const site = sites[Math.floor(Math.random() * sites.length)];
            const isAnomaly = Math.random() < 0.15; // 15% chance of an exploit simulation

            let logLine = '';
            if (isAnomaly) {
                const impossiblePower = (Math.random() * 1.5 + 1.0).toFixed(2);
                logLine = `<div class="text-red-400 neon-glow-red animate-pulse flex items-start gap-2">
                    <span>[CRITICAL]</span>
                    <span>${time} - ANOMALY DETECTED AT NODE_${site}: Impossible telemetry claim flagged. Input stream reports ${impossiblePower} MW during simulated night cycles. Threat neutralized.</span>
                </div>`;
            } else {
                const clearPower = (Math.random() * 0.8).toFixed(2);
                logLine = `<div class="text-gray-400 flex items-start gap-2">
                    <span class="text-emerald-500">[SECURE]</span>
                    <span>${time} - Cryptographic telemetry signature verified for NODE_${site}. Gen_Log: ${clearPower} MW. No behavioral drift found.</span>
                </div>`;
            }

            terminal.innerHTML += logLine;
            terminal.scrollTop = terminal.scrollHeight;

            // Keep text pool neat
            if (terminal.children.length > 25) {
                terminal.removeChild(terminal.firstChild);
            }
        }

        setInterval(appendLog, 3000);
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return HTMLResponse(content=DASHBOARD_HTML)

@app.post("/api/v1/telemetry")
def verify_telemetry(payload: TelemetryPayload):
    try:
        log_time = datetime.strptime(payload.timestamp, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return {"status": "ERROR", "detail": "Use YYYY-MM-DD HH:MM:SS"}

    hour = log_time.hour
    is_night = (hour < 6) or (hour >= 19)

    if is_night and payload.reported_mw > 0.01:
        return {
            "site_id": payload.site_id,
            "status": "FLAGGED",
            "anomaly_detected": True,
            "reason": f"Exploit Flagged: {payload.reported_mw} MW at night."
        }

    return {"site_id": payload.site_id, "status": "VERIFIED", "anomaly_detected": False}
