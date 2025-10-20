# app.py
from flask import Flask, render_template, request, jsonify
from unicorn import *
from unicorn.x86_const import *
from keystone import *

app = Flask(__name__)

def run_simulation(asm_code: str):
    """
    Assembles and runs the 8086 code using Keystone and Unicorn.
    """
    try:
        # Initialize Keystone for 16-bit x86 assembly
        ks = Ks(KS_ARCH_X86, KS_MODE_16)
        machine_code, count = ks.asm(asm_code)
        
        # Define a memory address to load the code
        CODE_ADDRESS = 0x1000

        # Initialize Unicorn for 16-bit x86 CPU
        mu = Uc(UC_ARCH_X86, UC_MODE_16)
        # Map 2MB of memory for the emulator
        mu.mem_map(CODE_ADDRESS, 2 * 1024 * 1024)
        # Write the machine code to the emulator's memory
        mu.mem_write(CODE_ADDRESS, bytes(machine_code))

        # Start the emulation from the code address
        mu.emu_start(CODE_ADDRESS, CODE_ADDRESS + len(machine_code))

        # After emulation, read the final values of all required registers
        registers = {
            'AX': f"{mu.reg_read(UC_X86_REG_AX):04X}",
            'BX': f"{mu.reg_read(UC_X86_REG_BX):04X}",
            'CX': f"{mu.reg_read(UC_X86_REG_CX):04X}",
            'DX': f"{mu.reg_read(UC_X86_REG_DX):04X}",
            'SI': f"{mu.reg_read(UC_X86_REG_SI):04X}",
            'DI': f"{mu.reg_read(UC_X86_REG_DI):04X}",
            'SP': f"{mu.reg_read(UC_X86_REG_SP):04X}",
            'BP': f"{mu.reg_read(UC_X86_REG_BP):04X}",
            'IP': f"{mu.reg_read(UC_X86_REG_IP):04X}",
        }
        
        # Note: Flag registers are more complex to read in Unicorn.
        # We will omit them for this version, but they can be added.
        flags = {} # Placeholder for flags

        return {'success': True, 'registers': registers, 'flags': flags}
        
    except Exception as e:
        # Return an error if assembly or emulation fails
        return {'success': False, 'error': str(e)}


@app.route('/')
def index():
    """Renders the main simulator page."""
    return render_template('index.html')


@app.route('/execute', methods=['POST'])
def execute_code():
    """API endpoint to execute assembly code."""
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'success': False, 'error': 'Invalid request.'}), 400

    asm_code = data['code']
    result = run_simulation(asm_code)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)