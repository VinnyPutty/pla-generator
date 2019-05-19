import inspect
import os
import math

# global constants
BLANK_LAYOUT_ENTRIES = {
        "array": "A  {0} {1} {2} {3};\n",
        "composite": "C \"{0}\" T {1},{2};\n",
        "3-pt-wire": "W 400 {0},{1} {2},{3} {4},{5};\n",
        "contact": "B 200,200 {0},{1};\n",
        "label": "T 50 {0},{1} 0 FONTWIRE \"{2}\";\n"
    }


def load_cmos_layers(load_from_file=False):
    if load_from_file:
        cmos_layers_file = open("./definitions/cmos_layers.lay", "r")
        cmos_layers = cmos_layers_file.read()[:-1]
        cmos_layers_file.close()
    else:
        cmos_layers = inspect.cleandoc(
            '''
            (Lay File generated by Layout)
            0 10000 ;
            L "Default" NONE 192 0 0 0 1 1 1 0 0 0 1200 100 5 100 0 0;
            L CWN NONE 128 128 128 1 1 1 1 0 1 0 1200 100 50 100 12 8;
            L CAN NONE 0 128 0 0 1 1 0 0 0 0 1200 100 50 400 0 0;
            L CAP NONE 255 255 0 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CPG NONE 255 0 0 0 1 1 0 0 0 0 1200 100 50 200 0 0;
            L CM1 NONE 72 72 200 0 1 1 0 0 1 0 1200 100 50 100 1 0;
            L CCC NONE 64 0 64 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM2 NONE 255 170 170 1 1 1 0 0 0 0 1200 100 50 400 12 0;
            L CV1 NONE 255 255 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM3 NONE 128 255 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM4 NONE 160 0 0 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM5 NONE 128 255 128 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CV2 NONE 244 213 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CV3 NONE 138 21 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CV4 NONE 21 21 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L XP NONE 255 255 213 1 0 1 0 0 1 0 1200 100 50 100 0 0;
            L COG NONE 255 0 128 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L BND NONE 255 128 0 1 0 1 0 0 1 0 100 100 50 100 0 0;
            L TXT NONE 0 255 255 0 1 1 0 0 0 0 50 100 50 100 0 0;
            '''
        ) + '\n'
    return cmos_layers


def load_pla_codes(load_from_file=False):
    pla_codes = ""
    if load_from_file:
        pla_codes_file = open("./pla_codes/1024x1024_pla_codes.pla")
        pla_codes = pla_codes_file.read()
        pla_codes_file.close()
    else:
        pla_codes = inspect.cleandoc(
            '''
            inputs:in
            outputs:out
            ---
            codes:
            out:0,1
            '''
        )

    # TODO add '..' operator functionality to pla inputs reader and move to separate function
    #   '..' op definition:
    #   '..' op should allow for the definition of a sequence of inputs using only the starting
    #   and ending numbers, chars, etc.; we should try to infer the step and type of sequence from
    #   the given start and end to the sequence
    #   '..' op is allowed to be incorporated into any input in the comma-separated list, so the sequence
    #   will need to be expanded in place while extracting the inputs into a data struct
    pla_inputs = tuple(pla_codes[pla_codes.index(':', pla_codes.index("inputs")) + 1:pla_codes.index('outputs') - 1].split(','))
    # TODO implement pla_outputs parser and add to pla_inputs_outputs_parser function
    pla_outputs = tuple()
    # print(pla_codes)
    pla_codes = pla_codes[pla_codes.index('\n', pla_codes.index("codes")) + 1:].split('\n')
    # print(type(pla_codes))
    # print(pla_codes)

    pla_codes_dict = {}
    code_count = 0
    line = ''
    for line in pla_codes:
        line = line.split(':')
        if line[1]:
            codes = tuple(line[1].split(','))
            pla_codes_dict[line[0]] = codes
            code_count += len(codes)

    # print(pla_dict)

    input_count = len(pla_codes[0].split(':')[1].split(',')[0])
    output_count = len(pla_codes_dict)

    return (pla_inputs, pla_outputs, pla_codes_dict, code_count, input_count, output_count)


def load_definitions(load_from_file=False):
    success = True
    definitions = None
    if load_from_file:
        success = False
        while not success:
            if not os.path.isfile("./definitions/compiled_definitions.lay"):
                return load_definitions(False)
            definitions_file = open("./definitions/compiled_definitions.lay", "r")
            definitions = definitions_file.read()
            definitions_file.close()
            success = True
            break
    else:
        definitions = inspect.cleandoc(
            '''
            (Lay File generated by Layout)
            0 10000 ;
            L "Default" NONE 192 0 0 0 1 1 1 0 0 0 1200 100 5 100 0 0;
            L CWN NONE 128 128 128 1 1 1 1 0 1 0 1200 100 50 100 12 8;
            L CAN NONE 0 128 0 0 1 1 0 0 0 0 1200 100 50 400 0 0;
            L CAP NONE 255 255 0 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CPG NONE 255 0 0 0 1 1 0 0 0 0 1200 100 50 200 0 0;
            L CM1 NONE 72 72 200 0 1 1 0 0 1 0 1200 100 50 100 1 0;
            L CCC NONE 64 0 64 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM2 NONE 255 170 170 1 1 1 0 0 0 0 1200 100 50 400 12 0;
            L CV1 NONE 255 255 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM3 NONE 128 255 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM4 NONE 160 0 0 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CM5 NONE 128 255 128 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CV2 NONE 244 213 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CV3 NONE 138 21 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L CV4 NONE 21 21 255 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L XP NONE 255 255 213 1 0 1 0 0 1 0 1200 100 50 100 0 0;
            L COG NONE 255 0 128 0 1 1 0 0 1 0 1200 100 50 100 0 0;
            L BND NONE 255 128 0 1 0 1 0 0 1 0 100 100 50 100 0 0;
            L TXT NONE 0 255 255 0 1 1 0 0 0 0 50 100 50 100 0 0;
            DS "PLA_OrPullup";
            L "Default";
            L CWN;
            B 3200,2400 1150,1800;
            L CAN;
            B 400,400 1150,2400;
            L CAP;
            B 400,400 350,1400;
            B 400,400 1950,1400;
            B 300,600 1950,1900;
            B 300,600 350,1900;
            B 400,400 1950,2400;
            B 400,400 350,2400;
            L CPG;
            B 2300,400 1150,1900;
            B 400,400 1150,1500;
            L CM1;
            B 400,1600 350,800;
            B 400,1700 1150,850;
            B 400,1600 1950,800;
            B 2300,400 1150,2400;
            L CCC;
            B 200,200 1950,1400;
            B 200,200 350,1400;
            B 200,200 1150,1500;
            B 200,200 350,2400;
            B 200,200 1950,2400;
            B 200,200 1150,2400;
            L CM2;
            B 2300,400 1150,500;
            W 400 200,2400 2100,2400;
            L CV1;
            B 200,200 1150,500;
            B 200,200 1150,2400;
            L BND;
            B 2300,3000 1150,1500;
            DF;
            DS "PLA_input";
            L "Default";
            L CWN;
            B 2400,2500 -1000,-2450;
            L CAN;
            B 1200,450 -1000,-375;
            B 400,400 -1400,-3200;
            L CAP;
            B 100,0 -650,-400;
            B 1200,900 -1000,-2250;
            L CPG;
            B 200,1400 -200,-700;
            B 300,400 -450,-1200;
            B 400,400 -700,-3200;
            W 200 -1000,-100 -1000,-750 -1100,-850 -1100,-1550 -1000,-1650 -1000,-3300;
            L CM1;
            B 400,2500 -600,-1450;
            B 400,900 -1400,-650;
            B 400,1600 -1400,-2600;
            B 400,400 -700,-3200;
            B 400,400 -400,-1200;
            L CCC;
            B 200,200 -1400,-400;
            B 200,200 -600,-400;
            B 200,200 -400,-1200;
            B 200,200 -1400,-2000;
            B 200,200 -1400,-2500;
            B 200,200 -600,-2000;
            B 200,200 -600,-2500;
            B 200,200 -700,-3200;
            B 200,200 -1400,-3200;
            L CM2;
            W 400 -200,-900 -1400,-900;
            W 400 -1400,-2500 -200,-2500;
            B 400,400 -700,-3200;
            L CV1;
            B 200,200 -1400,-900;
            B 200,200 -1400,-2500;
            B 200,200 -700,-3200;
            L BND;
            B 1600,3700 -800,-1850;
            DF;
            DS "PLA_io_if";
            L "Default";
            L CWN;
            B 900,1900 450,-2750;
            L CAN;
            B 400,1200 400,-2700;
            L CAP;
            B 400,400 200,-400;
            L CM1;
            B 400,1600 400,-2500;
            B 900,400 450,-400;
            L CCC;
            B 200,200 400,-2300;
            B 200,200 400,-2700;
            B 200,200 400,-3100;
            B 200,200 200,-400;
            L CM2;
            W 400 700,-200 700,-900 200,-900;
            B 400,800 400,-2100;
            W 400 200,-2500 336,-2500 436,-2600 700,-2600;
            L CV1;
            B 200,200 400,-1900;
            B 200,200 700,-400;
            L BND;
            B 900,3700 450,-1850;
            DF;
            DS "PLA_orPlane";
            L "Default";
            L CAP;
            B 400,400 1150,1050;
            L CPG;
            B 2300,200 1150,1450;
            B 2300,200 1150,650;
            L CM1;
            B 400,2100 1950,1050;
            B 400,2100 1150,1050;
            B 400,2100 350,1050;
            L CCC;
            B 200,200 1150,1050;
            L BND;
            B 2300,2100 1150,1050;
            B 200,200 350,1050;
            B 200,200 1950,1050;
            B 200,100 1150,50;
            B 200,200 1150,200;
            B 200,200 1150,1900;
            B 200,100 1150,2050;
            DF;
            DS "PLA_ip_if";
            L "Default";
            L CAP;
            B 400,400 200,1050;
            L CPG;
            B 400,400 700,1750;
            B 400,400 700,350;
            B 200,200 800,1450;
            B 200,200 800,650;
            L CM1;
            B 900,400 450,1750;
            B 900,400 450,1050;
            B 900,400 450,350;
            L CCC;
            B 200,200 700,350;
            B 200,200 700,1750;
            B 200,200 200,1050;
            L CM2;
            W 400 700,1900 700,200;
            L CV1;
            B 200,200 700,1050;
            L BND;
            B 900,2100 450,1050;
            B 200,200 200,1750;
            B 200,200 200,350;
            DF;
            DS "PLA_andPlane";
            L "Default";
            L CAP;
            B 400,400 -1400,1050;
            L CPG;
            B 200,2100 -1000,1050;
            B 200,2100 -200,1050;
            L CM1;
            B 1600,400 -800,350;
            B 1600,400 -800,1050;
            B 1600,400 -800,1750;
            L CCC;
            B 200,200 -1400,1050;
            L BND;
            B 1600,2100 -800,1050;
            B 200,200 -1400,1750;
            B 200,200 -600,1050;
            B 200,200 -1400,350;
            DF;
            DS "PLA_pullup";
            L "Default";
            L CWN;
            B 2600,3000 -1900,1050;
            L CAN;
            B 400,400 -2400,1050;
            L CAP;
            B 400,400 -2400,350;
            B 400,400 -2400,1750;
            B 600,300 -1900,350;
            B 600,300 -1900,1750;
            B 400,400 -1400,1750;
            B 400,400 -1400,350;
            L CPG;
            B 400,400 -1500,1050;
            B 400,2100 -1900,1050;
            L CM1;
            B 400,2100 -2400,1050;
            B 1600,400 -800,1750;
            B 1700,400 -850,1050;
            B 1600,400 -800,350;
            L CCC;
            B 200,200 -2400,1050;
            B 200,200 -1500,1050;
            B 200,200 -2400,1750;
            B 200,200 -2400,350;
            B 200,200 -1400,350;
            B 200,200 -1400,1750;
            L CM2;
            B 400,2100 -2400,1050;
            L CV1;
            B 200,200 -2400,1050;
            L BND;
            B 3200,2100 -1600,1050;
            DF;
            DS "Pla_output";
            L "Default";
            L CWN;
            B 3200,2100 1150,-2850;
            L CAN;
            B 2000,450 1150,-975;
            L CAP;
            B 2000,900 1150,-2850;
            L CPG;
            B 400,400 450,-300;
            B 400,400 1850,-300;
            B 200,3400 750,-1800;
            B 200,3400 1550,-1800;
            L CM1;
            B 400,2900 350,-2250;
            B 400,2900 1950,-2250;
            B 400,1500 1150,-2550;
            B 400,500 1950,-250;
            B 400,1200 1150,-600;
            B 400,500 350,-250;
            B 100,400 600,-300;
            B 100,400 1700,-300;
            L CCC;
            B 200,200 450,-300;
            B 200,200 1850,-300;
            B 200,200 1150,-1000;
            B 200,200 1950,-1000;
            B 200,200 350,-1000;
            B 200,200 350,-2600;
            B 200,200 350,-3100;
            B 200,200 1150,-2600;
            B 200,200 1950,-2600;
            B 200,200 1150,-3100;
            B 200,200 1950,-3100;
            L CM2;
            B 400,400 350,-3500;
            B 400,400 1950,-3500;
            W 400 1150,-2000 1150,-2300;
            W 400 200,-2600 2100,-2600;
            L CV1;
            B 200,200 350,-3500;
            B 200,200 1950,-3500;
            B 200,200 1150,-2000;
            L BND;
            B 2300,3700 1150,-1850;
            DF;
            E
            '''
        )

    definitions = definitions[definitions.index("DS"):-1]
    # print(definitions)
    # print(repr(definitions))

    return (success, definitions)


def generate_pla_components_layout(code_count, input_count, output_count):
    vert_count = math.ceil(code_count / 2)
    hor_count = math.ceil(output_count / 2)

    pla_components_dict = {
        "PLA_ip_if": (1, vert_count, 900, 2100, 1600 * (input_count - 1), 0),
        "PLA_orPlane": (hor_count, vert_count, 2300, 2100, 1600 * (input_count - 1) + 900, 0),
        "PLA_input": (input_count, 1, 1600, 3700, 0, 0),
        "PLA_andPlane": (input_count, vert_count, 1600, 2100, 0, 0),
        "PLA_pullup": (1, vert_count, 3200, 2100, -1600, 0),
        "PLA_OrPullup": (hor_count, 1, 2300, 3000, 1600 * (input_count - 1) + 900, 2100 * vert_count),
        "Pla_output": (hor_count, 1, 2300, 3700, 1600 * (input_count - 1) + 900, 0)
    }

    pla_components = ""

    pla_components += "L \"Default\";\n"
    for (component, params) in pla_components_dict.items():
        pla_components += BLANK_LAYOUT_ENTRIES["array"].format(params[0], params[1], params[2], params[3])
        pla_components += BLANK_LAYOUT_ENTRIES["composite"].format(component, params[4], params[5])
    pla_components += BLANK_LAYOUT_ENTRIES["composite"].format("PLA_io_if", 1600 * (input_count - 1), 0)

    return pla_components


# TODO implement func generate_pla_wires_layout
def generate_pla_wires_layout():
    current_label_pos = 0
    current_code_wire_pos = 0
    current_output_wire_pos = 0
    bottom_entry_code = True
    return


# TODO implement func generate_pla_contacts_layout
def generate_pla_contacts_layout():
    return


# TODO implement func generate_pla_labels_layout
def generate_pla_labels_layout(pla_inputs, pla_outputs):
    pla_labels = ""
    for (output, codes) in pla_outputs:
        pla_labels += BLANK_LAYOUT_ENTRIES["label"].format(10, 10, output)
    return pla_labels


def write_output_to_file(pla_layout_output):
    output_file_number = 0
    while os.path.isfile("./pla_layout/pla_layout_output_{}.lay".format(output_file_number)):
        output_file_number += 1
    output_file = open("./pla_layout/pla_layout_output_{}.lay".format(output_file_number), "w")
    output_file.write(pla_layout_output)
    output_file.close()

    print("PLA layout written to ./pla_layout/pla_layout_output_{}.lay".format(output_file_number))


def generate_pla_layout(write_to_file):
    success = False
    pla_layout_output = None

    while not success:

        # region Load pre-defined layouts
        cmos_layers = load_cmos_layers(True)

        (success, pla_definitions) = load_definitions(True)
        if not success:
            break

        (pla_inputs, pla_outputs, pla_codes_dict, code_count, input_count, output_count) = load_pla_codes(True)
        # endregion

        # region Generate PLA layout per specifications in input file
        # pla_components = ""
        # pla_wires = ""
        # pla_contacts = ""
        # pla_labels = ""

        pla_components = generate_pla_components_layout(code_count, input_count, output_count)
        pla_wires = generate_pla_wires_layout()
        pla_contacts = generate_pla_contacts_layout()
        pla_labels = generate_pla_labels_layout(pla_inputs, pla_outputs)
        # endregion

        # region Integrate loaded and generated layout components into one file openable in layout.exe
        pla_layout_output = ""
        pla_layout_output += cmos_layers
        pla_layout_output += pla_definitions
        pla_layout_output += pla_components
        pla_layout_output += pla_wires
        pla_layout_output += pla_contacts
        pla_layout_output += pla_labels
        pla_layout_output += "E"
        # endregion

        # region Prints for console-based debugging
        print(pla_layout_output)
        print(repr(pla_layout_output))
        print("input_count: {}\noutput_count: {}".format(input_count, output_count))
        # endregion

        if write_to_file:
            write_output_to_file(pla_layout_output)

        success = True
        break

    return (success, pla_layout_output)


if __name__ == '__main__':
    # load_definitions()
    generate_pla_layout(True)
    # load_pla_codes(False)
