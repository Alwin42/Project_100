// static/main.js
document.addEventListener('DOMContentLoaded', () => {
    const runButton = document.getElementById('runButton');
    const codeInput = document.getElementById('codeInput');
    const outputLog = document.getElementById('outputLog');

    runButton.addEventListener('click', async () => {
        const code = codeInput.value;
        if (!code.trim()) {
            outputLog.className = 'alert alert-warning';
            outputLog.textContent = 'Code editor is empty.';
            return;
        }

        outputLog.className = 'alert alert-info';
        outputLog.textContent = 'Executing...';
        runButton.disabled = true;

        // Reset register and flags display
        resetUI();

        try {
            const response = await fetch('/execute', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ code: code }),
            });

            const result = await response.json();

            if (result.success) {
                updateUI(result.registers, result.flags);
                outputLog.className = 'alert alert-success';
                outputLog.textContent = 'Execution successful!';
            } else {
                outputLog.className = 'alert alert-danger';
                outputLog.textContent = `Error: ${result.error}`;
            }
        } catch (error) {
            outputLog.className = 'alert alert-danger';
            outputLog.textContent = `Network or server error: ${error}`;
        } finally {
            runButton.disabled = false;
        }
    });

    function resetUI() {
        // Reset registers to 0000
        const registerElements = document.querySelectorAll('.register-value');
        registerElements.forEach(el => el.textContent = '0000');

        // Turn off all flag LEDs
        const flagLEDs = document.querySelectorAll('.flag-led');
        flagLEDs.forEach(led => led.classList.remove('active'));
    }

    function updateUI(registers, flags) {
        // Update all register values on the page
        for (const reg in registers) {
            const element = document.getElementById(`reg-${reg.toLowerCase()}`);
            if (element) {
                element.textContent = registers[reg];
            }
        }

        // Update all flag LEDs on the page
        // Note: As mentioned, the current Unicorn setup doesn't easily expose individual flags.
        // This part will only work if the backend is updated to provide actual flag values (0 or 1).
        for (const flag in flags) {
            const element = document.getElementById(`flag-${flag.toLowerCase()}`);
            if (element) {
                if (flags[flag] === 1) {
                    element.classList.add('active');
                } else {
                    element.classList.remove('active');
                }
            }
        }
    }
});