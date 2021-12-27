from math import ceil
from typing import List
from pprint import pprint

def get_packets():
    with open("Day16/input.txt", 'r') as f:
        binary_string = ""
        for line in f.read().splitlines():
            binary_string += str(bin(int('1'+line, 16)))[3:]
    return binary_string


def find_subpacket(packets_string: str, index: int, pad_zeros: bool = True):
    packet_version = int(packets_string[index:index+3], 2)
    current_type_id = "literal" if int(packets_string[index+3:index+6], 2) == 4 else "operator"
   
    print(int(packets_string[index+3:index+6], 2) == 4, current_type_id, index)

    if current_type_id == "operator":
        length_type_id = 11 if int(packets_string[index+6], 2) else 15

        sub_packets = []
        if length_type_id == 15:
            length_subpackets = int(packets_string[index+7:index+7+length_type_id], 2)
            # I think we have to do a bit of recursion here ->
            # essentially we call this function again with an index determined by the length of the nested packets
            # we should create a function that calculates the length of the packet
            print(length_subpackets)
            while True:
                if sub_packets:
                    if (sub_packet_length :=sum(sub_packet['full_binary_length'] for sub_packet in sub_packets)) == length_subpackets:     
                        break
                extra = sum(sub_packet['full_binary_length'] for sub_packet in sub_packets) if sub_packets else 0
                sub_packets.append(find_subpacket(packets_string, index+7+length_type_id+extra, pad_zeros = False))
                print(sub_packets)
        elif length_type_id == 11:
            number_subpackets = int(packets_string[index+7:index+7+length_type_id], 2)
            while True:
                if len(sub_packets) == number_subpackets:
                    break
                extra = sum(sub_packet['full_binary_length'] for sub_packet in sub_packets) if sub_packets else 0
                print(index+7+length_type_id+extra)
                sub_packets.append(find_subpacket(packets_string, index+7+length_type_id+extra, pad_zeros=False))
        packet = {
            "packet_version": packet_version,
            "type_id": current_type_id,
            "other_packets": sub_packets,
            "value": None,
            "full_binary_length": sum(sub_packet['full_binary_length'] for sub_packet in sub_packets) + 7 + length_type_id,  # add up length of subpackets plus length of packet
        }
        index = 1 + (4*ceil((index+packet["full_binary_length"])/4))
        
    elif current_type_id == "literal":
        # check each 5 bits and make sure that the first bit of each one is 1
        # if you find 5 bits that are prefixed with 0, then this is the final group
        # make sure to add padding for the extra zeros, round up to nearest multiple of 4
        binary_values: List[str] = []
        binary_number_count = 0
        while True:
            full_value = packets_string[index+6+(binary_number_count*5):index+11+(binary_number_count*5)]
            binary_values.append(full_value[1:])
            if int(full_value[0], 2) == 0:
                break
            else:
                binary_number_count += 1
        print(packets_string[index: index+11+(binary_number_count*5)])
        packet = {
            "packet_version": packet_version,
            "type_id": current_type_id,
            "other_packets": [],
            "value": int("".join(binary_values), 2),
            "full_binary_length": (4 * ceil((index+11+(binary_number_count*5))/4)) - index if pad_zeros else index+11+(binary_number_count*5) - index
        }
        index = 1 + (4 * ceil((index+11+(binary_number_count*5))/4))  # set i to the next packet, which will be current index where the values in the literal packet end, ROUNDED UP to the nearest multiple of 4
    return packet


def calculate_total_packet_version(packet: dict, total_version: int) -> int:
    sub_packets = packet['other_packets']
    previous_versions = 0
    if sub_packets:
        for sub_packet in sub_packets:
            previous_versions += calculate_total_packet_version(sub_packet, total_version=total_version)
    total_version += packet['packet_version']
    return total_version + previous_versions

if __name__ == "__main__":
    packets_string = get_packets()
    i = 0
    print(packets_string)
    packet = find_subpacket(packets_string, i)
    pprint(packet)
    total_packet_version = calculate_total_packet_version(packet, 0)
    print(total_packet_version)
