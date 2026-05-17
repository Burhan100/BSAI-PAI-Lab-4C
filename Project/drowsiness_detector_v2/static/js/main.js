const statusCard  = document.getElementById('statusCard');
const statusIcon  = document.getElementById('statusIcon');
const statusText  = document.getElementById('statusText');
const earValue    = document.getElementById('earValue');
const earBar      = document.getElementById('earBar');
const frameCount  = document.getElementById('frameCount');
const overlay     = document.getElementById('overlay');
const alarm       = document.getElementById('alarmSound');

let alarmPlaying  = false;
let audioCtx      = null;
let beepInterval  = null;

// Web Audio API beep — backup jab file load na ho
function startBeep() {
  if (beepInterval) return;
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  function beep() {
    const osc  = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.frequency.value = 880;
    gain.gain.setValueAtTime(0.8, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.4);
    osc.start();
    osc.stop(audioCtx.currentTime + 0.4);
  }
  beep();
  beepInterval = setInterval(beep, 800);
}

function stopBeep() {
  clearInterval(beepInterval);
  beepInterval = null;
  if (audioCtx) { audioCtx.close(); audioCtx = null; }
}

function playAlarm() {
  alarm.play().catch(() => {
    startBeep();
  });
}

function stopAlarm() {
  alarm.pause();
  alarm.currentTime = 0;
  stopBeep();
}

async function fetchStatus() {
  try {
    const res  = await fetch('/status');
    const data = await res.json();

    statusText.textContent = data.status;
    statusCard.className   = 'status-card';

    if (data.drowsy) {
      statusCard.classList.add('alert');
      statusIcon.textContent = '😴';
      overlay.classList.remove('hidden');
      if (!alarmPlaying) {
        playAlarm();
        alarmPlaying = true;
      }
    } else {
      if (data.status === 'Alert & Awake') {
        statusCard.classList.add('ok');
        statusIcon.textContent = '✅';
      } else {
        statusIcon.textContent = '👁️';
      }
      overlay.classList.add('hidden');
      stopAlarm();
      alarmPlaying = false;
    }

    const ear = data.ear;
    const pct = Math.min((ear / 0.4) * 100, 100);
    earValue.textContent     = ear.toFixed(3);
    earBar.style.width       = pct + '%';
    earBar.style.background  = ear < 0.25 ? '#dc2626' : '#16a34a';

    frameCount.textContent = data.frames;

  } catch (e) {
    statusText.textContent = 'Connection error';
  }
}

setInterval(fetchStatus, 200);
fetchStatus();
