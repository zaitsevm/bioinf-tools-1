
def length_control(seq_length: int, bounds: tuple or num) -> bool: 
    if type(bounds) == tuple:
    	return bounds[0] <= seq_length <= bounds[1]
    else:
    	return seq_length <= bounds


def gc_control(sequence: str, bounds: tuple or num) -> bool:
    gc_content = 100 * (sequence.count("C") + sequence.count("G")) / len(sequence)
    if type(bounds) == tuple:
    	return bounds[0] <= gc_content <= bounds[1]
    else:
    	return gc_content <= bounds

