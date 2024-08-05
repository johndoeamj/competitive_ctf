import gmpy2


def cube_root_mod(c, n):
    # Convert c and n to gmpy2 mpz integers
    c = gmpy2.mpz(c)
    n = gmpy2.mpz(n)

    # Compute the integer cube root
    m = gmpy2.iroot(c, 3)[0]

    # Check if the cube of m mod n equals c
    if gmpy2.powmod(m, 3, n) == c:
        return m
    else:
        raise ValueError("Cube root modulo does not match")

def number_to_hex(n):
    hex_string = hex(n)[2:]  # Convert to hex and remove '0x' prefix
    # Make sure the length of hex_string is even
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    return hex_string

def hex_to_ascii(hex_string):
    bytes_object = bytes.fromhex(hex_string)
    return bytes_object.decode("ASCII")

c = 13037717184940851534440408074902031173938827302834506159512256813794613267487160058287930781080450199371859916605839773796744179698270340378901298046506802163106509143441799583051647999737073025726173300915916758770511497524353491642840238968166849681827669150543335788616727518429916536945395813
n = 135112325288715136727832177735512070625083219670480717841817583343851445454356579794543601926517886432778754079508684454122465776544049537510760149616899986522216930847357907483054348419798542025184280105958211364798924985051999921354369017984140216806642244876998054533895072842602131552047667500910960834243

try:
    m = cube_root_mod(c, n)
    print(f"Plaintext message (m) is: {m}")

    number = 235360648501923597413504426673122110620436456645077837051697081536135487875222175025616363200782717
    hex_string = number_to_hex(number)
    ascii_message = hex_to_ascii(hex_string)

    print(f"Flag: {ascii_message}")
except ValueError as e:
    print(e)
