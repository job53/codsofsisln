import re

MORSE_CODE = {
    '.-': 'A',   '-...': 'B', '-.-.': 'C',  '-..': 'D',
    '.': 'E',    '..-.': 'F', '--.': 'G',   '....': 'H',
    '..': 'I',   '.---': 'J', '-.-': 'K',   '.-..': 'L',
    '--': 'M',   '-.': 'N',   '---': 'O',   '.--.': 'P',
    '--.-': 'Q', '.-.': 'R',  '...': 'S',   '-': 'T',
    '..-': 'U',  '...-': 'V', '.--': 'W',   '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    
    ".-.-.-": ".", "--..--": ",", "..--..": "?", ".----.": "'",
    "-.-.--": "!", "-..-.": "/", "-.--.": "(", "-.--.-": ")",
    ".-...": "&", "---...": ":", "-.-.-.": ";", "-...-": "=",
    ".-.-.": "+", "-....-": "-", "..--.-": "_", ".-..-.": '"',
    "...-..-": "$", ".--.-.": "@"
}

def decode_bits(bits):
    b = bits.strip('0')
    if not b: return ""
    groups = re.findall(r'(1+|0+)', b)
    unit = min(len(g) for g in groups)
    code = ""
    for g in groups:
        l = len(g) // unit
        if g[0] == '1':
            code += '.' if l == 1 else '-' if l == 3 else '.'
        else:
            if l == 3:
                code += ' '
            elif l == 7:
                code += '   '
            # En otros casos (pausas intermedias) se aproxima a la separación entre letras
            elif l > 1:
                code += ' ' if l < 7 else '   '
    return code

def decode_morse(morse):
    return " ".join(
        "".join(MORSE_CODE.get(c, "") for c in w.split())
        for w in morse.strip().split("   ")
    )

# Ejemplo de uso:
if __name__ == '__main__':
    bits_input = ("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")
    print(decode_morse(decode_bits(bits_input)))  # Output: HEY JUDE