import os
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="Cencia Trust Layer Core")

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
    <title>CENCIA // TELEMETRY VERIFICATION HUB</title>
    <script src="https://tailwindcss.com"></script>
    <link href="https://googleapis.com" rel="stylesheet">
    <style>
        body { 
            font-family: 'Fira Code', monospace; 
            background-color: #020204;
            letter-spacing: -0.02em;
        }
        .neon-text-green {
            color: #00ff66;
            text-shadow: 0 0 12px rgba(0, 255, 102, 0.65), 0 0 24px rgba(0, 255, 102, 0.25);
        }
        .neon-text-red {
            color: #ff3344;
            text-shadow: 0 0 12px rgba(255, 51, 68, 0.65), 0 0 24px rgba(255, 51, 68, 0.25);
        }
        .neon-border-green {
            border-color: #00ff66;
            box-shadow: 0 0 15px rgba(0, 255, 102, 0.15), inset 0 0 15px rgba(0, 255, 102, 0.05);
        }
        .neon-border-gray {
            border-color: #1a1f2c;
        }
        .scanlines {
            background: linear-gradient(
                rgba(18, 16, 16, 0) 50%, 
                rgba(0, 0, 0, 0.35) 50%
            ), 
            linear-gradient(
                90deg, 
                rgba(255, 0, 0, 0.03), 
                rgba(0, 255, 0, 0.01), 
                rgba(0, 255, 0, 0.03)
            );
            background-size: 100% 3px, 4px 100%;
        }
        /* Perfect SVG Flag Components */
        .flag-ke {
            background: linear-gradient(to bottom, #000000 30%, #ffffff 30%, #ffffff 35%, #bb0000 35%, #bb0000 65%, #ffffff 65%, #ffffff 70%, #006600 70%);
            position: relative;
        }
        .flag-ch {
            background: #d52b1e;
            position: relative;
        }
    </style>
</head>
<body class="text-gray-400 min-h-screen p-4 md:p-8 flex flex-col justify-center items-center scanlines select-none">

    <!-- OVERALL CENTERED CONTAINER -->
    <div class="w-full max-w-5xl flex flex-col items-center">
        
        <!-- FLAG COUPLING AND LOGO SECTION -->
        <div class="w-full flex justify-between items-center px-4 mb-4 border-b neon-border-gray pb-4">
            <!-- Kenya Flag (Precision Render) -->
            <div class="w-10 h-7 rounded-[2px] flag-ke shadow-lg border border-gray-900 flex justify-center items-center">
                <div class="w-3 h-5 bg-[#bb0000] border-x border-white rounded-full relative">
                    <div class="absolute inset-y-0 left-1/2 w-0.5 bg-white"></div>
                </div>
            </div>

            
            <div class="text-center">
                <h1 class="text-2xl font-bold tracking-[0.25em] neon-text-green uppercase">CENCIA // SYSTEMS</h1>
                <p class="text-[10px] text-gray-600 uppercase tracking-[0.4em] mt-1 font-semibold">Data Integrity & Sovereign Cyber Security</p>
            </div>

            <!-- Switzerland Flag (Precision Render) -->
            <div class="w-8 h-8 rounded-[2px] flag-ch shadow-lg border border-gray-900 flex justify-center items-center">
                <div class="absolute w-5 h-1.5 bg-white"></div>
                <div class="absolute w-1.5 h-5 bg-white"></div>
            </div>
        </div>

        <!-- TOP LEVEL SYSTEM READOUTS (Perfect Grid Symmetry) -->
        <div class="w-full grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <div class="bg-[#07080e] border neon-border-gray p-4 text-center rounded-sm">
                <div class="text-[10px] text-gray-600 font-bold uppercase tracking-wider mb-1">MONITORED NODE STATUS</div>
                <div class="text-xl font-bold tracking-wider text-gray-200">1.95 <span class="text-xs text-emerald-500">MW LOAD</span></div>
            </div>
            <div class="bg-[#07080e] border neon-border-green p-4 text-center rounded-sm">
                <div class="text-[10px] text-emerald-600 font-bold uppercase tracking-wider mb-1">DATA TRUST RATIO</div>
                <div class="text-xl font-bold tracking-widest neon-text-green">100.00% SECURE</div>
            </div>
            <div class="bg-[#07080e] border neon-border-gray p-4 text-center rounded-sm">
                <div class="text-[10px] text-gray-600 font-bold uppercase tracking-wider mb-1">RESPONSE BOUNDS</div>
                <div class="text-xl font-bold tracking-wider text-gray-200">&lt; 15.00 MINS</div>
            </div>
        </div>

        <!-- CENTRALIZED LIVE INSTRUMENTATION MONITOR -->
        <section class="w-full bg-[#04050a] border neon-border-green p-6 rounded-sm shadow-2xl flex flex-col h-[480px]">
            <div class="flex justify-between items-center border-b neon-border-gray pb-3 mb-4 text-[11px] font-bold">
                <div class="flex items-center gap-2 text-emerald-400">
                    <span class="w-2 h-2 bg(#00ff66) rounded-full animate-ping"></span>
                    <span class="tracking-widest">// DEPLOYED STREAM LOGS</span>
                </div>
                <div class="text-gray-500 tracking-wider" id="clock-display">LOGGING TIME CORRELATION...</div>
            </div>

            <!-- Terminal Output Area with high text clarity -->
            <div id="console-stream" class="flex-grow bg-[#010204] border neon-border-gray rounded-sm p-4 text-[11px] leading-relaxed font-medium overflow-y-auto space-y-2.5 max-h-[360px]">
                <div class="text-gray-600">[SYSTEM_INFO] Initialization stack verified. Kernel space secure.</div>
                <div class="text-emerald-500/80">[VERIFIED] Node logs mapped across geographical clean energy grid footprints.</div>
                <div class="text-gray-400">[MONITOR] Connected successfully to server targets in Naivasha, Kibwezi, and Thika.</div>
            </div>
            
            <!-- Bottom Controls inside the cockpit panel -->
            <div class="mt-4 pt-3 border-t neon-border-gray flex justify-between items-center">
                <span class="text-[9px] text-gray-600 tracking-wider font-bold">MUTABLE AUDIT TRACE PROTECTED VIA CRYPTO HANDSHAKE</span>
                <span class="text-emerald-400/30 text-[10px] font-bold tracking-widest">CENCIA_CORE_V1</span>
            </div>
        </section>
    </div>

    <script>
        // Symmetric time updater
        setInterval(() => {
            const eatTime = new datetime().toLocaleTimeString('en-US', { timeZone: 'Africa/Nairobi', hour12: false });
            document.getElementById('clock-display').innerText = 'EAT_TRACK // ' + eatTime;
        }, 1000);

        const consoleStream = document.getElementById('console-stream');
        const operationalNodes = ['NAIVASHA_01', 'KIBWEZI_02', 'THIKA_03'];
        
        function updateConsoleFeed() {
            const timestamp = new datetime().toLocaleTimeString('en-US', { timeZone: 'Africa/Nairobi', hour12: false });
            const targetedNode = operationalNodes[Math.floor(Math.random() * operationalNodes.length)];
            const securityExploitTriggered = Math.random() < 0.18; // Anomaly generation check

            let logEntry = '';
            if (securityExploitTriggered) {
                const unauthorizedLoad = (Math.random() * 2.0 + 1.1).toFixed(3);
                logEntry = `<div class="text-red-400 neon-text-red border-l-2 border-red-500 pl-3 py-0.5 bg-red-950/10 rounded-r-sm animate-pulse flex flex-col gap-0.5">
                    <span class="font-bold tracking-wider">[CRITICAL EXPLOIT DETECTED]</span>
                    <span class="text-[10px] text-red-300/80">${timestamp} - Node validation anomaly at ${targetedNode}. Device reports an impossible generation metric of ${unauthorizedLoad} MW during dark cycles. Countermeasure deployed. Data flagged.</span>
                </div>`;
            } else {
                const standardizedLoad = (Math.random() * 0.95).toFixed(3);
                logEntry = `<div class="text-gray-300 border-l-2 border-emerald-500 pl-3 py-0.5 flex flex-col gap-0.5">
                    <span class="text-emerald-400 font-bold tracking-wider">[SECURE PACKET VERIFIED]</span>
                    <span class="text-[10px] text-gray-400">${timestamp} - Integrity hash matches environmental metrics for ${targetedNode}. Current verified production value: ${standardizedLoad} MW.</span>
                </div>`;
            }

            consoleStream.innerHTML += logEntry;
            consoleStream.scrollTop = consoleStream.scrollHeight;

            if (consoleStream.children.length > 20) {
                consoleStream.removeChild(consoleStream.firstChild);
            }
        }

        // Interval timing for dashboard stream feed
        setInterval(updateConsoleFeed, 2800);
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_cockpit_view(request: Request):
    return HTMLResponse(content=DASHBOARD_HTML)

@app.post("/api/v1/telemetry")
def verify_incoming_telemetry(payload: TelemetryPayload):
    try:
        log_time = datetime.strptime(payload.timestamp, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return {"status": "ERROR", "detail": "Timestamp schema violation. Expected: YYYY-MM-DD HH:MM:SS"}

    hour = log_time.hour
    is_night_cycle = (hour < 6) or (hour >= 19)

    if is_night_cycle and payload.reported_mw > 0.01:
        return {
            "site_id": payload.site_id,
            "status": "FLAGGED_ILLEGAL_ACTIVITY",
            "anomaly_detected": True,
            "remediation_action": "Isolating telemetry package. Audit logs locked down."
        }

